import os
import json
import time
from pathlib import Path
import redis # 👈 Nueva dependencia Engram

# Logic based on internal/factory-doctor
# Standard: Stark-Solidity Forensic Audit (v5.0-MCP)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)

def execute_doctor(
    target_project: str,
    agent: str, # Ajustado para la firma del mcp_app
    action: str = "diagnose",
    strict_mode: bool = True,
    sync_neo4j: bool = True
) -> tuple[dict, list]:
    """Pure logic for forensic disk audit and project state reconstruction (v5.0-MCP)."""
    start_time = time.time()
    project_path = Path(target_project).resolve()
    tasks_root = project_path / "TASKS"
    
    if not project_path.exists():
        raise FileNotFoundError(f"PHYSICAL_ERROR: Project {target_project} not found.")

    # 1. FORENSIC SCAN (Dictatorship of the Disk)
    new_registry = []
    folders = {"PENDING": "01_PENDING", "IN_PROGRESS": "02_IN_PROGRESS", "COMPLETED": "03_COMPLETED"}
    
    for status, folder_name in folders.items():
        folder_path = tasks_root / folder_name
        if folder_path.exists():
            for task_file in folder_path.glob("*.json"):
                try:
                    with open(task_file, 'r', encoding='utf-8') as f:
                        task_data = json.load(f)
                        task_data["status"] = status
                        new_registry.append(task_data)
                except: continue

    # 2. ATOMIC SYNC: registry.json (tempfile + os.replace for POSIX atomicity)
    registry_file = tasks_root / "registry.json"
    import tempfile
    tmp_fd, tmp_path = tempfile.mkstemp(dir=str(tasks_root), suffix='.json.tmp')
    try:
        with os.fdopen(tmp_fd, 'w', encoding='utf-8') as tmp_f:
            json.dump(new_registry, tmp_f, indent=2)
        os.replace(tmp_path, str(registry_file))
    except Exception:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
        raise
    
    reg_size_b = registry_file.stat().st_size # SI Units: Bytes

    # 3. PHASE DETECTION BY ARTEFACT HIERARCHY (Deterministic cascade, no regression)
    # Order matters: check from highest phase down to lowest.
    detected_phase = "M1"
    workspace_path = project_path / "WORKSPACE"
    
    if (project_path / "INFRA" / "Dockerfile").exists() or (project_path / "DOCKER_IA_CONFIG.md").exists():
        detected_phase = "M5"
    elif (project_path / "LOGS" / "TEST_REPORTS.md").exists() or list((project_path / "LOGS").glob("*E2E*")) if (project_path / "LOGS").exists() else False:
        detected_phase = "M4"
    elif workspace_path.exists() and any(workspace_path.iterdir()):
        detected_phase = "M3"
    elif (project_path / "DOCS" / "ARCH").exists() and any((project_path / "DOCS" / "ARCH").glob("ADR-*.md")):
        detected_phase = "M2"
    elif (project_path / "PRP_CONTRACT.json").exists():
        detected_phase = "M1"

    # 4. HEALING: PROJECT_STATE.json
    state_file = project_path / "PROJECT_STATE.json"
    new_state = {
        "factory_version": "v5.0-MCP",
        "project_status": "SOLIDIFIED",
        "current_phase": detected_phase,
        "phases": {
            "M1": "APPROVED" if detected_phase in ["M2", "M3", "M4", "M5"] else "IN_PROGRESS",
            "M2": "APPROVED" if detected_phase in ["M3", "M4", "M5"] else ("IN_PROGRESS" if detected_phase == "M2" else "PENDING"),
            "M3": "APPROVED" if detected_phase in ["M4", "M5"] else ("IN_PROGRESS" if detected_phase == "M3" else "PENDING"),
            "M4": "PENDING", "M5": "PENDING"
        }
    }
    with open(state_file, 'w', encoding='utf-8') as f:
        json.dump(new_state, f, indent=2)

    # --- FASE 2: ENGRAM SYNC (Inyección de advertencia post-curación) ---
    try:
        cache_key = f"dasafo:engram:rules:{detected_phase}:global"
        cached_rules = redis_client.get(cache_key)
        rules_list = json.loads(cached_rules) if cached_rules else []
        
        healing_rule = f"CRITICAL CONTEXT ALERT: El estado del proyecto acaba de ser reconstruido por Factory Doctor a la fase {detected_phase}. Confía únicamente en los archivos físicos, no asumas contexto previo."
        
        if healing_rule not in rules_list:
            rules_list.append(healing_rule)
            redis_client.set(cache_key, json.dumps(rules_list), ex=14400) # TTL 4 horas
    except Exception:
        pass

    execution_duration_s = time.time() - start_time
    
    result_payload = {
        "industrial_status": "HEALED",
        "reconstructed_tasks": len(new_registry),
        "detected_phase": detected_phase,
        "metrics": {
            "registry_bytes": reg_size_b,
            "execution_duration_seconds": round(execution_duration_s, 4)
        },
        "summary": f"Forensic audit complete. Project healed to phase {detected_phase}. Registry rebuilt ({len(new_registry)} tasks)."
    }
    
    return result_payload, [str(registry_file), str(state_file)]