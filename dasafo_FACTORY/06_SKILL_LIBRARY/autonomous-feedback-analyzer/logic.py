import os
import json
import time
import re
from pathlib import Path
from datetime import datetime
from neo4j import GraphDatabase

# autonomous-feedback-analyzer | LTP Persister v5.1-MCP (Solidified)
# ==============================================================================

def get_neo4j_driver():
    """Conectividad con Zero-Trust y Hostname Fallback."""
    uri = os.getenv("NEO4J_URI", "bolt://dasafo-shared-kg:7687")
    user = os.getenv("NEO4J_USER", "neo4j")
    pwd = os.getenv("NEO4J_PASSWORD")
    if not pwd:
        raise PermissionError("ZERO-TRUST: NEO4J_PASSWORD no configurado en entorno.")

    # Intentar Docker name -> Localhost
    uris_to_try = [uri]
    if "dasafo-shared-kg" in uri:
        uris_to_try.append(uri.replace("dasafo-shared-kg", "localhost"))
    
    for attempt_uri in uris_to_try:
        try:
            driver = GraphDatabase.driver(attempt_uri, auth=(user, pwd))
            driver.verify_connectivity()
            return driver
        except:
            continue
    return None

def persist_to_knowledge_graph(target_project, feedback_payload, agent):
    """
    Persistencia de largo plazo (LTP) v5.1.
    Sincroniza Golden Rules, Negative Engrams y Lessons Learned.
    """
    start_time = time.time()
    project_name = Path(target_project).name
    driver = get_neo4j_driver()
    if not driver:
        return {"success": False, "message": "LTP_ERROR: No connection to Neo4j."}, 0

    engrams_synced = 0
    try:
        with driver.session() as session:
            # 1. GOLDEN RULES (Positivas)
            for rule in feedback_payload.get("golden_rules", []):
                session.run("""
                    MERGE (t:Technology {name: $tech})
                    MERGE (ph:Phase {name: $phase})
                    MERGE (cv:CulturalViolation {name: 'PATTERN_RECURRENCE'})
                    MERGE (cv)-[:CAUSED_BY]->(t)
                    CREATE (r:GoldenRule {
                        rule_id: $rule_id, content: $text, agent: $agent,
                        project: $project, timestamp: datetime($ts), skill: $skill
                    })
                    CREATE (r)-[:ADDRESSES]->(cv)
                    CREATE (r)-[:BELONGS_TO_PHASE]->(ph)
                """, {
                    "tech": rule.get("tech", "global"),
                    "phase": rule.get("phase", "GLOBAL"),
                    "text": rule.get("text"),
                    "rule_id": f"GR-{int(time.time()*1000)}",
                    "agent": agent,
                    "project": project_name,
                    "skill": rule.get("skill", "unknown"),
                    "ts": datetime.now().isoformat()
                })
                engrams_synced += 1

            # 2. NEGATIVE ENGRAMS (Errores a evitar)
            for engram in feedback_payload.get("negative_engrams", []):
                session.run("""
                    MERGE (n:NegativeEngram {engram_id: $id})
                    SET n.description = $desc, n.agent = $agent, n.ts = datetime($ts)
                """, {"id": f"NE-{int(time.time()*1000)}", "desc": engram.get("description"), "agent": agent, "ts": datetime.now().isoformat()})
                engrams_synced += 1

        return {"success": True, "message": f"Sincronizados {engrams_synced} engramas."}, engrams_synced
    except Exception as e:
        return {"success": False, "message": str(e)}, 0
    finally:
        driver.close()

def execute_feedback_analysis(
    target_project: str,
    agent: str,
    action: str = "analyze_file",
    file_path: str = "LOGS/FEEDBACK-LOG.md",
    raw_text: str = None
) -> tuple[dict, list]:
    """Punto de entrada industrial."""
    start_time = time.time()
    project_path = Path(target_project).resolve()
    
    if action == "analyze_file":
        input_file = project_path / file_path
        if not input_file.exists():
            return {"industrial_status": "ERROR"}, []
        content = input_file.read_text(encoding="utf-8")
    else: content = raw_text or ""

    # --- Motor de Extracción ---
    golden_rules = []
    negative_engrams = []
    
    entries = re.findall(r'(\{(?:[^{}]|\{[^{}]*\})*\})', content, re.DOTALL)
    for entry_raw in entries:
        try:
            entry = json.loads(entry_raw)
            if "golden_rule" in entry:
                golden_rules.append({
                    "text": entry["golden_rule"],
                    "tech": entry.get("tech", "global").lower(),
                    "phase": entry.get("phase", "M3_PRODUCTION"),
                    "skill": entry.get("skill")
                })
            if entry.get("severity") in ["critical", "high"]:
                negative_engrams.append({"description": entry.get("reason", "Unknown violation")})
        except: continue

    # === BLOQUE LTP v5.1 (TU INTEGRACIÓN) ===
    feedback_payload = {
        "golden_rules": golden_rules,
        "negative_engrams": negative_engrams,
        "lessons_learned": [] # Placeholder para Fase 2
    }

    ltp_result, synced_count = persist_to_knowledge_graph(target_project, feedback_payload, agent)

    # --- Reporte Final ---
    execution_duration_s = round(time.time() - start_time, 4)
    result_payload = {
        "industrial_status": "LTP_SOLIDIFIED",
        "metrics": {"engrams_synced": synced_count, "execution_s": execution_duration_s},
        "ltp_sync": ltp_result
    }
    
    report_file = project_path / "LOGS" / f"LTP_SYNC_{int(time.time())}.json"
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(result_payload, f, indent=2)

    return result_payload, [str(report_file)]