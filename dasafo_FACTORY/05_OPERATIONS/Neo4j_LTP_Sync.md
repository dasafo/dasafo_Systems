# 🕸️ MOC | Neo4j LTP Sync (v5.0-MCP)

> [ ⬆️ Up: [[MOC_OPERATIONS]] | 📂 Global: [[../00_GLOBAL_KNOWLEDGE/MOC_GLOBAL]] ]

## 🧠 Long-Term Persistence (LTP)
Este protocolo define cómo los agentes vuelcan su aprendizaje efímero en el Grafo de Conocimiento persistente.

### 🍱 Sincronización de Engramas
1. **Trigger:** Se activa tras cada hito (M1-M5) o mediante el comando `sync-memory`.
2. **Destino:** Instancia de Neo4j en el contenedor `kg-db`.
3. **Métrica:** Se reporta el número de nodos inyectados y la latencia en segundos (s).

---
### 🧬 Related Engrams
- [[../00_GLOBAL_KNOWLEDGE/FEEDBACK_SCHEMA.json]]
- [[../MOC_CORE_SCRIPTS]]
