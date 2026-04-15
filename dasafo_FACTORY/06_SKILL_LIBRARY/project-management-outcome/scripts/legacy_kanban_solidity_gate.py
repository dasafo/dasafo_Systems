import os
import json
import time
import subprocess
import sys
from pathlib import Path

# Logic: Industrial Phase Gate & Vibe Dashboard (v5.0-MCP)

def execute_gate(
    target_project: str,
    action: str = "audit",
    proposed_phase: str = None,
    port: int = 3001
) -> tuple[dict, list]:
    """Pure logic for physical task verification and dashboard orchestration."""
    start_time = time.time()
    project_path = Path(target_project).resolve()
    tasks_dir = project_path / "TASKS"
    registry_file = tasks_dir / "registry.json"
    state_file = project_path / "PROJECT_STATE.json"

    if action == "audit":
        if not registry_file.exists():
            raise FileNotFoundError(f"PHYSICAL_ERROR: registry.json not found at {tasks_dir}")
        
        with open(registry_file, 'r', encoding='utf-8') as f:
            registry = json.load(f)
        
        pending_tasks = []
        completed_count = 0
        total_tasks = len(registry)
        
        # 🔍 Physical Verification (Zero-Trust)
        for task in registry:
            tid = task.get("id")
            if task.get("status") == "COMPLETED":
                proof_path = tasks_dir / "03_COMPLETED" / f"{tid}.json"
                if proof_path.exists():
                    completed_count += 1
                else:
                    pending_tasks.append(f"{tid} (Missing physical proof)")
            else:
                pending_tasks.append(tid)

        solidity_score = round(completed_count / total_tasks if total_tasks > 0 else 1.0, 2)
        gate_passed = (solidity_score == 1.0 and not pending_tasks)
        
        execution_duration_s = round(time.time() - start_time, 4)

        result_payload = {
            "industrial_status": "SOLIDIFIED - GATE PASSED" if gate_passed else "LOCKED - PENDING TASKS",
            "gate_passed": gate_passed,
            "solidity_score": solidity_score,
            "pending_tasks": pending_tasks,
            "metrics": {
                "verified_tasks": completed_count,
                "total_tasks": total_tasks,
                "execution_duration_seconds": execution_duration_s
            }
        }
        return result_payload, []

    elif action == "start_dashboard":
        server_script = Path(__file__).parent / "server.py"
        # Launching the industrial Vibe server in background
        subprocess.Popen([sys.executable, str(server_script), str(port), str(project_path)])
        
        result_payload = {
            "industrial_status": "SOLIDIFIED - DASHBOARD ACTIVE",
            "dashboard_url": f"http://localhost:{port}",
            "execution_duration_seconds": round(time.time() - start_time, 4)
        }
        return result_payload, []

    raise ValueError(f"Action '{action}' is not supported in the v5.0 pipeline.")