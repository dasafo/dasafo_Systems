---
version: 3.4.0-S
agent: ALL AGENTS
source: https://skills.sh/supercent-io/skills-template/vibe-kanban
---

# 🛂 Skill | Kanban Solidity Gate & Vibe Dashboard (v3.4.0-S)

## Objective

Programmatically enforce the "Zero-Pending Rule" for industrial project transitions and provide a visual, parallelized task management dashboard via **Vibe Kanban**. This skill acts as the **Aduana Universal** (Customs), preventing phase advancement if tasks remain unaddressed physically, while allowing parallel agent execution through isolated worktrees.

## 🛠️ Interface (v3.4.0-S)

### Input Schema (SkillInput.params)

- `action` (enum): `audit` (default) | `start_dashboard` | `create_workspace` | `sync`.
- `target_project` (string, mandatory): Absolute path to the project workspace.
- `proposed_phase` (string, optional): The phase to validate (M1-M5).
- `port` (integer, optional): Dashboard port (default 3001).

### Output Schema (SkillOutput.result)

- `gate_passed`: (boolean) True if all requirements are cleared physically.
- `solidity_score`: (float) Confidence metric (0.0-1.0).
- `dashboard_url`: (string, optional) URL for the Vibe Kanban board.
- `pending_tasks`: (list) Task IDs blocking progress.
- `industrial_status`: (string) "SOLIDIFIED - GATE PASSED" | "LOCKED - PENDING TASKS DETECTED".

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica de rendimiento, tiempo de validación o latencia del dashboard debe expresarse estrictamente en **segundos** (s).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Physical SSoT:** All validations must parse `TASKS/registry.json` and the physical `.json` artifacts of each task. Registry-only status is NOT TRUSTED.
- **Isolation Guarantee:** Vibe Kanban workspaces must use Git Worktrees to prevent concurrent file conflicts between agents.
- **Fail-Fast:** The gate MUST fail if even a single task mapping is missing or inconsistent with `PROJECT_STATE.json`.
- **Zero-Ghost Tasks:** Any task displayed in the dashboard must correspond to a physical artifact on disk.

## 🧠 Core Strategy (v3.4.0-S)

1. **Physical Scan:** Iterate through the `TASKS/` directory. Each task ID in `registry.json` must have a corresponding file in `COMPLETED/` to pass.
2. **Phase Lock:** Block any `phase_transition` request if the solidity score < 1.0.
3. **Visual Sync:** Update the Vibe Kanban board state based on the physical disk reality.
4. **Parallel Execution:** Orchestrate multiple agents using isolated worktrees to decompose epics into independent, auditable tasks.

---
**ORIGIN:** [vibe-kanban by supercent-io](https://skills.sh/supercent-io/skills-template/vibe-kanban)
*Skill v3.4.0-S | Status: Standardized & Industrialized (The Heart of the Factory).*
