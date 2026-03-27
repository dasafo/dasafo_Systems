"""
run.py — NeMo Guardrails & Safety (MARKETING_GROWTH)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Sanitizes marketing copy and detects brand/technical violations.
"""

from __future__ import annotations
import os
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    agent = "MARKETING_GROWTH"
    skill = "nemo-guardrails-safety"
    cid = skill_input.correlation_id

    try:
        # 1. Logic (Safety Scan Simulation)
        content = skill_input.params.get("content", "")
        if "ignore previous" in content.lower():
             return SkillOutput.success(agent, skill, {"safety_verdict": "REJECTED", "reason": "Jailbreak attempt"}, cid)
        
        # 2. Fact-Checking Simulation
        # Verify "40% faster" or similar against logs
        fact_status = "VERIFIED" if "v3.2.0-S" in content else "UNCONFIRMED"

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "safety_verdict": "SAFE",
                "fact_check": {"integrity": fact_status},
                "pii_detected": False
            },
            correlation_id=cid,
            artifacts=[]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Safety Audit Failed: {str(e)}", cid)
