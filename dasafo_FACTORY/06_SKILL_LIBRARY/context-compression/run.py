import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Context Compression (MEMORY_OPTIMIZER)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Compresses episodic logs into semantic memory assets.
"""

import os
import shutil
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Industrialized entry point: Physical Zip Compression."""
    agent = "MEMORY_OPTIMIZER"
    skill = "context-compression"
    cid = skill_input.correlation_id

    try:
        # 1. Path Resolution
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
            return SkillOutput.failure(agent, skill, "Missing TARGET_PROJECT", cid)
        
        project_path = Path(target).resolve()
        source_dir = project_path / "LOCAL_KNOWLEDGE"
        
        if not source_dir.exists():
            return SkillOutput.failure(agent, skill, "LOCAL_KNOWLEDGE not found. Nothing to compress.", cid)
            
        # 2. Logic: Physical Compression
        archive_name = project_path / "LOGS" / f"knowledge_compress_{cid}"
        shutil.make_archive(str(archive_name), 'zip', str(source_dir))
        
        final_zip = archive_name.with_suffix('.zip')
        size_bytes = final_zip.stat().st_size
        
        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "archive_size_bytes": size_bytes,
                "status": "PHYSICALLY_COMPRESSED",
                "industrial_verification": True,
                "index_path": str(final_zip)
            },
            correlation_id=cid,
            artifacts=[str(final_zip)]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Compression Failed: {str(e)}", cid)
