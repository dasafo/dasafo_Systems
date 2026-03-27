---
version: 3.2.0-S
agent: ORCHESTRATOR
---

# 🏛️ Skill | Structured System Design (SSD)

## Objective
Execute advanced industrial orchestration using the TEA (Task-Execute-Architect) meta-framework within every phase of the Universal Pipeline.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `current_phase` (string): M1 | M2 | M3 | M4 | M5.
- `status_update` (object, optional): Data to persist in the SSD state.

### Output Schema (SkillOutput.result)
- `tea_loop_status`: (string) "T" | "E" | "A".
- `phase_gate_verdict`: (string) "PASS" | "FAIL" | "REVISE".
- `next_atomic_tasks`: (list) Decomposition for the current phase.

### ⚖️ Mandato SI (Sistema Internacional)
Los tiempos de ciclo TEA (T1, T2) y el presupuesto de tokens asignado a cada subtarea deben reportarse en el SI.

## The TEA Cycle (Internal Loop)
1.  **T → Task (Decomposition):** Break phase into atomic, assignable tasks.
2.  **E → Execute (Parallelism):** Launch multiple agentic tasks where dependencies allow.
3.  **A → Architect (Validation):** Audits outputs for coherence and cross-phase solidity.
4.  **Gate Constraint:** No phase (N) advances to (N+1) without a `PASS` architecture verdict.

---
*Skill v3.2.0-S | Status: Standardized.*
