---
version: 3.2.0-S
agent: FACTORY_EVOLVER
---

# 🧠 Skill | Autonomous Feedback Analyzer

## Objective
Proactively analyze logs, rejections, and feedback patterns to improve the agentic factory's systemic performance.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `log_path` (string, optional): Absolute path to `FEEDBACK-LOG.md`.
- `analyze_rejections` (boolean, optional): Default `true`.

### Output Schema (SkillOutput.result)
- `status`: (string) "PASS" | "EVOLUTION_REQUIRED"
- `patterns_discovered`: (integer) Total unique recurring failure patterns.
- `analysis`: (list) List of pattern objects:
  - `id`: (string) FB-ID.
  - `pattern`: (string) Description of the recurring failure.
  - `agents`: (list) Agents involved.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica de rendimiento analizada (tiempos medios entre fallos, tasas de error por segundo) debe expresarse según el SI.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Log Verification:** Requires physical access to `FEEDBACK-LOG.md`. Failure to find the artifact returns a `SkillOutput.success` with empty findings, never hallucinations.
- **Deterministic Clustering:** Pattern identification is based on physical string matching in logs.

## Protocol

1. **Log Ingestion:** Physically read `FEEDBACK-LOG.md` and standard error logs.
2. **Error Categorization:** Label errors as "Minor", "Structural", or "Critical".
3. **Causality Check:** Determine root cause (prompting, tools, architecture).
4. **Automated Fix:** Propose updates to corresponding physical `SKILL.md` or `IDENTITY.md`.

---
*Skill v3.2.0-S | Status: Standardized.*
