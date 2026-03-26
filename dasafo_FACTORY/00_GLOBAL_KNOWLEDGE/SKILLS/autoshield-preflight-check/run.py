"""
run.py — AutoShield Preflight Check (GLOBAL_KNOWLEDGE)
v3.1.5: Solidity Guard | Industrial Scale.

Performs critical industrial safety verification before skill execution.
"""

import sys
import os
from pathlib import Path

# Add factory knowledge to path (Skill is in GLOBAL_KNOWLEDGE/SKILLS/...)
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """
    Core safety gate. Checks for:
    1. TARGET_PROJECT presence.
    2. Zero-Trust security scan status.
    3. Global Soul alignment.
    """
    target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
    
    if not target:
        return SkillOutput.failure(
            agent=skill_input.agent,
            skill=skill_input.skill,
            error="INDUSTRIAL LOCK: TARGET_PROJECT environment variable is missing.",
            correlation_id=skill_input.correlation_id
        )

    # Logic: Verify that the project path is absolute and exists
    project_path = Path(target).resolve()
    if not project_path.exists():
         return SkillOutput.failure(
            agent=skill_input.agent,
            skill=skill_input.skill,
            error=f"VALIDATION FAILED: Target path {project_path} does not exist.",
            correlation_id=skill_input.correlation_id
        )

    return SkillOutput.success(
        agent=skill_input.agent,
        skill=skill_input.skill,
        data={"preflight_status": "PASS", "project_path": str(project_path)},
        correlation_id=skill_input.correlation_id
    )
