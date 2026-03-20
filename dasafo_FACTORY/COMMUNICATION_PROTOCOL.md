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

1. **PENDING:** New tasks created by managers.
2. **IN_PROGRESS:** Tasks moved by workers when they begin execution.
3. **COMPLETED:** Tasks moved by workers for QA review.
4. **ARCHIVE:** Final destination after QA and Architect approval.
5. **REJECTED:** Tasks returned by QA or SECURITY with feedback for the original worker.

## 4. Code Output and Context Injection (Workspace)

- **Context Injection:** Agents operate on external projects via the `$TARGET_PROJECT` environment variable or injected parameter.
- All production code MUST be written exclusively inside the `$TARGET_PROJECT/WORKSPACE/` directory, divided into:
  - `$TARGET_PROJECT/WORKSPACE/backend/`: For API and server-side logic (Python/FastAPI).
  - `$TARGET_PROJECT/WORKSPACE/frontend/`: For user interface (Next.js/React/Vite).
  - `$TARGET_PROJECT/WORKSPACE/shared/`: For common schemas, types, and cross-departmental DTOs.
- **Rule of Immutability:** Development agents have "Read-Only" access to the `dasafo_FACTORY`. They cannot modify their own identities or global logs. All state changes occur strictly in `$TARGET_PROJECT`.

## 5. Universal Pipeline & The QA Gate

To ensure systematic integrity, all workflows must follow an immutable sequence:

1. **Discovery (M1):** `PRODUCT_OWNER` defines state, `RESEARCH` gathers data.
2. **Architecture (M2):** `ARCHITECT` creates system design. No code is written until this is approved.
3. **Isolated Execution (M3):** Developers write code exclusively inside their `06_WORKSPACE` silos.
4. **The QA Gate (Crucial):**
   - A task in `03_COMPLETED` is NOT finished.
   - Only the `QA_TESTER` and `SECURITY_AUDITOR` have the clearance to move a task from `COMPLETED` to `04_ARCHIVE`.
   - If UI/UX, logic, or SI constraints fail, QA **must** reject the task and return it to `05_REJECTED` along with a QA feedback log.
   - No task N can begin if its prerequisite N-1 is not in `04_ARCHIVE`.

## 6. Error & Conflict Resolution

- If an agent detects a security flaw, it must stop execution and ping the SECURITY_AUDITOR.
- If two agents provide conflicting technical solutions, the ARCHITECT has the final decision.
- All errors must be logged in `LOGS/agents/[agent_name].log` before notifying the manager.

## 7. Technical Rigor

- Use SI units in all technical specifications.
- Avoid "fluff" or conversational fillers in task descriptions. Be technical and precise.
