"""
run.py — Atomic Design Tokens (FRONTEND_DEV)
v3.1.5: Solidity Guard | Industrial Scale.

Generates semantic CSS variables for the project.
"""

import sys
from pathlib import Path

# Add factory knowledge to path BEFORE imports
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "00_GLOBAL_KNOWLEDGE"))

from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """
    Generates semantic CSS variables for the project.
    """
    theme = skill_input.params.get("theme", "dark")
    
    tokens = {
        "--color-primary": "hsl(210, 100%, 50%)" if theme == "light" else "hsl(210, 100%, 10%)",
        "--color-accent": "hsl(350, 100%, 60%)",
        "--spacing-base": "8px",
        "--radius-premium": "12px",
        "--vibe-blur": "10px",
        "--vibe-opacity": "0.7",
        "--solidity-version": "3.1.5"
    }
    
    return SkillOutput.success(
        agent=skill_input.agent,
        skill=skill_input.skill,
        data={"tokens": tokens, "theme": theme},
        correlation_id=skill_input.correlation_id
    )
