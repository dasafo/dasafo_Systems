---
version: v4.0-MCP
agent: DEVOPS_SRE / QA_TESTER
source: internal/skill-creator
---

# 🔨 Skill | Build & Test Executor (v4.0-MCP)

## Objective

Execute compilation, testing, or build commands and generate the mandatory `BUILD_REPORT.json` required by the Universal Customs (`session_hook.py`) to authorize phase transitions (M3 -> M4).

## 🛠️ Interface (v4.0-MCP)

### Input Schema (SkillInput.params)

- `action` (enum): `run_build`, `run_tests`.
- `command` (string, optional): The technical command to run (e.g., `npm run build`, `pytest`).
- `target_project` (string, mandatory): Absolute path to the project workspace.

### Output Schema (SkillOutput.result)

- `build_status`: (string) `SUCCESS` or `FAILED`.
- `report_path`: (string) Path to `LOGS/BUILD_REPORT.json`.
- `metrics`: (object) Output sizes and execution times.
- `industrial_status`: (string) "SOLIDIFIED - BUILD VERIFIED"

### ⚖️ SI Mandate (International System)

Any build metrics must indicate the time in **seconds** (s) and the size of the generated bundle in **bytes** (B).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Aduana Passport:** This skill MUST generate a physical `BUILD_REPORT.json` in the `LOGS/` directory, acting as the unforgeable proof of compilation.
- **Fail-Fast:** If the command fails, the `build_status` must be `FAILED`, blocking any phase transition attempts.
