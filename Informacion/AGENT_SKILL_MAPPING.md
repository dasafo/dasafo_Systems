# 🗺️ Agent-Skill Mapping | Dasafo Factory (v4.0-S)

Este documento define la matriz de autoridad entre los Agentes de la Factoría y la **Skill Library**. Solo los agentes listados tienen permiso para invocar las skills correspondientes bajo protocolo industrial.

---

## 🏛️ 1. STRATEGY & MARKETING

| Agente | Skills Autorizadas | Propósito Principal |
| :--- | :--- | :--- |
| **ORCHESTRATOR** | `delegate-clean-session`, `prp-generator`, `kanban-solidity-gate`, `registry-manager`, `factory-doctor`, `project-backbone-validator` | Orquestación, deconstrucción, control de fases, sanación de estados y validación de andamiaje. |
| **PRODUCT_OWNER** | `prp-generator`, `apify-trend-analysis`, `startup-metrics-framework`, `registry-manager` | Creación de PRP_MASTER, análisis de mercado, viabilidad financiera y gestión de registro. |
| **MARKETING_GROWTH** | `apify-trend-analysis`, `social-content-strategy`, `hallucination-guardrail`, `registry-manager` | Ejecución de campañas, análisis de señales externas y auditoría de marca. |

---

## 📐 2. ARCHITECTURE & RESEARCH

| Agente | Skills Autorizadas | Propósito Principal |
| :--- | :--- | :--- |
| **ARCHITECT** | `architecture-decision-records`, `api-contract-generator`, `database-architect-strategic`, `registry-manager`, `factory-doctor` | Diseño de planos técnicos, contratos API, modelado de datos y auditoría previa a M2. |
| **RESEARCH_AGENT** | `arxiv-technical-digest`, `apify-trend-analysis`, `registry-manager`, `hallucination-guardrail` | Investigación científica, validación de hipótesis y auditoría factual. |

---

## ⚙️ 3. PRODUCTION (M3)

| Agente | Skills Autorizadas | Propósito Principal |
| :--- | :--- | :--- |
| **BACKEND_DEV** | `async-fastapi-logic`, `supabase-stack-expert`, `pytest-logic-verifier`, `registry-manager`, `nodejs-backend-patterns`, `agentic-thought-secret-scanner` | Implementación de APIs, lógica de dominio, patrones Repository y verificación de seguridad. |
| **FRONTEND_DEV** | `shadcn-component-library`, `atomic-design-tokens`, `registry-manager`, `frontend-ui-designer`, `playwright-e2e-tester` | Construcción de UIs atómicas, diseño premium, pruebas de regresión y flujos de usuario. |
| **DB_MASTER** | `database-architect-strategic`, `supabase-stack-expert`, `registry-manager`, `agentic-thought-secret-scanner` | Ejecución de esquemas, migraciones físicas y seguridad de datos RLS. |
| **DATA_SCIENTIST** | `autonomous-feedback-analyzer`, `apify-trend-analysis`, `agentic-thought-secret-scanner`, `registry-manager` | Modelado IA, análisis de patrones y protección de PII/Secretos en datasets. |

---

## 🛡️ 4. COMPLIANCE & QUALITY

| Agente | Skills Autorizadas | Propósito Principal |
| :--- | :--- | :--- |
| **SECURITY_AUDITOR** | `agentic-thought-secret-scanner`, `factory-audit-pro`, `registry-manager` | Caza de vulnerabilidades, escaneo de secretos y auditoría de salud industrial. |
| **QA_TESTER** | `factory-audit-pro`, `hallucination-guardrail`, `agentic-thought-secret-scanner`, `build-test-executor`, `playwright-e2e-tester`, `registry-manager` | Auditoría, validación de evidencias físicas, ejecución de CI local y pruebas E2E. |
| **DOCS_MASTER** | `api-docs-generator`, `arxiv-technical-digest`, `registry-manager`, `hallucination-guardrail` | Extracción de documentación técnica, manuales y verificación de veracidad factual. |

---

## 🚀 5. OPERATIONS & EVOLUTION

