---
version: 3.2.0-S
agent: QA_TESTER
---

# 🕵️‍♂️ Skill | ScoutQA Automated Suite Generation

## Objective

Automatically generate high-coverage Unit and Integration test suites by analyzing code structure and identifying industrial edge cases before deployment.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `target_dir` (string): Absolute path to the code to test.
- `coverage_threshold` (float, optional): Default 0.80 (80%).

### Output Schema (SkillOutput.result)

- `generated_files`: (list) List of `test_*.py` created.
- `estimated_coverage`: (float) (0.0-1.0).
- `edge_cases_covered`: (list) List of scenarios handled.

### ⚖️ Mandato SI (Sistema Internacional)

Toda métrica de rendimiento de los tests (tiempo de ejecución en segundos, uso de memoria en bytes) debe reportarse en el SI.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Physical Execution:** Succesful suite generation REQUIRES physical verification via `pytest --collect-only`.
- **Threshold Enforcement:** Rejects any suite with less than 80% code coverage. This is a physical gate.

## Core Process

1. **Code Discovery:** Use `grep` or `list_dir` to find new modifications in production agents.
2. **Suite Generation:** Create `test_*.py` files for Happy Path, Unhappy Path (Exceptions), and Edge Cases (Null/Overflow).
3. **Execution:** Run the suite and produce a `TEST_REPORT.json`.
4. **Threshold Enforcement:** Rejects any suite with less than 80% code coverage.

---
*Skill v3.2.0-S | Status: Standardized.*
