import sys
import json
import subprocess
import os

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
                        "serverInfo": {"name": "dasafo_factory", "version": "1.0.0"}
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
                                "description": "Lanza una habilidad de un agente de la factoría.",
                                "inputSchema": {
                                    "type": "object",
                                    "properties": {
                                        "agent": {"type": "string", "description": "ID del agente (ej: security_auditor)"},
                                        "skill": {"type": "string", "description": "Nombre de la habilidad (ej: run)"},
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
                    
                    runner_path = "/home/david/Documents/AI/AGENTES/dasafo_Systems/dasafo_FACTORY/00_GLOBAL_KNOWLEDGE/skills_runner.py"
                    cmd = [
                        "python3", runner_path,
                        "--agent", agent,
                        "--skill", skill,
                        "--target-project", "/home/david/Documents/AI/AGENTES"
                    ]
                    if input_data: cmd.extend(["--input", input_data])
                    
                    result = subprocess.run(cmd, capture_output=True, text=True)
                    response = {
                        "jsonrpc": "2.0", "id": msg_id,
                        "result": {
                            "content": [{"type": "text", "text": result.stdout if result.returncode == 0 else result.stderr}]
                        }
                    }
                    sys.stdout.write(json.dumps(response) + "\n"); sys.stdout.flush()

        except EOFError: break
        except Exception: pass

if __name__ == "__main__":
    main()
