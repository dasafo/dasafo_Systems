# ⚙️ MOC | Global Infrastructure Services (v5.0-MCP)

> [ ⬆️ Up: [[../dasafo_FACTORY/_dasafo_FACTORY]] | 📂 Global: [[../dasafo_FACTORY/00_GLOBAL_KNOWLEDGE/MOC_GLOBAL]] ]

## 🌐 Central Node (The Power Grid)

Este directorio gestiona los servicios compartidos para todo el ecosistema de la factoría.

### 🍱 Main Services Stack (Docker)
- **Neo4j (`kg-db`)**: Grafo de Conocimiento centralizado para orquestación y LTP.
- **Postgres (`shared-db`)**: Almacenamiento relacional de metadatos operativos.
- **Redis (`cache-node`)**: Caché de sesiones y protección contra bucles de engramas.
- **Glances**: Monitorización en tiempo real del hardware y contenedores (Puerto 61208).
- **Supabase**: Hub industrial para proyectos que lo requieran.

### 📜 Archivos de Configuración
- `docker-compose.yml`: Definición de la orquesta de servicios.
- `.env`: Variables de entorno y credenciales seguras.
- [[README]]: Guía rápida de comandos e inicio.

### 🚀 Comandos Rápidos
1. `docker-compose up -d`: Levantar infraestructura.
2. `docker-compose down`: Apagar servicios.
3. `docker logs -f [service]`: Ver telemetría en vivo.

---
### 🧬 Related Engrams
- [[../dasafo_FACTORY/05_OPERATIONS/MOC_OPERATIONS]]
- [[../dasafo_FACTORY/00_GLOBAL_KNOWLEDGE/NATIVE_MCP_PROTOCOL]]
