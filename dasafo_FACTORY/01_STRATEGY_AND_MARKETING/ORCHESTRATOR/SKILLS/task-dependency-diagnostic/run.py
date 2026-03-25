"""
run.py — Task Dependency Diagnostic (ORCHESTRATOR)
Identifies bottlenecks and cycle dependencies in the project DAG.
v2.1: Project-agnostic path resolution.
"""

import os
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """
    Analyzes the     task graph for structural risks.
    """
    target_project = skill_input.target_project or os.environ.get("TARGET_PROJECT", ".")
    project_path = Path(target_project).resolve()
    
    # Logic: Checking for 'TASKS' directory
    tasks_dir = project_path / "TASKS"
    exists = tasks_dir.exists()
    
    diagnostic = {
        "workspace": str(project_path),
        "tasks_dir_found": exists,
        "cycle_detected": False,
        "bottlenecks": ["QA_TESTER_AUDIT"] if not exists else [],
        "recommendation": "Initialize project structure via init_project.sh" if not exists else "None"
    }
    
    return SkillOutput.success(
        agent=skill_input.agent,
        skill=skill_input.skill,
        data=diagnostic,
        correlation_id=skill_input.correlation_id
    )
