# 🗺️ Mapeo Exhaustivo de AGENTES Y SKILLS

> **Versión:** v5.0.2-MCP "Engram-Solidified"
> **Misión:** Establecer la matriz definitiva de autoridad, sentidos (senses) y capacidades técnicas mediante MCP.
> **Gobernanza:** Zero-Trust / Engram Persistence (LTP) / Loop Detection / Unidades SI (s, B)

Este documento define las fronteras de acción de cada uno de los **agentes industriales**. Bajo el estándar **v5.0-MCP**, la ejecución se protege mediante el sistema **Antifatiga (Redis)** y se enriquece mediante **Engram Memory (Neo4j)**, garantizando ejecuciones coherentes, seguras y resilientes.

---

## 🏛️ Hub 01: Estrategia y Orquestación (The Brain & Vision)

| AGENTE | ROL INDUSTRIAL | SKILLS AUTORIZADAS (Skill Library) | SENTIDOS (Senses) |
| :--- | :--- | :--- | :--- |
| **ORCHESTRATOR** | Master Flow Controller | `delegate-clean-session`, `project-management` (analyze_schedule + warm_up_engram), `kanban-solidity-gate`, `registry-manager`, `factory-doctor`, `project-backbone-validator` | **Emergency Preemption, DAG, Registry, State, Contract, Engram State** |
| **PRODUCT_OWNER** | Arquitecto de Visión | `apify-trend-analysis`, `startup-metrics-framework`, `prp-generator`, `project-management` (warm_up_engram) | **Market, Business KPIs, DAST, Registry** |
| **MARKETING_GROWTH** | Estratega de Crecimiento | `apify-trend-analysis`, `social-content-strategy`, `hallucination-guardrail` | **Spec, Targeted File (DOCS/MARKETING/), DAST** |

* **Interacción Clave (SOP `init-contract`):** El **Product Owner** sella la visión y sincroniza el **Engram** inicial; el **Orquestador** activa el pipeline detectando prioridades de emergencia.

---

## 📐 Hub 02: Arquitectura e Investigación (Blueprints & Feasibility)

| AGENTE | ROL INDUSTRIAL | SKILLS AUTORIZADAS (Skill Library) | SENTIDOS (Senses) |
| :--- | :--- | :--- | :--- |
| **ARCHITECT** | Diseñador del Backbone | `architecture-decision-records`, `api-contract-generator`, `database-architect-strategic`, `factory-doctor` | **PRP, DAST, Blueprint (DOCS/ARCH/)** |
| **RESEARCH_AGENT** | Analista Factual | `arxiv-technical-digest`, `apify-trend-analysis`, `research-manager`, `hallucination-guardrail` | **Spec, Knowledge Digestion, Filesystem (DOCS/RESEARCH/), DAST** |

* **Interacción Clave (SOP `arch-diagram`):** La **Arquitectura** solidifica los planos (M2); la **Investigación** valida la viabilidad técnica antes del primer byte de código.

---

## 🛠️ Hub 03: Producción e Implementación (Implementation & Logic)

| AGENTE | ROL INDUSTRIAL | SKILLS AUTORIZADAS (Skill Library) | SENTIDOS (Senses) |
| :--- | :--- | :--- | :--- |
| **AI_ENGINEER** | Ingeniero de IA | `async-fastapi-logic`, `hallucination-guardrail` | **Workspace (backend), Model Latency, Architecture** |
| **BACKEND_DEV** | Lógica de Servidor | `async-fastapi-logic`, `supabase-stack-expert`, `pytest-logic-verifier`, `nodejs-backend-patterns` | **Workspace, Architecture Boundary, DAST** |
| **FRONTEND_DEV** | Interfaz y UX | `shadcn-component-library`, `atomic-design-tokens`, `frontend-ui-designer`, `playwright-e2e-tester` | **Workspace, UI/UX Tokens, Blueprint** |
| **DB_MASTER** | Guardián de Datos | `database-architect-strategic`, `supabase-stack-expert`, `agentic-thought-secret-scanner` | **Spec, Targeted Schema, DAST, Secret X-Ray** |
| **DATA_SCIENTIST** | Analista de Patrones | `autonomous-feedback-analyzer`, `apify-trend-analysis` | **Spec, Targeted File (data), DAST** |

---

## ⚖️ Hub 04: Calidad y Cumplimiento (Compliance & Audit)

