import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Cost Tracker (ORCHESTRATOR / PRODUCT_OWNER)
v3.3.0-S: Modular Toolbox | Industrial Scale.

Estimates token costs, monitor infrastructure spend, and enforce project budgets.
"""

from __future__ import annotations
import os
import json
import time
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

# Industrial Pricing Model (v3.3.0-S Baseline)
PRICING = {
    "claude-3-5-sonnet": {"in": 3.0, "out": 15.0},  # $ per 1M tokens
    "claude-3-opus": {"in": 15.0, "out": 75.0},
    "gemini-1.5-pro": {"in": 3.5, "out": 10.5},
    "default": {"in": 10.0, "out": 30.0}
}

def run(skill_input: SkillInput) -> SkillOutput:
    """Industrialized entry point for cost tracking."""
    agent = skill_input.agent or "ORCHESTRATOR"
    skill = "cost-tracker"
    cid = skill_input.correlation_id

    try:
        # 1. Path Resolution
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
            return SkillOutput.failure(agent, skill, "Missing TARGET_PROJECT context.", cid)
        
        project_path = Path(target).resolve()
        costs_file = project_path / "PROJECT_COSTS.json"

        # 2. Parameters
        in_tokens = skill_input.params.get("input_tokens", 0)
        out_tokens = skill_input.params.get("output_tokens", 0)
        model_id = skill_input.params.get("model_id", "claude-3-5-sonnet")
        
        price = PRICING.get(model_id, PRICING["default"])
        current_tx_cost = (in_tokens * price["in"] / 10**6) + (out_tokens * price["out"] / 10**6)

        # 3. Persistence (Ledger Management)
        if costs_file.exists():
            with open(costs_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = {
                "project_name": project_path.name,
                "version": "3.3.0-S",
                "accumulated_cost": 0.0,
                "budget_limit": 50.0,
                "currency": "USD",
                "last_transaction": "",
                "history": []
            }

        data["accumulated_cost"] += current_tx_cost
        data["last_transaction"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        
        # Add to history if cost is significant
        if current_tx_cost > 0:
            data["history"].append({
                "timestamp": data["last_transaction"],
                "agent": agent,
                "cost": round(current_tx_cost, 6),
                "cid": cid
            })

        # Keep history manageable (last 50 tx)
        data["history"] = data["history"][-50:]

        with open(costs_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        # 4. Budget Check
        status = "OK"
        budget_limit = data.get("budget_limit", 50.0)
        if data["accumulated_cost"] >= budget_limit:
            status = "BUDGET_EXCEEDED"
        elif data["accumulated_cost"] >= (budget_limit * 0.8):
            status = "WARNING"

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "current_cost": round(current_tx_cost, 6),
                "total_accumulated": round(data["accumulated_cost"], 4),
                "budget_limit": budget_limit,
                "status": status,
                "ledger": str(costs_file)
            },
            correlation_id=cid,
            artifacts=[str(costs_file)]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Cost Tracking Fault: {str(e)}", cid)
