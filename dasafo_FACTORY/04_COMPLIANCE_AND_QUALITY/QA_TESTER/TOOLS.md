# 🛠️ QA_TESTER | Tools & Senses

> **Standard:** v4.0-MCP "Industrial Core - DAST Optimized"

## 📡 Senses

- **Spec Sense:** Authority to read `SPEC_LITE.json` and architectural ADRs.
- **Codebase X-Ray:** Read-only access to all `WORKSPACE/` layers for compliance auditing.
- **DAST Sense:** Ability to verify the physical integrity of tasks and the registry before issuing a compliance failure.

## 🧰 Authorized Skills (Factory Engine)

*(CRITICAL: All skills MUST be invoked EXCLUSIVELY by passing their name to the `execute_industrial_skill` MCP Tool. Do NOT use bash).*

- `factory-audit-pro`: Deep scan for architecture and DTO compliance.
- `hallucination-guardrail`: Verify logic alignment against the `SPEC_LITE`.
- `agentic-thought-secret-scanner`: Final safety gate to ensure no implementation agent leaked credentials.
- `build-test-executor`: Compilation and test execution to generate the Aduana BUILD_REPORT.json.
- `playwright-e2e-tester`: Browser flow verification and UI testing.

---
*QA Tester v4.0-MCP | Status: Autonomous Guardian & Solidified.*
