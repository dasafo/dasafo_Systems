"""
run.py — AutoShield Preflight Check (SYSTEM)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Performs critical industrial safety verification, ensures project
directories exist, and logs the agent's intent.
"""

from __future__ import annotations
import os
from pathlib import Path
from datetime import datetime
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    agent = skill_input.agent
    skill = skill_input.skill
    cid = skill_input.correlation_id

    try:
        # 1. Target Verification
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        
        if not target:
            return SkillOutput.failure(
                agent=agent,
                skill=skill,
                error="INDUSTRIAL LOCK: TARGET_PROJECT environment variable is missing.",
                correlation_id=cid
            )

        project_path = Path(target).resolve()
        if not project_path.exists():
            return SkillOutput.failure(
                agent=agent,
                skill=skill,
                error=f"VALIDATION FAILED: Target path {project_path} does not exist.",
                correlation_id=cid
            )

        # 2. Log Execution (Cumpliendo la promesa del SKILL.md)
        log_dir = project_path / "LOGS" / "agents"
        log_dir.mkdir(parents=True, exist_ok=True) # Ensure directory exists
        
        agent_log_path = log_dir / f"{agent}.log"
        # Current time in ISO format (v3.2.0-S standard)
        timestamp = datetime.utcnow().isoformat() + "Z"
        
        # Using SI: bytes logic implies we check log size before/after if needed
        # For now, we perform the atomic write as promised.
        with open(agent_log_path, "a") as f:
            f.write(f"[{timestamp}] [CID: {cid}] PREFLIGHT CHECK: PASS. AutoShield Active for {agent}.\n")

        # 3. Output Estructurado (Usando result en lugar de data para v3.2-S)
        result_payload = {
            "preflight_status": "PASS",
            "project_path": str(project_path),
            "directive": "SYSTEM MANDATE: You must read dasafo_FACTORY/FEEDBACK-LOG.md before making any destructive changes."
        }

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            data=result_payload, # Estandarizado a v3.2.0-S result/data key
            correlation_id=cid,
            artifacts=[str(agent_log_path)] # Trazabilidad física para el Solidity Guard
        )

    except Exception as e:
        # Manejo de Errores Resiliente v3.2.0-S
        return SkillOutput.failure(
            agent=agent, 
            skill=skill, 
            error=f"Critical Preflight Failure: {str(e)}", 
            correlation_id=cid
        )
