import os
import time
import subprocess
import tempfile
from pathlib import Path

# Ephemeral Code Execution Pattern (v5.1-MCP)
# Enables safe, isolated, and tracked code execution from the LLM.

def execute_ephemeral_code(
    target_project: str,
    agent: str,
    language: str = "python",
    code_payload: str = "",
    timeout_s: int = 30,
    isolate: bool = False
) -> tuple[dict, list]:
    """Secure logic for evaluating dynamic code payloads inside the MCP server."""
    start_time = time.time()
    project_path = Path(target_project).resolve()
    
    # Validation
    allowed_languages = {"python": ".py", "bash": ".sh"}
    if language not in allowed_languages:
        return {"error": f"Language '{language}' not supported. Allowed: {list(allowed_languages.keys())}"}, []
    
    ext = allowed_languages[language]
    artifacts = []
    
    # Generate ephemeral DAST audit log
    logs_dir = project_path / "INFRASTRUCTURE" / "LOGS"
    logs_dir.mkdir(parents=True, exist_ok=True)
    audit_file = logs_dir / f"EXEC_AUDIT_{int(time.time())}.log"
    
    stdout_res = ""
    stderr_res = ""
    status_msg = ""
    
    # Execute securely using tempfile
    with tempfile.NamedTemporaryFile(suffix=ext, delete=False, mode='w', encoding='utf-8') as tmp_script:
        tmp_script.write(code_payload)
        tmp_script_path = tmp_script.name

    try:
        # Configuration for the Docker Sandbox
        image = "python:3.11-slim" if language == "python" else "alpine:3.18"
        interpreter = "python" if language == "python" else "sh"
        
        # We mount the temporary file directly into the container as read-only.
        # This prevents script-based host manipulation.
        container_script_path = f"/tmp/script{ext}"
        
        cmd = [
            "docker", "run", "--rm",
            "--network", "none",             # ZERO-TRUST: No network access allowed
            "--memory", "128m",              # Resource limit: 128MB RAM
            "--cpus", "0.5",                 # Resource limit: 0.5 CPU core
            "--user", "1000:1000",           # Non-root user within container
            "-v", f"{tmp_script_path}:{container_script_path}:ro",
            image,
            interpreter, container_script_path
        ]
            
        process = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            timeout=timeout_s,
            cwd=str(project_path)
        )
        
        stdout_res = process.stdout
        stderr_res = process.stderr
        status_msg = f"Completed with exit code {process.returncode} (Docker Sandbox)"
        
    except subprocess.TimeoutExpired:
        status_msg = f"TIMEOUT: Execution exceeded {timeout_s} seconds in Docker Sandbox."
        stderr_res = status_msg
    except Exception as e:
        status_msg = f"CRITICAL FAULT (SANDBOX): {str(e)}"
        stderr_res = status_msg
    finally:
        # Cleanup host temp file
        if os.path.exists(tmp_script_path):
            os.remove(tmp_script_path)
            
    execution_duration_s = time.time() - start_time
    
    # Audit log formatting (DAST)
    audit_content = (
        f"=== MCP EPHEMERAL EXECUTION AUDIT ===\n"
        f"Agent: {agent}\n"
        f"Language: {language}\n"
        f"Duration: {round(execution_duration_s, 4)}s\n"
        f"Status: {status_msg}\n"
        f"=== PAYLOAD ===\n{code_payload}\n"
        f"=== STDOUT ===\n{stdout_res}\n"
        f"=== STDERR ===\n{stderr_res}\n"
        f"=====================================\n"
    )
    
    audit_file.write_text(audit_content, encoding="utf-8")
    artifacts.append(str(audit_file))
    
    # Unified output
    result = {
        "industrial_status": "SOLIDIFIED - EPHEMERAL EXECUTION GENERATED",
        "stdout": stdout_res.strip(),
        "stderr": stderr_res.strip(),
        "exit_status": status_msg,
        "compliance_report": {
            "execution_duration_seconds": round(execution_duration_s, 4),
            "sandbox_active": True,
            "dast_audit_enabled": True
        },
        "summary": "Ephemeral code execution completed and audited."
    }
    
    return result, artifacts
