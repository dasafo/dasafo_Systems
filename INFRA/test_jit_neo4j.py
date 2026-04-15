from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

# Cargar secretos de INFRA/.env
load_dotenv("/home/david/Documents/AI/AGENTES/INFRA/.env")

URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
USER = os.getenv("NEO4J_USER", "neo4j")
PASSWORD = os.getenv("NEO4J_PASSWORD", "freedom85")

def test_jit_engram_pipeline():
    print("🧠 Iniciando Protocolo Mnemónico (Test Neo4j JIT)...")
    
    # 1. Establecer Conexión (El "driver")
    try:
        # Usamos localhost para la prueba local en lugar del nombre del contenedor si el script corre en el host
        local_uri = URI.replace("dasafo-shared-kg", "localhost")
        driver = GraphDatabase.driver(local_uri, auth=(USER, PASSWORD))
        driver.verify_connectivity()
        print("🟢 [Conectado al Knowledge Graph]")
    except Exception as e:
        print(f"🔴 ERROR CRITICO: La sinapsis ha fallado - {e}")
        return

    # 2. Inyección (Engrama Negativo)
    engram_code = "ERR-M3-001"
    engram_text = "ANTI-PATTERN: Nunca inyectar dependencias cíclicas en el router FastAPI de ContentRepurpose."
    
    with driver.session() as session:
        # Guardar nodo
        session.run(
            """
            MERGE (e:NegativeEngram {code: $code})
            SET e.content = $text, 
                e.phase = 'M3', 
                e.timestamp = timestamp()
            """,
            code=engram_code, text=engram_text
        )
        print(f"✅ Engrama Inyectado: {engram_code}")

    # 3. Lectura (JIT Query del Orquestador)
    print("\n🔍 Simulando Orquestador despachando tarea M3...")
    with driver.session() as session:
        result = session.run(
            """
            MATCH (e:NegativeEngram)
            WHERE e.phase = 'M3'
            RETURN e.code AS code, e.content AS content
            ORDER BY e.timestamp DESC LIMIT 1
            """
        )
        record = result.single()
        if record:
            print(f"⚡ JIT INJECTION RECIBIDA:")
            print(f"   [{record['code']}]: {record['content']}")
        else:
            print("⚠️ Amnesia. El Engrama no se recuperó.")

    # 4. Limpieza (Purga Quirúrgica post-test)
    with driver.session() as session:
        session.run("MATCH (e:NegativeEngram {code: $code}) DETACH DELETE e", code=engram_code)
        
    driver.close()
    print("\n🧹 Rastro de prueba eliminado. Sistema estable.")

if __name__ == "__main__":
    test_jit_engram_pipeline()
