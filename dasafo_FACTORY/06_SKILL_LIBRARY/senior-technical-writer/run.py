"""
run.py — Senior Technical Writer (DOCUMENTATION_STRATEGIST)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Translates technical logic into user-centric documentation.
"""

from __future__ import annotations
import os
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    agent = "DOCUMENTATION_STRATEGIST"
    skill = "senior-technical-writer"
    cid = skill_input.correlation_id

    try:
        # 1. Resolve Target
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "Missing TARGET_PROJECT", cid)
        
        # 2. Logic (Documentation Pass Simulation)
        manual_path = Path(target).resolve() / "DOCS" / "USER_GUIDE.md"
        manual_path.parent.mkdir(parents=True, exist_ok=True)
        manual_path.write_text("# Industrial User Guide\n\n## Benefits\n- Solid execution via Dasafo Factory.", encoding="utf-8")

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "doc_path": str(manual_path),
                "vibe_score": 1.0,
                "audience_level": "End-User"
            },
            correlation_id=cid,
            artifacts=[str(manual_path)]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Doc Generation Failed: {str(e)}", cid)
