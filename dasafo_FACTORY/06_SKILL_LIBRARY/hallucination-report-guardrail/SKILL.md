---
version: 3.3.0-S
agent: Multiple (DOCS_MASTER / QA_TESTER)
source: https://skills.sh/supercent-io/skills-template/hallucination-report-guardrail
---

# 🛡️ Skill | Hallucination Report Guardrail

## Objective

Perform meticulous fact-checking on QA results themselves to ensure zero false positives reach the developers, maintaining absolute trust in the factory reports.

## 🛠️ Interface (v3.3.0-S)

### Input Schema (SkillInput.params)

- `report_path` (string): Absolute path to the QA Report.
- `evidence_required` (boolean, optional): Default `true`.

### Output Schema (SkillOutput.result)

- `solidity_score`: (integer) 0-100 reliability score.
- `solidity_verdict`: (string) "VERIFIED_SOLID" | "VOID_LACK_OF_EVIDENCE" | "HALLUCINATION_DETECTED".
- `missing_evidence`: (list) Missing logs, file paths, or line numbers.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica de error (latencia capturada, diferencia de bytes) debe coincidir con la telemetría del sistema expresada en el SI.

## Protocol

1. **Evidence Checklist:** Every identified bug MUST include:
   - Path and Line Number.
   - Log Snippet.
   - Expected vs Actual behavior comparison.
2. **Veracity Filter:** Flag reports lacking evidence as "Unconfirmed Observations".
3. **Tone:** Enforce strict, meticulous, and objective voice.

---
**ORIGIN:** [hallucination-report-guardrail by supercent-io](https://skills.sh/supercent-io/skills-template/hallucination-report-guardrail)
*Skill v3.3.0-S | Status: Standardized & Industrialized.*
