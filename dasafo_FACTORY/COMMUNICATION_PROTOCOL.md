# dasafo_System | Communication Protocol
>
> **Scope:** Inter-agent interaction rules and data exchange formats.

## 1. Chain of Command

- **Direct Reporting:** Workers (Production/Compliance) report ONLY to the ARCHITECT.
- **Leadership:** The ARCHITECT reports to the PRODUCT_OWNER.
- **Final Authority:** The PRODUCT_OWNER reports directly to dasafo (The Owner).
- **Prohibited:** Specialized workers cannot assign tasks to each other; all cross-department requests must go through the ARCHITECT.

## 2. Task Exchange Format

- All task-related communication must be performed via `.json` files in the `/TASKS` directory.
- **Internal Encoding:** UTF-8.
- **Required Fields:** `task_id`, `sender`, `recipient`, `action_required`, `priority`, `context_files`.

## 3. Directory Lifecycle

1. **`01_PENDING`:** New tasks created by managers.
2. **`02_IN_PROGRESS`:** Tasks moved by workers when they begin execution.
3. **`03_COMPLETED`:** Tasks moved by workers for QA review.
4. **`04_ARCHIVE`:** Final destination after QA and Architect approval.
5. **`05_REJECTED`:** Tasks returned by QA or SECURITY with feedback for the original worker.

## 4. Code Output, The Workspace, and Context Injection

- **Context Injection:** Agents operate on external projects via the `$TARGET_PROJECT` environment variable or injected parameter.
- The `$TARGET_PROJECT` MUST respect the following master skeleton architecture:
  - `$TARGET_PROJECT/PROJECT_STATE.json`: Meta-status and core user requirements.
  - `$TARGET_PROJECT/LOCAL_KNOWLEDGE/`: Research and architectural blueprints.
  - `$TARGET_PROJECT/TASKS/`: The Kanban directories (`01_PENDING` through `05_REJECTED`).
  - `$TARGET_PROJECT/LOGS/`: Agent-specific logs (`agents/`) and critical errors.
  - `$TARGET_PROJECT/WORKSPACE/`: For production code, strictly subdivided into `backend/`, `frontend/`, `shared/`.
- **Rule of Immutability:** Development agents have "Read-Only" access to the `dasafo_FACTORY`. They cannot modify their own identities or factory laws. All state changes occur strictly in `$TARGET_PROJECT`.

## 5. Universal Pipeline & The QA Gate

To ensure systematic integrity, all workflows must follow an immutable sequence:

1. **Discovery (M1):** `PRODUCT_OWNER` defines state, `RESEARCH` gathers data.
2. **Architecture (M2):** `ARCHITECT` creates system design. No code is written until this is approved.
3. **Isolated Execution (M3):** Developers write code exclusively inside their `$TARGET_PROJECT/WORKSPACE` silos.
4. **The QA Gate (Crucial):**
   - A task in `03_COMPLETED` is NOT finished.
   - Only the `QA_TESTER` and `SECURITY_AUDITOR` have the clearance to move a task from `COMPLETED` to `04_ARCHIVE`.
   - If UI/UX, logic, or SI constraints fail, QA **must** reject the task and return it to `05_REJECTED` along with a QA feedback log.
   - **QA Integration Rule:** The QA must verify that any new code includes its proper Entry Point (e.g., `main.py`, `index.tsx`) and is fully integrated into the existing workspace before promoting to `04_ARCHIVE`.
   - **Docker Proof-of-Build:** For projects with containerization, the QA MUST execute a dry-run or full build of the `Dockerfile` in the workspace to catch missing dependencies (e.g., `package-lock.json`) before validation.
   - No task N can begin if its prerequisite N-1 is not in `04_ARCHIVE`.

## 6. Multi-Tier Memory Architecture

To prevent Token Exhaustion and maintain systemic coherence across long workflows, agents MUST respect the following memory tiers:
- **Transactional Memory (Short-Term):** Maintained only in the LLM's active context window or temporary in-memory stores (e.g., Redis). Flushed after task completion.
- **Episodic Memory (Persistent):** Raw conversational logs and step-by-step reasoning (Chain of Thought) saved continuously in `$TARGET_PROJECT/LOGS/`.
- **Semantic Memory (Retrospective):** Compacted vector embeddings (managed by the `MEMORY_OPTIMIZER`) that allow agents to search past project blueprints logically without reading monolithic JSONs.

## 7. Event-Driven Execution (Asynchronous Delegation)

- **No Synchronous Coupling:** Agents must NOT wait idly for another agent to finish.
- **Publish/Subscribe Logic:** When a task involves multiple disciplines (e.g., UX design and DB schema formulation), the `ORCHESTRATOR` creates parallel tickets in `01_PENDING`.
- **Dependency Resolution:** If `FRONTEND_DEV` needs the `DTO` from `ARCHITECT`, it must pause its execution loop and check the `04_ARCHIVE` for the Architect's ticket. If missing, it yields execution until the dependency is resolved.

## 8. Error, Conflict Resolution & Feedback Loop

- If an agent detects a security flaw, it must stop execution and ping the SECURITY_AUDITOR.
- If two agents provide conflicting technical solutions, the ARCHITECT has the final decision.
- All errors must be logged in `$TARGET_PROJECT/LOGS/agents/[agent_name].log` before notifying the manager.
- **The Feedback Log (`FEEDBACK-LOG.md`):** If an agent makes a mistake that is caught by QA, Security, or Architecture, the structural correction MUST be logged here. ALL agents must read `FEEDBACK-LOG.md` before taking action on tasks.

## 7. Technical Rigor

- Use SI units in all technical specifications.
- Avoid "fluff" or conversational fillers in task descriptions. Be technical and precise.
