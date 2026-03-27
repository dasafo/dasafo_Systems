---
version: 3.2.0-S
agent: FACTORY_EVOLVER
---

# 🛡️ Skill | AutoShield Pattern Analysis

## Objective
Periodically scan the `FEEDBACK-LOG.md` to identify systemic patterns, recurring agent weaknesses, and opportunities for factory-wide golden rule distillation.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `log_path` (string, optional): Path to the `FEEDBACK-LOG.md`.
- `time_window_days` (integer, optional): Number of days to look back. Default 30.

### Output Schema (SkillOutput.result)
- `health_score`: (integer) Factory intelligence score (0-100).
- `hotspots`: (list) Areas with recurring errors.
- `proposals`: (list) Proposed skill upgrades or new rules.
- `report`: (string) Full Antifragility Report.

### ⚖️ Mandato SI (Sistema Internacional)
Cualquier métrica temporal (ventanas de tiempo, frecuencia de errores por hora) o de rendimiento del sistema debe reportarse bajo las unidades del SI.

## 🧠 Protocol
1.  **Scan:** Parse the `FEEDBACK-LOG.md`.
2.  **Cluster:** Group entries by category, agent, and severity.
3.  **Identify:** Find hotspots (>3 entries in 30 days) and repeat offenders.
4.  **Evolve:** Propose new Golden Rules or Skill upgrades.
5.  **Report:** Generate the "Antifragility Report" for human review.

---
*Skill v3.2.0-S | Status: Standardized.*
