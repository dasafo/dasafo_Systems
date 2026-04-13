# ⚙️ MOC | Core Scripts & Entry Points

Este nodo documenta los archivos ejecutables que forman el motor de la factoría. Son los encargados de la orquestación, seguridad y despliegue del ecosistema.

## 🛂 Gateway & Communication
- `factory_mcp_server.py`: El servidor FastMCP central. Es el único punto de entrada autorizado para que los agentes invoquen herramientas industriales. Implementa el protocolo de "Aduana Universal".
- `session_hook.py`: El interceptor de sesiones. Garantiza que cada tarea se ejecute en un entorno limpio y con las reglas de Neo4j inyectadas.

## 🏗️ Project Lifecycle
- `init_project.sh`: Script de inicialización de infraestructura DAST. Crea el backbone (DOCS, TASKS, WORKSPACE) para nuevos proyectos SaaS.

## 🧬 Conectividad con la Factoría
> [ ⬆️ Up: [[_dasafo_FACTORY]] | 📂 Global: [[00_GLOBAL_KNOWLEDGE/MOC_GLOBAL]] ]

**Nota:** Estos scripts trabajan en conjunto con las implementaciones de herramientas en [[mcp_tools/MOC_MCP_TOOLS]].
