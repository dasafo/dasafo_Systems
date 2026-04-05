import os
import json
import time
import re
from pathlib import Path
import redis # 👈 Nueva dependencia Engram

# Logic based on: https://skills.sh/phuryn/pm-skills/sentiment-analysis

# Inicialización del Cliente Redis (Conexión industrial)
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)

def execute_feedback_analysis(
    target_project: str,
    agent: str,
    action: str = "analyze_file",
    file_path: str = "LOGS/FEEDBACK-LOG.md",
    raw_text: str = None,
    overwrite: bool = False
) -> tuple[dict, list]:
    """Pure logic for autonomous feedback analysis and LTP/Engram sync (v5.0-MCP)."""
    start_time = time.time()
    project_path = Path(target_project).resolve()
    logs_dir = project_path / "LOGS"
    
    # Context pointers resolution
    if action == "analyze_file":
        input_file = project_path / file_path
        if not input_file.exists():
            raise FileNotFoundError(f"Feedback log not found at {input_file}")
        content = input_file.read_text(encoding="utf-8")
    else:
        content = raw_text or ""

    total_bytes_processed = len(content.encode("utf-8"))
    golden_rules_extracted = []
    critical_errors = 0

    # Pattern analysis
    entries = re.findall(r'(\{.*?\})', content, re.DOTALL)
    for entry_raw in entries:
        try:
            entry = json.loads(entry_raw)
            if "golden_rule" in entry:
                # Basic tech deduction
                tech = "global"
                f_path = entry.get("context", {}).get("file", "").lower()
                if "shadcn" in f_path: tech = "shadcn"
                elif ".py" in f_path: tech = "fastapi"
                
                phase = entry.get("context", {}).get("phase", "M3_PRODUCTION")
                rule = entry["golden_rule"]
                
                golden_rules_extracted.append({
                    "rule": rule,
                    "tech": tech,
                    "phase": phase
                })

                # --- FASE 2: ENGRAM INJECTION EN TIEMPO REAL ---
                # Aceleramos la disponibilidad de la regla poniéndola en Caché
                try:
                    cache_key = f"dasafo:engram:rules:{phase}:{tech}"
                    cached_rules = redis_client.get(cache_key)
                    rules_list = json.loads(cached_rules) if cached_rules else []
                    
                    if rule not in rules_list:
                        rules_list.append(rule)
                        redis_client.set(cache_key, json.dumps(rules_list), ex=14400) # TTL 4 horas
                except Exception:
                    pass # Caer silenciosamente si Redis falla, Neo4j es el primario

            if entry.get("severity") in ["critical", "high"]:
                critical_errors += 1
        except: continue

    # LTP Sync (Neo4j)
    # Se asume que persist_to_knowledge_graph existe y gestiona el guardado a largo plazo.
    try:
        from .logic import persist_to_knowledge_graph
        sync_success, sync_msg = persist_to_knowledge_graph(
            golden_rules_extracted, project_path.name, agent
        )
    except ImportError:
        sync_success, sync_msg = False, "persist_to_knowledge_graph logic is missing or decoupled."

    # DAST Persistence
    report_name = f"ANALYSIS_LTP_{int(time.time())}.json"
    report_path = logs_dir / report_name
    
    analysis_data = {
        "industrial_status": "SOLIDIFIED - FEEDBACK ANALYZED",
        "metrics": {
            "total_rules": len(golden_rules_extracted),
            "payload_bytes": total_bytes_processed
        },
        "ltp_sync": {"success": sync_success, "message": sync_msg}
    }
    
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(analysis_data, f, indent=2)

    return analysis_data, [str(report_path)]