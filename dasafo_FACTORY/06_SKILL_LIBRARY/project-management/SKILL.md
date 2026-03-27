---
version: 3.2.0-S
agent: PRODUCT_OWNER
---

# 📊 Skill | Project Management

## Objective
Execute strategic backlog grooming, prioritization, and task decomposition to translate business vision into high-solidity industrial execution.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `current_goal` (string): High-level mission objective.
- `priority_strategy` (string, optional): "MoSCoW" | "Lean" | "Standard". Default "Standard".

### Output Schema (SkillOutput.result)
- `task_count`: (integer) Number of `TSK_` JSON files created.
- `registry_updated`: (boolean) True if `TASKS/registry.json` was refreshed.
- `solidity_index`: (float) confidence metric (0.0-1.0).

### ⚖️ Mandato SI (Sistema Internacional)
Los tiempos estimados de entrega y la duración de los sprints deben reportarse en unidades del SI (segundos, horas).

## Strategic Process
1.  **Backlog Grooming:** Prioritize tasks based on business impact and systemic urgency.
2.  **Decomposition:** Break goals into manageable, machine-readable `TSK_` JSON files.
3.  **Governance:** Verify every task has a clear DoD (Definition of Done) and Objective.
4.  **Lifecycle:** Orchestrate the flow from "01_PENDING" to "04_ARCHIVE" through the Solidity Gate.

---
*Skill v3.2.0-S | Status: Standardized.*