| Agente | Skills Autorizadas | Propósito Principal |
| :--- | :--- | :--- |
| **DEVOPS_SRE** | `docker-stack-provisioner`, `terraform-iac-builder`, `deployment-health-check`, `registry-manager`, `agentic-thought-secret-scanner`, `hallucination-guardrail` | Provisión IaC, contenedores, monitoreo de infraestructura y seguridad de despliegue. |
| **DEPLOYMENT_MONITOR** | `deployment-health-check`, `playwright-e2e-tester`, `registry-manager`, `hallucination-guardrail` | Análisis de salud en tiempo real (s/B) y monitoreo sentinel de entornos live. |
| **FACTORY_EVOLVER** | `skill-refactor-pro`, `autonomous-feedback-analyzer`, `registry-manager`, `factory-doctor`, `hallucination-guardrail` | Optimización del ADN de la factoría, refactorización de skills y sanación del sistema. |
| **MEMORY_OPTIMIZER** | `autonomous-feedback-analyzer`, `context-pruning-sieve`, `registry-manager`, `hallucination-guardrail` | Sincronización con Neo4j, poda de contexto y arquitectura de memoria LTP. |

---

### 🛡️ Guardrail Transversal

Skills que pueden (y deben) ser invocadas por cualquier agente en modo auditoría o como paso final de tarea:

- `hallucination-guardrail`: Verificación de integridad factual contra SSoT.
- `agentic-thought-secret-scanner`: Prevención de fugas de credenciales en logs y pensamiento.
- `registry-manager`: Único medio autorizado para marcar tareas como `COMPLETED` físicamente.

---

## 🧰 6. Mapeo Inverso: Skill → Agentes Autorizados (v4.0-S)

| Skill | Agentes que la Utilizan |
| :--- | :--- |
| `prp-generator` | `PRODUCT_OWNER`, `ORCHESTRATOR` |
| `apify-trend-analysis` | `PRODUCT_OWNER`, `MARKETING_GROWTH`, `RESEARCH_AGENT`, `DATA_SCIENTIST` |
| `registry-manager` | `TODOS` (Mandatorio para transiciones físicas) |
| `factory-doctor` | `ORCHESTRATOR`, `ARCHITECT`, `FACTORY_EVOLVER` |
| `hallucination-guardrail` | `TODOS` |
| `agentic-thought-secret-scanner` | `TODOS` (Principalmente `SECURITY`, `BACKEND`, `QA`, `DEVOPS`) |
| `factory-audit-pro` | `QA_TESTER`, `SECURITY_AUDITOR` |
| `architecture-decision-records` | `ARCHITECT` |
| `api-contract-generator` | `ARCHITECT` |
| `database-architect-strategic` | `ARCHITECT`, `DB_MASTER` |
| `api-docs-generator` | `DOCS_MASTER` |
| `async-fastapi-logic` | `BACKEND_DEV` |
| `nodejs-backend-patterns` | `BACKEND_DEV` |
| `arxiv-technical-digest` | `RESEARCH_AGENT`, `DOCS_MASTER` |
| `supabase-stack-expert` | `BACKEND_DEV`, `DB_MASTER` |
| `shadcn-component-library` | `FRONTEND_DEV` |
| `atomic-design-tokens` | `FRONTEND_DEV` |
| `frontend-ui-designer` | `FRONTEND_DEV` |
| `autonomous-feedback-analyzer` | `DATA_SCIENTIST`, `FACTORY_EVOLVER`, `MEMORY_OPTIMIZER` |
| `playwright-e2e-tester` | `QA_TESTER`, `FRONTEND_DEV`, `DEPLOYMENT_MONITOR` |
| `pytest-logic-verifier` | `BACKEND_DEV` |
| `build-test-executor` | `QA_TESTER` |
| `docker-stack-provisioner` | `DEVOPS_SRE` |
| `terraform-iac-builder` | `DEVOPS_SRE` |
| `deployment-health-check` | `DEVOPS_SRE`, `DEPLOYMENT_MONITOR` |
| `skill-refactor-pro` | `FACTORY_EVOLVER` |
| `context-pruning-sieve` | `MEMORY_OPTIMIZER` |
| `project-backbone-validator` | `ORCHESTRATOR` |
| `startup-metrics-framework` | `PRODUCT_OWNER` |
| `social-content-strategy` | `MARKETING_GROWTH` |

---
> [!NOTE]
> **Mapping v4.0-S | Dasafo Factory Industry Standard**
> Este mapping es inmutable para los agentes; cualquier desviación resultará en fallo de ejecución por falta de autoridad.
