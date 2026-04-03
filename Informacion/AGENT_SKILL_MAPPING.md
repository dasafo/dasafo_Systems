# 🗺️ Mapeo Exhaustivo de AGENTES Y SKILLS

> **Versión:** v4.0-MCP "Native Industrial Core"
> **Misión:** Establecer la matriz definitiva de autoridad, sentidos (senses) y capacidades técnicas mediante MCP.
> **Gobernanza:** Zero-Trust / Spec Driven Development / MCP Tool Mandate / Unidades SI (s, B)

Este documento define las fronteras de acción de cada uno de los **17 agentes**. Bajo el estándar **v4.0-MCP**, la ejecución de habilidades se realiza exclusivamente a través del motor industrial (`execute_industrial_skill`), garantizando la auditoría total y la soberanía del disco (DAST).

---

## 🏛️ HUB 01: ESTRATEGIA, PRODUCTO Y MARKETING

El centro de mando que transforma necesidades humanas en contratos industriales y coordina el pipeline.

| Agente | Rol Industrial | Skills Autorizadas (Hub 01) | Sentidos (Senses) |
| :--- | :--- | :--- | :--- |
| **ORCHESTRATOR** | Director Estratégico | `delegate-clean-session`, `kanban-solidity-gate`, `registry-manager`, `factory-doctor`, `project-backbone-validator` | **Registry, Hub, Contract, Evidence** |
| **PRODUCT_OWNER** | Arquitecto de Visión | `prp-generator`, `startup-metrics-framework`, `apify-trend-analysis`, `registry-manager` | **Market, Contract, Evidence** |
| **MARKETING_GROWTH** | Estratega de Crecimiento | `social-content-strategy`, `hallucination-guardrail`, `copywriting-evidence`, `registry-manager` | **Market, Targeted File** |

*   **Interacción Clave (SOP `init-contract`):** El **Product Owner** sella la visión; el **Orquestador** activa el pipeline vía MCP.

---

## 📐 HUB 02: ARQUITECTURA E INVESTIGACIÓN

El núcleo técnico que define la estructura ósea y reduce la incertidumbre tecnológica.

| Agente | Rol Industrial | Skills Autorizadas (Hub 02) | Sentidos (Senses) |
| :--- | :--- | :--- | :--- |
| **ARCHITECT** | Diseñador del Backbone | `architecture-decision-records`, `api-contract-generator`, `database-architect-strategic`, `data-schema-generator`, `registry-manager` | **Structural, Evidence, Schema X-Ray** |
| **RESEARCH_AGENT** | Analista Factual | `web-research-engine`, `arxiv-technical-digest`, `hallucination-guardrail`, `registry-manager` | **Deep Search, Market, Evidence** |

*   **Interacción Clave (SOP `arch-diagram`):** La **Arquitectura** solidifica los planos (M2); la **Investigación** valida la viabilidad técnica antes del primer byte de código.

---

## ⚙️ HUB 03: PRODUCCIÓN E IMPLEMENTACIÓN

La línea de montaje física donde se construye el código, los esquemas de datos y la UI.

| Agente | Rol Industrial | Skills Autorizadas (Hub 03) | Sentidos (Senses) |
| :--- | :--- | :--- | :--- |
| **BACKEND_DEV** | Ingeniero de Lógica | `async-fastapi-logic`, `nodejs-backend-patterns`, `pytest-logic-verifier`, `registry-manager` | **Spec, Targeted File** |
| **FRONTEND_DEV** | Diseñador de Interfaz | `frontend-ui-designer`, `shadcn-component-library`, `playwright-e2e-tester`, `atomic-design-tokens`, `registry-manager` | **Spec, Targeted File** |
| **DB_MASTER** | Estratega de Datos | `database-architect-strategic`, `supabase-stack-expert`, `sql-migration-pro`, `registry-manager` | **Spec, Schema X-Ray** |
| **DATA_SCIENTIST** | Analista de Patrones | `autonomous-feedback-analyzer`, `telemetry-reporting`, `registry-manager` | **Schema X-Ray, Evidence** |
| **AI_ENGINEER** | Ingeniero de IA | `llm-logic-integration`, `prompt-engineering-refactor`, `agentic-pattern-builder`, `registry-manager` | **Spec, Targeted File** |

