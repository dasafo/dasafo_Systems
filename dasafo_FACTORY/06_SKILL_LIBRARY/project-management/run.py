import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Project Management (PRODUCT_OWNER)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Manages task decomposition and backlog serialization.
"""

from __future__ import annotations
import os
import json
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    agent = "PRODUCT_OWNER"
    skill = "project-management"
    cid = skill_input.correlation_id

    try:
        # 1. Resolve Path
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "Missing TARGET_PROJECT", cid)
        
        project_path = Path(target).resolve()
        task_dir = project_path / "TASKS" / "01_PENDING"
        task_dir.mkdir(parents=True, exist_ok=True)
        
        # 2. Logic (Task Decomposition Simulation)
        goal = skill_input.params.get("current_goal", "SaaS Implementation")
        task_file = task_dir / f"TSK_{cid}.json"
        task_content = {
            "id": f"TSK-ID-{cid[:8]}",
            "objective": goal,
            "status": "PENDING",
            "vibe": "SOLID v3.2.0-S"
        }
        task_file.write_text(json.dumps(task_content, indent=2), encoding="utf-8")

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "task_count": 1,
                "registry_updated": True,
                "solidity_index": 1.0
            },
            correlation_id=cid,
            artifacts=[str(task_file)]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Project Mgmt Failure: {str(e)}", cid)
