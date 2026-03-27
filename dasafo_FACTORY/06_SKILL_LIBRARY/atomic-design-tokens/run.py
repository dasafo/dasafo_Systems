"""
run.py — Atomic Design Tokens (FRONTEND_DEV)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Generates semantic CSS variables for the project.
"""

from __future__ import annotations
import os
import json
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    agent = "FRONTEND_DEV"
    skill = "atomic-design-tokens"
    cid = skill_input.correlation_id

    try:
        # 1. Resolution
        theme = skill_input.params.get("theme", "dark")
        target = skill_input.params.get("target_project") or skill_input.target_project or os.environ.get("TARGET_PROJECT")
        
        # 2. Token Definition (v3.2.0-S)
        tokens = {
            "--color-primary": "hsl(210, 100%, 50%)" if theme == "light" else "hsl(210, 100%, 10%)",
            "--color-accent": "hsl(350, 100%, 60%)",
            "--spacing-base": "8px",
            "--radius-premium": "12px",
            "--vibe-blur": "10px",
            "--solidity-version": "3.2.0-S"
        }
        
        artifacts = []
        output_path = None
        
        if target:
            project_path = Path(target).resolve()
            styles_dir = project_path / "ui" / "styles"
            styles_dir.mkdir(parents=True, exist_ok=True)
            output_path = styles_dir / "tokens.json"
            
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(tokens, f, indent=2)
            artifacts.append(str(output_path))

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "tokens": tokens,
                "theme": theme,
                "path": str(output_path) if output_path else None
            },
            correlation_id=cid,
            artifacts=artifacts
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Token Generation Failed: {str(e)}", cid)
