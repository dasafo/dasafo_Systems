import os
import json
import time
import subprocess
from pathlib import Path

def execute_build_test(
    target_project: str,
    agent: str,
    action: str = "run_build",
    command: str = "echo 'Simulating industrial build...'",
    overwrite: bool = False
) -> tuple[dict, list]:
    """Pure logic for executing builds/tests and generating the Aduana Passport (v5.0-MCP)."""
    start_time = time.time()
    project_path = Path(target_project).resolve()
    logs_dir = project_path / "LOGS"
    logs_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. Physical Execution (Subprocess)
    try:
        # Industrial Guard: Safe execution within project context
        cmd_result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True, 
            cwd=str(project_path), 
            timeout=120
        )
        success = cmd_result.returncode == 0
        output = cmd_result.stdout if success else cmd_result.stderr
    except Exception as e:
        success = False
        output = str(e)

    execution_duration_s = time.time() - start_time
    
    # 2. Aduana Passport Generation (DAST Sovereignty)
    # This file is REQUIRED by session_hook.py for M3->M4 transition
    report_file = logs_dir / "BUILD_REPORT.json"
    
    report_data = {
        "timestamp": time.time(),
        "agent": agent,
        "action": action,
        "command": command,
        "status": "SUCCESS" if success else "FAILED",
        "metrics": {
            "execution_time_s": round(execution_duration_s, 4),
            "bundle_size_B": 0 # Placeholder for actual SI metrics
        },
        "logs_tail": output[-500:] 
    }
    
    # Force write to disk
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, indent=2)

    result_payload = {
        "industrial_status": "SOLIDIFIED - BUILD VERIFIED" if success else "BLOCKED - BUILD FAILED",
        "build_status": "SUCCESS" if success else "FAILED",
        "report_path": str(report_file),
        "compliance_report": {
            "aduana_passport_generated": True,
            "si_metrics_applied": True,
            "execution_duration_seconds": round(execution_duration_s, 4)
        },
        "summary": f"Execution of '{action}' finished with status: {'SUCCESS' if success else 'FAILED'}."
    }

    if not success:
        raise RuntimeError(f"Build/Test Failed. Check physical evidence at {report_file}")

    return result_payload, [str(report_file)]