| AGENTE | ROL INDUSTRIAL | SKILLS AUTORIZADAS (Skill Library) | SENTIDOS (Senses) |
| :--- | :--- | :--- | :--- |
| **QA_TESTER** | Auditor de Lógica | `factory-audit-pro`, `hallucination-guardrail`, `agentic-thought-secret-scanner`, `build-test-executor`, `playwright-e2e-tester`, `pytest-logic-verifier` | **Spec, Codebase X-Ray, DAST** |
| **SECURITY_AUDITOR** | Guardián Zero-Trust | `agentic-thought-secret-scanner`, `factory-audit-pro` | **Spec, Zero-Trust, DAST, Secret X-Ray** |
| **DOCS_MASTER** | Gestor del Conocimiento | `api-docs-generator`, `arxiv-technical-digest`, `hallucination-guardrail` | **Spec, Targeted File (DOCS/), DAST** |

---

## 📦 SKILL CROSS-REFERENCE (Agentes por Skill)

Esta lista detalla qué agentes tienen permiso para invocar cada skill de la `06_SKILL_LIBRARY` vía MCP.

* **`agentic-thought-secret-scanner`**: `BACKEND_DEV`, `DB_MASTER`, `DATA_SCIENTIST`, `QA_TESTER`, `SECURITY_AUDITOR`, `DEVOPS_SRE`
* **`api-contract-generator`**: `ARCHITECT`
* **`api-docs-generator`**: `DOCS_MASTER`
* **`apify-trend-analysis`**: `PRODUCT_OWNER`, `MARKETING_GROWTH`, `RESEARCH_AGENT`, `DATA_SCIENTIST`
* **`architecture-decision-records`**: `ARCHITECT`
* **`arxiv-technical-digest`**: `RESEARCH_AGENT`, `DOCS_MASTER`
* **`async-fastapi-logic`**: `AI_ENGINEER`, `BACKEND_DEV`
* **`atomic-design-tokens`**: `FRONTEND_DEV`
* **`autonomous-feedback-analyzer`**: `DATA_SCIENTIST`, `DEPLOYMENT_MONITOR`, `FACTORY_EVOLVER`, `MEMORY_OPTIMIZER`
* **`build-test-executor`**: `QA_TESTER`
* **`context-pruning-sieve`**: `MEMORY_OPTIMIZER`
* **`database-architect-strategic`**: `ARCHITECT`, `DB_MASTER`
* **`delegate-clean-session`**: `ORCHESTRATOR`
* **`deployment-health-check`**: `DEVOPS_SRE`, `DEPLOYMENT_MONITOR`
* **`docker-stack-provisioner`**: `DEVOPS_SRE`
* **`factory-audit-pro`**: `QA_TESTER`, `SECURITY_AUDITOR`
* **`factory-doctor`**: `ORCHESTRATOR`, `ARCHITECT`, `FACTORY_EVOLVER`
* **`frontend-ui-designer`**: `FRONTEND_DEV`
* **`hallucination-guardrail`**: `MARKETING_GROWTH`, `RESEARCH_AGENT`, `DOCS_MASTER`, `QA_TESTER`, `DEVOPS_SRE`, `DEPLOYMENT_MONITOR`, `FACTORY_EVOLVER`, `MEMORY_OPTIMIZER`
* **`kanban-solidity-gate`**: `ORCHESTRATOR`
* **`nodejs-backend-patterns`**: `BACKEND_DEV`
* **`playwright-e2e-tester`**: `FRONTEND_DEV`, `QA_TESTER`, `DEPLOYMENT_MONITOR`
* **`project-backbone-validator`**: `ORCHESTRATOR`
* **`project-management`**: `ORCHESTRATOR`
* **`prp-generator`**: `ORCHESTRATOR`, `PRODUCT_OWNER`
* **`pytest-logic-verifier`**: `BACKEND_DEV`
* **`registry-manager`**: `ORCHESTRATOR`
* **`research-manager`**: `RESEARCH_AGENT`
* **`shadcn-component-library`**: `FRONTEND_DEV`
* **`skill-refactor-pro`**: `FACTORY_EVOLVER`
* **`social-content-strategy`**: `MARKETING_GROWTH`
* **`startup-metrics-framework`**: `PRODUCT_OWNER`
* **`supabase-stack-expert`**: `BACKEND_DEV`, `DB_MASTER`
* **`terraform-iac-builder`**: `DEVOPS_SRE`

---

## 🛑 EL MANDATO MCP (Restricciones Críticas)

1. **PROHIBICIÓN TOTAL DE BASH**: Ningún agente puede usar `bash_command` para tareas industriales.
2. **DAST OBLIGATORIO**: Todo cambio de estado requiere evidencia física en el disco.
3. **UNIDADES SI**: Todas las métricas deben reportarse en **segundos (s)** y **bytes (B)**.
4. **SESSION ISOLATION**: La delegación debe usar siempre `delegate-clean-session`.

---
> [!TIP]
> Volver al [[00_INFO_START|Centro de Información]].


---
> [!NOTE]
> Este documento es **referencia estática**. Para operar en la factoría real, usa [[../dasafo_FACTORY/_dasafo_FACTORY]].