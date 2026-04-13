---
version: v5.0-MCP (Native)
agent_authorization: [ARCHITECT, DB_MASTER]
production_category: PLAN
source: https://skills.sh/sickn33/antigravity-awesome-skills/database-architect
protocol: Schema-First / DAST
---

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]


# 🗄️ Skill | database-architect-strategic

## Objective

Provide strategic database modeling and architecture. Ensures that all data persistence follows the Hybrid Infrastructure Mandate (LTP) and SI standards.

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use direct typed arguments. The `params_json` structure is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your Agent ID (ARCHITECT or DB_MASTER).
- `target_project` (string): Path to project root.
- `action` (enum): `design_schema`, `evaluate_tech`, `plan_migration`.
- `resource_entity` (string): Primary entity name (e.g., 'user').
- `overwrite` (boolean): Bypass Redundancy Lock.
- `isolation_mode` (boolean): If `true`, targets local DB instead of Shared INFRA.
- `isolate` (boolean): Execution in Clean Session.

## 🛡️ Industrial Constraints

- **SI Standards:** All throughput must be in **Bytes/s (B/s)** and latency in **Seconds (s)**.
- **LTP Alignment:** By default, architecture must align with `dasafo-shared-db`.
- **DAST Sovereignty:** Schemas must be physically persisted in `INFRASTRUCTURE/DATABASE/`.

---

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]

**ORIGIN:** [database-architect by sickn33](https://skills.sh/sickn33/antigravity-awesome-skills/database-architect)
