# 🛠️ Security Auditor | Tools & Senses

> **Standard:** v3.2.0-S Modular Toolbox
> **Scope:** Secret scanning, vulnerability assessment, and LLM guardrail enforcement.

## 📡 Senses (MCP Protocol)

- **Filesystem Sense:** Full recursive access to `$TARGET_PROJECT` for deep secret scanning.
- **Python Sense:** Security scripting, policy enforcement, and log analysis.
- **Terminal Sense:** Execution of specialized security tools (Husky, Bandit, etc.).

## 🧰 Authorized Skills (Skill Library)
*(Invoked via `execute_factory_skill`)*

- `agentic-thought-secret-scanner`: Mandatory detection of hardcoded credentials.
- `nemo-llm-guardrails`: Enforcement of AI safety and prompt injection protection.
- `owasp-llm-enforcement`: Compliance check against OWASP Top 10 for LLMs.
- `autoshield-preflight-check`: Mandatory pre-execution environment validation.
- `kanban-solidity-gate`: Mandatory gate for updating security task status in the Registry SSoT.

---
*Security Auditor v3.2.0-S | Status: Modularized.*
