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
from pathlib import Path
from functools import wraps

from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

# Importar la aduana original (session_hook no tiene dependencias circulares)
import session_hook

mcp = FastMCP("dasafo_FACTORY_Core_v5.0")
FACTORY_ROOT = Path(__file__).resolve().parent.parent

# =====================================================================
# 🛡️ EL DECORADOR INDUSTRIAL (Reemplaza a skill_engine.py)
# =====================================================================

def aduana_universal(skill_name: str):
    """
    Decorador que envuelve cada herramienta MCP con el protocolo DAST.
    Sincroniza disco, verifica firmas, inyecta variables y hace auto-commit.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(agent: str, target_project: str, *args, isolate: bool = False, **kwargs):
            project_path = Path(target_project)
            
            # 1. PRE-FLIGHT SYNC (DAST)
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
                                import logging
                                logging.getLogger("AduanaUniversal_v5.0").warning(
                                    f"DAST Sync: Corrupted task file {task_file}: {e}"
                                )
                with open(registry_file, 'w', encoding='utf-8') as f:
                    json.dump(physical_tasks, f, indent=2)

            # 2. INYECCIÓN INFRA
            infra_env = FACTORY_ROOT.parent / "INFRA" / ".env"
            if infra_env.exists():
                load_dotenv(infra_env)

            if isolate:
                os.environ["CLEAN_SESSION"] = "True"

            # 3. VERIFICACIÓN DE LA ADUANA (session_hook)
            is_allowed, reason = session_hook.verify_project_state(target_project, skill_name, agent)
            if not is_allowed:
                return {
                    "success": False, 
                    "error": f"Aduana Blocked: {reason}",
                    "industrial_status": "BLOCKED"
                }, []

            # 4. EJECUCIÓN DE LA HERRAMIENTA NATIVA
            try:
                # La función debe devolver: dict(result), list(artifacts)
                result_payload, artifacts = func(agent, target_project, *args, isolate=isolate, **kwargs)
                
                # 5. AUTO-COMMIT (Si es aislada y no es bypass)
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
