# 📡 dasafo_FACTORY | Communication Protocol
>
> **Standard:** Sensory Bridge v3.1.5 "Solidity Guard"
> **Focus:** Shared Resources & Multi-Agent Industrial Orchestration
## 📚 Role-Based Interaction

### 1. The Sensory Bridge (MCP)

- Agents interact with the physical and digital world through **Senses** (Tools).
- Every tool call is an **Observation**. Every output is a **Perception**.

### 2. AutoShield (Collective Intelligence)

- No agent operates in isolation. All agents MUST query the `FEEDBACK-LOG.md` before execution.
- Discovered patterns must be written back to the factory's immune system.

### 3. The PRP Validation Gate & Industrial Guardrails

- **PO Approval:**
    - **Output:** Draft `PRP_CONTRACT.json`.
    - **Validation:** User approval of the vision and scope.
-   **Rule 3: Zero-Pending Gate**: Phase promotion is strictly prohibited if the physical Kanban (`task.md`) contains any open tasks (`[ ]` or `[/]`).
-   **Rule 4: Segregation of Duties (Solidity v3.1.5)**:
    - [x] Rule 3: Technical logs must be 100% in English.
    - [x] Rule 4: Segregation of Duties. Agents CANNOT mark their own tasks as COMPLETED. Only Verification agents (Role: ARCHITECT/QA) or HUMANS can authorize task finalization.
- **Industrial Solidity v3.1.5 (Mandatory):**
    - **Strict Coupling:** Code generation is strictly coupled to `TASKS/02_DONE`. No agent shall write into `WORKSPACE` without a verified and completed JSON task.
    - **Log-First Execution:** ALL mission-critical actions must be preceded by a telemetry log entry in `$TARGET_PROJECT/LOGS/`.
    - **Human Sync-Points:** Every project milestone REQUIRES explicit user sign-off via Antigravity before proceeding.
- **Infrastructure Quotas:** Every project must declare resource limits in `.env`.
- **Compliance:** All communications must follow the SI unit mandate and SoC rules.


### 4. Telemetry Log (Industrial Chronicle v3.1.1)

- ALL mission-critical actions MUST be recorded in `$TARGET_PROJECT/LOGS/EXECUTION_LOG.md`.
- This file is the **Single Source of Truth**. Strategic reports are merged into this chronicle.
- **Mandatory Structure**:
    - **Header**: Current Factory Health (Ports/Docker) and Agent Role Matrix.
    - **Kanban Snapshot**: High-level progress of the 5 Phase Pipeline.
    - **Audit Trail**: Chronological entries with `Task | Agent | Context | Timestamp`.

---
*Communication Protocol v3.1.5 | Status: Solidified.*
