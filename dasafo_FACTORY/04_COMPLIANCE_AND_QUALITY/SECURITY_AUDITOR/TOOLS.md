# 🛠️ SECURITY_AUDITOR | Tools & Senses

> **Standard:** v4.0-MCP "Industrial Core - DAST Optimized"
> **Scope:** Static analysis (SAST), secret scanning, and dependency auditing.

## 📡 Senses (Context-Limited)

- **Spec Sense:** Authority to read and interpret `SPEC_LITE.json`.
- **Zero-Trust Sense:** Read-only access to all files in `WORKSPACE/`.
- **DAST Sense:** Ability to verify the physical integrity of artifacts and the registry.
- **Secret X-Ray:** Deep scan access to file contents and environment variable templates.

## 🧰 Authorized Skills (Factory Engine)

*(CRITICAL: All skills MUST be invoked EXCLUSIVELY by passing their name to the `execute_industrial_skill` MCP Tool. Do NOT use bash).*

- `agentic-thought-secret-scanner`: **[CRITICAL]** Deep scanning for secrets, keys, and credentials.
- `factory-audit-pro`: Security scoring and health report generation.
- `dependency-vulnerability-scanner`: Scan dependencies for known CVEs.

---
*Security Auditor v4.0-MCP | Status: Autonomous Guardian & Solidified.*
