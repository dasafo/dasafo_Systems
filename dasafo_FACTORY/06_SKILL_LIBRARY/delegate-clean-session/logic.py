import os
import json
import time
import shutil
from pathlib import Path

# Logic based on dasafo_FACTORY Core v4.0-MCP
# Integrated with Neo4j for Long-Term Persistence (LTP) rules

def fetch_golden_rules(tech_hints: list[str], current_phase: str) -> list[str]:
    """Queries the Knowledge Graph for historical critical rules by Phase and Tech."""
    try:
        from neo4j import GraphDatabase
    except ImportError:
        return ["Warning: neo4j driver not installed. Skipping rule injection."]

    uri = os.getenv("NEO4J_URI", "bolt://dasafo-shared-kg:7687")
    user = os.getenv("NEO4J_USER", "neo4j")
    pwd = os.getenv("NEO4J_PASSWORD", "freedom85")
    
    rules = []
    try:
        driver = GraphDatabase.driver(uri, auth=(user, pwd))
        with driver.session() as session:
            result = session.run("""
                MATCH (r:GoldenRule)-[:ADDRESSES]->(cv:CulturalViolation)-[:CAUSED_BY]->(t:Technology)
                MATCH (r)-[:BELONGS_TO_PHASE]->(ph:Phase)
                WHERE toLower(t.name) IN $techs 
                  AND (ph.name = $phase OR ph.name = 'GLOBAL')
                RETURN r.content AS rule
            """, techs=[t.lower() for t in tech_hints], phase=current_phase)
            rules = [record["rule"] for record in result]
        driver.close()
    except Exception as e:
        return [f"LTP Warning: Failed to query Neo4j - {str(e)}"]
    
    return rules

def execute_delegation(
    target_project: str,
    spec_path: str,
    agent_type: str,
    current_phase: str = "M3"
) -> tuple[dict, list]:
    """Pure logic for context-isolated delegation and DAST auto-start (v5.0-MCP)."""
    start_time = time.time()
    project_path = Path(target_project).resolve()
    
    spec_file_name = Path(spec_path).name
    pending_path = project_path / "TASKS" / "01_PENDING" / spec_file_name
    in_progress_path = project_path / "TASKS" / "02_IN_PROGRESS" / spec_file_name
    
    # 1. AUTO-START DAST (Physical Move)
    if pending_path.exists():
        shutil.move(str(pending_path), str(in_progress_path))
        actual_spec_path = in_progress_path
    elif in_progress_path.exists():
        actual_spec_path = in_progress_path
    else:
        raise FileNotFoundError(f"PHYSICAL_ERROR: Spec {spec_file_name} not found in PENDING/IN_PROGRESS.")

    with open(actual_spec_path, 'r', encoding='utf-8') as f:
        spec_data = json.load(f)

    # 2. JIT NEO4J INJECTION
    tech_hints = ["global"]
    pointers = str(spec_data.get("metadata", {}).get("context_pointers", [])).lower()
    if any(x in pointers for x in ["fastapi", ".py"]): tech_hints.append("fastapi")
    if any(x in pointers for x in ["next", ".tsx"]): tech_hints.append("nextjs")
    
    golden_rules = fetch_golden_rules(tech_hints, current_phase)
    
    if golden_rules:
        spec_data.setdefault("specification", {}).setdefault("03_constraints", [])
        spec_data["specification"]["03_constraints"].append("--- NEO4J INJECTED GOLDEN RULES ---")
        spec_data["specification"]["03_constraints"].extend(golden_rules)
        
        with open(actual_spec_path, 'w', encoding='utf-8') as f:
            json.dump(spec_data, f, indent=2)

    execution_duration_s = time.time() - start_time
    
    result = {
        "industrial_status": "DELEGATION_COMPLETE",
        "task_status": "COMPLETED",
        "summary": f"Delegation successful to {agent_type}. {len(golden_rules)} rules injected.",
        "metrics": {
            "ltp_rules_injected": len(golden_rules),
            "execution_duration_seconds": round(execution_duration_s, 4)
        }
    }
    
    return result, [str(actual_spec_path)]