---
version: 3.2.0-S
agent: QA_TESTER
---

# 📋 Skill | Requirements Validation Audit

## Objective

Act as the industrial "Devil's Advocate" to ensure that implementation matches the RA5 requirements validated by the Product Owner.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `task_id` (string): ID of the task to audit.
- `ra_level_required` (integer, optional): Default 5.

### Output Schema (SkillOutput.result)

- `audit_verdict`: (string) "COMPLIANT" | "NON_COMPLIANT".
- `traceability_report`: (object) Mapping of tests to goals.
- `coverage_percentage`: (float) (0-100).

### ⚖️ Mandato SI (Sistema Internacional)

La validación de unidades consistentes (SI) es parte obligatoria del checklist de auditoría.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Evidence Lock:** Verdicts MUST be based on physical execution of tests and reading of `PROJECT_STATE.json`.
- **Unit Audit:** Any technical output (logs, reports) not following the SI Mandate triggers an automatic `NON_COMPLIANT` verdict.

## Audit Workflow

1. **Traceability:** Map test cases in `PROJECT_STATE.json` to requirement IDs.
2. **Compliance:** Verify if the feature solves the original problem (not just running without errors).
3. **V-Model Pass:** Mandate 100% coverage for acceptance criteria before allowing transition to "DONE".
4. **Unit Consistency:** Verify Mandato SI in all technical outputs.

---
*Skill v3.2.0-S | Status: Standardized.*
