# 🗃️ AGENT REGISTRY & CAPABILITIES LOG

> **Objective:** A centralized ledger defining the strict operational boundaries, authorized external capabilities (MCP Tools), and preferred LLM parameters for every agent within `dasafo_FACTORY`.

---

## 🧭 C-Suite & Strategy (01)

### `PRODUCT_OWNER`
- **Domain:** Requirement gathering, feasibility analysis, creating `PROJECT_STATE.json`.
- **Skills:** `project-management`, `requirements-analysis-framework`, `stakeholder-value-audit`.
- **Authorized MCPs:** `github` (read repo), `search_web` (market gap analysis).
- **LLM Settings:** High Context Window (128k+), Temperature: 0.6 (Balanced creativity/structure).

### `RESEARCH_AGENT`
- **Domain:** Scientific/Technical viability, deep technical research, and fact-checking.
- **Skills:** `continuous-research`, `deep-semantic-search`, `arxiv-technical-digest`, `hallucination-guardrail`, `mcp-capabilities-architect`.
- **Authorized MCPs:** `search_web`, `read_url_content`, `arxiv_api`, `github_api`, `notebooklm`.
- **LLM Settings:** Specialized Research Models (O1/O3-mini/Gemini-Thinking), Temperature: 0.2 (Factual).

---

## 🧠 Meta-Agents (Orchestration & Reflection)

### `ORCHESTRATOR` (Semantic Router)
- **Domain:** Main Ingress Controller. Receives natural language intents, decomposes them into Directed Acyclic Graphs (DAG), and publishes events to `TASKS/01_PENDING`.
- **Skills:** `ra-agile-orchestration`, `dag-routing`, `nblm-factory-biographer`, `structured-system-design`, `bmad-ssd-orchestration`, `task-dependency-diagnostic`.
- **Authorized MCPs:** `filesystem`, `notebooklm`, `communication_relay`.
- **LLM Settings:** High-context reasoning Models. Temperature: 0.2 (Agile routing logic).

---

## 🏗️ Technical Execution (02 & 03)

### `ARCHITECT`
- **Domain:** Designing DTOs, Schemas, and System Topologies (`ARCHITECTURE.md`).
- **Skills:** `architecture-decision-records`, `tech-stack-evaluator`, `api-contract-generator`, `design-token-definition`.
- **Authorized MCPs:** `filesystem` (read-only previous projects for pattern matching).
- **LLM Settings:** High Reasoning capability. Temperature: 0.1.

### `BACKEND_DEV`
- **Domain:** Python/FastAPI logic, PostGIS schemas, Machine Learning interop.
- **Skills:** `fastapi-repository-pattern`, `async-fastapi-logic`, `safe-db-migrations`, `resilient-error-handling`.
- **Authorized MCPs:** `filesystem` (write to `$TARGET_PROJECT/WORKSPACE/backend`), `run_command` (Python interpreters/Pytest).
- **LLM Settings:** Coding-specialized Models (Claude 3.5 Sonnet / GPT-4o). Temperature: 0.0.

### `FRONTEND_DEV`
- **Domain:** React/Next.js UI components. Enforcing Atomic Design tokens.
- **Skills:** `premium-dashboard-architecture`, `framer-motion-transitions`, `shadcn-component-library`, `atomic-design-tokens`.
- **Authorized MCPs:** `filesystem` (write to `$TARGET_PROJECT/WORKSPACE/frontend`), `run_command` (Node/npm).
- **LLM Settings:** Coding-specialized Models. Temperature: 0.2 (Slight leeway for visual creativity).

### `DATA_SCIENTIST`
- **Domain:** Explanatory Data Analysis (EDA), predictive modeling, and statistical reporting.
- **Skills:** `sklearn-pipeline-master`, `pandas-vectorized-pro`, `notebooklm-nexus`, `ml-experiment-log`.
- **Authorized MCPs:** `python_interpreter`, `sql_connector`, `jupyter_mcp`, `visualization_engine`, `notebooklm`.
- **LLM Settings:** Reasoning-heavy models (e.g., Claude 3.5 Sonnet). Temperature: 0.1 (Precise).

### `DB_MASTER`
- **Domain:** Database architecture, schema integrity, and performance tuning.
- **Skills:** `supabase-stack-expert`, `database-architect-strategic`, `sql-performance-tuner`, `nblm-schema-nexus`.
- **Authorized MCPs:** `sql_engine`, `erd_generator`, `migration_manager`, `performance_profiler`, `notebooklm`, `supabase`.
- **LLM Settings:** Logic-focused (GPT-4o / Claude 3.5 Sonnet). Temperature: 0.0 (Strict).

---

## 🛡️ QA & Feedback Loop (04)

### `QA_TESTER`
- **Domain:** End-to-end integration testing and requirement validation.
- **Skills:** `scoutqa-automated-suites`, `playwright-visual-testing`, `requirements-validation-audit`, `hallucination-report-guardrail`.
- **Authorized MCPs:** `run_command` (docker-compose, pytest, npm run test), `browser_sandbox`, `filesystem`.
- **LLM Settings:** Strict Code Review Models (e.g., Claude 3.5 Sonnet). Temperature: 0.0 (Strictly deterministic).

### `SECURITY_AUDITOR` (Guardrail)
- **Domain:** Prompt injection mitigation, PII masking, Zero-Trust enforcement.
- **Skills:** `nemo-llm-guardrails`, `agentic-thought-secret-scanner`, `owasp-llm-enforcement`.
- **Authorized MCPs:** `snyk_mcp`, `gitleaks_tool`, `agent_guardrail_scanner`, `dependency_graph`.
- **LLM Settings:** Security-optimized Models (Maximum Caution). Temperature: 0.0 (Strictly deterministic).

---

## 🚀 Operations & Scaling (05)

### `DEVOPS_SRE`
- **Domain:** Infrastructure as Code (IaC), CI/CD, and MLOps deployment.
- **Skills:** `docker-devops-expert`, `github-actions-cicd-patterns`, `infra-as-code-terraform-pro`, `mlops-deployment-guard`.
- **Authorized MCPs:** `docker_engine`, `terraform_cloud`, `bash_runtime`, `github_actions_runner`, `system_monitor`.
- **LLM Settings:** Logic-heavy Models. Temperature: 0.0 (High Reliability).

### `MARKETING_GROWTH`
- **Domain:** Channel optimization, Go-To-Market strategies, and evidence-based storytelling.
- **Skills:** `apify-trend-analysis`, `social-content-strategy`, `evidence-based-copywriting`, `nemo-guardrails-safety`, `content-quality-auditor`.
- **Authorized MCPs:** `search_web`, `read_url_content`, `apify`.
- **LLM Settings:** Balanced capability (GPT-4o / Claude 3.5 Sonnet). Temperature: 0.3.

### `MEMORY_OPTIMIZER`
- **Domain:** Context management, log distillation, and long-term memory curation.
- **Skills:** `search-context-distillation-pro`, `ml-history-indexer`, `nblm-memory-bridge`, `clutch-resource-cleaner`.
- **Authorized MCPs:** `filesystem`, `notebooklm`, `sql_engine` (Vector ops).
- **LLM Settings:** Compression-specialized Models. Temperature: 0.1 (Precise summaries).
