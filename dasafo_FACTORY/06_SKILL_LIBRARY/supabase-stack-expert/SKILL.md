---
version: 3.4.0-S
agent: DB_MASTER
source: https://skills.sh/supabase/agent-skills/supabase-postgres-best-practices
---

# 🐘 Skill | Supabase Stack Expert (v3.4.0-S)

## Objective

Operate as a high-performance database engineer specialized in the Supabase/Postgres ecosystem. This skill enforces 8 priority categories of Postgres best practices (Query Performance, Connection Management, Security/RLS, Schema Design, Concurrency, Data Access, Monitoring, and Advanced Features) to ensure scalability, security, and industrial-grade reliability.

## 🛠️ Interface (v3.4.0-S)

### Input Schema (SkillInput.params)

- `action` (enum): `tune_query`, `audit_schema`, `enforce_rls`, `monitor_performance`.
- `target_project` (string, mandatory): Absolute path to the backend/database workspace.
- `sql_script` (string, optional): The SQL script or schema definition to analyze.
- `overwrite` (boolean, optional): Whether to overwrite existing report files.
- `isolation_mode` (boolean, optional): If `True`, targets a local/isolated database instead of the shared INFRA node (`dasafo-shared-db`).
- `audit_scope` (array, optional): Default `["query", "security", "schema"]`.

### Output Schema (SkillOutput.result)

- `industrial_status`: (string) "SOLIDIFIED - DATABASE OPTIMIZED".
- `optimization_report`: (string) Detailed analysis based on the 8 priority categories.
- `suggested_indexes`: (array) List of missing or partial indexes identified.
- `rls_verification`: (object) Status of Row-Level Security policies.
- `performance_metrics`: (object) Estimated time (s) and impact of changes.
- `compliance_report`: (object) Verification of SI mandates and Hybrid Infra alignment.
- `summary`: (string) Human-readable outcome of the specific database action.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica de rendimiento (latencia de consulta, tiempo de ejecución de EXPLAIN, tiempos de recuperación ante fallos, tamaños de tabla e índices) debe expresarse estrictamente en el SI (**segundos**, **bytes**).

## 🛡️ Industrial Constraints (Zero-Trust)

- **RLS by Default:** No table can exist in the public schema without a defined and verified Row-Level Security policy.
- **Index Guardrail:** Every table over 1,000,000 bytes (1MB) must have verified indexes for common query patterns.
- **Explain-Before-Commit:** Substantial query changes must include a simulated or actual `EXPLAIN ANALYZE` output in seconds (s).
- **Physical Migrations:** All database changes must be saved as physical migration files (`.sql`) in `INFRASTRUCTURE/DATABASE/`.

## 🧠 Database Workflow (v3.4.0-S)

1. **Pre-Audit:** Analyze the schema or query using the 8 priority categories (Query, Conn, Security, Schema, Lock, Data, Monitor, Advanced).
2. **Indexing Strategy:** Implement partial or covering indexes to reduce execution time (< 0.1s for OLTP).
3. **Security Lockdown:** Configure RLS using `auth.uid()` or similar patterns for shared multi-tenant environments.
4. **Optimization:** Apply connection pooling and tuning for Postgres-specific features (JSONB indexing, Full-text search).
5. **Physical Record:** Document the EXPLAIN analysis and performance metrics in the project's architecture folder.

---
**ORIGIN:** [supabase-postgres-best-practices by supabase](https://skills.sh/supabase/agent-skills/supabase-postgres-best-practices)
*Skill v3.4.0-S | Status: Standardized & Industrialized (Dasafo Edition).*
