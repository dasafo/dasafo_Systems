# 🏭 dasafo_FACTORY Operations Manual

This document is the **Technical Constitution** of the Factory. It defines how software projects are created, executed, and validated autonomously, non-deterministically, and ultra-robustly.

---

## 🏗️ 1. Two-Hemisphere Architecture
The Factory operates under the principle of **Total Separation between Logic and State**:

1.  **Control Hemisphere (`dasafo_FACTORY/`):**
    *   **Immutable:** Contains identities, missions, authorized tools, and communication protocols. It is the "Factory Software."
    *   **Global Knowledge:** Lessons recorded in `00_GLOBAL_KNOWLEDGE` or `FEEDBACK-LOG.md` apply to ALL future projects.
2.  **Execution Hemisphere (`PROJECTS/$TARGET_PROJECT/`):**
    *   **Mutable:** The working space for the current project. Contains code, logs, tasks, and local databases.
    *   **Isolated:** An agent working on "Project A" has no visibility of "Project B" unless explicitly injected.

---

## 👥 2. The Agent Council (Roles & Specialties)

### 💎 Meta-Agents (Orchestration & Memory)
*   **ORCHESTRATOR:** The managing brain. Breaks down complex goals into **Directed Acyclic Graphs (DAG)** of tasks. Implements the **TEA Cycle (Task-Execute-Architect)**: no phase closes without internal architecture validation. Manages **Deadlocks** by purging orphan locks.
*   **MEMORY_OPTIMIZER:** Prevents token collapse. Summarizes verbose logs into immutable facts injected into `SEMANTIC_INDEX.md`.

### 🔭 Strategy & Discovery Phase
*   **PRODUCT_OWNER:** Defines business success. Maintains `PROJECT_STATE.json` and the user BACKLOG.
*   **RESEARCH_AGENT:** Scientific explorer. Investigates external APIs, library compatibility, and technical docs before coding.

### 🛡️ Security & Quality Phase
*   **ARCHITECT:** Designs data contracts (DTOs) and SQL schemas. The "gatekeeper" of code: nothing is programmed without their prior design.
*   **SECURITY_AUDITOR:** Paranoid guardian. Scans for prompt injections, secret leaks, and library vulnerabilities. Implements the **Cognitive Guardrail** and semantic validation.
*   **QA_TESTER:** Solidness judge. Executes Docker builds, validates SI units, and ensures UI responsiveness/atomic design.

### ⚙️ Construction & DevOps Phase
*   **BACKEND_DEV / FRONTEND_DEV / DB_MASTER:** Code artisans. Write modular, commented, and typed software inside the `WORKSPACE/` folder.
*   **DEVOPS_SRE:** Infrastructure architect. Creates `docker-compose.yml`, manages volumes, and ensures one-click deployment.

---

## 🔄 3. Universal Pipeline (Life Cycle M0-M5)

*   **M0 - Bootstrap:** `init_project.sh` creates the physical skeleton.
*   **M1 - Discovery:** Product Owner and Research define the "What" and technical "How."
*   **M2 - Architecture:** Architect creates schemas and API contracts.
*   **M3 - Isolated Execution:** Developers consume tasks from `01_PENDING` using the **.lock protocol** and move them to `03_COMPLETED`.
*   **M4 - Quality Gate:** QA and Security Auditor review code and perform **Semantic JSON validation**. If fail -> `05_REJECTED`. If pass -> `04_ARCHIVE`.
*   **M5 - Go-Live:** DevOps deploys the environment.

---

## 📝 4. Context & Communication Protocol

*   **Context Injection:** Agents receive the `$TARGET_PROJECT` path as an environment variable.
*   **Atomic State Transitions:** Task movements must be OS-level atomic operations (`mv`).
*   **Idempotency:** Agents check `EXECUTION_LOG.md` before processing to prevent duplicate execution.

---

## 🛡️ 5. Technical Rigor & Golden Rules

1.  **SI Units Only:** Use Kilograms, Meters, Seconds, and Kelvins.
2.  **Atomic Solidity:** UI components must not contain business logic. Backend services must not know about HTML.
3.  **Chesterton’s Fence:** Agents must declare the understood purpose of existing code before refactoring it.
4.  **Feedback Loop & Versioning (`FEEDBACK-LOG.md`):** 
    *   **Versioning:** Every new policy must include a version header (e.g., `## Version: v1.1`).
    *   **Human-In-The-Loop:** Agents cannot write directly to the global `FEEDBACK-LOG.md`. They must prompt the user via OAM: `"Proposed entry for Core. Approve [Y/N]?"`.
5.  **Retry Limits:** If a task `retry_count > 3`, it must be locked in `05_REJECTED` for human rescue.

---

## 📂 6. Project Master Structure (`$TARGET_PROJECT`)
```bash
├── PROJECT_STATE.json     # Goals, status, and project KPIs.
├── LOCAL_KNOWLEDGE/       # Research, architecture blueprints, and indices.
├── TASKS/                 # Physical Kanban (01_PENDING to 05_REJECTED).
├── LOGS/                  # Agent memory and execution logs.
└── WORKSPACE/             # Source code (Frontend, Backend, Shared).
```

---

*The Factory is a coordinated organism designed so that even if the primary AI fails, the structures and protocols force the next iteration to be better.*
