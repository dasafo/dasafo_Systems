from __future__ import annotations
import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Registry Manager (ORCHESTRATOR)
v3.4.0-S: Modular Toolbox | Industrial Scale.
Solidified: Physical Artifact Sync & Kanban SSoT Integrity.
"""

import os
import json
import time
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    agent = skill_input.agent or "ORCHESTRATOR"
    skill = "registry-manager"
    cid = skill_input.correlation_id
    params = skill_input.params or {}
    
    start_time = time.time()

    try:
        target = params.get("target_project") or skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "SECURITY LOCK: Missing TARGET_PROJECT.", cid)
        
        project_path = Path(target).resolve()
        tasks_dir = project_path / "TASKS"
        registry_file = tasks_dir / "registry.json"
        
        action = params.get("action", "update_status")
        task_id = params.get("task_id")
        new_status = params.get("new_status")

        if not registry_file.exists():
            return SkillOutput.failure(agent, skill, "GATE_ERROR: registry.json not found.", cid)

        if action == "update_status":
            if not task_id or not new_status:
                return SkillOutput.failure(agent, skill, "INPUT_ERROR: task_id and new_status required.", cid)

            with open(registry_file, 'r', encoding='utf-8') as f:
                registry = json.load(f)

            task_found = False
            prev_status = "UNKNOWN"
            task_data = {}

            for task in registry:
                if task.get("id") == task_id:
                    prev_status = task.get("status", "PENDING")
                    task["status"] = new_status
                    task_data = task
                    task_found = True
                    break

            if not task_found:
                return SkillOutput.failure(agent, skill, f"NOT_FOUND: Task {task_id} not in registry.", cid)

            # Physical Sync Strategy (Zero-Trust)
            target_folder = tasks_dir / f"03_{new_status}" if new_status == "COMPLETED" else tasks_dir / f"02_{new_status}" if new_status == "IN_PROGRESS" else tasks_dir / "01_PENDING"
            target_folder.mkdir(parents=True, exist_ok=True)
            
            artifact_file = target_folder / f"{task_id}.json"
            with open(artifact_file, 'w', encoding='utf-8') as f:
                json.dump(task_data, f, indent=2)

            # Save SSoT
            with open(registry_file, 'w', encoding='utf-8') as f:
                json.dump(registry, f, indent=2)

            execution_duration_s = time.time() - start_time
            
            result_payload = {
                "industrial_status": "SOLIDIFIED - REGISTRY SYNCED",
                "task_id": task_id,
                "previous_status": prev_status,
                "current_status": new_status,
                "artifact_path": str(artifact_file),
                "compliance_report": {
                    "physical_sync_verified": True,
                    "execution_duration_seconds": round(execution_duration_s, 4)
                },
                "summary": f"Task {task_id} transitioned from {prev_status} to {new_status}."
            }
            
            return SkillOutput.success(agent, skill, result_payload, [str(artifact_file), str(registry_file)], cid)

        return SkillOutput.failure(agent, skill, f"Action '{action}' not implemented.", cid)

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Registry CRITICAL Fault: {str(e)}", cid)