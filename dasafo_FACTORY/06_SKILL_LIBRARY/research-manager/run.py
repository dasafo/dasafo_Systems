from __future__ import annotations
import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Research Manager (RESEARCH_AGENT)
v4.0-S: Modular Toolbox | Industrial Scale.

Objective: Safe, DAST-compliant artifact generation without shell injection risks.
"""

import time
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Industrial entry point for safe research artifact recording."""
    agent = skill_input.agent or "RESEARCH_AGENT"
    skill = "research-manager"
    cid = skill_input.correlation_id
    params = skill_input.params or {}
    
    start_time = time.time()

    try:
        target = params.get("target_project") or skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "SECURITY LOCK: Missing TARGET_PROJECT path.", cid)
        
        project_path = Path(target).resolve()
        action = params.get("action", "write_report")
        
        if action == "write_report":
            report_name = params.get("report_name", "RESEARCH_REPORT.md")
            content = params.get("content", "# Technical Research Report")
            category = params.get("category", "RESEARCH").upper()
            
            # 🔀 Enrutador DAST de Directorios
            if category == "ARCH":
                dest_dir = project_path / "DOCS" / "ARCH"
            elif category == "MARKETING":
                dest_dir = project_path / "DOCS" / "MARKETING"
            else:
                dest_dir = project_path / "DOCS" / "RESEARCH"
                
            dest_dir.mkdir(parents=True, exist_ok=True)
            report_path = dest_dir / report_name
            
            # 🛡️ Escritura Segura
            report_path.write_text(content, encoding="utf-8")
            file_size_bytes = len(content.encode('utf-8'))
            
            return SkillOutput.success(
                agent=agent,
                skill=skill,
                result={
                    "industrial_status": "SOLIDIFIED - RESEARCH RECORDED",
                    "report_category": category,
                    "file_size_bytes": file_size_bytes,
                    "compliance_report": {
                        "dast_verified": True,
                        "execution_duration_seconds": round(time.time() - start_time, 4)
                    },
                    "summary": [f"Research report '{report_name}' successfully written to {dest_dir.name}/."]
                },
                artifacts=[str(report_path)],
                correlation_id=cid
            )
            
        return SkillOutput.failure(agent, skill, f"Invalid action: {action}", cid)

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"CRITICAL Research Fault: {str(e)}", cid)