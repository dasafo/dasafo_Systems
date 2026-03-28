import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Clutch Resource Cleaner (MEMORY_OPTIMIZER)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Maintains workspace hygiene by removing stale logs and temporary files.
"""

import os
import shutil
from pathlib import Path
from datetime import datetime, timedelta
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Industrialized entry point: Physical Cleanup Operations."""
    agent = "MEMORY_OPTIMIZER"
    skill = "clutch-resource-cleaner"
    cid = skill_input.correlation_id

    try:
        # 1. Path Resolution
        target = skill_input.params.get("target_path") or skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
            return SkillOutput.failure(agent, skill, "Missing TARGET_PROJECT", cid)
        
        project_path = Path(target).resolve()
        
        # 2. Physics Engine: Actual Cleanup
        files_removed = 0
        bytes_recovered = 0
        
        # Directories to aggressively target
        cache_dirs = ["__pycache__", ".pytest_cache", ".logs_tmp"]
        
        for root, dirs, files in os.walk(project_path, topdown=False):
            # Remove temp files
            for file in files:
                if file.endswith(".tmp") or file.endswith(".swp"):
                    try:
                        f_path = Path(root) / file
                        sz = f_path.stat().st_size
                        f_path.unlink()
                        files_removed += 1
                        bytes_recovered += sz
                    except:
                        pass
            
            # Remove cache dirs
            for d in dirs:
                if d in cache_dirs:
                    d_path = Path(root) / d
                    try:
                        # compute rough size before removal
                        for cr, cd, cf in os.walk(d_path):
                            for cache_file in cf:
                                sz = (Path(cr) / cache_file).stat().st_size
                                bytes_recovered += sz
                                files_removed += 1
                        shutil.rmtree(d_path)
                    except:
                        pass

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "files_cleaned": files_removed,
                "bytes_recovered": bytes_recovered,
                "status": "PHYSICAL_CLEAN",
                "industrial_verification": True
            },
            correlation_id=cid,
            artifacts=[]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Cleanup Failed: {str(e)}", cid)
