---
version: v5.0-MCP (Native)
agent_authorization: [QA_TESTER, FRONTEND_DEV]
production_category: VERIFY
protocol: E2E-Validation / DAST
---

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]


# 🎭 Skill | playwright-e2e-tester

## Objective

Execute End-to-End (E2E) browser testing using Playwright to ensure UI/UX workflows match functional criteria. Generates physical evidence (JSON/Video) for quality audits.

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use direct typed arguments. `params_json` is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your Agent ID (QA_TESTER or FRONTEND_DEV).
- `target_project` (string): Absolute path to project root.
- `action` (enum): `run_e2e` (default) | `generate_spec`.
- `spec_path` (string): (Optional) Path to the task specification defining the flow.
- `url` (string): (Optional) Staging or localhost URL to test (default: `http://localhost:3000`).
- `isolate` (boolean): Execution in Clean Session.

## 🛡️ Industrial Constraints

- **Physical Proof:** Every run MUST generate a `PLAYWRIGHT_REPORT.json` in `LOGS/`.
- **SI Standards:** Durations in **Seconds (s)** and video/trace sizes in **Bytes (B)**.
- **Contract Parity:** Assertions must map 1:1 to user stories in the project contract.

---

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]

*Standard v5.0-MCP | Dasafo Factory Compliance Hub.*
