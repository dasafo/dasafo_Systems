---
version: 3.2.0-S
agent: DB_MASTER
---

# 🗄️ Skill | Safe Database Migrations

## Objective

Execute database schema evolutions safely and without downtime, strictly enforcing industrial fallback and rollback verification.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `tool`: (string) "alembic" | "prisma" | "supabase".
- `action`: (string) "generate" | "upgrade" | "downgrade".
- `message`: (string, optional): Required for "generate".

### Output Schema (SkillOutput.result)

- `status`: (string) "SUCCESS" | "FAILED".
- `migration_output`: (string) CLI engine response.
- `rollback_ready`: (boolean) Verified `down` path.

### ⚖️ Mandato SI (Sistema Internacional)

Los tiempos de ejecución de las migraciones deben registrarse en segundos (s) y el tamaño de los volcados en megabytes (MB).

## Logic & Safety Checklist

1. **Read-Only First:** Ensure the migration does not block concurrent production reads.
2. **Concurrency:** In PostgreSQL, indexes MUST be created `CONCURRENTLY`.
3. **Unbreakable Rollback:** Every `upgrade` MUST have a pre-verified `down` path in the versioning tool.

---
*Skill v3.2.0-S | Status: Standardized.*
