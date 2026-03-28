import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Framer Motion Transitions (FRONTEND_DEV)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Generates premium animation snippets for UI fluidity.
"""

from __future__ import annotations
import os
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    agent = "FRONTEND_DEV"
    skill = "framer-motion-transitions"
    cid = skill_input.correlation_id

    try:
        # 1. Params
        anim = skill_input.params.get("animation_type", "page")
        duration = skill_input.params.get("duration_ms", 200)
        
        if duration > 300:
             duration = 300 # Enforce industrial constraint

        # 2. Logic (Snippet Generation)
        snippet = f"""
// Premium {anim.capitalize()} Transition (v3.2.0-S)
const transitionVariant = {{
  initial: {{ opacity: 0, y: 5 }},
  animate: {{ opacity: 1, y: 0 }},
  exit: {{ opacity: 0, y: -5 }},
  transition: {{ duration: {duration / 1000}, ease: "easeOut" }}
}};
"""

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "code_snippet": snippet,
                "vibe_check": "PREMIUM"
            },
            correlation_id=cid,
            artifacts=[]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Animation Snippet Failed: {str(e)}", cid)
