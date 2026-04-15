import os
from neo4j import GraphDatabase

class ProceduralMemory:
    def __init__(self):
        uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
        user = os.getenv("NEO4J_USER", "neo4j")
        pwd = os.getenv("NEO4J_PASSWORD")
        if not pwd:
            raise PermissionError("ZERO-TRUST: NEO4J_PASSWORD no configurado.")
        self.driver = GraphDatabase.driver(uri, auth=(user, pwd))

    def get_rules(self, phase: str):
        query = "MATCH (p:Phase {name: $phase})-[:HAS_RULE]->(r:GoldenRule) RETURN r.description AS rule"
        with self.driver.session() as session:
            result = session.run(query, phase=phase)
            return [record["rule"] for record in result]
