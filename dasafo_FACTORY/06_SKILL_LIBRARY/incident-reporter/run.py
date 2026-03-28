import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Incident Reporter (DEVOPS_SRE)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Translates service failures into structured incident intelligence.
"""

from __future__ import annotations
import os
from pathlib import Path
from datetime import datetime
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    agent = "DEVOPS_SRE"
    skill = "incident-reporter"
    cid = skill_input.correlation_id

    try:
        # 1. Resolve Paths
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "Missing TARGET_PROJECT", cid)
        
        project_path = Path(target).resolve()
        
        # 2. Logic (Incident Formatting)
        url = skill_input.params.get("target_url", "UNKNOWN")
        code = skill_input.params.get("error_code", 500)
        priority = skill_input.params.get("priority", "HIGH")
        
        incident_id = f"INC-{datetime.now().strftime('%Y%m%d-%H%M')}"
        
        report = f"""🚨 MISSION CRITICAL INCIDENT | {incident_id}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Project: {project_path.name}
Target: {url}
Error Code: {code}
Priority: {priority}
Timestamp: {datetime.now().isoformat()}

Status: DOWN v3.2.0-S
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""

        report_dir = project_path / "LOGS" / "incidents"
        report_dir.mkdir(parents=True, exist_ok=True)
        report_file = report_dir / f"{incident_id}_{cid}.log"
        report_file.write_text(report, encoding="utf-8")

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "incident_id": incident_id,
                "incident_path": str(report_file),
                "status": "REPORTED"
            },
            correlation_id=cid,
            artifacts=[str(report_file)]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Incident Reporting Failed: {str(e)}", cid)
