# 🗺️ Mapeo Exhaustivo de AGENTES Y SKILLS

> **Versión:** v5.0-MCP "Native Industrial Core"
> **Misión:** Establecer la matriz definitiva de autoridad, sentidos (senses) y capacidades técnicas mediante MCP.
> **Gobernanza:** Zero-Trust / Spec Driven Development / MCP Tool Mandate / Unidades SI (s, B)

Este documento define las fronteras de acción de cada uno de los **17 agentes**. Bajo el estándar **v5.0-MCP**, la ejecución de habilidades se realiza exclusivamente a través del motor industrial (las herramientas MCP **directamente por nombre**), garantizando la auditoría total y la soberanía del disco (DAST).

---

## 🏛️ Hub 01: Estrategia y Marketing (The Brain & Vision)

| AGENTE | ROL INDUSTRIAL | SKILLS AUTORIZADAS (Skill Library) | SENTIDOS (Senses) |
| :--- | :--- | :--- | :--- |
| **ORCHESTRATOR** | Master Flow Controller | `delegate-clean-session`, `prp-generator`, `kanban-solidity-gate`, `registry-manager`, `factory-doctor`, `project-backbone-validator` | **Hub, Registry, State, Contract, Evidence** |
| **PRODUCT_OWNER** | Arquitecto de Visión | `apify-trend-analysis`, `startup-metrics-framework`, `prp-generator` | **Market, DAST, Registry** |
| **MARKETING_GROWTH** | Estratega de Crecimiento | `apify-trend-analysis`, `social-content-strategy`, `hallucination-guardrail` | **Spec, Targeted File, DAST** |

*   **Interacción Clave (SOP `init-contract`):** El **Product Owner** sella la visión; el **Orquestador** activa el pipeline vía MCP.

---

## 📐 Hub 02: Arquitectura e Investigación (Blueprints & Feasibility)

| AGENTE | ROL INDUSTRIAL | SKILLS AUTORIZADAS (Skill Library) | SENTIDOS (Senses) |
| :--- | :--- | :--- | :--- |
| **ARCHITECT** | Diseñador del Backbone | `architecture-decision-records`, `api-contract-generator`, `database-architect-strategic`, `factory-doctor` | **PRP, DAST, Blueprint** |
| **RESEARCH_AGENT** | Analista Factual | `arxiv-technical-digest`, `apify-trend-analysis`, `research-manager`, `hallucination-guardrail` | **Spec, Knowledge Digestion, Filesystem, DAST** |

*   **Interacción Clave (SOP `arch-diagram`):** La **Arquitectura** solidifica los planos (M2); la **Investigación** valida la viabilidad técnica antes del primer byte de código.

---

## 🛠️ Hub 03: Producción (Implementation & Logic)

| AGENTE | ROL INDUSTRIAL | SKILLS AUTORIZADAS (Skill Library) | SENTIDOS (Senses) |
| :--- | :--- | :--- | :--- |
| **AI_ENGINEER** | Ingeniero de IA | `async-fastapi-logic` | **Workspace, Architecture** |
| **BACKEND_DEV** | Lógica de Servidor | `async-fastapi-logic`, `supabase-stack-expert`, `pytest-logic-verifier`, `nodejs-backend-patterns`, `agentic-thought-secret-scanner` | **Workspace, Architecture** |
| **FRONTEND_DEV** | Interfaz y UX | `shadcn-component-library`, `atomic-design-tokens`, `frontend-ui-designer`, `playwright-e2e-tester` | **Workspace, UI/UX Blueprint** |
| **DB_MASTER** | Guardián de Datos | `database-architect-strategic`, `supabase-stack-expert`, `agentic-thought-secret-scanner` | **Spec, Targeted File, Schema X-Ray, DAST** |
| **DATA_SCIENTIST** | Analista de Patrones | `autonomous-feedback-analyzer`, `apify-trend-analysis`, `agentic-thought-secret-scanner` | **Spec, Targeted File, DAST, Terminal** |

*   **Interacción Clave (SOP `execute-task`):** Los agentes de producción operan en **Clean Sessions** (M3) aisladas por el wrapper MCP, consumiendo specs físicas.

---

## ⚖️ Hub 04: Calidad y Cumplimiento (Compliance & Audit)

| AGENTE | ROL INDUSTRIAL | SKILLS AUTORIZADAS (Skill Library) | SENTIDOS (Senses) |
| :--- | :--- | :--- | :--- |
| **QA_TESTER** | Auditor de Lógica | `factory-audit-pro`, `hallucination-guardrail`, `agentic-thought-secret-scanner`, `build-test-executor`, `playwright-e2e-tester` | **Spec, Codebase X-Ray, DAST** |
| **SECURITY_AUDITOR** | Guardián Zero-Trust | `agentic-thought-secret-scanner`, `factory-audit-pro`, `dependency-vulnerability-scanner` | **Spec, Zero-Trust, DAST, Secret X-Ray** |
| **DOCS_MASTER** | Gestor del Conocimiento | `api-docs-generator`, `arxiv-technical-digest`, `hallucination-guardrail` | **Spec, Targeted File, DAST** |

*   **Interacción Clave (SOP `audit` / `scan`):** El **Auditor de Seguridad** valida el escudo Zero-Trust; el **QA** garantiza que los resultados respeten el Mandato de Unidades SI.

---

## 🚀 Hub 05: Operaciones y Evolución (Infrastructure & LTP)

