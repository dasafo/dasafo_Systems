---
version: 3.2.0-S
agent: DB_MASTER
---

# ⚡ Skill | Supabase Stack Expert

## Objective
Architect and manage high-velocity full-stack database ecosystems using Supabase, enforcing RLS-only policies and strict migration-driven version control.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `action` (string): "init" | "generate_migration" | "test_rls".
- `table_design` (object, optional): Schematic for the new table.

### Output Schema (SkillOutput.result)
- `migration_path`: (string) Absolute path to the new SQL file.
- `rls_verification`: (string) "CONFIRMED".
- `auth_ready`: (boolean) True.

### ⚖️ Mandato SI (Sistema Internacional)
Métricas de rendimiento de consulta y almacenamiento (Cloud storage en GB) deben reportarse en el SI.

## Workflow Rules
1.  **RLS Mandatory:** Table creation is FORBIDDEN without explicit Row Level Security policies.
2.  **Migration-Driven:** Hand-patching live data is forbidden. Every change must be in a versioned migration file.
3.  **Auth Integration:** Every feature must bridge directly to `auth.users` for multi-tenancy security.
4.  **Local Isolation:** Docker-based local testing of RLS policies is a prerequisite for production push.

---
*Skill v3.2.0-S | Status: Standardized.*
