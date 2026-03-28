import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Apify Trend Analysis (MARKETING_GROWTH)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Executes Apify actors to gather trend intelligence.
"""

import os
import json
from datetime import datetime
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Industrialized entry point: Strict Deterministic Check."""
    agent = "MARKETING_GROWTH"
    skill = "apify-trend-analysis"
    cid = skill_input.correlation_id

    try:
        # 0. Strict API Enforcement (Zero-Trust)
        if not os.environ.get("APIFY_API_TOKEN"):
             return SkillOutput.failure(agent, skill, "SECURITY LOCK: APIFY_API_TOKEN is missing. Mock execution is forbidden in v3.2.4-S.", cid)

        try:
             import apify_client
        except ImportError:
             return SkillOutput.failure(agent, skill, "DEPENDENCY FATAL: apify-client is not installed in the environment.", cid)

        # 1. Path Resolution
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
            return SkillOutput.failure(agent, skill, "Missing TARGET_PROJECT", cid)
        
        project_path = Path(target).resolve()
        actor = skill_input.params.get("actor")
        if not actor:
            return SkillOutput.failure(agent, skill, "Missing 'actor' parameter.", cid)

        # 2. Logic: Physical Client interaction
        client = apify_client.ApifyClient(os.environ["APIFY_API_TOKEN"])
        
        # Initiate the run
        run_data = client.actor(actor).call()
        dataset_id = run_data.get("defaultDatasetId")
        
        if not dataset_id:
            return SkillOutput.failure(agent, skill, f"Actor {actor} failed to yield a dataset.", cid)
            
        items = client.dataset(dataset_id).list_items().items
        
        timestamp = datetime.now().strftime("%Y-%m-%d")
        safe_actor = actor.replace("/", "_")
        results_dir = project_path / "LOCAL_KNOWLEDGE" / "trends"
        results_dir.mkdir(parents=True, exist_ok=True)
        results_file = results_dir / f"{timestamp}_{safe_actor}.json"

        output_payload = {
            "actor": actor,
            "timestamp": timestamp,
            "data_points": len(items),
            "raw_data": items
        }

        with open(results_file, "w", encoding="utf-8") as f:
            json.dump(output_payload, f, indent=2)

        # 3. Return
        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "status": "SUCCESS",
                "data_points_count": len(items),
                "industrial_verification": True,
                "file": str(results_file)
            },
            correlation_id=cid,
            artifacts=[str(results_file)]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Trend Analysis Failed: {str(e)}", cid)
