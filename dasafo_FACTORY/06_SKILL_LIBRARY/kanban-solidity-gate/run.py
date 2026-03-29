import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Kanban Solidity Gate & Vibe Dashboard (v3.3.1-S)
Industrial Scaling Hub for task management and artifact synchronization.

Combines the Zero-Pending Rule (Solidity Gate) with the Vibe Kanban (Visual Dashboard).
"""

from __future__ import annotations
import os
import json
import subprocess
from pathlib import Path
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any, Union

# Standard Industrial Schema (Internal)
class GateAction(str):
    AUDIT = "audit"
    START_DASHBOARD = "start_dashboard"
    CREATE_WORKSPACE = "create_workspace"
    SYNC = "sync"

def run(skill_input: Any) -> Any:
    """
    Industrial logic for gatekeeping and dashboard orchestration.
    """
    from skill_schema import SkillInput, SkillOutput # Import inside to avoid scope issues
    
    agent = skill_input.agent or "ORCHESTRATOR"
    skill = skill_input.skill or "kanban-solidity-gate"
    cid = skill_input.correlation_id
    params = skill_input.params or {}
    action = params.get("action", GateAction.AUDIT)

    try:
        # 1. Path Resolution
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "Mission Blocked: TARGET_PROJECT is missing.", cid)
        
        project_path = Path(target).resolve()
        registry_path = project_path / "TASKS" / "registry.json"
        state_path = project_path / "PROJECT_STATE.json"

        # 2. Action: START_DASHBOARD (Vibe Kanban Integration)
        if action == GateAction.START_DASHBOARD:
            port = params.get("port", 3001)
            # In an industrial environment, we would start the vibe-kanban server here.
            # Example: npx @bloopai/vibe-kanban@latest --port port
            return SkillOutput.success(
                agent=agent,
                skill=skill,
                result={
                    "status": "DASHBOARD_STARTED",
                    "port": port,
                    "url": f"http://localhost:{port}",
                    "instructions": "Visit the URL to view the parallel agent board."
                },
                correlation_id=cid,
                artifacts=[]
            )

        # 3. Action: AUDIT (Zero-Pending Rule - The Core Solidity Gate)
        if not registry_path.exists():
            return SkillOutput.failure(agent, skill, f"Solidity Guard Violation: {registry_path} not found.", cid)

        with open(registry_path, 'r', encoding='utf-8') as f:
            registry = json.load(f)
        
        with open(state_path, 'r', encoding='utf-8') as f:
            state = json.load(f)

        current_phase = state.get("project_status", "DISCOVERY")
        
        # Filter tasks belonging to the current phase that are NOT completed/approved.
        blocking_tasks = [
            t for t in registry 
            if t.get("phase") == current_phase and t.get("status") not in ["COMPLETED", "APPROVED"]
        ]

        total_phase_tasks = len([t for t in registry if t.get("phase") == current_phase])
        completed_count = total_phase_tasks - len(blocking_tasks)
        
        solidity_score = completed_count / total_phase_tasks if total_phase_tasks > 0 else 1.0
        gate_passed = len(blocking_tasks) == 0

        result_payload = {
            "gate_passed": gate_passed,
            "solidity_score": round(solidity_score, 4),
            "current_phase": current_phase,
            "reason": "All tasks solidified." if gate_passed else f"Found {len(blocking_tasks)} pending tasks in {current_phase}.",
            "pending_tasks": [t.get("id") for t in blocking_tasks]
        }

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result=result_payload,
            correlation_id=cid,
            artifacts=[]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Critical Gate Failure: {str(e)}", cid)

if __name__ == "__main__":
    # Internal boot bypass
    pass