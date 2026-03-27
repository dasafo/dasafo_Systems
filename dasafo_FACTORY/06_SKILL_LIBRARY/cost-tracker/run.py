"""
run.py — Cost Tracker (DEVOPS_SRE)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Estimates token costs and enforces project budgets.
"""

from __future__ import annotations
import os
import json
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    agent = "DEVOPS_SRE"
    skill = "cost-tracker"
    cid = skill_input.correlation_id

    try:
        # 1. Path Resolution
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "Missing TARGET_PROJECT", cid)
        
        project_path = Path(target).resolve()
        costs_file = project_path / "PROJECT_COSTS.json"

        # 2. Parameters
        in_tokens = skill_input.params.get("input_tokens", 0)
        out_tokens = skill_input.params.get("output_tokens", 0)
        
        # Mock Pricing ($15 per 1M in, $75 per 1M out for a flagship model)
        current_cost = (in_tokens * 15 / 10**6) + (out_tokens * 75 / 10**6)

        # 3. Persistence
        if costs_file.exists():
            with open(costs_file, "r") as f:
                data = json.load(f)
        else:
            data = {"accumulated_cost": 0.0, "budget": 10.0}

        data["accumulated_cost"] += current_cost
        
        with open(costs_file, "w") as f:
            json.dump(data, f, indent=2)

        # 4. Result
        status = "OK"
        if data["accumulated_cost"] >= data["budget"]:
            status = "BUDGET_EXCEEDED"
        elif data["accumulated_cost"] >= (data["budget"] * 0.8):
            status = "WARNING"

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "current_cost": current_cost,
                "accumulated_cost": data["accumulated_cost"],
                "budget_status": status
            },
            correlation_id=cid,
            artifacts=[str(costs_file)]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Cost Tracking Failed: {str(e)}", cid)
