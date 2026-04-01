# 🗺️ Agent-Skill Mapping | Dasafo Factory (v4.0-S)

Este documento define la matriz de autoridad entre los Agentes de la Factoría y la **Skill Library**. Solo los agentes listados tienen permiso para invocar las skills correspondientes bajo protocolo industrial.

---

## 🏛️ 1. STRATEGY & MARKETING

| Agente | Skills Autorizadas | Propósito Principal |
| :--- | :--- | :--- |
| **ORCHESTRATOR** | `delegate-clean-session`, `prp-generator`, `kanban-solidity-gate`, `registry-manager` | Delegación, deconstrucción de PRP, control de fases y gestión del registro Kanban. |
| **PRODUCT_OWNER** | `prp-generator`, `apify-trend-analysis`, `project-management` | Creación de PRP_MASTER, análisis de mercado y gestión de procesos. |
| **MARKETING_GROWTH** | `apify-trend-analysis`, `social-content-strategy`, `hallucination-guardrail`, `factory-audit-pro` | Ejecución de campañas, análisis de tendencias y auditoría de marca. |

---

## 📐 2. ARCHITECTURE & RESEARCH

| Agente | Skills Autorizadas | Propósito Principal |
| :--- | :--- | :--- |
| **ARCHITECT** | `architecture-decision-records`, `api-contract-generator`, `database-architect-strategic`, `api-docs-generator`, `async-fastapi-logic` | Diseño de planos, contratos API, modelado de datos y scaffolding. |
| **RESEARCH_AGENT** | `arxiv-technical-digest`, `apify-trend-analysis`, `hallucination-guardrail` | Investigación académica, validación de tendencias y auditoría factual. |

---

## ⚙️ 3. PRODUCTION (M3)

| Agente | Skills Autorizadas | Propósito Principal |
| :--- | :--- | :--- |
| **BACKEND_DEV** | `async-fastapi-logic`, `supabase-stack-expert`, `agentic-thought-secret-scanner`, `api-contract-generator`, `pytest-logic-verifier` | Implementación de APIs, lógica de dominio, seguridad y verificación de lógica backend. |
| **FRONTEND_DEV** | `shadcn-component-library`, `atomic-design-tokens`, `playwright-ui-tester`, `playwright-e2e-tester` | Construcción de UIs atómicas, pruebas de regresión visual y flujos E2E. |
| **DB_MASTER** | `database-architect-strategic`, `supabase-stack-expert`, `agentic-thought-secret-scanner` | Ejecución de esquemas, migraciones y seguridad RLS. |
| **DATA_SCIENTIST** | `autonomous-feedback-analyzer`, `apify-trend-analysis`, `agentic-thought-secret-scanner` | Modelado IA, análisis de datos y protección PII. |

---

## 🛡️ 4. COMPLIANCE & QUALITY

| Agente | Skills Autorizadas | Propósito Principal |
| :--- | :--- | :--- |
| **SECURITY_AUDITOR** | `agentic-thought-secret-scanner`, `factory-audit-pro`, `dependency-vulnerability-scanner` | Caza de vulnerabilidades, escaneo de secretos y auditoría de CVEs. |
| **QA_TESTER** | `factory-audit-pro`, `hallucination-guardrail`, `agentic-thought-secret-scanner`, `build-test-executor`, `playwright-e2e-tester`, `pytest-logic-verifier` | Auditoría, validación de evidencias, ejecución de builds y pruebas lógicas/E2E. |
| **DOCS_MASTER** | `api-docs-generator`, `arxiv-technical-digest`, `hallucination-guardrail` | Documentación técnica, manuales y verificación de veracidad. |

---

## 🚀 5. OPERATIONS & EVOLUTION

