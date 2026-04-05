# 🏛️ Manual Maestro de Instrucciones: dasafo_Systems v5.0.2-MCP

> **"Industrializando la Excelencia Evolutiva a través del Model Context Protocol (MCP), la Soberanía del Disco (DAST) y la Memoria Estratificada (Engram)."**

**dasafo_Systems** es un ecosistema industrial de IA de alto rendimiento que opera bajo el estándar **v5.0.2-MCP "Engram-Solidified"**. Este sistema elimina la improvisación del "Vibe Coding" mediante una arquitectura de seguridad por diseño, donde cada acción está auditada por la **Aduana Universal** y respaldada por evidencia física en disco.

---

## 🏗️ I. ARQUITECTURA DE NODOS (El Ecosistema)

### 🧠 A. `dasafo_FACTORY` (El Núcleo Inmutable)

El núcleo se modulariza en Hubs especializados para garantizar la separación de responsabilidades:

- **`00_GLOBAL_KNOWLEDGE`**: Contiene la Constitución Core, esquemas de feedback y el conocimiento transversal.
- **`mcp_tools/`**: Motor industrial que define el singleton `FastMCP` y el decorador `@aduana_universal`.
- **`06_SKILL_LIBRARY`**: Lógica atómica de cada skill, clasificada bajo la taxonomía de **19 Skills de Producción** (DEFINE, PLAN, BUILD, VERIFY, REVIEW, SHIP).

### ⚡ B. `INFRA` (Power Grid)

Nodo de servicios persistentes:

- **Postgres**: Datos operacionales relacionales.
- **Neo4j (LTP)**: Persistencia a largo plazo de "Reglas de Oro" y lecciones aprendidas.
- **Redis (Engram)**: Memoria de corto plazo y sistema **Antifatiga** para inyección de reglas JIT (Just-In-Time) y detección de bucles infinitos.

---

## ⚙️ II. EL MOTOR INDUSTRIAL (Mecanismos de Solidificación)

### 🛂 1. Aduana Universal y Antifatiga

El decorador `@aduana_universal` actúa como el primer filtro de seguridad:

- **Loop Detection**: Utiliza Redis para contar las llamadas por sesión; si un agente excede el `max_retries` configurado para una herramienta, la ejecución se bloquea para proteger tokens.
- **DAST Sync**: Reconstruye el `registry.json` basándose exclusivamente en los archivos físicos presentes en `TASKS/`.

### 🛡️ 2. Double-Gating (Autorización por Evidencia)

Un agente solo puede operar si existe una **SPEC_LITE.json** física que le asigne la tarea. En caso de fallos críticos de infraestructura, el sistema genera automáticamente una **EMERGENCY_SPEC.json** para activar el protocolo de **Auto-Healing**.

### ⚡ 3. Engram Memory (Redis-First)

Antes de cada tarea, el Orquestador ejecuta un `warm_up_engram`. Esto carga las reglas críticas de Neo4j en Redis, permitiendo que las herramientas MCP inyecten restricciones técnicas en milisegundos sin latencia de base de datos.

---

## 🚀 III. CICLO DE VIDA Y TAXONOMÍA (Fases M1-M5)

El progreso se mide por la transición física entre hitos, categorizando cada skill según su función cognitiva:

- **🕵️ M1: Discovery (DEFINE):** Formulación de ROI y firma del contrato maestro `PRP_MASTER.json`.
- **📐 M2: Architecture (PLAN):** Solidificación del Backbone y registro de Decisiones Arquitectónicas (ADRs).
- **⚙️ M3: Production (BUILD):** Ejecución paralela en **Clean Sessions** autorizadas por la Aduana.
- **🛡️ M4: Compliance (VERIFY/REVIEW):** Auditoría de **Solidity Guard**, escaneo Zero-Trust de secretos y pruebas E2E.
- **🚀 M5: Operations (SHIP):** Uptime monitorizado, auto-sanación de servicios y persistencia LTP.

---

## ⚖️ IV. MANDATOS CONSTITUCIONALES

- **MANDATO MCP**: Prohibido usar `bash` para tareas industriales. Solo invocación directa MCP por nombre.
- **UNIDADES SI**: Tiempo en **segundos (s)**, Espacio en **bytes (B)**.
- **HITL OBLIGATORIO**: Ninguna fase avanza sin la firma humana en `APPROVAL_MX.md`.
- **GUARDIAN ANGEL**: El uso del hook pre-commit `.githooks/guardian.py` es obligatorio para desarrolladores humanos para prevenir fugas de secretos y fallos de estructura locales.

---

## 🕹️ V. MATRIZ DE CONTROL (SOPs via MCP)

| SOP / Tool | Categoría | Función Industrial | Responsable |
| :--- | :--- | :--- | :--- |
| `prp-generator` | DEFINE | Generación del contrato maestro y specs. | Product Owner |
| `warm_up_engram` | PLAN | Sincronización de memoria rápida Redis. | Orchestrator |
| `factory-orchestrate`| PLAN | Análisis de DAG y despacho prioritario de emergencias. | Orchestrator |
| `delegate-clean-session`| BUILD | Delegación aislada con inyección de reglas JIT. | Orchestrator |
| `factory-audit-pro` | REVIEW | Auditoría de solidez y reporte de métricas SI. | QA Tester |
| `auto-heal` | SHIP | Sanación autónoma de infra y re-despliegue. | Factory Evolver |

---
*Ratificado: 2026-04-05 | dasafo_Factory v5.0.2-MCP | Soberanía Industrial Garantizada.*
