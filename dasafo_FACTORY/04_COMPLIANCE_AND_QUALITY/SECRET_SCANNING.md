# 🔒 Standard | Secret Scanning & Zero-Trust

> [ ⬆️ Up: [[MOC_COMPLIANCE]] | 📂 Index: [[MOC_COMPLIANCE]] ]

## 🛡️ Credential Protection
The factory operates under a strict "No Hardcoded Secrets" policy. All agents must use the `agentic-thought-secret-scanner` before any commit to a production branch.

### 🔍 Scanning Scope
- **API Keys:** OpenAI, Supabase, Anthropic, GCP.
- **DB Strings:** PostgreSQL, Neo4j, Redis.
- **Personal Data (PII):** Emails, addresses, and phone numbers in code comments.

---
*Tooling: agentic-thought-secret-scanner (v5.0-MCP).*