| AGENTE | ROL INDUSTRIAL | SKILLS AUTORIZADAS (Skill Library) | SENTIDOS (Senses) |
| :--- | :--- | :--- | :--- |
| **DEVOPS_SRE** | Arquitecto de Nube | `docker-stack-provisioner`, `terraform-iac-builder`, `deployment-monitor`, `agentic-thought-secret-scanner`, `hallucination-guardrail` | **Spec, DAST, Infra Sandbox** |
| **DEPLOYMENT_MONITOR**| Guardián de Telemetría| `telemetry-analyzer`, `playwright-ui-tester`, `hallucination-guardrail`, `deployment-health-check` | **Log, Endpoint X-Ray, DAST** |
| **FACTORY_EVOLVER** | Arquitecto de ADN | `skill-refactor-pro`, `autonomous-feedback-analyzer`, `factory-doctor`, `hallucination-guardrail` | **Knowledge Graph (LTP), DAST, Skill Sandbox** |
| **MEMORY_OPTIMIZER** | Curador de Engramas | `autonomous-feedback-analyzer`, `context-pruning-sieve`, `hallucination-guardrail` | **Knowledge Graph (Neo4j), Context X-Ray, DAST** |

*   **Interacción Clave (SOP `sync-memory`):** El **SRE** provisiona la infraestructura; el **Optimizador de Memoria** persiste los engramas finales en Neo4j (LTP).

---
## 📦 SKILL CROSS-REFERENCE (Agentes por Skill)

Esta lista detalla qué agentes tienen permiso para invocar cada skill de la `06_SKILL_LIBRARY` vía MCP.

- **`agentic-thought-secret-scanner`**: `BACKEND_DEV`, `DATA_SCIENTIST`, `DB_MASTER`, `QA_TESTER`, `SECURITY_AUDITOR`, `DEVOPS_SRE`
- **`api-contract-generator`**: `ARCHITECT`
- **`api-docs-generator`**: `DOCS_MASTER`
- **`apify-trend-analysis`**: `MARKETING_GROWTH`, `PRODUCT_OWNER`, `RESEARCH_AGENT`, `DATA_SCIENTIST`
- **`architecture-decision-records`**: `ARCHITECT`
- **`arxiv-technical-digest`**: `RESEARCH_AGENT`, `DOCS_MASTER`
- **`async-fastapi-logic`**: `AI_ENGINEER`, `BACKEND_DEV`
- **`atomic-design-tokens`**: `FRONTEND_DEV`
- **`autonomous-feedback-analyzer`**: `DATA_SCIENTIST`, `FACTORY_EVOLVER`, `MEMORY_OPTIMIZER`
- **`build-test-executor`**: `QA_TESTER`
- **`context-pruning-sieve`**: `MEMORY_OPTIMIZER`
- **`database-architect-strategic`**: `ARCHITECT`, `DB_MASTER`
- **`delegate-clean-session`**: `ORCHESTRATOR`
- **`dependency-vulnerability-scanner`**: `SECURITY_AUDITOR`
- **`deployment-health-check`**: `DEPLOYMENT_MONITOR`
- **`deployment-monitor`**: `DEVOPS_SRE`
- **`docker-stack-provisioner`**: `DEVOPS_SRE`
- **`factory-audit-pro`**: `QA_TESTER`, `SECURITY_AUDITOR`
- **`factory-doctor`**: `ORCHESTRATOR`, `ARCHITECT`, `FACTORY_EVOLVER`
- **`frontend-ui-designer`**: `FRONTEND_DEV`
- **`hallucination-guardrail`**: `MARKETING_GROWTH`, `RESEARCH_AGENT`, `DOCS_MASTER`, `QA_TESTER`, `DEPLOYMENT_MONITOR`, `DEVOPS_SRE`, `FACTORY_EVOLVER`, `MEMORY_OPTIMIZER`
- **`kanban-solidity-gate`**: `ORCHESTRATOR`
- **`nodejs-backend-patterns`**: `BACKEND_DEV`
- **`playwright-e2e-tester`**: `FRONTEND_DEV`, `QA_TESTER`
- **`playwright-ui-tester`**: `DEPLOYMENT_MONITOR`
- **`project-backbone-validator`**: `ORCHESTRATOR`
- **`prp-generator`**: `ORCHESTRATOR`, `PRODUCT_OWNER`
- **`pytest-logic-verifier`**: `BACKEND_DEV`
- **`registry-manager`**: `ORCHESTRATOR`
- **`research-manager`**: `RESEARCH_AGENT`
- **`shadcn-component-library`**: `FRONTEND_DEV`
- **`skill-refactor-pro`**: `FACTORY_EVOLVER`
- **`social-content-strategy`**: `MARKETING_GROWTH`
- **`startup-metrics-framework`**: `PRODUCT_OWNER`
- **`supabase-stack-expert`**: `BACKEND_DEV`, `DB_MASTER`
- **`telemetry-analyzer`**: `DEPLOYMENT_MONITOR`
- **`terraform-iac-builder`**: `DEVOPS_SRE`

---
## 🛑 EL MANDATO MCP (Restricciones Críticas)

1. **Prohibición de Terminal:** Los agentes no pueden usar `bash` para mover archivos o ejecutar scripts de la `06_SKILL_LIBRARY`. El uso de las herramientas MCP **directamente por nombre** es obligatorio.
2. **Soberanía DAST:** Si una habilidad se ejecuta vía MCP y el resultado no aparece físicamente en el disco, la sesión se considera nula.
3. **Aislamiento de Escritura:** Las herramientas genéricas de `filesystem` están restringidas a la capa de `WORKSPACE/` para prevenir sabotajes accidentales en la estructura de la factoría.

---
*Mapping v5.0-MCP | Dasafo Factory Industry Standard | Soberanía Industrial Garantizada.*
