import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — FastAPI Repository Pattern (BACKEND_DEV)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Scaffolds a clean FastAPI project structure following Repository and Service patterns.
"""

from __future__ import annotations
import os
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    agent = "BACKEND_DEV"
    skill = "fastapi-repository-pattern"
    cid = skill_input.correlation_id

    try:
        # 1. Resolve Paths
        module = skill_input.params.get("module_name", "core")
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "Missing TARGET_PROJECT", cid)
        
        app_root = Path(target).resolve() / "app"
        
        # 2. Logic (Scaffolding Simulation)
        folders = ["models", "repositories", "services", "api", "schemas"]
        generated = []
        
        for folder in folders:
            f_path = app_root / folder
            f_path.mkdir(parents=True, exist_ok=True)
            init_file = f_path / "__init__.py"
            init_file.touch()
            generated.append(str(init_file))

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "scaffold_status": "CREATED",
                "files_generated": generated,
                "vibe_check": "SOLID"
            },
            correlation_id=cid,
            artifacts=generated
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Scaffolding Failed: {str(e)}", cid)
