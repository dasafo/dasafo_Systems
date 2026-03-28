"""
run.py — Factory Audit Pro (QA_TESTER)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Structural integrity scanner for factory documentation and standards.
"""

from __future__ import annotations
import os
from pathlib import Path
from datetime import datetime
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Industrialized entry point: Standard Structure Scanner."""
    agent = "QA_TESTER"
    skill = "factory-audit-pro"
    cid = skill_input.correlation_id

    try:
        # 1. Resolve Paths
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "Missing TARGET_PROJECT for audit.", cid)
        
        project_path = Path(target).resolve()
        
        # 2. Logic: Physical Project Verification
        findings = []
        essentials = ["PRP_CONTRACT.json", "TASKS", "LOGS"]
        
        for file in essentials:
            if not (project_path / file).exists():
                 findings.append(f"CRITICAL: Missing required factory component '{file}' in project.")

        health_score = 100 if not findings else 80

        # 3. Report Persistence
        audit_id = f"AUDIT-{datetime.now().strftime('%Y%m%d')}"
        logs_dir = project_path / "LOGS" / "audits"
        logs_dir.mkdir(parents=True, exist_ok=True)
        report_file = logs_dir / f"{audit_id}_{cid}.txt"
        report_file.write_text(f"Project Audit Score: {health_score}\nFindings: {findings}", encoding="utf-8")

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "health_score": health_score,
                "findings": findings,
                "audit_id": audit_id,
                "target_verified": str(project_path),
                "industrial_verification": True
            },
            correlation_id=cid,
            artifacts=[str(report_file)]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Factory Audit Failed: {str(e)}", cid)
