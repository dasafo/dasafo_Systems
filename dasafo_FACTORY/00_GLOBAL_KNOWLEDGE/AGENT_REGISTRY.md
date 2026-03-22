# 🗃️ AGENT REGISTRY & CAPABILITIES LOG

> **Objective:** A centralized ledger defining the strict operational boundaries, authorized external capabilities (MCP Tools), and preferred LLM parameters for every agent within `dasafo_FACTORY`.

---

## 🧭 C-Suite & Strategy (01)

### `PRODUCT_OWNER`
- **Domain:** Requirement gathering, feasibility analysis, creating `PROJECT_STATE.json`.
- **Authorized MCPs:** `github` (read repo), `search_web` (market gap analysis).
- **LLM Settings:** High Context Window (128k+), Temperature: 0.6 (Balanced creativity/structure).

### `RESEARCH_AGENT`
- **Domain:** Scientific/Technical viability, generating `LOCAL_KNOWLEDGE/RESEARCH_NOTES.md`.
- **Authorized MCPs:** `search_web`, `read_url_content`.
- **LLM Settings:** Specialized Research Models (O1/O3-mini/Gemini-Thinking), Temperature: 0.2 (Factual).

---

## 🧠 Meta-Agents (Orchestration & Reflection)

### `ORCHESTRATOR` (Semantic Router)
- **Domain:** Main Ingress Controller. Receives natural language intents, decomposes them into Directed Acyclic Graphs (DAG), and publishes events to `TASKS/01_PENDING`.
- **Authorized MCPs:** Intra-filesystem reading only.
- **LLM Settings:** High Speed/Low Latency (e.g., GPT-4o-mini, Haiku). Temperature: 0.0 (Strictly deterministic JSON routing).

### `MEMORY_OPTIMIZER`
- **Domain:** Context compression. Reads historical logs, compresses episodic memory into semantic vectors to prevent Token Exhaustion.
- **Authorized MCPs:** Vector DB integrations (Pinecone/Supabase Vector).
- **LLM Settings:** High Speed, Temperature: 0.1.

---

## 🏗️ Technical Execution (02 & 03)

### `ARCHITECT`
- **Domain:** Designing DTOs, Schemas, and System Topologies (`ARCHITECTURE.md`).
- **Authorized MCPs:** `filesystem` (read-only previous projects for pattern matching).
- **LLM Settings:** High Reasoning capability. Temperature: 0.1.

### `BACKEND_DEV`
- **Domain:** Python/FastAPI logic, PostGIS schemas, Machine Learning interop.
- **Authorized MCPs:** `filesystem` (write to `$TARGET_PROJECT/WORKSPACE/backend`), `run_command` (Python interpreters/Pytest).
- **LLM Settings:** Coding-specialized Models (Claude 3.5 Sonnet / GPT-4o). Temperature: 0.0.

### `FRONTEND_DEV`
- **Domain:** React/Next.js UI components. Enforcing Atomic Design tokens.
- **Authorized MCPs:** `filesystem` (write to `$TARGET_PROJECT/WORKSPACE/frontend`), `run_command` (Node/npm).
- **LLM Settings:** Coding-specialized Models. Temperature: 0.2 (Slight leeway for visual creativity).

---

## 🛡️ QA & Feedback Loop (04)

### `QA_TESTER`
- **Domain:** Integration testing. Validating Atomic Completeness and Docker Proof-of-Build.
- **Authorized MCPs:** `run_command` (docker-compose, pytest, npm run test).
- **LLM Settings:** Strict Code Review Models. Temperature: 0.0.

### `SECURITY_AUDITOR` (Guardrail)
- **Domain:** Prompt injection mitigation, PII masking, Zero-Trust enforcement.
- **Authorized MCPs:** Static analysis tools (`bandit`, `npm audit`).
- **LLM Settings:** specialized security fine-tunes. Temperature: 0.0.

---

## 🚀 DevOps & MLOps (05)

### `DEVOPS_SRE`
- **Domain:** Containerization, `docker-compose.yml`, CI/CD pipelines, Auto-deployments.
- **Authorized MCPs:** `run_command` (Docker Engine, shell).
- **LLM Settings:** Highly deterministic. Temperature: 0.0.
