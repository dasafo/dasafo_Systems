---
version: v4.0-S
agent: QA_TESTER / BACKEND_DEV
source: internal/skill-creator
---

# 🐍 Skill | Pytest Logic Verifier (v4.0-S)

## Objective

Programmatically generate and execute Python logic tests (Pytest) to verify that backend code strictly adheres to the constraints defined in the `SPEC_LITE.json`.

## 🛠️ Interface (v4.0-S)

### Input Schema (SkillInput.params)

- `action` (enum): `generate_test`, `run_test`.
- `target_project` (string, mandatory): Absolute path to the project workspace.
- `spec_path` (string, mandatory): Path to the `SPEC_LITE.json` acting as the source of truth.
- `module_path` (string, optional): Specific backend module to test (e.g., `WORKSPACE/backend/auth.py`).

### Output Schema (SkillOutput.result)

- `test_status`: (string) `PASSED` or `FAILED`.
- `report_path`: (string) Path to the generated physical report in `LOGS/`.
- `coverage_percentage`: (float) Test coverage metric.
- `industrial_status`: (string) "SOLIDIFIED - LOGIC VERIFIED" | "BLOCKED - LOGIC FAILED".

### ⚖️ SI Mandate (International System)

Any test performance metrics must be expressed in **seconds** (s).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Spec-Driven Validation:** Tests cannot be hallucinated. They must explicitly assert the criteria listed in `specification.02_success_evidence` of the `SPEC_LITE.json`.
- **Physical Proof:** The results MUST be written to `LOGS/PYTEST_REPORT.json` so the Orchestrator can audit them.
- **No Silent Failures:** If a single assertion fails, `test_status` must be FAILED, halting the pipeline.

## 🧠 Workflow (v4.0-S)

1. **Read Contract:** Load the `SPEC_LITE.json` to understand the acceptance criteria.
2. **Generate Test:** Scaffold the `test_*.py` file using Pytest fixtures.
3. **Execute:** Run the test suite against the target module.
4. **Persist Truth:** Generate the JSON report in `LOGS/`.
