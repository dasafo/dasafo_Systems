"""
run.py — RA-Agile Orchestration (ORCHESTRATOR)
Scales agentic workflows based on project milestones.
v2.1: Project-agnostic and English-only.
"""

import os
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """
    Executes agile sprint planning for the agents.
    """
    milestone = skill_input.params.get("milestone", "ALPHA")
    target_project = skill_input.target_project or os.environ.get("TARGET_PROJECT", "PROJECT_UNKNOWN")
    
    sprint_data = {
        "sprint_id": f"S-{milestone}-01",
        "focus": f"Achieving {milestone} deliverable for {target_project}",
        "team": ["architect", "backend_dev", "frontend_dev", "qa_tester"],
        "governance": "PRP_CONTRACT_V2.1"
    }
    
    return SkillOutput.success(
        agent=skill_input.agent,
        skill=skill_input.skill,
        data=sprint_data,
        correlation_id=skill_input.correlation_id
    )