*   **Interacción Clave (SOP `execute-task`):** Los agentes de producción operan en **Clean Sessions** (M3) aisladas por el wrapper MCP, consumiendo specs físicas.

---

## 🛡️ HUB 04: CALIDAD Y CUMPLIMIENTO (COMPLIANCE)

El departamento que garantiza la seguridad, solidez y veracidad de cada entrega.

| Agente | Rol Industrial | Skills Autorizadas (Hub 04) | Sentidos (Senses) |
| :--- | :--- | :--- | :--- |
| **QA_TESTER** | Inspector de Solidez | `playwright-e2e-tester`, `build-test-executor`, `hallucination-guardrail`, `factory-audit-pro`, `registry-manager` | **Codebase X-Ray, Spec, Evidence** |
| **SECURITY_AUDITOR** | Guardián Zero-Trust | `agentic-thought-secret-scanner`, `factory-audit-pro`, `dependency-vulnerability-scanner`, `registry-manager` | **Secret X-Ray, Codebase X-Ray** |
| **DOCS_MASTER** | Gestor del Conocimiento | `api-docs-generator`, `readme-sync-expert`, `registry-manager` | **Codebase X-Ray, Targeted File** |

*   **Interacción Clave (SOP `audit` / `scan`):** El **Auditor de Seguridad** valida el escudo Zero-Trust; el **QA** garantiza que los resultados respeten el Mandato de Unidades SI.

---

## 🚀 HUB 05: OPERACIONES Y EVOLUCIÓN

La capa externa que gestiona el despliegue, la salud del sistema y el aprendizaje de la factoría.

| Agente | Rol Industrial | Skills Autorizadas (Hub 05) | Sentidos (Senses) |
| :--- | :--- | :--- | :--- |
| **DEVOPS_SRE** | Ingeniero de Plataforma | `infra-provisioner`, `terraform-iac-builder`, `docker-stack-provisioner`, `registry-manager`, `auto-heal-trigger` | **Infra, Deploy, Evidence** |
| **DEPLOYMENT_MONITOR** | Centinela Sentinel | `deployment-health-check`, `latency-pulse-reporter`, `registry-manager` | **Deploy, Physical Disk** |
| **FACTORY_EVOLVER** | Arquitecto de ADN | `skill-refactor-pro`, `factory-upgrade-manager`, `factory-doctor`, `registry-manager` | **Skill X-Ray, Registry, Evidence** |
| **MEMORY_OPTIMIZER** | Curador de Engramas | `context-pruning-sieve`, `kg-db-sync`, `registry-manager` | **Skill X-Ray, Evidence** |

*   **Interacción Clave (SOP `sync-memory`):** El **SRE** provisiona la infraestructura; el **Optimizador de Memoria** persiste los engramas finales en Neo4j (LTP).

---

## 🛑 EL MANDATO MCP (Restricciones Críticas)

1. **Prohibición de Terminal:** Los agentes no pueden usar `bash` para mover archivos o ejecutar scripts de la `06_SKILL_LIBRARY`. El uso de `execute_industrial_skill` es obligatorio.
2. **Soberanía DAST:** Si una habilidad se ejecuta vía MCP y el resultado no aparece físicamente en el disco, la sesión se considera nula.
3. **Aislamiento de Escritura:** Las herramientas genéricas de `filesystem` están restringidas a la capa de `WORKSPACE/` para prevenir sabotajes accidentales en la estructura de la factoría.

---
*Mapping v4.0-MCP | Dasafo Factory Industry Standard | Soberanía Industrial Garantizada.*
