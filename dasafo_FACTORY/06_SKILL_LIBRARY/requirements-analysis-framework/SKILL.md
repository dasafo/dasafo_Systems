---
version: 3.2.0-S
agent: PRODUCT_OWNER
---

# 🧠 Skill | Requirements Analysis Framework

## Objective

Diagnose the current state of a vague request and evolve it into "Validated Requirements" (RA5) before commissioning technical industrial work.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `raw_intent` (string): The initial user request.
- `current_context` (string, optional): Relevant project history.

### Output Schema (SkillOutput.result)

- `current_ra_level`: (integer) 0 (vague) to 5 (validated).
- `missing_clarity`: (list) Questions for the user.
- `disappoint_test_result`: (string) Potential failure modes if ignored.

### ⚖️ Mandato SI (Sistema Internacional)

Todas las restricciones cuantitativas del framework deben expresarse en el SI.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Verification Gate:** Requirements MUST be physically cross-referenced with the `PRP_CONTRACT.json` if it exists.
- **Traceability:** RA-level transitions MUST be documented in the task's metadata or `LOGS/PLANNING/`.

## Diagnostic Levels

- **RA0:** No Problem Statement found.
- **RA1:** Solution-First Thinking (Needs focus on the 'Why').
- **RA2:** Vague Needs (Needs the "Disappoint Test").
- **RA3:** Hidden Constraints found (Time, Skill, Budget).
- **RA4:** Scope Creep Risks mapped.
- **RA5:** Validated and ready for `TASKS/01_PENDING`.

---
*Skill v3.2.0-S | Status: Standardized.*
