"""
Módulo raíz del servidor MCP Industrial (v5.0 Nativo).
Define el singleton FastMCP y el Decorador de Aduana Universal.

ADR: Extraído de factory_mcp_server.py el 2026-04-03 para romper
la dependencia circular entre factory_mcp_server.py y los hub modules.
Los hubs SOLO importan desde este módulo. factory_mcp_server.py
importa los hubs para forzar su registro y luego ejecuta mcp.run().
"""

import json
import os
import hashlib
import uuid
import redis  # 👈 NUEVA DEPENDENCIA
from datetime import datetime
from pathlib import Path
from functools import wraps

from mcp.server.fastmcp import FastMCP
from fastapi import FastAPI, Request
from dotenv import load_dotenv

import session_hook

# Fuerza el modo sin estado para el patrón Octopus
app = FastAPI(title="dasafo_FACTORY MCP Server", stateless_http=True)
mcp = FastMCP("dasafo_FACTORY_Core_v5.0")

async def get_secure_session_id(request: Request, agent_id: str, task_id: str):
    """Genera un Session ID criptográficamente único para evitar colisiones en DAG paralelo"""
    revision_count = request.headers.get("X-Revision-Count", "0")
    # Genera un ID fuerte: Tarea + Agente + Revisión + Hash aleatorio
    safe_hash = str(uuid.uuid4())[:8]
    return f"{task_id}-{agent_id}-rev{revision_count}-{safe_hash}"

@app.middleware("http")
async def octopus_session_middleware(request: Request, call_next):
    """
    Middleware para inyectar o respetar el session_id en el flujo (v5.2-Octopus).
    Prioriza el ID enviado por el cliente para mantener la coherencia en ejecuciones paralelas.
    """
    # 1. Intentamos recuperar el Session ID inyectado por el cliente (mcp_client.py)
    session_id = request.headers.get("X-Session-ID")
    
    # 2. Si no viene (ej: llamada HTTP externa directa), lo generamos criptográficamente
    if not session_id:
        agent_id = request.headers.get("X-Agent-ID", "unknown")
        task_id = request.headers.get("X-Task-ID", "default-task")
        session_id = await get_secure_session_id(request, agent_id, task_id)
    
    request.state.session_id = session_id
    
    response = await call_next(request)
    response.headers["X-Session-ID"] = session_id
    return response

FACTORY_ROOT = Path(__file__).resolve().parent.parent

# =====================================================================
# ⚡ CONEXIÓN A CACHÉ INDUSTRIAL (Antifatiga)
# =====================================================================
# Intenta conectar a la red Docker (dasafo-cache-node) o cae a localhost para dev
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)

# =====================================================================
# 🛡️ EL DECORADOR INDUSTRIAL CON LOOP DETECTION
# =====================================================================

