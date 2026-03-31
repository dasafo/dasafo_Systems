"""
factory_cli.py — MCP Server (STDIO)
Bridges Antigravity/MCP requests to the Factory's skill_engine.py.
v3.4.0-S: Industrial Core - Hub-Level Discovery Enabled.
"""

import sys
import json
import subprocess
import os
from pathlib import Path

# Resolución de rutas relativas para portabilidad industrial
BASE_DIR = Path(__file__).resolve().parent
RUNNER_PATH = BASE_DIR / "skill_engine.py"

def get_hub_metadata():
    """
    Escanea físicamente los archivos TOOLS.md departamentales para informar 
    al Orquestador sobre las capacidades activas del sistema.
    """
    hubs = {}
    dept_paths = {
        "01": "01_STRATEGY_AND_MARKETING",
        "02": "02_ARCHITECTURE_AND_DESIGN",
        "03": "03_PRODUCTION",
        "04": "04_COMPLIANCE_AND_QUALITY",
        "05": "05_OPERATIONS"
    }
    for code, folder in dept_paths.items():
        tools_file = BASE_DIR / folder / "TOOLS.md"
        # DAST: La presencia física del archivo marca el estado del Hub
        hubs[f"L{code}_HUB"] = "ACTIVE" if tools_file.exists() else "MISSING"
    return hubs

def main():
    while True:
        try:
            line = sys.stdin.readline()
            if not line: break
            request = json.loads(line)
            method = request.get("method")
            msg_id = request.get("id")

            # 1. PROTOCOLO DE INICIALIZACIÓN (v3.4.0-S)
            if method == "initialize":
                hubs = get_hub_metadata()
                response = {
                    "jsonrpc": "2.0", "id": msg_id,
                    "result": {
                        "protocolVersion": "2026-03-29",
                        "capabilities": {"tools": {}},
                        "serverInfo": {
                            "name": "dasafo_factory", 
                            "version": "3.4.0-S",
                            "hubs_status": hubs # Inyectar metadatos de Hubs para el Orquestador
                        }
                    }
                }
                sys.stdout.write(json.dumps(response) + "\n"); sys.stdout.flush()

            # 2. LISTADO DE HERRAMIENTAS INDUSTRIALES
            elif method == "tools/list":
                hubs = get_hub_metadata()
                hub_desc = " | ".join([f"{k}:{v}" for k, v in hubs.items()])
                
                response = {
                    "jsonrpc": "2.0", "id": msg_id,
                    "result": {
                        "tools": [
                            {
                                "name": "execute_factory_skill",
                                "description": f"Industrial Core Runner (v3.4.0-S). Active Hubs: {hub_desc}",
                                "inputSchema": {
                                    "type": "object",
                                    "properties": {
                                        "agent": {"type": "string", "description": "Invoking agent ID (e.g., ORCHESTRATOR)"},
                                        "skill": {"type": "string", "description": "Skill name (e.g., kanban-solidity-gate)"},
                                        "input_data": {"type": "string", "description": "Optional parameters in JSON string format"}
                                    },
                                    "required": ["agent", "skill"]
                                }
                            }
                        ]
                    }
                }
                sys.stdout.write(json.dumps(response) + "\n"); sys.stdout.flush()

            # 3. EJECUCIÓN DE SKILLS (CON SESSION HOOK / ADUANA)
            elif method == "tools/call":
                params = request.get("params", {})
                tool_name = params.get("name")
                
                if tool_name == "execute_factory_skill":
                    args = params.get("arguments", {})
                    agent = args.get("agent")
                    skill = args.get("skill")
                    input_data = args.get("input_data", "")
                    
                    target_project = os.environ.get("TARGET_PROJECT", ".")
                    
                    # --- SESSION HOOK (ADUANA UNIVERSAL) ---
                    try:
                        from session_hook import verify_project_state
                        is_allowed, reason = verify_project_state(target_project, skill, agent)
                        if not is_allowed:
                            response = {
                                "jsonrpc": "2.0", "id": msg_id,
                                "result": {
                                    "content": [{"type": "text", "text": f"Solidity Protocol Blocked: {reason}\nOnly authorized skills can be executed until state is valid."}]
                                }
                            }
                            sys.stdout.write(json.dumps(response) + "\n"); sys.stdout.flush()
                            continue
                    except Exception as e:
                        response = {
                            "jsonrpc": "2.0", "id": msg_id,
                            "result": {
                                "content": [{"type": "text", "text": f"Solidity Protocol Fatal Error in Hook: {e}"}]
                            }
                        }
                        sys.stdout.write(json.dumps(response) + "\n"); sys.stdout.flush()
                        continue
                    # -------------------------------------------------------------------------
                    
                    cmd = [
                        sys.executable, str(RUNNER_PATH),
                        "--agent", agent,
                        "--skill", skill,
                        "--target-project", target_project
                    ]
                    if input_data: 
                        cmd.extend(["--input", input_data])
                    
                    # Ejecución atómica en el sistema de archivos
                    result = subprocess.run(cmd, capture_output=True, text=True)
                    response = {
                        "jsonrpc": "2.0", "id": msg_id,
                        "result": {
                            "content": [{"type": "text", "text": result.stdout if result.returncode == 0 else (result.stdout + "\n" + result.stderr)}]
                        }
                    }
                    sys.stdout.write(json.dumps(response) + "\n"); sys.stdout.flush()

        except EOFError: break
        except Exception:
            pass # Silencio industrial en errores de parsing de línea

if __name__ == "__main__":
    main()