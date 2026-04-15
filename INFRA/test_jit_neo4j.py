import os
import sys
from neo4j import GraphDatabase

uri = os.getenv("NEO4J_URI", "bolt://127.0.0.1:7687")
user = os.getenv("NEO4J_USER", "neo4j")
pwd = os.getenv("NEO4J_PASSWORD")
if not pwd:
    raise ValueError("🛑 ERROR CRÍTICO (Zero-Trust): La variable de entorno NEO4J_PASSWORD no está definida.")

try:
    print(f"Connecting to {uri} with user {user}...")
    driver = GraphDatabase.driver(uri, auth=(user, pwd))
    driver.verify_connectivity()
    print("SUCCESS: Connected to Neo4j.")
    
    with driver.session() as session:
        result = session.run("MATCH (n:GoldenRule) RETURN count(n) as count")
        count = result.single()["count"]
        print(f"GoldenRules found: {count}")
    driver.close()
except Exception as e:
    print(f"ERROR: {e}")
