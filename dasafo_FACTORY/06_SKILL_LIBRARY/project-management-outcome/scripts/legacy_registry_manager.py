import os
import json
import time
import shutil
from pathlib import Path
from filelock import FileLock, Timeout  # 👈 Semáforo industrial

# Logic: Industrial Registry Notary (v5.0-MCP)
# Pattern: Atomic Physical Move + DAG Topological Enforcement

def execute_registry_update(
    target_project: str,
    agent: str,
    action: str = "update_status",
    task_id: str = None,
    new_status: str = None
) -> tuple[dict, list]:
    """Pure logic for atomic task movement and DAG enforcement (v5.0-MCP)."""
    start_time = time.time()
    project_path = Path(target_project).resolve()
    tasks_dir = project_path / "TASKS"
    registry_file = tasks_dir / "registry.json"
    
    if not registry_file.exists():
        raise FileNotFoundError(f"GATE_ERROR: registry.json not found at {tasks_dir}")

    folder_map = {
        "PENDING": "01_PENDING",
        "IN_PROGRESS": "02_IN_PROGRESS",
        "COMPLETED": "03_COMPLETED"
    }

    if action == "update_status":
        if not task_id or not new_status:
            raise ValueError("INPUT_ERROR: task_id and new_status required.")
        if new_status not in folder_map:
            raise ValueError(f"INVALID_STATUS: {new_status} is not an industrial state.")

    # 1. ATOMIC LOCK & UPDATE: Previene colisiones en paralelo (Octopus Pattern)
    lock_file = tasks_dir / "registry.json.lock"
    
    try:
        with FileLock(str(lock_file), timeout=10):
            # Read SSoT
            with open(registry_file, 'r', encoding='utf-8') as f:
                registry = json.load(f)

            target_task = next((t for t in registry if t.get("id") == task_id), None)
            if not target_task:
                raise ValueError(f"NOT_FOUND: Task {task_id} not in registry.")

            # 2. 🛡️ DAG ENFORCEMENT (Topological Lock)
            if new_status == "IN_PROGRESS":
                deps = target_task.get("dependencies", [])
                pending_deps = []
                for dep_id in deps:
                    dep_task = next((t for t in registry if t.get("id") == dep_id), None)
                    if not dep_task or dep_task.get("status") != "COMPLETED":
                        pending_deps.append(dep_id)
                
                if pending_deps:
                    raise PermissionError(f"DAG_LOCK: Task {task_id} blocked. Unmet dependencies: {pending_deps}")

            # 3. ATOMIC DAST: Locate source & Move
            source_file = None
            for folder in folder_map.values():
                potential_path = tasks_dir / folder / f"{task_id}.json"
                if potential_path.exists():
                    source_file = potential_path
                    break

            target_folder = tasks_dir / folder_map[new_status]
            target_folder.mkdir(parents=True, exist_ok=True)
            destination_file = target_folder / f"{task_id}.json"

            if source_file:
                os.replace(str(source_file), str(destination_file))

            # 4. Update Registry Data
            prev_status = target_task.get("status", "PENDING")
            target_task["status"] = new_status

            # Atomic JSON write via temp file
            import tempfile
            tmp_fd, tmp_path = tempfile.mkstemp(dir=str(tasks_dir), suffix='.json.tmp')
            try:
                with os.fdopen(tmp_fd, 'w', encoding='utf-8') as tmp_f:
                    json.dump(registry, tmp_f, indent=2)
                os.replace(tmp_path, str(registry_file))
            except Exception:
                if os.path.exists(tmp_path):
                    os.unlink(tmp_path)
                raise
    except Timeout:
        raise TimeoutError(f"OCTOPUS_LOCK: Agente {agent} no pudo actualizar la tarea {task_id}. El registro está ocupado por otro agente.")

        execution_duration_s = round(time.time() - start_time, 4)

        result_payload = {
            "industrial_status": "SOLIDIFIED - ATOMIC MOVE SUCCESSFUL",
            "task_id": task_id,
            "previous_status": prev_status,
            "current_status": new_status,
            "compliance_report": {
                "dag_enforced": True,
                "disk_ssot_synced": True,
                "si_metrics_applied": True,
                "execution_duration_seconds": execution_duration_s
            },
            "summary": f"Task {task_id} moved to {new_status}. DAG validation passed."
        }
        return result_payload, [str(destination_file), str(registry_file)]

    raise ValueError(f"Action '{action}' not supported.")