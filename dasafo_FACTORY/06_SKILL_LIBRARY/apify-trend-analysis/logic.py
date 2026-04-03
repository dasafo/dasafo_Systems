import os
import json
import time
from datetime import datetime
from pathlib import Path

def execute_trend_analysis(
    target_project: str, 
    actor_id: str, 
    input_data: dict = None, 
    overwrite: bool = False
) -> tuple[dict, list]:
    """Lógica pura de captura de tendencias vía Apify (v5.0-MCP)."""
    start_time = time.time()
    
    # Security Guard (Zero-Trust)
    token = os.environ.get("APIFY_API_TOKEN") or os.environ.get("APIFY_TOKEN")
    if not token:
         raise PermissionError("SECURITY LOCK: APIFY_API_TOKEN is missing in INFRA/.env.")

    from apify_client import ApifyClient
    client = ApifyClient(token)
    project_path = Path(target_project).resolve()

    # Ejecución del Actor
    actor_run = client.actor(actor_id).call(run_input=input_data or {})
    dataset_id = actor_run.get("defaultDatasetId")
    
    if not dataset_id:
          raise ValueError(f"Actor {actor_id} run did not produce a dataset.")

    dataset_items = client.dataset(dataset_id).list_items().items
    
    # Persistencia DAST
    results_dir = project_path / "LOCAL_KNOWLEDGE" / "trends"
    results_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    safe_actor = actor_id.replace("/", "_")
    file_name = f"{timestamp}_{safe_actor}.json"
    results_file = results_dir / file_name

    if results_file.exists() and not overwrite:
         raise FileExistsError(f"REDUNDANCY LOCK: {file_name} ya existe.")

    results_file.write_text(json.dumps(dataset_items, indent=2, ensure_ascii=False), encoding="utf-8")
    
    result = {
        "industrial_status": "TREND_CAPTURED",
        "summary": f"Captured {len(dataset_items)} trends from actor {actor_id}.",
        "file_path": str(results_file),
        "execution_duration_seconds": round(time.time() - start_time, 4)
    }
    
    return result, [str(results_file)]