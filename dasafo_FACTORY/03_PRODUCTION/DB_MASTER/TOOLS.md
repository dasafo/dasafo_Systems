# 🛠️ DB_MASTER | Tools & Senses

> **Standard:** v3.4.0-S "SDD Implementation"
> **Scope:** Schema execution, SQL generation, and Supabase integration.

## 📡 Senses (Context-Limited)
- **Spec Sense:** Authority to read and interpret `SPEC_LITE.json`.
- **Targeted File Sense:** Read/Write access strictly restricted to `WORKSPACE/database/` and specific `context_pointers`.
- **Schema X-Ray:** Read access to `DOCS/ARCH/` to strictly follow the DTOs dictated by the Architect.

## 🧰 Authorized Skills (Skill Library)
*(Lazy loaded only when mandated by the Spec)*

- `database-architect-strategic`: tactical execution of SQL/NoSQL schema migrations based on M2 blueprints.
- `supabase-stack-expert`: Direct interaction with Postgres, RLS (Row Level Security), and Edge Functions.
- `agentic-thought-secret-scanner`: Mandatory check to ensure no database URLs or passwords leak into the migration scripts.

---
*DB Master v3.4.0-S | Status: Standardized & Industrialized.*
