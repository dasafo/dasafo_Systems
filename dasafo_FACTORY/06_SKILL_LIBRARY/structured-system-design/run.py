import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Structured System Design (ORCHESTRATOR)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Tracks the TEA cycle state and enforces phase gate transitions.
"""

from __future__ import annotations
import os
import json
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    agent = "ORCHESTRATOR"
    skill = "structured-system-design"
    cid = skill_input.correlation_id

    try:
        # 1. Resolve Target
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "Missing TARGET_PROJECT", cid)
        
        state_dir = Path(target).resolve() / "LOCAL_KNOWLEDGE"
        state_dir.mkdir(parents=True, exist_ok=True)
        state_file = state_dir / "ssd-state.json"
        
        # 2. Logic (TEA State Tracking)
        phase = skill_input.params.get("current_phase", "M1")
        
        # Load or Init State
        if state_file.exists():
             state = json.loads(state_file.read_text())
        else:
             state = {"phase": phase, "tea": "T", "verdict": "PENDING"}

        state["phase"] = phase
        state_file.write_text(json.dumps(state, indent=2))

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "tea_loop_status": state["tea"],
                "phase_gate_verdict": state["verdict"],
                "next_atomic_tasks": ["Research local stack", "Verify credentials"]
            },
            correlation_id=cid,
            artifacts=[str(state_file)]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"SSD Orchestration Failed: {str(e)}", cid)
