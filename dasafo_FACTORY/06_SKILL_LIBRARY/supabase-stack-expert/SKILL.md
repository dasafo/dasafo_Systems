---
version: v5.0-MCP (Native)
agent_authorization: [DB_MASTER]
production_category: BUILD
source: https://skills.sh/supabase/agent-skills/supabase-postgres-best-practices
protocol: DB-Optimization / DAST
---

# 🐘 Skill | supabase-stack-expert

## Objective

Operate as a high-performance database engineer specialized in the Supabase/Postgres ecosystem. Enforces strict RLS policies, indexing strategies, and SI-compliant performance monitoring.

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use direct typed arguments. `params_json` is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your Agent ID (must be 'DB_MASTER').
- `target_project` (string): Path to project root.
- `action` (enum): `tune_query`, `audit_schema`, `enforce_rls`, `monitor_performance`.
- `sql_script` (string): (Optional) The SQL/Schema to analyze.
- `overwrite` (boolean): Bypass Redundancy Lock for reports.
- `isolation_mode` (boolean): If `true`, targets local DB instead of Shared INFRA.
- `isolate` (boolean): Execution in Clean Session.

## 🛡️ Industrial Constraints

- **RLS Mandate:** No table can exist in the `public` schema without a verified Row-Level Security policy.
- **Index Guardrail:** Tables > 1MB MUST have verified indexes for common patterns.
- **SI Standards:** All latencies in **Seconds (s)** and sizes in **Bytes (B)**.
- **DAST Sovereignty:** All migrations and reports MUST be persisted in `INFRASTRUCTURE/DATABASE/`.

---
**ORIGIN:** [supabase-best-practices by supabase](https://skills.sh/supabase/agent-skills/supabase-postgres-best-practices)
