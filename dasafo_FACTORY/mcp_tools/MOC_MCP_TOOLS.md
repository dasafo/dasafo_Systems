# 🔌 MOC | MCP Hubs & Tools Implementation

Este nodo documenta los archivos de código fuente Python que implementan los servidores MCP de la factoría. Al ser archivos `.py`, no aparecen nativamente en el gráfico de Obsidian, pero aquí se centraliza su referencia técnica.

## 🧠 Core Engine
- `mcp_app.py`: El punto de entrada principal para el servidor MCP de la factoría.
- `core_dast.py`: Implementación de la lógica de persistencia atómica y validación DAST.

## 📡 Herramientas por Dominio (Hubs)
- `hub01_strategy.py`: Implementación de los sentidos y habilidades del dominio de Estrategia.
- `hub02_arch.py`: Herramientas para arquitectura, ADRs y gestión de investigación.
- `hub03_prod.py`: Lógica para generación de código (Backend, Frontend, DB) y scaffolding.
- `hub04_compliance.py`: Control de calidad, auditorías industriales y escaneo de secretos.
- `hub05_operations.py`: Gestión de infraestructura (Docker/Terraform), monitorización y auto-healing.

---
### 🧬 Conectividad con la Factoría
> [ ⬆️ Up: [[../_dasafo_FACTORY]] | 📂 Global: [[../00_GLOBAL_KNOWLEDGE/MOC_GLOBAL]] ]

**Nota:** Estos scripts son el "motor" que permite a los agentes ejecutar las habilidades definidas en [[../06_SKILL_LIBRARY/MOC_SKILL_LIBRARY]].
