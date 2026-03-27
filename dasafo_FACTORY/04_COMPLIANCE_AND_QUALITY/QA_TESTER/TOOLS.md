# 🛠️ QA Tester | Tools & Senses

> **Standard:** v3.2.0-S Modular Toolbox
> **Scope:** Quality assurance, visual validation, and requirement compliance.

## 📡 Senses (MCP Protocol)

- **Browser Sense:** Visual and functional UI testing via Playwright.
- **Filesystem Sense:** Access to `$TARGET_PROJECT/WORKSPACE/`, `LOCAL_KNOWLEDGE/`, and `LOGS/`.
- **Terminal Sense:** Execution of test suites (Pytest, Playwright) and linters.

## 🧰 Authorized Skills (Skill Library)
*(Invoked via `execute_factory_skill`)*

- `autoshield-feedback-writer`: Generation of actionable feedback in `FEEDBACK-LOG.md`.
- `browser-visual-validation`: Visual regression testing and diffing.
- `hallucination-report-guardrail`: Identifying agent-specific logic errors or false claims.
- `playwright-visual-testing`: End-to-end browser automation.
- `requirements-validation-audit`: Verification of code against contract specs.
- `scoutqa-automated-suites`: Industrial-scale test suite management.
- `autoshield-preflight-check`: Mandatory pre-execution validation.
- `kanban-solidity-gate`: Mandatory gate for updating task status in the Registry SSoT.

---
*QA Tester v3.2.0-S | Status: Modularized.*
