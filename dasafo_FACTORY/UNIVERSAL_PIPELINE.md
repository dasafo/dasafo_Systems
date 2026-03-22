# ⚙️ UNIVERSAL PIPELINE (The Factory OS)

> **Mandatory Directive** for all Agents instantiated in `dasafo_FACTORY`.

The lifecycle of any mission assigned to this factory must be resolved in **5 strict sequential phases**. Progress state is controlled by reading the quality gate (`04_ARCHIVE`) within the volume injected at `$TARGET_PROJECT`.

## Phase 0: Initialization (Bootstrap)

1. **PRODUCT_OWNER** or **DEVOPS_SRE** provisions the physical `$TARGET_PROJECT` root directory and generates its exact master skeleton (as strictly defined in `COMMUNICATION_PROTOCOL.md`).
2. No agent can operate on a project if its core filesystem (`TASKS/`, `WORKSPACE/`, `LOGS/`, `LOCAL_KNOWLEDGE/`) is not structurally sound.

## Phase 1: Discovery (M1)

1. **PRODUCT_OWNER** maps the client's objectives in `$TARGET_PROJECT/PROJECT_STATE.json`.
2. **RESEARCH_AGENT** investigates technical or scientific feasibility and deposits findings in `$TARGET_PROJECT/LOCAL_KNOWLEDGE/`.

## Phase 2: Architecture (M2)

1. **ARCHITECT** designs the solution (e.g., DTOs, Schemas, endpoints) referencing the `LOCAL_KNOWLEDGE`.
2. *No code is written until the Architect deposits the completed design tasks.*

## Phase 3: Isolated Execution (M3)

1. Production agents (`BACKEND_DEV`, `FRONTEND_DEV`, `DATA_SCIENTIST`, `DB_MASTER`) consume tasks from `$TARGET_PROJECT/TASKS/01_PENDING`.
2. **Pre-requisite:** Before executing ANY task or writing code, every agent MUST check `dasafo_FACTORY/FEEDBACK-LOG.md` to avoid repeating known mistakes.
3. Code is deposited EXCLUSIVELY in subdirectories within `$TARGET_PROJECT/WORKSPACE/`.

## Phase 4: Quality Gate (QA Gate)

1. A developer CANNOT mark a task as finished. They can only leave it in `03_COMPLETED`.
2. The **QA_TESTER** and **SECURITY_AUDITOR** audit the task (e.g., executing a build, checking SI units, reviewing permissions).
3. If it fails, it is returned to `05_REJECTED`. If it passes, it is promoted to `04_ARCHIVE`.
4. **Feedback Loop Action:** If a task is rejected due to a structural, logical, or recurring error, QA/SECURITY MUST register this error and its correction in `dasafo_FACTORY/FEEDBACK-LOG.md` so the rest of the factory learns from it.

## Phase 5: Go-Live

1. **DEVOPS_SRE** creates the deployment orchestration (e.g., `docker-compose.yml`) AND **must automatically spin up the local environment** so the User can immediately see and interact with the live application (Frontend/Backend) without running manual commands.
2. **MARKETING_GROWTH** extracts value and designs the Go-to-Market (GTM) strategy.

---

*Any attempt to bypass the Architecture phase (M2) or the QA Gate (Phase 4) will result in a violation of the Core protocol of the Factory.*
