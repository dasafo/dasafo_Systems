# 🏛️ Manual Maestro de Instrucciones: dasafo_Systems v5.0-MCP

> **"Industrializando la Excelencia Evolutiva a través del Model Context Protocol (MCP) y la Soberanía del Disco (DAST)."**

**dasafo_Systems** es un ecosistema industrial de IA de alto rendimiento. Opera bajo el estándar **v5.0-MCP "Native Industrial Core"**, que integra el protocolo MCP para eliminar la fricción humana y garantizar que cada acción esté auditada por la **Aduana Universal**.

---

## 🏗️ I. ARQUITECTURA DE NODOS (El Ecosistema)

### 🧠 A. `dasafo_FACTORY` (El Núcleo Inmutable)

El núcleo se ha modularizado para escalar mediante Hubs especializados:

- **`00_GLOBAL_KNOWLEDGE`**: Constitución Core, Esquemas de Feedback y Conocimiento Global.
- **`mcp_tools/`**: Directorio raíz del motor industrial.
  - `mcp_app.py`: Define el singleton `FastMCP` y el decorador `@aduana_universal`.
  - `core_dast.py`: Herramientas base (Delegación, Kanban Gate, Doctor).
  - `hub01-05`: Implementación de herramientas por departamento (Estrategia, Arq, Prod, Calidad, Ops).
- **`factory_mcp_server.py`**: Entrypoint del servidor. Orquesta la carga de hubs y expone las herramientas a Antigravity.
- **`06_SKILL_LIBRARY`**: Lógica atómica de cada skill, desacoplada del servidor MCP.

### ⚡ B. `INFRA` (Power Grid)

Nodo de servicios persistentes (Postgres, Neo4j, Redis). La Aduana inyecta automáticamente las credenciales JIT desde `INFRA/.env`.

### 📦 C. `PROJECTS` (El Taller / Workshop)

Espacio de construcción bajo el protocolo **DAST (Disk-as-Source-of-Truth)**. Solo existe aquello que tiene evidencia física en disco.

---

## ⚙️ II. EL MOTOR INDUSTRIAL (Mecanismos v5.0-MCP)

### 🛂 1. Aduana Universal y Pre-flight Sync

Cada vez que se invoca una herramienta, el decorador `@aduana_universal` ejecuta:

- **DAST Sync**: Escanea las carpetas `TASKS/01_PENDING`, `02_IN_PROGRESS`, etc., y reconstruye el `registry.json`. El disco manda sobre la memoria.
- **Auto-Commit**: Genera un mensaje de éxito atómico que cierra lógicamente la tarea en el payload de respuesta.

### 🛡️ 2. Double-Gating (Autorización por Evidencia)

Un agente solo puede operar si:

- Está en el roster de **17 agentes autorizados**.
- Existe una **SPEC_LITE.json** (o `EMERGENCY_SPEC.json`) física en el proyecto que le asigne explícitamente la tarea (`metadata.assigned_agent`).

### 🚦 3. Bypass Protocol

Ciertas herramientas de gestión (`factory-doctor`, `kanban-solidity-gate`, `registry-manager`) tienen pase libre por la aduana para permitir el diagnóstico y avance de fases sin Specs previas.

---

## 🚀 III. CICLO DE VIDA (Fases M1-M5)

- **🕵️ M1: Discovery:** ROI y visión sellados en el contrato maestro.
- **📐 M2: Architecture:** Solidificación del Backbone y ADRs técnicos.
- **⚙️ M3: Production:** Ejecución paralela en **Clean Sessions** (aislamientos atómicos).
- **🛡️ M4: Compliance:** Auditoría de **Solidity Guard** y escaneo Zero-Trust de secretos.
- **🚀 M5: Operations:** Uptime garantizado y persistencia LTP en Neo4j.

---

## ⚖️ IV. MANDATOS CONSTITUCIONALES

- **MANDATO MCP**: Prohibido usar `bash` para tareas industriales. Solo invocación directa MCP.
- **UNIDADES SI**: Tiempo en **segundos (s)**, Espacio en **bytes (B)**.
- **HITL OBLIGATORIO**: Ninguna fase avanza a `APPROVED` sin la firma del Director en `APPROVAL_MX.md`.

---

## 🕹️ V. MATRIZ DE CONTROL (SOPs via MCP)

| SOP / Tool | Función Industrial | Responsable Primario |
| :--- | :--- | :--- |
| `prp-generator` | Generación del contrato maestro M1. | Product Owner |
| `factory-orchestrate` | Análisis de topología DAG y despacho paralelo. | Orchestrator |
| `delegate-clean-session` | Delegación aislada con inyección JIT Neo4j. | Orchestrator |
| `kanban-solidity-gate` | Control de flujos, avance de fases y dashboard. | Orchestrator |
| `factory-audit-pro` | Auditoría de lógica y conformidad industrial. | QA Tester |
| `agentic-thought-secret-scanner` | Escaneo industrial de vulnerabilidades y secretos. | Security Auditor |
| `sync-memory` | Persistencia de engramas finales en el LTP. | Memory Optimizer |

---
*Ratificado: 2026-04-04 | Dasafo Factory v5.0-MCP | Soberanía Industrial Garantizada.*
