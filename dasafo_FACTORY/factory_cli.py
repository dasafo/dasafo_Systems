"""
factory_cli.py — MCP Server (STDIO)
Bridges Antigravity/MCP requests to the Factory's skill_engine.py.
v3.2.0-S: Modular Toolbox v3.2 - Centralized Skill Library.
"""

import sys
import json
import subprocess
import os
from pathlib import Path

# Relative path resolution for portability
BASE_DIR = Path(__file__).resolve().parent
RUNNER_PATH = BASE_DIR / "skill_engine.py"

def main():
    while True:
        try:
            line = sys.stdin.readline()
            if not line: break
            request = json.loads(line)
            method = request.get("method")
            msg_id = request.get("id")

            if method == "initialize":
                response = {
                    "jsonrpc": "2.0", "id": msg_id,
                    "result": {
                        "protocolVersion": "2024-11-05",
                        "capabilities": {"tools": {}},
                        "serverInfo": {"name": "dasafo_factory", "version": "3.2.0-S"}
                    }
                }
                sys.stdout.write(json.dumps(response) + "\n"); sys.stdout.flush()

            elif method == "tools/list":
                response = {
                    "jsonrpc": "2.0", "id": msg_id,
                    "result": {
                        "tools": [
                            {
                                "name": "execute_factory_skill",
                                "description": "Lanza una habilidad de la factoría (v3.2.0-S Modular Toolbox).",
                                "inputSchema": {
                                    "type": "object",
                                    "properties": {
                                        "agent": {"type": "string", "description": "ID del agente que invoca (ej: orchestrator)"},
                                        "skill": {"type": "string", "description": "Nombre de la habilidad (ej: kanban-solidity-gate)"},
                                        "input_data": {"type": "string", "description": "Parámetros opcionales"}
                                    },
                                    "required": ["agent", "skill"]
                                }
                            }
                        ]
                    }
                }
                sys.stdout.write(json.dumps(response) + "\n"); sys.stdout.flush()

            elif method == "tools/call":
                params = request.get("params", {})
                tool_name = params.get("name")
                
                if tool_name == "execute_factory_skill":
                    args = params.get("arguments", {})
                    agent = args.get("agent")
                    skill = args.get("skill")
                    input_data = args.get("input_data", "")
                    
                    # Target project strictly from environment variable
                    target_project = os.environ.get("TARGET_PROJECT", ".")
                    
                    # --- SESSION HOOK (ADUANA UNIVERSAL) ---
                    try:
                        from session_hook import verify_project_state
                        is_allowed, reason = verify_project_state(target_project, skill)
                        if not is_allowed:
                            response = {
                                "jsonrpc": "2.0", "id": msg_id,
                                "result": {
                                    "content": [{"type": "text", "text": f"Solidity Protocol Blocked: {reason}\nOnly authorized skills (stay passive if blocked) can be executed until state is valid."}]
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
                    # ---------------------------------------
                    
                    cmd = [
                        sys.executable, str(RUNNER_PATH),
                        "--agent", agent,
                        "--skill", skill,
                        "--target-project", target_project
                    ]
                    if input_data: 
                        cmd.extend(["--input", input_data])
                    
                    result = subprocess.run(cmd, capture_output=True, text=True)
                    response = {
                        "jsonrpc": "2.0", "id": msg_id,
                        "result": {
                            "content": [{"type": "text", "text": result.stdout if result.returncode == 0 else (result.stdout + "\n" + result.stderr)}]
                        }
                    }
                    sys.stdout.write(json.dumps(response) + "\n"); sys.stdout.flush()

        except EOFError: break
        except Exception as e:
            # Silent error handling for JSON-RPC stability, but logged in dev if needed
            pass

if __name__ == "__main__":
    main()
