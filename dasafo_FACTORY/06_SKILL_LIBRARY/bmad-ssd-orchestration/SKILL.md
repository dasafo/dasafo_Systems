---
version: 3.2.0-S
agent: ORCHESTRATOR
---

# 📐 Skill | BMAD SSD Orchestration

## Objective
Implement Structured System Design (SSD) to manage complex multi-agent workflows with automated phase gates and state management.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `action` (string, optional): "validate" | "advance" | "status". Default "status".
- `project_path` (string, optional): Path to the target project.

### Output Schema (SkillOutput.result)
- `current_phase`: (string) The active project phase.
- `gate_verdict`: (string) "PASS" | "FAIL".
- `pending_tasks`: (integer) Number of tasks blocking the next phase.

### ⚖️ Mandato SI (Sistema Internacional)
Cualquier medida de progreso temporal o de carga de trabajo (puntos de historia, horas estimadas) debe estar alineada con métricas del Sistema Internacional.

## Phase Gate Protocol
Before advancing to the next project phase (e.g., Analysis -> Planning):
1.  **Validate:** Scan all tasks in the current phase.
2.  **Verify Verdicts:** Ensure all critical tasks have `qa_passed: true`.
3.  **Check Coverage:** Ensure all requirements in `ARCHITECTURE.md` are mapped to tasks.
4.  **Advance:** Increment `current_phase` in `PROJECT_STATE.json` only if all checks PASS.

---
*Skill v3.2.0-S | Status: Standardized.*