| Agente | Skills Autorizadas | Propósito Principal |
| :--- | :--- | :--- |
| **DEVOPS_SRE** | `docker-stack-provisioner`, `terraform-iac-builder`, `agentic-thought-secret-scanner`, `hallucination-guardrail`, `build-test-executor`, `telemetry-analyzer` | Provisión de infra (IaC), contenedores, seguridad y monitoreo de salud. |
| **DEPLOYMENT_MONITOR** | `telemetry-analyzer`, `playwright-ui-tester`, `hallucination-guardrail` | Análisis de latencia (s/B) y monitoreo de salud en tiempo real. |
| **FACTORY_EVOLVER** | `autonomous-feedback-analyzer`, `skill-refactor-pro`, `autoshield-preflight-check`, `hallucination-guardrail` | Evolución del framework, refactorización de skills y mejora de tokens. |
| **MEMORY_OPTIMIZER** | `context-pruning-sieve`, `hallucination-guardrail` | Poda de contexto y optimización de memoria de sesión. |

---

### 🛡️ Guardrail Transversal

Skills que pueden ser invocadas por cualquier agente en modo auditoría:

- `hallucination-guardrail`: Verificación de integridad factual.
- `agentic-thought-secret-scanner`: Prevención de fugas de credenciales.

---
> [!NOTE]
> **Mapping v4.0-S | Dasafo Factory Industry Standard**

---

## 🧰 6. Mapeo Inverso: Skill → Agentes Autorizados

| Skill | Agentes que la Utilizan |
| :--- | :--- |
| `prp-generator` | `PRODUCT_OWNER`, `ORCHESTRATOR` |
| `apify-trend-analysis` | `PRODUCT_OWNER`, `MARKETING_GROWTH`, `RESEARCH_AGENT`, `DATA_SCIENTIST` |
| `project-management` | `PRODUCT_OWNER` |
| `delegate-clean-session` | `ORCHESTRATOR` |
| `kanban-solidity-gate` | `ORCHESTRATOR` |
| `social-content-strategy` | `MARKETING_GROWTH` |
| `hallucination-guardrail` | `TODOS` (Principalmente `QA`, `SECURITY`, `RESEARCH`, `OPS`) |
| `factory-audit-pro` | `MARKETING_GROWTH`, `QA_TESTER`, `SECURITY_AUDITOR` |
| `architecture-decision-records` | `ARCHITECT` |
| `api-contract-generator` | `ARCHITECT`, `BACKEND_DEV` |
| `database-architect-strategic` | `ARCHITECT`, `DB_MASTER` |
| `api-docs-generator` | `ARCHITECT`, `DOCS_MASTER` |
| `async-fastapi-logic` | `ARCHITECT`, `BACKEND_DEV` |
| `arxiv-technical-digest` | `RESEARCH_AGENT`, `DOCS_MASTER` |
| `supabase-stack-expert` | `BACKEND_DEV`, `DB_MASTER` |
| `agentic-thought-secret-scanner` | `TODOS` (Principalmente `SECURITY`, `BACKEND`, `DB`, `DEVOPS`) |
| `shadcn-component-library` | `FRONTEND_DEV` |
| `atomic-design-tokens` | `FRONTEND_DEV` |
| `playwright-ui-tester` | `FRONTEND_DEV`, `DEPLOYMENT_MONITOR` |
| `autonomous-feedback-analyzer` | `DATA_SCIENTIST`, `FACTORY_EVOLVER` |
| `dependency-vulnerability-scanner` | `SECURITY_AUDITOR` |
| `telemetry-analyzer` | `DEPLOYMENT_MONITOR`, `DEVOPS_SRE` |
| `docker-stack-provisioner` | `DEVOPS_SRE` |
| `terraform-iac-builder` | `DEVOPS_SRE` |
| `skill-refactor-pro` | `FACTORY_EVOLVER` |
| `autoshield-preflight-check` | `FACTORY_EVOLVER` |
| `context-pruning-sieve` | `MEMORY_OPTIMIZER` |
| `registry-manager` | `ORCHESTRATOR` |
| `build-test-executor` | `DEVOPS_SRE`, `QA_TESTER` |
| `playwright-e2e-tester` | `QA_TESTER`, `FRONTEND_DEV` |
| `pytest-logic-verifier` | `QA_TESTER`, `BACKEND_DEV` |

---
> [!NOTE]
> **Mapping v4.0-S | Dasafo Factory Industry Standard**
