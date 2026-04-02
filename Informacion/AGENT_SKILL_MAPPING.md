# 🗺️ Mapeo Exhaustivo de AGENTES Y SKILLS

> **Versión:** v4.0-S "Industrial Core - Mapping Enabled"
> **Misión:** Establecer la matriz definitiva de autoridad, sentidos (senses) y capacidades técnicas.
> **Gobernanza:** Zero-Trust de Identidad / SDD de Ejecución / Unidades SI (s, B)

Este documento define las fronteras de acción de cada uno de los **17 agentes** de la factoría. Solo los agentes listados poseen autorización técnica para invocar las habilidades correspondientes dentro del entorno industrial.

---

## 🏛️ HUB 01: ESTRATEGIA, PRODUCTO Y MARKETING

El centro de mando que transforma necesidades humanas en contratos industriales y coordina el pipeline.

| Agente | Rol Industrial | Skills Autorizadas (Hub 01) | Sentidos (Senses) |
| :--- | :--- | :--- | :--- |
| **ORCHESTRATOR** | Director Estratégico | `delegate-clean-session`, `kanban-solidity-gate`, `registry-manager`, `factory-doctor`, `project-backbone-validator` | **Registry, Hub, Contract, Evidence** |
| **PRODUCT_OWNER** | Arquitecto de Visión | `prp-generator`, `startup-metrics-framework`, `apify-trend-analysis`, `registry-manager` | **Market, Contract, Evidence** |
| **MARKETING_GROWTH** | Estratega de Crecimiento | `social-content-strategy`, `hallucination-guardrail`, `copywriting-evidence`, `registry-manager` | **Market, Targeted File** |

*   **Interacción Clave:** El **Product Owner** firma el contrato (M1); el **Orquestador** lo deconstruye y el **Marketing** lo posiciona.

---

## 📐 HUB 02: ARQUITECTURA E INVESTIGACIÓN

El núcleo técnico que define la estructura ósea y reduce la incertidumbre tecnológica.

| Agente | Rol Industrial | Skills Autorizadas (Hub 02) | Sentidos (Senses) |
| :--- | :--- | :--- | :--- |
| **ARCHITECT** | Diseñador del Backbone | `architecture-decision-records`, `api-contract-generator`, `database-architect-strategic`, `data-schema-generator`, `registry-manager` | **Structural, Evidence, Schema X-Ray** |
| **RESEARCH_AGENT** | Analista Factual | `web-research-engine`, `arxiv-technical-digest`, `hallucination-guardrail`, `registry-manager` | **Deep Search, Market, Evidence** |

*   **Interacción Clave:** La **Arquitectura** traduce la visión en planos (M2); la **Investigación** valida que las herramientas propuestas sean viables y estables.

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

*   **Interacción Clave:** Los peones de producción trabajan bajo **Clean Sessions** (M3), guiados por las especificaciones del Arquitecto.

---

## 🛡️ HUB 04: CALIDAD Y CUMPLIMIENTO (COMPLIANCE)

El departamento que garantiza la seguridad, solidez y veracidad de cada entrega.

| Agente | Rol Industrial | Skills Autorizadas (Hub 04) | Sentidos (Senses) |
| :--- | :--- | :--- | :--- |
| **QA_TESTER** | Inspector de Solidez | `playwright-e2e-tester`, `build-test-executor`, `hallucination-guardrail`, `factory-audit-pro`, `registry-manager` | **Codebase X-Ray, Spec, Evidence** |
| **SECURITY_AUDITOR** | Guardián Zero-Trust | `agentic-thought-secret-scanner`, `factory-audit-pro`, `dependency-vulnerability-scanner`, `registry-manager` | **Secret X-Ray, Codebase X-Ray** |
| **DOCS_MASTER** | Gestor del Conocimiento | `api-docs-generator`, `readme-sync-expert`, `registry-manager` | **Codebase X-Ray, Targeted File** |

*   **Interacción Clave:** El **Auditor de Seguridad** bloquea el pipeline (Gate M4) si detecta filtraciones; el **QA** garantiza que las **Unidades SI** se cumplan.

---

## 🚀 HUB 05: OPERACIONES Y EVOLUCIÓN

La capa externa que gestiona el despliegue, la salud del sistema y el aprendizaje de la factoría.

| Agente | Rol Industrial | Skills Autorizadas (Hub 05) | Sentidos (Senses) |
| :--- | :--- | :--- | :--- |
| **DEVOPS_SRE** | Ingeniero de Plataforma | `infra-provisioner`, `terraform-iac-builder`, `docker-stack-provisioner`, `registry-manager`, `auto-heal-trigger` | **Infra, Deploy, Evidence** |
| **DEPLOYMENT_MONITOR** | Centinela Sentinel | `deployment-health-check`, `latency-pulse-reporter`, `registry-manager` | **Deploy, Physical Disk** |
| **FACTORY_EVOLVER** | Arquitecto de ADN | `skill-refactor-pro`, `factory-upgrade-manager`, `factory-doctor`, `registry-manager` | **Skill X-Ray, Registry, Evidence** |
| **MEMORY_OPTIMIZER** | Curador de Engramas | `context-pruning-sieve`, `kg-db-sync`, `registry-manager` | **Skill X-Ray, Evidence** |

*   **Interacción Clave:** El **SRE** despliega el producto (M5); el **Optimizador de Memoria** sincroniza los aprendizajes finales con el Grafo de Neo4j (LTP).

---

## ☣️ ESPECIFICACIONES DE SEGURIDAD TRANSVERSAL

Existen habilidades que operan fuera de la jerarquía de Hubs para garantizar la integridad absoluta:

1.  **`registry-manager`**: Única herramienta autorizada para el movimiento físico de tareas entre carpetas (`01_PENDING` -> `03_COMPLETED`). Es el motor del DAST.
2.  **`hallucination-guardrail`**: Filtro de salida obligatorio para todos los agentes. Compara respuestas contra la base de conocimiento global.
3.  **`agentic-thought-secret-scanner`**: Escudo proactivo que escanea el pensamiento del agente antes de que cualquier acción se ejecute en el disco.

---
*Mapping v4.0-S | Dasafo Factory Industry Standard | Inmutable y Verificable.*
