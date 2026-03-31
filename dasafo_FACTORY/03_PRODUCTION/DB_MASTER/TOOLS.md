# 🛠️ DB_MASTER | Tools & Senses (v3.4.0-S)

> **Standard:** v3.4.0-S "Industrial Core - DAST Optimized"
> **Scope:** Schema execution, SQL generation, and Supabase integration.

## 📡 Senses (Context-Limited)

- **Spec Sense:** Authority to read and interpret `SPEC_LITE.json`.
- **Targeted File Sense:** Read/Write access strictly restricted to `WORKSPACE/database/` and specific `context_pointers`.
- **Schema X-Ray:** Read access to `DOCS/ARCH/` to strictly follow the DTOs dictated by the Architect.
- **DAST Sense:** Capacidad para verificar la integridad física de los esquemas y tareas en el disco antes de aplicar migraciones.

## 🧰 Authorized Skills (Skill Library)

*(Lazy loaded only when mandated by the Spec)*

### ⚙️ Logic & Implementation

- `database-architect-strategic`: Tactical execution of SQL/NoSQL schema migrations based on M2 blueprints.
- `supabase-stack-expert`: Direct interaction with Postgres, RLS (Row Level Security), and Edge Functions.
- **`registry-manager`**: Acción `update_status` para ejecutar el movimiento atómico de tareas y sincronización de disco.

### 🛡️ Guardrails & Security

- `agentic-thought-secret-scanner`: Mandatory check to ensure no database URLs or passwords leak into the migration scripts.

---
*DB Master v3.4.0-S | Status: Guardián de Persistencia Autónomo & Solidificado.*
