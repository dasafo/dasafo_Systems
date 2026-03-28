import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Hallucination Report Guardrail (QA_TESTER)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Verifies QA reports against evidence requirements to eliminate false positives.
"""

from __future__ import annotations
import os
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    agent = "QA_TESTER"
    skill = "hallucination-report-guardrail"
    cid = skill_input.correlation_id

    try:
        # 1. Path Resolution
        path = skill_input.params.get("report_path")
        if not path:
             return SkillOutput.failure(agent, skill, "Missing report_path.", cid)
        
        report_file = Path(path).resolve()
        
        # 2. Logic (Evidence Verification Simulation)
        # Check if report contains file paths and logs
        missing = []
        if report_file.exists():
            content = report_file.read_text(encoding="utf-8")
            if "L-" not in content:
                 missing.append("Line number breadcrumbs")
            if "LOG" not in content.upper():
                 missing.append("Console/Terminal logs")

        verdict = "VERIFIED" if not missing else "VOID_LACK_OF_EVIDENCE"

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "solidity_verdict": verdict,
                "missing_evidence": missing
            },
            correlation_id=cid,
            artifacts=[str(report_file)] if report_file.exists() else []
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Report Guardrail Failed: {str(e)}", cid)
