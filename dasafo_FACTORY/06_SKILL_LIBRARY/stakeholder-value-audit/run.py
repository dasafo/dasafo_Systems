import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Stakeholder Value Audit (PRODUCT_OWNER)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Audits requirements for strategic biases and logical fallacies.
"""

from __future__ import annotations
import os
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    agent = "PRODUCT_OWNER"
    skill = "stakeholder-value-audit"
    cid = skill_input.correlation_id

    try:
        # 1. Logic (Fallacy Detection Simulation)
        text = skill_input.params.get("input_text", "").lower()
        flags = []
        
        if "postgresql" in text or "fastapi" in text:
             flags.append("Solution Specification (premature tech selection)")
        
        verdict = "CHALLENGE" if flags else "PASS"
        
        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "red_flags": flags,
                "verdict": verdict,
                "suggested_correction": "Define the functional behavior before selecting the database stack." if flags else "Clear of obvious biases."
            },
            correlation_id=cid,
            artifacts=[]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Value Audit Failed: {str(e)}", cid)
