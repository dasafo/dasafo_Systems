import os
import json
import time
import shutil
from pathlib import Path
import redis # 👈 Nueva dependencia para Engram Cache

# Logic based on dasafo_FACTORY Core v5.0-MCP
# Integrated with Neo4j (LTP) and Redis (Short-Term Engram)

# Inicialización del Cliente Redis (Conexión industrial compartida)
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)

def fetch_rules_from_neo4j(tech_hints: list[str], current_phase: str) -> list[str]:
    """Consulta de respaldo al Knowledge Graph (Neo4j) con hostname fallback."""
    try:
        from neo4j import GraphDatabase
    except ImportError:
        return ["Warning: neo4j driver not installed. Skipping rule injection."]

    uri = os.getenv("NEO4J_URI", "bolt://dasafo-shared-kg:7687")
    user = os.getenv("NEO4J_USER", "neo4j")
    pwd = os.getenv("NEO4J_PASSWORD")
    if not pwd:
        raise PermissionError("ZERO-TRUST: NEO4J_PASSWORD no configurado en entorno.")
    
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
        return ["LTP Warning: Failed to connect to Neo4j at any URI."]
    
    rules = []
    try:
        with driver.session() as session:
            result = session.run("""
                MATCH (r:GoldenRule)-[:ADDRESSES]->(t:Technology)
                MATCH (r)-[:BELONGS_TO_PHASE]->(ph:Phase)
                WHERE toLower(t.name) IN $techs 
                  AND (ph.name = $phase OR ph.name = 'GLOBAL')
                RETURN r.content AS rule
            """, techs=[t.lower() for t in tech_hints], phase=current_phase)
            rules = [record["rule"] for record in result]
    except Exception as e:
        return [f"LTP Warning: Failed to query Neo4j - {str(e)}"]
    finally:
        driver.close()
    
    return rules

def fetch_golden_rules(tech_hints: list[str], current_phase: str) -> list[str]:
    """Lógica Redis-First para la Memoria Engram (v5.0-MCP)."""
    all_rules = []
    techs_to_query_neo4j = []

    # 1. INTENTO DESDE REDIS (Engram Memory)
    for tech in tech_hints:
        cache_key = f"dasafo:engram:rules:{current_phase}:{tech.lower()}"
        cached_rules = redis_client.get(cache_key)
        
        if cached_rules:
            all_rules.extend(json.loads(cached_rules))
        else:
            techs_to_query_neo4j.append(tech)

    # 2. FALLBACK A NEO4J (Solo para conocimiento no cacheado)
    if techs_to_query_neo4j:
        neo4j_rules = fetch_rules_from_neo4j(techs_to_query_neo4j, current_phase)
        all_rules.extend(neo4j_rules)
    
    return list(set(all_rules)) # Eliminación de redundancias

def execute_delegation(
    target_project: str,
    spec_path: str,
    agent_type: str,
    current_phase: str = "M3"
) -> tuple[dict, list]:
    """Lógica pura para delegación aislada y auto-inicio DAST (v5.0-MCP)."""
    start_time = time.time()
    project_path = Path(target_project).resolve()
    
    spec_file_name = Path(spec_path).name
    pending_path = project_path / "TASKS" / "01_PENDING" / spec_file_name
    in_progress_path = project_path / "TASKS" / "02_IN_PROGRESS" / spec_file_name
    
    # 1. AUTO-START DAST (Movimiento físico del archivo de tarea)
    if pending_path.exists():
        shutil.move(str(pending_path), str(in_progress_path))
        actual_spec_path = in_progress_path
    elif in_progress_path.exists():
        actual_spec_path = in_progress_path
    else:
        raise FileNotFoundError(f"PHYSICAL_ERROR: Spec {spec_file_name} no encontrada.")

    with open(actual_spec_path, 'r', encoding='utf-8') as f:
        spec_data = json.load(f)

    # 2. JIT ENGRAM INJECTION (Redis + Neo4j)
    tech_hints = ["global"]
    pointers = str(spec_data.get("metadata", {}).get("context_pointers", [])).lower()
    
    # Comprehensive stack detection via file extensions AND dependency manifests
    tech_map = {
        "fastapi": [".py", "fastapi", "uvicorn", "requirements.txt", "pyproject.toml"],
        "django": ["django", "manage.py", "wsgi.py"],
        "flask": ["flask"],
        "nextjs": [".tsx", ".jsx", "next.config", "next/"],
        "react": ["react", ".tsx", ".jsx"],
        "vue": [".vue", "nuxt", "vite.config"],
        "nodejs": ["package.json", ".ts", ".js", "nestjs", "express"],
        "golang": [".go", "go.mod", "go.sum"],
        "postgres": ["sqlalchemy", "prisma", "supabase", ".sql"],
    }
    for tech, markers in tech_map.items():
        if any(m in pointers for m in markers) and tech not in tech_hints:
            tech_hints.append(tech)
    
    golden_rules = fetch_golden_rules(tech_hints, current_phase)
    
    if golden_rules:
        spec_data.setdefault("specification", {}).setdefault("03_constraints", [])
        spec_data["specification"]["03_constraints"].append("--- ENGRAM INJECTED GOLDEN RULES ---")
        spec_data["specification"]["03_constraints"].extend(golden_rules)
        
        with open(actual_spec_path, 'w', encoding='utf-8') as f:
            json.dump(spec_data, f, indent=2)

    execution_duration_s = time.time() - start_time
    
    result = {
        "industrial_status": "DELEGATION_COMPLETE",
        "task_status": "COMPLETED",
        "summary": f"Delegación exitosa a {agent_type}. {len(golden_rules)} reglas inyectadas.",
        "metrics": {
            "engram_rules_injected": len(golden_rules),
            "execution_duration_seconds": round(execution_duration_s, 4)
        }
    }
    
    return result, [str(actual_spec_path)]