# Skill: Safe Database Migrations
> **Source:** https://skills.sh/affaan-m/everything-claude-code/database-migrations
> **Agent:** BACKEND_DEV

## Objective
Execute database schema changes safely and without downtime using Alembic or Prisma.

## Safety Checklist
1.  **Read-Only First:** Can the new schema be applied without blocking existing reads?
2.  **Column Addition:** Adding a column with a default value must be done in two steps (Add -> Set Default) for large tables.
3.  **Indexing:** Create indexes CONCURRENTLY (PostgreSQL specific) to avoid table locks.
4.  **Rollback Strategy:** Every migration MUST have a corresponding `down` or `undo` path.

## Workflow
- **Alembic:** Use `alembic revision --autogenerate` -> Review -> `alembic upgrade head`.
- **Validation:** Check the `DB_MASTER` state before and after the migration.
