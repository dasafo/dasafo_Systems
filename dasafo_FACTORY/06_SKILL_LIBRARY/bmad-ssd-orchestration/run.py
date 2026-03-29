import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — BMAD SSD Orchestration (ORCHESTRATOR)
v3.3.0-S: Modular Toolbox | Industrial Scale.

Implements Structured System Design (SSD) with advanced phase-gate management.
"""

from __future__ import annotations
import os
import json
import time
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

PHASE_ORDER = ["Discovery", "Analysis", "Planning", "Solutioning", "Implementation", "Closure"]

def run(skill_input: SkillInput) -> SkillOutput:
    """Industrialized entry point for SSD Orchestration."""
    agent = "ORCHESTRATOR"
    skill = "bmad-ssd-orchestration"
    cid = skill_input.correlation_id

    try:
        # 1. Configuration & Path Resolution
        target = skill_input.params.get("project_path") or skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
            return SkillOutput.failure(agent, skill, "Missing TARGET_PROJECT context.", cid)
        
        project_path = Path(target).resolve()
        state_file = project_path / "PROJECT_STATE.json"
        registry_file = project_path / "TASKS" / "registry.json"
        action = skill_input.params.get("action", "status")

        # 2. State Initialization (if missing)
        if not state_file.exists():
            initial_state = {
                "project_name": project_path.name,
                "version": "3.3.0-S",
                "current_phase": "Discovery",
                "last_update": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "phases": {p: "PENDING" for p in PHASE_ORDER}
            }
            initial_state["phases"]["Discovery"] = "IN_PROGRESS"
            state_file.parent.mkdir(parents=True, exist_ok=True)
            with open(state_file, "w", encoding="utf-8") as f:
                json.dump(initial_state, f, indent=2)

        with open(state_file, "r", encoding="utf-8") as f:
            state = json.load(f)

        current_phase = state.get("current_phase", "Discovery")
        phases = state.get("phases", {})
        
        # 3. Task Validation Logic
        pending_dir = project_path / "TASKS" / "01_PENDING"
        progress_dir = project_path / "TASKS" / "02_IN_PROGRESS"
        
        pending_count = 0
        if pending_dir.exists():
            pending_count += len([f for f in os.listdir(pending_dir) if f.endswith(".json") or f.endswith(".md")])
        if progress_dir.exists():
            pending_count += len([f for f in os.listdir(progress_dir) if f.endswith(".json") or f.endswith(".md")])

        # 4. Action Dispatcher
        verdict = "PASS" if pending_count == 0 else "FAIL"
        message = f"Orchestration status for {current_phase}."

        if action == "validate":
            message = f"Validation for phase {current_phase}: {verdict}. (Pending: {pending_count} tasks)"
            
        elif action == "advance":
            if verdict == "FAIL":
                return SkillOutput.failure(agent, skill, f"Gate Blocked: Phase {current_phase} has {pending_count} pending tasks.", cid)
            
            # Transition Logic
            try:
                idx = PHASE_ORDER.index(current_phase)
                if idx < len(PHASE_ORDER) - 1:
                    next_phase = PHASE_ORDER[idx + 1]
                    phases[current_phase] = "APPROVED"
                    phases[next_phase] = "IN_PROGRESS"
                    state["current_phase"] = next_phase
                    state["last_update"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
                    
                    with open(state_file, "w", encoding="utf-8") as f:
                        json.dump(state, f, indent=2)
                    
                    message = f"Phase Gate SUCCESS: Advanced from {current_phase} to {next_phase}."
                    current_phase = next_phase
                else:
                    message = "Project successfully concluded (Closure Phase)."
            except ValueError:
                return SkillOutput.failure(agent, skill, f"Invalid current phase: {current_phase}", cid)

        # 5. Result Construction
        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "action": action,
                "current_phase": current_phase,
                "gate_verdict": verdict,
                "pending_tasks": pending_count,
                "message": message,
                "project_state": str(state_file)
            },
            correlation_id=cid,
            artifacts=[str(state_file)]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Orchestration Fault: {str(e)}", cid)
