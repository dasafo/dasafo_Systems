import os
import json
import time
from pathlib import Path
import redis

# Logic: Industrial Project Coordination & Engram Management (v5.0-MCP)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)

def get_project_metrics(project_path: Path) -> dict:
    """Extrae métricas reales del disco (DAST)."""
    registry_path = project_path / "TASKS" / "registry.json"
    state_path = project_path / "PROJECT_STATE.json"
    
    metrics = {
        "total_tasks": 0,
        "completed_tasks": 0,
        "current_phase": "M1_DISCOVERY",
        "progress_percent": 0
    }
    
    if registry_path.exists():
        try:
            with open(registry_path, 'r', encoding='utf-8') as f:
                tasks = json.load(f)
                metrics["total_tasks"] = len(tasks)
                metrics["completed_tasks"] = sum(1 for t in tasks if t.get("status") == "COMPLETED")
                if metrics["total_tasks"] > 0:
                    metrics["progress_percent"] = round((metrics["completed_tasks"] / metrics["total_tasks"]) * 100, 2)
        except: pass
            
    if state_path.exists():
        try:
            with open(state_path, 'r', encoding='utf-8') as f:
                state = json.load(f)
                metrics["current_phase"] = state.get("current_phase", "M1_DISCOVERY")
        except: pass
        
    return metrics

def analyze_dag(tasks: list) -> dict:
    """Cálculo topológico y detección de ciclos (v5.0-MCP)."""
    graph = {t["id"]: t.get("dependencies", []) for t in tasks}
    status_map = {t["id"]: t.get("status", "PENDING") for t in tasks}
    
    visited, rec_stack, cycles = set(), set(), []
    
    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
            elif neighbor in rec_stack:
                cycles.append(f"{node} -> {neighbor}")
        rec_stack.remove(node)
        
    for node in graph:
        if node not in visited: dfs(node)
            
    ready_tasks = [
        t["id"] for t in tasks 
        if t.get("status") == "PENDING" and all(status_map.get(d) == "COMPLETED" for d in t.get("dependencies", []))
    ]
                
    return {
        "is_valid_dag": len(cycles) == 0,
        "ready_to_execute": ready_tasks,
        "blocked_pending_tasks": [t["id"] for t in tasks if t["status"] == "PENDING" and t["id"] not in ready_tasks]
    }

def execute_management(
    target_project: str,
    agent: str,
    action: str = "standup_report",
    report_data: dict = None,
    overwrite: bool = False
) -> tuple[dict, list]:
    """Lógica pura para coordinación industrial y gestión del Engram."""
    start_time = time.time()
    project_path = Path(target_project).resolve()
    registry_path = project_path / "TASKS" / "registry.json"
    metrics = get_project_metrics(project_path)
    
    # --- ACCIÓN NUEVA: WARM_UP_ENGRAM (Fase 2) ---
    if action == "warm_up_engram":
        from neo4j import GraphDatabase
        uri = os.getenv("NEO4J_URI", "bolt://dasafo-shared-kg:7687")
        user = os.getenv("NEO4J_USER", "neo4j")
        pwd = os.getenv("NEO4J_PASSWORD")
        if not pwd:
            raise PermissionError("ZERO-TRUST: NEO4J_PASSWORD no configurado en entorno.")
        
        current_phase = metrics["current_phase"]
        
        try:
            # Intelligent hostname resolution: Try Docker name, fallback to localhost
            uris_to_try = [uri]
            if "dasafo-shared-kg" in uri:
                uris_to_try.append(uri.replace("dasafo-shared-kg", "localhost"))
            
            driver = None
            for attempt_uri in uris_to_try:
                try:
                    driver = GraphDatabase.driver(attempt_uri, auth=(user, pwd))
                    driver.verify_connectivity()
                    break
                except Exception:
                    driver = None
                    continue
            
            if driver is None:
                return {"industrial_status": "ERROR", "error": "LTP_ERROR: Could not connect to Neo4j at any URI."}, []
            
            with driver.session() as session:
                # Consulta masiva de reglas para la fase activa y globales
                result = session.run("""
                    MATCH (r:GoldenRule)-[:ADDRESSES]->(cv:CulturalViolation)-[:CAUSED_BY]->(t:Technology)
                    MATCH (r)-[:BELONGS_TO_PHASE]->(ph:Phase)
                    WHERE ph.name = $phase OR ph.name = 'GLOBAL'
                    RETURN toLower(t.name) as tech, collect(r.content) as rules
                """, phase=current_phase)
                
                count = 0
                for record in result:
                    tech, rules = record["tech"], record["rules"]
                    cache_key = f"dasafo:engram:rules:{current_phase}:{tech}"
                    redis_client.set(cache_key, json.dumps(rules), ex=14400) # 4 horas de TTL
                    count += 1
            driver.close()
            
            return {
                "industrial_status": "ENGRAM_WARM_UP_COMPLETE",
                "summary": f"Memoria Engram sincronizada para fase {current_phase} ({count} tecnologías).",
                "metrics": {"techs_cached": count, "duration": round(time.time() - start_time, 4)}
            }, []
        except Exception as e:
            return {"industrial_status": "ERROR", "error": f"Engram Sync Failed: {str(e)}"}, []

    # --- ACCIÓN: ANALYZE_SCHEDULE ---
    if action == "analyze_schedule":
        if not registry_path.exists(): raise FileNotFoundError("registry.json ausente.")
        with open(registry_path, 'r') as f: tasks = json.load(f)
        dag_report = analyze_dag(tasks)
        
        return {
            "industrial_status": "DAG ANALYZED",
            "dag_metrics": dag_report,
            "summary": f"DAG procesado. Tareas listas: {len(dag_report['ready_to_execute'])}."
        }, []

    # --- ACCIÓN: STANDUP_REPORT ---
    elif action == "standup_report":
        if not registry_path.exists(): raise FileNotFoundError("registry.json ausente.")
        with open(registry_path, 'r') as f: tasks = json.load(f)
        dag_report = analyze_dag(tasks)
        
        return {
            "industrial_status": "PULSE REPORT GENERATED",
            "metrics": metrics,
            "tasks": {
                "total": len(tasks),
                "ready": dag_report.get("ready_to_execute", []),
                "blocked": dag_report.get("blocked_pending_tasks", [])
            },
            "summary": f"Fase: {metrics['current_phase']} | Progreso: {metrics['progress_percent']}%"
        }, []

    raise ValueError(f"Acción '{action}' no implementada.")