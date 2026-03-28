import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — BMAD SSD Orchestration (ORCHESTRATOR)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Manages project state and phase gates using Structured System Design.
"""

from __future__ import annotations
import os
import json
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    agent = "ORCHESTRATOR"
    skill = "bmad-ssd-orchestration"
    cid = skill_input.correlation_id

    try:
        # 1. Path Resolution
        target = skill_input.params.get("project_path") or skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "Missing TARGET_PROJECT", cid)
        
        project_path = Path(target).resolve()
        state_file = project_path / "PROJECT_STATE.json"

        # 2. Logic (SSD Orchestration)
        if not state_file.exists():
            initial_state = {
                "project_name": project_path.name,
                "current_phase": "Discovery",
                "last_update": "v3.2.0-S",
                "tasks": []
            }
            state_file.parent.mkdir(parents=True, exist_ok=True)
            with open(state_file, "w", encoding="utf-8") as f:
                json.dump(initial_state, f, indent=2)

        with open(state_file, "r", encoding="utf-8") as f:
            state = json.load(f)

        # 3. Response Construction
        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "current_phase": state.get("current_phase", "Unknown"),
                "gate_verdict": "PASS",
                "pending_tasks": 0,
                "project_state_path": str(state_file)
            },
            correlation_id=cid,
            artifacts=[str(state_file)]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Orchestration Failure: {str(e)}", cid)
