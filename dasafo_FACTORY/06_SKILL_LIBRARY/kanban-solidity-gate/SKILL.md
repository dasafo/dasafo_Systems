---
version: 3.2.0-S
agent: ORCHESTRATOR
---

# 🛂 Skill | Kanban Solidity Gate

## Objective

Programmatically enforce the "Zero-Pending Rule" for industrial project transitions. This skill is the **Aduana Universal** (Universal Customs), preventing any phase advancement if tasks remain unaddressed in the registry.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `task_id` (string, optional): Specific task ID to validate. Default "T-000".
- `proposed_phase` (string, optional): The phase the project intends to enter (M1-M5).

### Output Schema (SkillOutput.result)

- `gate_passed`: (boolean) True if all requirements are cleared physically.
- `solidity_score`: (float) Confidence metric (0.0-1.0) based on task completion ratio.
- `reason`: (string) Detailed explanation for gate status.
- `pending_tasks`: (list) List of IDs that blocked the gate.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica de rendimiento o tiempo de validación debe expresarse estrictamente en segundos (s).

## 🧠 Logic

1. **Registry Scan:** Analyze `TASKS/registry.json` (SSoT) for any task not marked as "COMPLETED" or "APPROVED" in the current active phase.
2. **State Sync:** Compare findings against `PROJECT_STATE.json` to ensure no "Phase Jumps" occur without physical authorization.
3. **Zero-Pending Rule:** The gate fails if even a single task marker is pending.

---
*Skill v3.2.0-S | Status: Solidified (The Heart of the Factory).*
