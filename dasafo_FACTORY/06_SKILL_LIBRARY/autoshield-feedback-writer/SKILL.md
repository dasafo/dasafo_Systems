---
version: 3.2.0-S
agent: QA_TESTER
---

# ✍️ Skill | AutoShield Feedback Writer

## Objective
Transform rejected tasks and errors into structured collective intelligence assets within the `FEEDBACK-LOG.md`.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `id` (string): FB-ID (e.g., "FB-0001").
- `pattern` (string): Description of the detected failure pattern.
- `severity` (string): "critical" | "high" | "medium" | "low".
- `affected_agent` (string): The agent role that committed or is affected by the error.
- `golden_rule` (string, optional): Actionable universal rule derived from the error.

### Output Schema (SkillOutput.result)
- `message`: (string) Feedback recording status.
- `path`: (string) Path to the updated FEEDBACK-LOG.md.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier valor numérico relacionado con la severidad técnica o el impacto debe monitorizarse bajo métricas del Sistema Internacional.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Append Integrity:** This skill physically appends to `FEEDBACK-LOG.md`. If the file is missing in the project root, it attempts to locate the central factory log.
- **Standard Enforcement:** Every entry MUST include a `validated_standard: "v3.2.0-S"` field for auditability.

## 🧠 Protocol

1. **Capture:** Extract technical details of the failure.
2. **Classify:** Assign severity and category tags.
3. **Synthesize:** Formulate a **Golden Rule** (Universal, context-independent).
4. **Persist:** Physically append to `FEEDBACK-LOG.md` within the factory root or project.

---
*Skill v3.2.0-S | Status: Standardized.*
