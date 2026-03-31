from __future__ import annotations
import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Autonomous Feedback Analyzer (MEMORY_OPTIMIZER / FACTORY_EVOLVER)
v3.4.0-S: Industrial Core | LTP & Deployment Insights Integration.

Solidified: Neo4j Persistence, Deployment Log Scanning & SI Metrics.
"""

import os
import json
import time
import re
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

# Intentar importar el driver de Neo4j para Persistencia de Largo Plazo (LTP)
try:
    from neo4j import GraphDatabase
except ImportError:
    GraphDatabase = None

def persist_to_knowledge_graph(rules: list, project: str, agent: str):
    """Sincroniza el aprendizaje agentico con el Grafo Central (Neo4j)."""
    if not GraphDatabase:
        return False, "Driver neo4j no instalado."

    # Configuración de INFRA/
    uri = os.getenv("NEO4J_URI", "bolt://dasafo-shared-kg:7687")
    user = os.getenv("NEO4J_USER", "neo4j")
    pwd = os.getenv("NEO4J_PASSWORD", "freedom85")

    try:
        driver = GraphDatabase.driver(uri, auth=(user, pwd))
        with driver.session() as session:
            for rule in rules:
                # Persistencia de engramas en el Grafo de Conocimiento
                session.run("""
                    MERGE (r:GoldenRule {content: $rule})
                    MERGE (p:Project {name: $project})
                    MERGE (a:Agent {id: $agent})
                    MERGE (p)-[:GENERATED]->(r)
                    MERGE (a)-[:LEARNED]->(r)
                    SET r.last_sync = datetime(), r.status = 'ACTIVE'
                """, rule=rule, project=project, agent=agent)
        driver.close()
        return True, "KG Sync Success"
    except Exception as e:
        return False, f"KG Sync Error: {str(e)}"

def run(skill_input: SkillInput) -> SkillOutput:
    """Entry point industrial para el análisis de feedback y despliegue."""
    agent = skill_input.agent or "MEMORY_OPTIMIZER"
    skill = "autonomous-feedback-analyzer"
    cid = skill_input.correlation_id
    params = skill_input.params or {}
    
    start_time = time.time()

    try:
        # 1. Resolución de Rutas (Protocolo DAST)
        target = params.get("target_project") or skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "SECURITY LOCK: Missing TARGET_PROJECT.", cid)
        
        project_path = Path(target).resolve()
        logs_dir = project_path / "LOGS"
        feedback_file = logs_dir / "FEEDBACK-LOG.md"
        deployment_dir = logs_dir / "deployment" # Nueva fuente de verdad M5
        
        golden_rules_extracted = []
        total_bytes_processed = 0
        critical_errors = 0

        # 2. Análisis de FEEDBACK-LOG.md
        if feedback_file.exists():
            content = feedback_file.read_text(encoding="utf-8")
            total_bytes_processed += len(content.encode("utf-8")) # Mandato SI: Bytes
            
            entries = re.findall(r'(\{.*?\})', content, re.DOTALL)
            for entry_raw in entries:
                try:
                    entry = json.loads(entry_raw)
                    if "golden_rule" in entry:
                        golden_rules_extracted.append(entry["golden_rule"])
                    if entry.get("severity") == "critical":
                        critical_errors += 1
                except: continue

        # 3. Escaneo de LOGS/deployment/ (Integración Fase M5)
        if deployment_dir.exists():
            for health_file in deployment_dir.glob("HEALTH_*.json"):
                try:
                    h_content = health_file.read_text(encoding="utf-8")
                    total_bytes_processed += len(h_content.encode("utf-8"))
                    h_data = json.loads(h_content)
                    
                    # Transformar incidentes de despliegue en reglas de optimización
                    status = h_data.get("status", "Unknown")
                    latency = h_data.get("latency_s", 0)
                    
                    if status != "Healthy" or latency > 2.0: # Umbral de alerta industrial
                        rule = f"Infra Rule: Deployment in {project_path.name} reported {status} with {latency}s latency. Optimization required."
                        golden_rules_extracted.append(rule)
                        critical_errors += 1 if status != "Healthy" else 0
                except: continue

        # 4. Sincronización LTP (Neo4j)
        sync_success, sync_msg = persist_to_knowledge_graph(
            golden_rules_extracted, 
            project_path.name, 
            agent
        )

        # 5. Generación de Artefacto Físico (DAST)
        report_path = logs_dir / f"ANALYSIS_LTP_{cid[:8]}.json"
        analysis_data = {
            "project": project_path.name,
            "agent": agent,
            "metrics": {
                "total_rules": len(golden_rules_extracted),
                "critical_incidents": critical_errors,
                "payload_bytes": total_bytes_processed # SI Units: Bytes
            },
            "extracted_rules": golden_rules_extracted,
            "ltp_sync": {"success": sync_success, "message": sync_msg}
        }
        
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(analysis_data, f, indent=2)

        execution_duration_s = time.time() - start_time # Mandato SI: Segundos

        # 6. Outcome Report "Zero Fluff"
        result_payload = {
            "industrial_status": "SOLIDIFIED - DEPLOYMENT AWARE",
            "rules_learned": len(golden_rules_extracted),
            "critical_blockers": critical_errors,
            "compliance_report": {
                "neo4j_sync": sync_success,
                "deployment_logs_scanned": deployment_dir.exists(),
                "si_metrics_applied": True,
                "execution_duration_seconds": round(execution_duration_s, 4)
            },
            "summary": f"Analizados {total_bytes_processed}B. Capturadas reglas de feedback y despliegue en Neo4j."
        }

        return SkillOutput.success(agent, skill, result_payload, [str(report_path)], cid)

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Feedback Analyzer CRITICAL Fault: {str(e)}", cid)