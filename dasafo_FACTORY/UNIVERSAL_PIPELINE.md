# ⚙️ UNIVERSAL PIPELINE (The Factory OS)

> **Mandatory Directive** for all Agents instantiated in `dasafo_FACTORY`.

The lifecycle of any mission assigned to this factory must be resolved in **5 strict sequential phases**. Progress state is controlled by reading the quality gate (`04_ARCHIVE`) within the volume injected at `$TARGET_PROJECT`.

## Phase 0: Initialization (Bootstrap)

1. **PRODUCT_OWNER** or **DEVOPS_SRE** provisions the physical `$TARGET_PROJECT` root directory and generates its exact master skeleton (as strictly defined in `COMMUNICATION_PROTOCOL.md`).

2. No agent can operate on a project if its core filesystem (`TASKS/`, `WORKSPACE/`, `LOGS/`, `LOCAL_KNOWLEDGE/`) is not structurally sound.

### ♾️ The Orchestrator's TEA Loop (Continuous Execution)

> Unlike standard agents, the **ORCHESTRATOR** operates continuously *above* all phases. For every phase below (M1 to M5), the Orchestrator MUST execute a TEA cycle (Task -> Execute -> Architect). No phase can advance to the next until the Orchestrator's internal `Architect` validation yields a `PASS` and records it in `$TARGET_PROJECT/LOCAL_KNOWLEDGE/ssd-state.json`.

## Phase 1: Discovery (M1)


1. **PRODUCT_OWNER** maps the client's objectives in `$TARGET_PROJECT/PROJECT_STATE.json`.
2. **RESEARCH_AGENT** investigates technical or scientific feasibility and deposits findings in `$TARGET_PROJECT/LOCAL_KNOWLEDGE/`.

## Phase 1.5: PRP Contract Gate (M1.5)

> **The Contrato.** No agent may advance past Discovery without a signed PRP contract.

1. **PRODUCT_OWNER** executes the `prp-validation-gate` skill to interview the user.
2. The user declares the **What**, **Why**, **Who**, **Success Criteria**, **Constraints**, and **Non-Goals**.
3. A `PRP_CONTRACT.json` is produced in `$TARGET_PROJECT/LOCAL_KNOWLEDGE/` with `prp_status: "draft"`.
4. The user reviews and confirms the contract → status transitions to `"validated"`.
5. **GATE RULE:** No agent may advance to M2 until `PRP_CONTRACT.json` has `prp_status: "validated"`. The ORCHESTRATOR must verify this gate before publishing any M2 tasks.
6. Once validated, the PRP Contract is **IMMUTABLE**. Scope changes require a new version (`version` field increment and a fresh validation cycle).

## Phase 2: Architecture (M2)

1. **ARCHITECT** designs the solution (e.g., DTOs, Schemas, endpoints) referencing the `LOCAL_KNOWLEDGE` **and the validated PRP Contract's `success_criteria`**.
2. *No code is written until the Architect deposits the completed design tasks.*
3. **PRP Alignment Check:** Every architectural decision MUST trace back to at least one `success_criteria` entry in the PRP Contract. Untraced design elements are rejected.

## Phase 3: Isolated Execution (M3)

1. Production agents (`BACKEND_DEV`, `FRONTEND_DEV`, `DATA_SCIENTIST`, `DB_MASTER`) consume tasks from `$TARGET_PROJECT/TASKS/01_PENDING`.
2. **Lock Acquisition:** The agent MUST acquire the ticket by renaming it to `.lock` and registering its `owner_agent_id` and `timestamp`. Execution starts ONLY if the `task_id` check in `EXECUTION_LOG.md` passes (Idempotency).
3. **AutoShield Preflight:** Before executing ANY task or writing code, every agent MUST execute the `autoshield-preflight-check` skill (from `00_GLOBAL_KNOWLEDGE/SKILLS/`) to load relevant golden rules from `FEEDBACK-LOG.md`.
4. Code is deposited EXCLUSIVELY in subdirectories within `$TARGET_PROJECT/WORKSPACE/`.
5. **Heartbeat & Timeout Cleanup:** Agents SHOULD update a heartbeat timestamp. If a task is inside `02_IN_PROGRESS` or held as `.lock` longer than the global timeout without heartbeat updates, the Orchestrator will clean the orphan lock and abort the execution to unbrick the system.

## Phase 4: Quality Gate (QA Gate)

1. A developer CANNOT mark a task as finished. They can only leave it in `03_COMPLETED`.
2. The **QA_TESTER** and **SECURITY_AUDITOR** audit the task (e.g., executing a build, checking SI units, reviewing permissions, checking **semantic JSON validation**).
3. **MCP Visual Validation (Mandatory for UI projects):** QA_TESTER MUST execute the `browser-visual-validation` skill to visually confirm the application functions end-to-end via browser MCP. See `MCP_SENSES_PROTOCOL.md` for details.
4. **MCP Data Validation (Mandatory for DB projects):** DB_MASTER MUST execute the `supabase-live-validation` skill to confirm schema integrity and data constraints via Supabase MCP.
5. Si falla, el `retry_count` se incrementa y se devuelve a `05_REJECTED`. Si sobrepasa el límite (ej. > 3 retries), se bloquea la tarea requiriendo rescate humano.
6. Si pasa limpiamente, es promovida a `04_ARCHIVE`.
7. **Feedback Loop Action:** If a task is rejected, QA/SECURITY MUST execute the `autoshield-feedback-writer` skill to register the error and correction in `FEEDBACK-LOG.md` (via Human Approval Gate) so the rest of the factory learns from it.

## Phase 5: Go-Live

1. **DEVOPS_SRE** creates the deployment orchestration (e.g., `docker-compose.yml`) AND **must automatically spin up the local environment** so the User can immediately see and interact with the live application (Frontend/Backend) without running manual commands.
2. **MARKETING_GROWTH** extracts value and designs the Go-to-Market (GTM) strategy.

---

*Any attempt to bypass the Architecture phase (M2) or the QA Gate (Phase 4) will result in a violation of the Core protocol of the Factory.*
