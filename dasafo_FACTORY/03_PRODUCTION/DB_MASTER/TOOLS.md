# 🛠️ DB_MASTER | Tools & Senses (v4.0-MCP)

> **Standard:** v4.0-MCP "Industrial Core - DAST Optimized"
> **Scope:** Schema execution, SQL generation, and Supabase integration.

## 📡 Senses (Context-Limited)

- **Spec Sense:** Authority to read and interpret `SPEC_LITE.json`.
- **Targeted File Sense:** Read/Write access strictly restricted to `WORKSPACE/database/` and specific `context_pointers`.
- **Schema X-Ray:** Read access to `DOCS/ARCH/` to strictly follow the DTOs dictated by the Architect.
- **DAST Sense:** Ability to verify the physical integrity of schemas and tasks on disk before applying migrations.

## 🧰 Authorized Skills (Skill Library)

*(CRITICAL: All skills must be executed by passing the skill name to the `execute_industrial_skill` MCP Tool).*

### ⚙️ Logic & Implementation

- `database-architect-strategic`: Tactical execution of SQL/NoSQL schema migrations based on M2 blueprints.
- `supabase-stack-expert`: Direct interaction with Postgres, RLS (Row Level Security), and Edge Functions.

### 🛡️ Guardrails & Security

- `agentic-thought-secret-scanner`: Mandatory check to ensure no database URLs or passwords leak into the migration scripts.

---
*DB Master v4.0-MCP | Status: Autonomous Persistence Guardian & Solidified.*
