---
version: 3.2.0-S
agent: ORCHESTRATOR
---

# 🔍 Skill | Task Dependency Diagnostic

## Objective

Perform structural diagnosis of task dependencies within the mission plan to prevent "blocked" states, circular dependencies, and industrial idle time.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `mission_plan_path` (string, optional): Absolute path to the plan to audit.
- `diag_depth` (string, optional): "light" | "deep". Default "light".

### Output Schema (SkillOutput.result)

- `dependency_status`: (string) "HEALTHY" | "BLOCKED" | "CIRCULAR".
- `blocked_task_ids`: (list) Tasks unable to move to `02_IN_PROGRESS`.
- `critical_path`: (list) Sequenced list of bottleneck tasks.

### ⚖️ Mandato SI (Sistema Internacional)

Los tiempos de inactividad detectados (idle time) y la duración estimada del camino crítico deben reportarse exclusivamente en segundos (s) o días (d).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Physical Plan:** Diagnostics MUST be performed on the physical `MISSION_PLAN.json` or equivalent.
- **Lock Purge Trace:** Every "Stale Lock" removal MUST be physically logged with the original task ID and duration (SI).

## Diagnostic Workflow

1. **Blocked Scan:** Identify tasks in `01_PENDING` with unarchived deliverable dependencies.
2. **Audit:** Trace "Parent" task status. Detect "Stale Locks" (Idleness > 1800s).
3. **Resolution:**
   - **Stale Lock:** Self-purge via `stale-lock-purger`.
   - **Circular:** Immediate halt and human notification via `FEEDBACK-LOG.md`.
   - **Rejection Trace:** Reprioritize parents of rejected tasks with high urgency flags.

---
*Skill v3.2.0-S | Status: Standardized.*