# 👈 AÑADIDO: max_retries por defecto a 3
def aduana_universal(skill_name: str, max_retries: int = 3): 
    """
    Decorador que envuelve cada herramienta MCP con el protocolo DAST y Loop Detection.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(agent: str, target_project: str, *args, isolate: bool = False, **kwargs):
            project_path = Path(target_project)
            
            # --- 🛑 1. LOOP DETECTION (Antifatiga con Circuit Breaker) ---
            loop_key = f"dasafo:loop:{agent}:{skill_name}:{target_project}"
            
            try:
                current_attempts = redis_client.get(loop_key)
                
                if current_attempts and int(current_attempts) >= max_retries:
                    import logging
                    logging.getLogger("AduanaUniversal_v5.0").error(f"Loop Blocked for {agent} on {skill_name}")
                    return {
                        "success": False, 
                        "error": f"CulturalViolation: LOOP_DETECTED. La skill {skill_name} ha fallado o se ha repetido {max_retries} veces. Ejecución abortada para proteger tokens.",
                        "industrial_status": "BLOCKED_BY_ANTIFATIGUE"
                    }, []
                
                redis_client.incr(loop_key)
                redis_client.expire(loop_key, 3600)
            except Exception:
                # CIRCUIT BREAKER: Redis down → fallback to disk-based loop counter
                import logging
                logging.getLogger("AduanaUniversal_v5.0").warning("Redis unavailable. Falling back to disk loop counter.")
                loop_dir = project_path / "TASKS" / ".loop_counters"
                loop_dir.mkdir(parents=True, exist_ok=True)
                safe_key = hashlib.md5(loop_key.encode()).hexdigest()
                loop_file = loop_dir / f"{safe_key}.json"
                
                disk_count = 0
                if loop_file.exists():
                    try:
                        disk_count = json.loads(loop_file.read_text()).get("count", 0)
                    except Exception:
                        pass
                
                if disk_count >= max_retries:
                    return {
                        "success": False, 
                        "error": f"CulturalViolation: LOOP_DETECTED (disk fallback). Skill {skill_name} blocked.",
                        "industrial_status": "BLOCKED_BY_ANTIFATIGUE"
                    }, []
                
                loop_file.write_text(json.dumps({"count": disk_count + 1, "key": loop_key}))
            
            # --- 💰 1.5. TOKEN BUDGET CIRCUIT BREAKER (L1) ---
            prp_file = project_path / "PRP_CONTRACT.json"
            if prp_file.exists():
                try:
                    prp_data = json.loads(prp_file.read_text(encoding="utf-8"))
                    budget = prp_data.get("metadata", {}).get("budget")
                    if budget:
                        # L1 Simulación heurística basada en invocación industrial
                        estimated_call_tokens = 1500
                        estimated_call_cost = 0.015
                        
                        budget["tokens_consumed"] = budget.get("tokens_consumed", 0) + estimated_call_tokens
                        budget["cost_consumed_usd"] = budget.get("cost_consumed_usd", 0.0) + estimated_call_cost
                        
                        if budget["tokens_consumed"] > budget.get("max_tokens", 1000000):
                            import logging
                            logging.getLogger("AduanaUniversal_v5.0").error(f"BUDGET EXCEEDED in {target_project}")
                            return {
                                "success": False,
                                "error": f"CulturalViolation: TOKEN_BUDGET_EXCEEDED. Límite de {budget['max_tokens']} superado.",
                                "industrial_status": "BLOCKED_BY_BUDGET"
                            }, []
                            
                        # DAST: Escritura Atómica del Presupuesto
                        import tempfile
                        tmp_fd, tmp_path = tempfile.mkstemp(dir=str(project_path), suffix='.json.tmp')
                        with os.fdopen(tmp_fd, 'w', encoding='utf-8') as tmp_f:
                            json.dump(prp_data, tmp_f, indent=2, ensure_ascii=False)
                        os.replace(tmp_path, str(prp_file))
                except Exception:
                    pass

            # --- 📂 2. PRE-FLIGHT SYNC (DAST) ---
            tasks_root = project_path / "TASKS"
            registry_file = tasks_root / "registry.json"
            if tasks_root.exists() and registry_file.exists():
                folders = {"PENDING": "01_PENDING", "IN_PROGRESS": "02_IN_PROGRESS", "COMPLETED": "03_COMPLETED"}
                physical_tasks = []
                for status, folder_name in folders.items():
                    folder_path = tasks_root / folder_name
                    if folder_path.exists():
                        for task_file in folder_path.glob("*.json"):
                            try:
                                with open(task_file, 'r', encoding='utf-8') as f:
                                    task_data = json.load(f)
                                    task_data["status"] = status
                                    physical_tasks.append(task_data)
                            except Exception:
                                pass

                # --- ATOMIC WRITE: Prevent race condition in parallel DAG ---
                import tempfile
                tmp_fd, tmp_path = tempfile.mkstemp(dir=str(tasks_root), suffix='.json.tmp')
                try:
                    with os.fdopen(tmp_fd, 'w', encoding='utf-8') as tmp_f:
                        json.dump(physical_tasks, tmp_f, indent=2)
                    os.replace(tmp_path, str(registry_file))  # Atomic on POSIX
                except Exception:
                    if os.path.exists(tmp_path):
                        os.unlink(tmp_path)
                    raise

            # --- 💉 3. INYECCIÓN INFRA ---
            infra_env = FACTORY_ROOT.parent / "INFRA" / ".env"
            if infra_env.exists():
                load_dotenv(infra_env)

            if isolate:
                os.environ["CLEAN_SESSION"] = "True"

            # --- 🛂 4. VERIFICACIÓN DE LA ADUANA ---
            is_allowed, reason = session_hook.verify_project_state(target_project, skill_name, agent)
            if not is_allowed:
                return {
                    "success": False, 
                    "error": f"Aduana Blocked: {reason}",
                    "industrial_status": "BLOCKED"
                }, []

            # --- ⚙️ 5. EJECUCIÓN DE LA HERRAMIENTA NATIVA ---
            start_perf = time.perf_counter()
            try:
                result_payload, artifacts = func(agent, target_project, *args, isolate=isolate, **kwargs)
                duration_ms = (time.perf_counter() - start_perf) * 1000
                
                # 👈 TELEMETRY ENGINE (v5.2-MCP)
                telemetry_log = {
                    "timestamp": datetime.now().isoformat(),
                    "agent": agent,
                    "skill": skill_name,
                    "project": target_project,
                    "latency_ms": round(duration_ms, 2),
                    "estimated_tokens": estimated_call_tokens,
                    "estimated_cost_usd": estimated_call_cost,
                    "status": "SUCCESS"
                }
                
                metrics_file = FACTORY_ROOT / "INFRASTRUCTURE" / "METRICS" / "telemetry.jsonl"
                with open(metrics_file, "a", encoding="utf-8") as f:
                    f.write(json.dumps(telemetry_log) + "\n")

                # 👈 RESET DE FATIGA: Si la tarea se completa exitosamente, borramos el loop
                if result_payload.get("task_status") == "COMPLETED" or result_payload.get("status") == "SUCCESS":
                    redis_client.delete(loop_key)
                
                # AUTO-COMMIT
                if isolate and skill_name not in session_hook.BYPASS_SKILLS:
                    if result_payload.get("task_status") == "COMPLETED":
                        result_payload["auto_commit"] = "Task logically and physically closed via MCP."

                return {
                    "success": True,
                    "industrial_status": result_payload.get("industrial_status", "SUCCESS"),
                    "summary": result_payload.get("summary", "Ejecución completada."),
                    "artifacts_generated": artifacts,
                    "details": result_payload
                }, artifacts

            except Exception as e:
                duration_ms = (time.perf_counter() - start_perf) * 1000
                # Log Failure Telemetry
                telemetry_err = {
                    "timestamp": datetime.now().isoformat(),
                    "agent": agent,
                    "skill": skill_name,
                    "project": target_project,
                    "latency_ms": round(duration_ms, 2),
                    "status": "ERROR",
                    "error": str(e)
                }
                metrics_file = FACTORY_ROOT / "INFRASTRUCTURE" / "METRICS" / "telemetry.jsonl"
                with open(metrics_file, "a", encoding="utf-8") as f:
                    f.write(json.dumps(telemetry_err) + "\n")
                    
                return {"success": False, "error": f"Tool Exception: {str(e)}"}, []

        return wrapper
    return decorator