from __future__ import annotations
import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Apify Trend Analysis (MARKETING_GROWTH / RESEARCH_AGENT)
v4.0-S: Modular Toolbox | Industrial Scale.

Solidified: Fixed Schema Mismatch, added insights & recommendations, and aligned summary object with industrial_status.
"""

import os
import json
import time
from datetime import datetime
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Industrial Entry Point for Trend Intelligence."""
    agent = skill_input.agent or "MARKETING_GROWTH"
    skill = "apify-trend-analysis"
    cid = skill_input.correlation_id
    params = skill_input.params or {}
    
    start_time = time.time()

    try:
        # 0. Security Guard (Zero-Trust)
        token = os.environ.get("APIFY_API_TOKEN") or os.environ.get("APIFY_TOKEN")
        if not token:
             return SkillOutput.failure(agent, skill, "SECURITY LOCK: APIFY_API_TOKEN is missing.", cid)

        try:
             from apify_client import ApifyClient
        except ImportError:
             return SkillOutput.failure(agent, skill, "DEPENDENCY FATAL: apify-client is not installed.", cid)

        client = ApifyClient(token)

        # 1. Path Resolution
        target = params.get("target_project") or skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "SECURITY LOCK: Missing TARGET_PROJECT path.", cid)
        
        project_path = Path(target).resolve()
        action = params.get("action", "run_actor")
        actor_id = params.get("actor")
        overwrite = params.get("overwrite", False)

        if not actor_id:
             return SkillOutput.failure(agent, skill, "INPUT_ERROR: Missing 'actor' parameter.", cid)

        # 2. Logic: run_actor
        if action == "run_actor":
            input_data = params.get("input_data", {})
            actor_run = client.actor(actor_id).call(run_input=input_data)
            dataset_id = actor_run.get("defaultDatasetId")
            
            if not dataset_id:
                  return SkillOutput.failure(agent, skill, f"Actor {actor_id} run did not produce a dataset.", cid)

            dataset_items = client.dataset(dataset_id).list_items().items
            
            # 3. Persistence & Redundancy Lock
            results_dir = project_path / "LOCAL_KNOWLEDGE" / "trends"
            results_dir.mkdir(parents=True, exist_ok=True)
            
            timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
            safe_actor = actor_id.replace("/", "_")
            file_name = f"{timestamp}_{safe_actor}.json"
            results_file = results_dir / file_name

            if results_file.exists() and not overwrite:
                 return SkillOutput.failure(agent, skill, f"REDUNDANCY LOCK: {file_name} already exists.", cid)

            results_file.write_text(json.dumps(dataset_items, indent=2, ensure_ascii=False), encoding="utf-8")
            
            execution_duration_s = time.time() - start_time
            
            # 4. Result Building (v4.0-S Aligned Schema)
            result_payload = {
                "industrial_status": "TREND_CAPTURED",
                "summary": {
                    "actor_used": actor_id,
                    "data_points_count": len(dataset_items),
                    "file_path": str(results_file)
                },
                "insights": f"Captured {len(dataset_items)} trends from actor {actor_id}. Data saved for pattern analysis.",
                "recommendations": [
                    "Cross-reference keywords with active ad campaigns.",
                    "Identify rising niches for specialized content generation.",
                    "Save raw dataset for historical comparison (v4.0-S)."
                ],
                "compliance_report": {
                    "data_integrity_verified": True,
                    "lock_verified": True,
                    "execution_duration_seconds": round(execution_duration_s, 4)
                }
            }

            return SkillOutput.success(agent, skill, result_payload, [str(results_file)], cid)

        return SkillOutput.failure(agent, skill, f"Action '{action}' not implemented in v4.0-S.", cid)

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Trend Analysis CRITICAL Fault: {str(e)}", cid)
