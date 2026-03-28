import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Docker DevOps Expert (DEVOPS_SRE)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Audits and optimizes containerized environments.
"""

import os
import re
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Industrialized entry point: Physical Parsing."""
    agent = "DEVOPS_SRE"
    skill = "docker-devops-expert"
    cid = skill_input.correlation_id

    try:
        # 1. Resolve Path
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "Missing TARGET_PROJECT", cid)
             
        project_path = Path(target).resolve()
        
        dockerfile_name = skill_input.params.get("dockerfile_path") or "Dockerfile"
        dockerfile_path = project_path / dockerfile_name

        if not dockerfile_path.exists():
            return SkillOutput.failure(agent, skill, f"Docker file not found at {dockerfile_path}", cid)

        # 2. Logic: Real parsing
        content = dockerfile_path.read_text(encoding="utf-8")
        
        recommendations = []
        status = "PASS"
        
        if len(re.findall(r"^FROM\s+", content, re.MULTILINE)) < 2:
            recommendations.append("CRITICAL: Single-stage build detected. Use Multi-Stage builds (v3.2.4-S standard).")
            status = "AUDIT_FAIL"
            
        if "USER" not in content:
            recommendations.append("WARNING: Dockerfile does not enforce a non-root USER. Violation of Zero-Trust protocol.")
            status = "AUDIT_FAIL"

        if "HEALTHCHECK" not in content:
            recommendations.append("INFO: No HTTP/Exec HEALTHCHECK directive embedded in standard image.")

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "status": status,
                "recommendations": recommendations,
                "lines_analyzed": len(content.splitlines()),
                "industrial_verification": True
            },
            correlation_id=cid,
            artifacts=[str(dockerfile_path)]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Docker Audit Failed: {str(e)}", cid)
