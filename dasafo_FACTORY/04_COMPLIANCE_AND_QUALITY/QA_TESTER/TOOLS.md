# 🛠️ QA_TESTER | Tools & Senses

> **Standard:** v3.4.0-S "SDD Implementation"

## 📡 Senses

- **Spec Sense:** Authority to read `SPEC_LITE.json` and architectural ADRs.
- **Codebase X-Ray:** Read-only access to all `WORKSPACE/` layers for compliance auditing.

## 🧰 Authorized Skills

- `factory-audit-pro`: Deep scan for architecture and DTO compliance.
- `hallucination-guardrail`: Verify logic alignment against the `SPEC_LITE`.
- `agentic-thought-secret-scanner`: Final safety gate to ensure no implementation agent leaked credentials or environment variables into the codebase.
- `build-test-executor`: Compilation and test execution to generate the Aduana BUILD_REPORT.json.
- `pytest-logic-verifier`: Programmatic backend logic testing via Pytest.
- `playwright-e2e-tester`: Browser flow verification and UI testing.
