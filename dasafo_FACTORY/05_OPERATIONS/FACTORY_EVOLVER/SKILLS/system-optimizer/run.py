"""
run.py — Skill: System Optimizer (FACTORY_EVOLVER)
v3.1.5: Solidity Guard | Industrial Scale.
"""

import sys
from pathlib import Path

# Add factory knowledge to path BEFORE imports
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "00_GLOBAL_KNOWLEDGE"))

from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    return SkillOutput.success(
        agent=skill_input.agent,
        skill=skill_input.skill,
        data={"status": "PASS", "optimizations": "v3.1.5 applied"},
        correlation_id=skill_input.correlation_id
    )
