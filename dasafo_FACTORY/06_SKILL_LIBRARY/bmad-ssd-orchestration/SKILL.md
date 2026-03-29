---
version: 3.3.0-S
agent: ORCHESTRATOR
source: https://skills.sh/supercent-io/skills-template/bmad-orchestrator
---

# 📐 Skill | BMAD SSD Orchestration

## Objective
Implement Structured System Design (SSD) to manage complex multi-agent workflows with automated phase gates and physical state management.

## 🛠️ Interface (v3.3.0-S)

### Input Schema (SkillInput.params)
- `action` (string, optional): "status" | "validate" | "advance". Default "status".
- `project_path` (string, optional): Path to the target project.

### Output Schema (SkillOutput.result)
- `action`: (string) The executed action.
- `current_phase`: (string) The active project phase.
- `gate_verdict`: (string) "PASS" | "FAIL".
- `pending_tasks`: (integer) Number of tasks blocking the next phase.
- `message`: (string) Detailed result message.
- `project_state`: (string) Path to the updated state file.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier medida de progreso temporal o de carga de trabajo (puntos de historia, horas estimadas) debe estar alineada con métricas del Sistema Internacional.

## 🛡️ Industrial Constraints (Zero-Trust)

- **State Persistence:** Operates strictly on the physical `PROJECT_STATE.json`. The orchestrator is forbidden from "simulating" transitions without updating the on-disk state.
- **Artifact Verification:** Phase advance requires physical check of the `TASKS/01_PENDING` and `02_IN_PROGRESS` directories. 

## Phase Gate Protocol

Before advancing to the next project phase (e.g., Analysis -> Planning):

1. **Validate:** Scan all physical tasks in the current phase.
2. **Verify Verdicts:** Ensure all critical tasks are moved to `03_COMPLETED`.
3. **Check Coverage:** Ensure the phase is clean of pending artifacts.
4. **Advance:** Increment `current_phase` in `PROJECT_STATE.json` physically only if `validate` returns `PASS`.

---
**ORIGIN:** [bmad-orchestrator by supercent-io/skills-template](https://skills.sh/supercent-io/skills-template/bmad-orchestrator)
*Skill v3.3.0-S | Status: Standardized & Industrialized.*
