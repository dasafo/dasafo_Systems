from __future__ import annotations
import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Apify Trend Analysis (MARKETING_GROWTH / RESEARCH_AGENT)
v3.4.0-S: Modular Toolbox | Industrial Scale.

Executes and manages Apify Actors for market trend analysis.
Based on apify-trend-analysis/agent-skills logic.
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

    try:
        # 0. Security Guard (Zero-Trust)
        token = os.environ.get("APIFY_API_TOKEN") or os.environ.get("APIFY_TOKEN")
        if not token:
             return SkillOutput.failure(agent, skill, "SECURITY LOCK: APIFY_API_TOKEN is missing. Live execution is required.", cid)

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

        if not actor_id:
             return SkillOutput.failure(agent, skill, "INPUT_ERROR: Missing 'actor' parameter.", cid)

        # 2. Logical Core
        if action == "fetch_details":
            # Fetch Actor Schema & Metadata
            actor_details = client.actor(actor_id).get()
            if not actor_details:
                return SkillOutput.failure(agent, skill, f"Actor {actor_id} not found or inaccessible.", cid)
            
            return SkillOutput.success(
                agent=agent,
                skill=skill,
                result={"status": "METADATA_FETCHED", "actor_details": actor_details},
                correlation_id=cid,
                artifacts=[]
            )

        elif action == "run_actor":
            # Execution (Physical API Call)
            input_data = params.get("input_data", {})
            
            # Start and wait for completion
            actor_run = client.actor(actor_id).call(run_input=input_data)
            dataset_id = actor_run.get("defaultDatasetId")
            
            if not dataset_id:
                 return SkillOutput.failure(agent, skill, f"Actor {actor_id} run did not produce a dataset.", cid)

            # Fetch results
            dataset_items = client.dataset(dataset_id).list_items().items
            
            # 3. Persistence (SI Compliance)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
            safe_actor = actor_id.replace("/", "_")
            results_dir = project_path / "LOCAL_KNOWLEDGE" / "trends"
            results_dir.mkdir(parents=True, exist_ok=True)
            
            out_format = params.get("format", "json").lower()
            file_name = f"{timestamp}_{safe_actor}.{out_format}"
            results_file = results_dir / file_name

            if out_format == "json":
                results_file.write_text(json.dumps(dataset_items, indent=2, ensure_ascii=False), encoding="utf-8")
            else:
                # Basic CSV generation for trend items
                import csv
                if dataset_items:
                    keys = dataset_items[0].keys()
                    with open(results_file, 'w', newline='', encoding='utf-8') as f:
                        dict_writer = csv.DictWriter(f, fieldnames=keys)
                        dict_writer.writeheader()
                        dict_writer.writerows(dataset_items)
                else:
                    results_file.touch()

            # 4. Insights Preparation
            insights = f"Capture complete: {len(dataset_items)} data points extracted from '{actor_id}'."
            if not dataset_items:
                insights += " WARNING: No data was found for the given parameters."

            result_payload = {
                "status": "TREND_CAPTURED",
                "summary": {
                    "actor_used": actor_id,
                    "data_points_count": len(dataset_items),
                    "file_path": str(results_file),
                    "execution_time_s": actor_run.get("finishedAt", 0) # Could calculate if needed
                },
                "insights": insights,
                "recommendations": [
                    "Analyze high-frequency keywords for content gap opportunities.",
                    "Cross-reference this data with Google Keyword Planner.",
                    "Look for rising hashtags that haven't peaked yet.",
                    "Save raw data for historical trend comparison."
                ]
            }

            return SkillOutput.success(
                agent=agent,
                skill=skill,
                result=result_payload,
                correlation_id=cid,
                artifacts=[str(results_file)]
            )

        else:
             return SkillOutput.failure(agent, skill, f"Invalid action: {action}", cid)

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Trend Analysis CRITICAL Fault: {str(e)}", cid)
