# Skill:# 🔍 Task Dependency Diagnostic
>
> **Standard:** v3.1.5 "Solidity Guard"
https://skills.sh/softaworks/agent-toolkit/dependency-updater (Adapted)
> **Agent:** ORCHESTRATOR

## Objective
Perform structural diagnosis of task dependencies to prevent "blocked" states in the factory.

## Diagnostic Workflow

### 1. Scan Blocked Tasks
Identify tasks in `01_PENDING` that cannot move to `02_IN_PROGRESS` because they depend on unarchived deliverables.
- **Example:** `BACKEND_DEV` cannot start without `ARCHITECT_DTO` schema.

### 2. Dependency Audit
For every blocked task, find the "Parent" task ID.
- **Status:** Check if the parent is in `02_IN_PROGRESS` (Active) or `05_REJECTED` (Needs feedback).
- **Security Check:** Verify the `EXECUTION_LOG.lock` status. If a parent task is locked but idle for >30m, it is a **Stale Lock Diagnosis**.

### 3. Resolution Actions
- **If Stale Lock:** Use the `stale-lock-purger` skill to clear the blockage.
- **If Parent Rejected:** Reprioritize the parent task and notify the corresponding agent with a "High Urgency" flag.
- **If Circular Dependency:** Halt execution and request human intervention via `FEEDBACK-LOG.md`.
