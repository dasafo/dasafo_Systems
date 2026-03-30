---
version: 3.4.0-S
agent: ORCHESTRATOR / PROJECT_MANAGER
source: internal/skill-creator
---

# 🗂️ Skill | Registry Manager (v3.4.0-S)

## Objective

Act as the industrial notary for the project's Kanban state. This skill mutates `TASKS/registry.json` and synchronizes the physical state of task artifacts across `01_PENDING`, `02_IN_PROGRESS`, and `03_COMPLETED` directories to satisfy the `kanban-solidity-gate`.

## 🛠️ Interface (v3.4.0-S)

### Input Schema (SkillInput.params)

- `action` (enum): `update_status`, `add_task`.
- `task_id` (string, mandatory): The ID of the task (e.g., "M3-001").
- `new_status` (enum): `PENDING`, `IN_PROGRESS`, `COMPLETED`.
- `target_project` (string, mandatory): Absolute path to the project workspace.

### Output Schema (SkillOutput.result)

- `task_id`: (string) The affected task.
- `previous_status`: (string)
- `current_status`: (string)
- `artifact_path`: (string) Path to the newly moved physical task JSON.
- `industrial_status`: (string) "SOLIDIFIED - REGISTRY SYNCED"

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica de latencia de I/O de disco debe registrarse en **segundos** (s).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Physical Artifact Sync:** If a task is marked `COMPLETED`, its JSON file MUST be physically moved/created in `TASKS/03_COMPLETED/`.
- **SSoT Integrity:** The `registry.json` must always perfectly mirror the physical directories.

## 🧠 Workflow (v3.4.0-S)

1. **Read SSoT:** Load `TASKS/registry.json`.
2. **Mutate State:** Update the status of the target `task_id`.
3. **Physical Sync:** Generate or move the task artifact to the correct subfolder based on `new_status`.
4. **Persist:** Save the updated `registry.json`.
