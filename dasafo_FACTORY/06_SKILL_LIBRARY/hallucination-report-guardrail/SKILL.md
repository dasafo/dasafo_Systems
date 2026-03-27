---
version: 3.2.0-S
agent: QA_TESTER
---

# 🛡️ Skill | Hallucination Report Guardrail

## Objective
Perform meticulous fact-checking on QA results themselves to ensure zero false positives reach the developers, maintaining absolute trust in the factory reports.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `report_path` (string): Absolute path to the QA Report.
- `evidence_required` (boolean, optional): Default `true`.

### Output Schema (SkillOutput.result)
- `solidity_verdict`: (string) "VERIFIED" | "VOID_LACK_OF_EVIDENCE".
- `missing_evidence`: (list) Missing logs, file paths, or line numbers.

### ⚖️ Mandato SI (Sistema Internacional)
Cualquier métrica de error (latencia capturada, diferencia de bytes) debe coincidir con la telemetría del sistema expresada en el SI.

## Protocol
1.  **Evidence Checklist:** Every identified bug MUST include:
    - Path and Line Number.
    - Log Snippet.
    - Expected vs Actual behavior comparison.
2.  **Veracity Filter:** Flag reports lacking evidence as "Unconfirmed Observations".
3.  **Tone:** Enforce strict, meticulous, and objective voice.

---
*Skill v3.2.0-S | Status: Standardized.*
