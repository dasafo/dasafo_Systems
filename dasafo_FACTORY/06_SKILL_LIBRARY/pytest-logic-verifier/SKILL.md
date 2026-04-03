---
version: v5.0-MCP (Native)
agent_authorization: [BACKEND_DEV]
protocol: Spec-Driven-Validation / DAST
---

# 🐍 Skill | pytest-logic-verifier

## Objective

Programmatically generate and execute Python logic tests (Pytest) to verify that backend code strictly adheres to the constraints and success evidence defined in the `SPEC_LITE.json`.

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use typed arguments. `params_json` is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your Agent ID (BACKEND_DEV).
- `target_project` (string): Absolute path to the project root.
- `action` (enum): `run_test` (default) | `generate_test`.
- `spec_path` (string): Path to the `SPEC_LITE.json` acting as the source of truth.
- `module_path` (string): (Optional) Specific backend module to test.
- `isolate` (boolean): Execution in Clean Session.

## 🛡️ Industrial Constraints

- **Zero-Trust Logic:** Tests MUST assert criteria listed in `specification.02_success_evidence`. Hallucinated tests are FORBIDDEN.
- **SI Standards:** Durations MUST be reported in **Seconds (s)**.
- **Physical Proof:** Every verification MUST persist a `PYTEST_REPORT_*.json` in `LOGS/`.

---
*Standard v5.0-MCP | Dasafo Factory Production Hub.*
