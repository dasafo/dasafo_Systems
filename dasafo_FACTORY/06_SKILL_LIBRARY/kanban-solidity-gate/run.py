import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Kanban Solidity Gate (ORCHESTRATOR)
v3.2.0-S: Modular Toolbox | Industrial Scale.

IMPORTANCE: This is the most critical skill. It acts as the 'Aduana Universal',
enforcing the Zero-Pending Rule across the project life cycle.
"""

from __future__ import annotations
import os
import json
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """
    Standardized entry point for the 'Solidity Guard'.
    """
    # Dynamic identity for industrial traceability
    agent = skill_input.agent or "ORCHESTRATOR"
    skill = skill_input.skill or "kanban-solidity-gate"
    cid = skill_input.correlation_id

    try:
        # 1. Path Resolution
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "Mission Blocked: TARGET_PROJECT is missing.", cid)
        
        project_path = Path(target).resolve()
        registry_path = project_path / "TASKS" / "registry.json"
        state_path = project_path / "PROJECT_STATE.json"

        if not registry_path.exists():
            return SkillOutput.failure(agent, skill, f"Solidity Guard Violation: {registry_path} not found.", cid)

        # 2. Load Logistics (SSoT)
        with open(registry_path, 'r', encoding='utf-8') as f:
            registry = json.load(f)
        
        with open(state_path, 'r', encoding='utf-8') as f:
            state = json.load(f)

        current_phase = state.get("project_status", "DISCOVERY")
        
        # 3. Core Logic: Zero-Pending Rule
        # Filters tasks belonging to the current phase that are NOT completed/approved.
        blocking_tasks = [
            t for t in registry 
            if t.get("phase") == current_phase and t.get("status") not in ["COMPLETED", "APPROVED"]
        ]

        total_phase_tasks = len([t for t in registry if t.get("phase") == current_phase])
        completed_count = total_phase_tasks - len(blocking_tasks)
        
        # Calculate Solidity Score (SI units not applicable for pure ratios, but logic is SI-ready)
        solidity_score = completed_count / total_phase_tasks if total_phase_tasks > 0 else 1.0
        gate_passed = len(blocking_tasks) == 0

        # 4. Result Formulation
        result_payload = {
            "gate_passed": gate_passed,
            "solidity_score": round(solidity_score, 4),
            "current_phase": current_phase,
            "reason": "All tasks solidified." if gate_passed else f"Found {len(blocking_tasks)} pending tasks in {current_phase}.",
            "pending_tasks": [t.get("id") for t in blocking_tasks],
            "project_path": str(project_path)
        }

        # 5. Success Return (No artifacts created, strictly a validation gate)
        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result=result_payload,
            correlation_id=cid,
            artifacts=[]
        )

    except Exception as e:
        # Resilient Error Handling
        return SkillOutput.failure(agent, skill, f"Critical Gate Failure: {str(e)}", cid)