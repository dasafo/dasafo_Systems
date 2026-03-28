import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Documentation Strategist (TECHNICAL_WRITER)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Audits and maps the documentation architecture of the factory.
"""

import os
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Industrialized entry point: Physical Markdown Validation."""
    agent = "TECHNICAL_WRITER"
    skill = "documentation-strategist"
    cid = skill_input.correlation_id

    try:
        # 1. Resolve Path
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "Missing TARGET_PROJECT", cid)
        
        project_path = Path(target).resolve()
        
        # 2. Physical File Scanning
        required_docs = {"README.md", "CONTRIBUTING.md", "ARCHITECTURE.md"}
        found_docs = set()
        
        # scan for standard markdown files in root
        for f in project_path.iterdir():
            if f.is_file() and f.name in required_docs:
                found_docs.add(f.name)
                
        # scan DOCS folder if exists
        docs_dir = project_path / "DOCS"
        if docs_dir.exists():
            for f in docs_dir.iterdir():
                if f.is_file() and f.name in required_docs:
                    found_docs.add(f.name)

        missing_docs = list(required_docs - found_docs)
        
        hierarchy = {
            "root": str(project_path),
            "docs_present": str(docs_dir.exists())
        }

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "hierarchy": hierarchy,
                "missing_docs": missing_docs,
                "health_status": "OK" if not missing_docs else "NEEDS_DOCUMENTATION",
                "industrial_verification": True
            },
            correlation_id=cid,
            artifacts=[]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Doc Strategy Failure: {str(e)}", cid)
