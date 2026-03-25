"""
mcp_agent_factory.py — MCP Server (STDIO)
Bridges Antigravity/MCP requests to the Factory's skills_runner.py.
v3.1: Infra-Aware orchestration and shared infrastructure support.
"""

import sys
import json
import subprocess
import os
from pathlib import Path

# Relative path resolution for portability
BASE_DIR = Path(__file__).resolve().parent
RUNNER_PATH = BASE_DIR / "skills_runner.py"

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
                        "serverInfo": {"name": "dasafo_factory", "version": "3.1.0"}
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
                    
                    # Target project strictly from environment variable
                    target_project = os.environ.get("TARGET_PROJECT", ".")
                    
                    cmd = [
                        "python3", str(RUNNER_PATH),
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
                            "content": [{"type": "text", "text": result.stdout if result.returncode == 0 else result.stderr}]
                        }
                    }
                    sys.stdout.write(json.dumps(response) + "\n"); sys.stdout.flush()

        except EOFError: break
        except Exception as e:
            # Silent error handling for JSON-RPC stability, but logged in dev if needed
            pass

if __name__ == "__main__":
    main()
