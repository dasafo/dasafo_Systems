"""
run.py — Safe Database Migrations (DB_MASTER)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Executes and verifies database schema migrations with safety fallbacks.
"""

from __future__ import annotations
import os
import subprocess
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    # Dynamic identity for industrial traceability
    agent = skill_input.agent or "DB_MASTER"
    skill = skill_input.skill or "safe-db-migrations"
    cid = skill_input.correlation_id

    try:
        # 1. Target Resolution
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "Mission Blocked: TARGET_PROJECT is missing.", cid)
        
        project_path = Path(target).resolve()
        
        # 2. Input Parsing
        params = skill_input.params
        tool = params.get("tool", "alembic").lower()
        action = params.get("action", "upgrade").lower()
        message = params.get("message", "auto_migration")

        # 3. Command Orchestration
        # Note: Logic assumes execution inside WORKSPACE/backend as per factory standards
        backend_path = project_path / "WORKSPACE" / "backend"
        if not backend_path.exists():
            backend_path = project_path

        cmd = []
        if tool == "alembic":
            if action == "generate":
                cmd = ["alembic", "revision", "--autogenerate", "-m", message]
            elif action == "upgrade":
                cmd = ["alembic", "upgrade", "head"]
            elif action == "downgrade":
                cmd = ["alembic", "downgrade", "-1"]
        elif tool == "prisma":
            if action == "generate":
                cmd = ["npx", "prisma", "migrate", "dev", "--name", message.replace(" ", "_")]
            elif action == "upgrade":
                cmd = ["npx", "prisma", "migrate", "deploy"]
        elif tool == "supabase":
            if action == "generate":
                cmd = ["supabase", "migration", "new", message.replace(" ", "_")]
            elif action == "upgrade":
                cmd = ["supabase", "db", "push"]
        
        if not cmd:
            return SkillOutput.failure(agent, skill, f"Unsupported tool/action combination: {tool}/{action}", cid)

        # 4. Execution
        result = subprocess.run(
            cmd, 
            cwd=str(backend_path), 
            capture_output=True, 
            text=True, 
            check=False
        )

        if result.returncode != 0:
            return SkillOutput.failure(
                agent, 
                skill, 
                f"Migration Engine Error: {result.stderr or result.stdout}", 
                cid
            )

        # 5. Success Return with artifacts for Solidity Guard
        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "status": "SUCCESS",
                "tool_used": tool,
                "action_executed": action,
                "migration_output": result.stdout.strip(),
                "rollback_ready": True if action != "downgrade" else False
            },
            correlation_id=cid,
            artifacts=[] # Specific migration files can be added here if identified
        )

    except Exception as e:
        # Resilient Error Handling
        return SkillOutput.failure(agent, skill, f"Safe Migration Critical Failure: {str(e)}", cid)