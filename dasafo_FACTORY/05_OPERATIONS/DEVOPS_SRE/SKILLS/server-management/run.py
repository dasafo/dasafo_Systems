"""
run.py — Server Management / Reprovisioning (DEVOPS_SRE)
Logic to ensure infrastructure state matches the desired configuration.
v2.1: Project-agnostic.
"""

import os
import json
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """
    Simulates a reprovisioning or server state check.
    """
    target_project = skill_input.target_project or os.environ.get("TARGET_PROJECT", ".")
    project_path = Path(target_project).resolve()
    
    # Simulate a state check
    state_report = {
        "project": str(project_path),
        "infra_provider": "docker-compose",
        "container_status": "RUNNING",
        "health_check": "PASSING",
        "actions_taken": ["No intervention needed — infra is stable."]
    }
    
    # Log to ops
    log_dir = project_path / "LOGS" / "ops"
    log_dir.mkdir(parents=True, exist_ok=True)
    
    with open(log_dir / "infra_state.json", "w") as f:
        json.dump(state_report, f, indent=4)
    
    return SkillOutput.success(
        agent=skill_input.agent,
        skill=skill_input.skill,
        data=state_report,
        correlation_id=skill_input.correlation_id
    )
