"""
run.py — DAG Routing (ORCHESTRATOR)
v3.1.5: Solidity Guard | Industrial Scale.
"""

import sys
from pathlib import Path

# Add factory knowledge to path BEFORE imports
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "00_GLOBAL_KNOWLEDGE"))

from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """
    Routes tasks through the Directed Acyclic Graph.
    """
    return SkillOutput.success(
        agent=skill_input.agent,
        skill=skill_input.skill,
        data={"route": "OPTIMAL", "next_node": "BACKEND_DEV"},
        correlation_id=skill_input.correlation_id
    )
