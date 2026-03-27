"""
run.py — Design Token Definition (ARCHITECT)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Defines and validates the visual identity tokens for premium UI.
"""

from __future__ import annotations
import os
import json
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

DEFAULT_TOKENS = {
    "colors": {
        "brand": "#00E5FF",  # Electric Blue
        "danger": "#FF3D00", # Neon Red
        "background": "rgba(10, 10, 10, 0.8)", # Glass Dark
        "surface": "rgba(255, 255, 255, 0.05)" # Glass Surface
    },
    "spacing": { "unit": 8, "xs": 4, "sm": 8, "md": 16, "lg": 24, "xl": 32 },
    "typography": { "primary": "Outfit, sans-serif", "secondary": "Inter, sans-serif" },
    "effects": {
        "glass_blur": "12px",
        "transition": "300ms cubic-bezier(0.4, 0, 0.2, 1)"
    }
}

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    agent = "ARCHITECT"
    skill = "design-token-definition"
    cid = skill_input.correlation_id

    try:
        # 1. Path Resolution
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "Missing TARGET_PROJECT", cid)
        
        project_path = Path(target).resolve()
        action = skill_input.params.get("action", "validate")

        # 2. Logic (Export/Validation)
        artifacts = []
        if action == "export":
            output_path = project_path / "LOCAL_KNOWLEDGE" / "architecture" / "design_tokens.json"
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(DEFAULT_TOKENS, f, indent=2)
            artifacts.append(str(output_path))

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "tokens": DEFAULT_TOKENS,
                "status": "PREMIUM",
                "doc_path": str(project_path / "DOCS" / "Visual_Standard.md")
            },
            correlation_id=cid,
            artifacts=artifacts
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Token Definition Failure: {str(e)}", cid)
