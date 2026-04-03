---
version: v5.0-MCP (Native)
agent_authorization: [QA_TESTER, DEVOPS_SRE]
source: internal/skill-creator
protocol: Build-Verification / DAST
---

# 🔨 Skill | build-test-executor

## Objective

Execute technical build or test commands and generate the mandatory **BUILD_REPORT.json** (Aduana Passport) required for phase transitions.

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use direct arguments. Generic `params_json` is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your authorized Agent ID (QA_TESTER, DEVOPS_SRE).
- `target_project` (string): Absolute path to project root.
- `action` (enum): `run_build` | `run_tests`.
- `command` (string): The actual shell command (e.g., `npm run build`, `pytest`).
- `overwrite` (boolean): (Optional) Bypass Redundancy Lock.
- `isolate` (boolean): Execution in Clean Session.

## 🛡️ Industrial Constraints

- **Customs Mandate:** This skill MUST generate a physical `LOGS/BUILD_REPORT.json`. No report = No phase transition.
- **Fail-Fast:** Any non-zero exit code will raise a critical exception to block the pipeline.
- **SI Standards:** Durations in **seconds (s)** and sizes in **bytes (B)**.

---
*Standard v5.0-MCP | Dasafo Factory Compliance Hub.*
