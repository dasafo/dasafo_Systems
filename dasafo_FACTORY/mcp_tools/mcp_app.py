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
import redis  # 👈 NUEVA DEPENDENCIA
from pathlib import Path
from functools import wraps

from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

import session_hook

mcp = FastMCP("dasafo_FACTORY_Core_v5.0")
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
            
            # --- 🛑 1. LOOP DETECTION (Antifatiga) ---
            # Genera un hash único por agente, skill y proyecto
            loop_key = f"dasafo:loop:{agent}:{skill_name}:{target_project}"
            current_attempts = redis_client.get(loop_key)
            
            if current_attempts and int(current_attempts) >= max_retries:
                import logging
                logging.getLogger("AduanaUniversal_v5.0").error(f"Loop Blocked for {agent} on {skill_name}")
                return {
                    "success": False, 
                    "error": f"CulturalViolation: LOOP_DETECTED. La skill {skill_name} ha fallado o se ha repetido {max_retries} veces. Ejecución abortada para proteger tokens.",
                    "industrial_status": "BLOCKED_BY_ANTIFATIGUE"
                }, []
            
            # Incrementa el contador y le da un TTL de 1 hora para limpiar sesiones colgadas
            redis_client.incr(loop_key)
            redis_client.expire(loop_key, 3600)
            
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
                            except Exception as e:
                                pass
                with open(registry_file, 'w', encoding='utf-8') as f:
                    json.dump(physical_tasks, f, indent=2)

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
            try:
                result_payload, artifacts = func(agent, target_project, *args, isolate=isolate, **kwargs)
                
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
                return {"success": False, "error": f"Tool Exception: {str(e)}"}, []

        return wrapper
    return decorator