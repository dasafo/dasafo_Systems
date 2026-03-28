# 🛠️ Security Auditor | Tools & Senses

> **Standard:** v3.2.5-S Modular Toolbox
> **Scope:** Secret scanning, vulnerability detection, and boundary security.

## 📡 Senses (MCP Protocol)

- **Search Sense:** Deep scanning of codebase for secrets, keys, and dangerous patterns.
- **Terminal Sense:** Execution of vulnerability scanners (Talisman, Gitleaks, safety) and static analysis.
- **Security Insight Sense:** Access to known vulnerability databases (OWASP, CVE).

## 🧰 Authorized Skills (Skill Library)
*(Invoked via `execute_factory_skill` or direct `run.py`)*

### 🛡️ Secret & Vuln Scanning
- `agentic-thought-secret-scanner`: **[CRITICAL]** In-depth scanning for secrets and credentials.
- `owasp-llm-enforcement`: Specific audit for LLM-integrated project vulnerabilities.
- `nemo-llm-guardrails`: Validation of AI safety at the prompt-logic boundary.

### 🛡️ Guardrails & Certification
- `factory-audit-pro`: High-level security certification.
- `kanban-solidity-gate`: Verify physical task evidence.
- `autoshield-preflight-check`: Mandatory pre-execution validation.
- `nemo-guardrails-safety`: Policy enforcement for AI behavior.

### 🏗️ Advanced Operations
- `resource-monitor`: Audit for suspicious infrastructure activity.
- `skill-optimization`: Ensure factory skills remain secure and up-to-date.
- `resilient-error-handling`: Audit for info leaks in error messages.

---
*Security Auditor v3.2.5-S | Status: Encapsulated & Modularized.*
