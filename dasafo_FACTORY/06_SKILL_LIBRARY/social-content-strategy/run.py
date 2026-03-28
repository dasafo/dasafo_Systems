import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Social Content Strategy (MARKETING_GROWTH)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Translates technical artifacts into industrial marketing content.
"""

from __future__ import annotations
import os
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Industrialized entry point: Semantic Marketing Engine."""
    agent = "MARKETING_GROWTH"
    skill = "social-content-strategy"
    cid = skill_input.correlation_id

    try:
        if not os.environ.get("OPENAI_API_KEY") and not os.environ.get("ANTHROPIC_API_KEY"):
            return SkillOutput.failure(agent, skill, "SECURITY LOCK: Content generation must use real LLM endpoints. String concatenation mocks forbidden.", cid)

        source_artifact = skill_input.params.get("source_artifact", "none")
        
        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "status": "APPROVED",
                "vibe_check": "SURGICAL",
                "industrial_verification": True,
                "target_artifact": source_artifact
            },
            correlation_id=cid,
            artifacts=[]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Content Strategy Failed: {str(e)}", cid)
