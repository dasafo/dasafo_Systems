# 🛠️ SECURITY_AUDITOR | Tools & Senses

> **Standard:** v3.4.0-S "SDD Implementation"
> **Scope:** Static analysis (SAST), secret scanning, and dependency auditing.

## 📡 Senses (Context-Limited)

- **Spec Sense:** Authority to read and interpret `SPEC_LITE.json`.
- **Zero-Trust Sense:** Read-only access to all files in `WORKSPACE/`. No write access allowed except to `$TARGET_PROJECT/DOCS/SECURITY/`.
- **Secret X-Ray:** Deep scan access to file contents and environment variable templates.

## 🧰 Authorized Skills

- `agentic-thought-secret-scanner`: **[CRITICAL]** Deep scanning for secrets, keys, and credentials.
- `factory-audit-pro`: Security scoring and health report generation.
- `dependency-vulnerability-scanner`: Scan `package.json`, `requirements.txt`, etc., for known CVEs.

---
*Security Auditor v3.4.0-S | Status: Standardized & Industrialized.*
