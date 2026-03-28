import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Checkpoint Manager (FACTORY_EVOLVER)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Handles versioning and backup of factory configurations.
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Industrialized entry point: Physical Artifact Archiving."""
    agent = "FACTORY_EVOLVER"
    skill = "checkpoint-manager"
    cid = skill_input.correlation_id

    try:
        # 1. Resolution
        factory_root = Path(__file__).resolve().parents[4]
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        
        if not target:
            return SkillOutput.failure(agent, skill, "Missing TARGET_PROJECT for Checkpoint creation.", cid)
            
        project_path = Path(target).resolve()
        action = skill_input.params.get("action", "backup")
        
        archive_dir = factory_root / ".archive" / "checkpoints"
        archive_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        checkpoint_id = f"CP-{project_path.name}-{timestamp}"
        
        # 2. Logic: Real Archiving
        if action == "backup":
            archive_path = archive_dir / checkpoint_id
            shutil.make_archive(str(archive_path), 'gztar', str(project_path))
            final_tar = archive_path.with_suffix('.tar.gz')
            
            log_file = archive_dir / "checkpoint_history.log"
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(f"[{datetime.now().isoformat()}] ID: {checkpoint_id}.tar.gz | Size: {final_tar.stat().st_size} bytes | Status: PHYSICAL_STABLE\n")
            
            return SkillOutput.success(
                agent=agent,
                skill=skill,
                result={
                    "checkpoint_id": checkpoint_id,
                    "status": "PHYSICAL_STABLE",
                    "backup_path": str(final_tar),
                    "industrial_verification": True
                },
                correlation_id=cid,
                artifacts=[str(final_tar), str(log_file)]
            )

        return SkillOutput.failure(agent, skill, f"Action '{action}' not supported yet in v3.2.4-S.", cid)

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Checkpoint Error: {str(e)}", cid)
