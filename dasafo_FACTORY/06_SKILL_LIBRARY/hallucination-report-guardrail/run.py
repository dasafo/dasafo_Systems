import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Hallucination Report Guardrail (QA_TESTER / DOCS_MASTER)
v3.3.0-S: Modular Toolbox | Industrial Scale.

Verifies reports and documentation against physical evidence to eliminate hallucinations.
"""

from __future__ import annotations
import os
import re
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Industrialized entry point for hallucination detection."""
    agent = skill_input.agent or "QA_TESTER"
    skill = "hallucination-report-guardrail"
    cid = skill_input.correlation_id

    try:
        # 1. Path Resolution
        path = skill_input.params.get("report_path")
        if not path:
            return SkillOutput.failure(agent, skill, "Missing 'report_path' parameter.", cid)
        
        report_file = Path(path).resolve()
        if not report_file.exists():
             return SkillOutput.failure(agent, skill, f"Report file not found: {path}", cid)

        # 2. Logic (Enhanced Evidence Verification)
        content = report_file.read_text(encoding="utf-8")
        missing_evidence = []
        
        # Pattern 1: Physical Path Citations (e.g. file:///... or absolute/path)
        if not re.search(r"(/|file:///)[a-zA-Z0-9._/-]+", content):
            missing_evidence.append("Physical file path citations")

        # Pattern 2: Line Numbers (L-xxx or line xxx)
        if not re.search(r"(L-|line\s+)\d+", content, re.IGNORECASE):
            missing_evidence.append("Specific line number references (L-xxx)")

        # Pattern 3: Log/Terminal Output (for QA) or Citation (for Docs)
        if agent == "QA_TESTER":
            if "LOG" not in content.upper() and "TERMINAL" not in content.upper():
                missing_evidence.append("Console/Terminal log artifacts")
        elif agent == "DOCS_MASTER":
            if "###" not in content and "Source:" not in content:
                 missing_evidence.append("Structural source citations")

        # 3. Verdict Synthesis
        score = 100 - (len(missing_evidence) * 30)
        verdict = "VERIFIED_SOLID" if score >= 70 else "VOID_LACK_OF_EVIDENCE"
        if score < 40:
            verdict = "HALLUCINATION_DETECTED"

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "solidity_score": score,
                "solidity_verdict": verdict,
                "missing_evidence": missing_evidence,
                "cid_sync": cid in content
            },
            correlation_id=cid,
            artifacts=[str(report_file)]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Guardrail Fault: {str(e)}", cid)
