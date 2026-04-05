---
version: v5.0-MCP (Native)
agent_authorization: [ORCHESTRATOR]
production_category: PLAN
source: internal/skill-creator
protocol: Registry-Notary / DAST
---

# 🗂️ Skill | registry-manager

## Objective

Act as the industrial notary for the project's Kanban state. Mutates `registry.json` and synchronizes the physical state of task artifacts across `01_PENDING`, `02_IN_PROGRESS`, and `03_COMPLETED` folders.

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use typed arguments. `params_json` is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your Agent ID (must be 'ORCHESTRATOR').
- `target_project` (string): Absolute path to the project root.
- `action` (enum): `update_registry` (default) | `add_task`.
- `key_value_pairs` (object): (Optional) Key-value data for the registry update (e.g., `{"task_id": "M3-001", "new_status": "COMPLETED"}`).
- `overwrite` (boolean): (Optional) Force overwrite of existing registry entries.
- `isolate` (boolean): Execution in Clean Session.

## 🛡️ Industrial Constraints

- **Atomic Move:** The JSON file MUST be physically moved between folders to match the status change.
- **SSoT Integrity:** `registry.json` must always perfectly mirror the physical directories. Discrepancies cause Gate Lock.
- **SI Standards:** Timing metrics reported in **Seconds (s)**.

---
*Standard v5.0-MCP | Dasafo Factory Core DAST.*
