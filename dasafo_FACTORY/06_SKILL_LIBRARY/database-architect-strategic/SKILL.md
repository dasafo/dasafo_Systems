---
version: v4.0-S
agent: ARCHITECT / DB_MASTER
source: https://skills.sh/sickn33/antigravity-awesome-skills/database-architect
---

# 🗄️ Skill | Database Architect Strategic (v4.0-S)

## Objective

Provide expert-level database architecture, technology selection, and strategic data modeling. This skill spans from conceptual ERD design to physical schema optimization across relational (Postgres/Supabase), NoSQL, Graph, and Time-series models.

## 🛠️ Interface (v4.0-S)

### Input Schema (SkillInput.params)

- `action` (enum): One of `evaluate_tech`, `design_schema`, `plan_migration`, `optimize_indexing`.
- `target_project` (string, mandatory): Absolute path to the project workspace.
- `resource_entity` (string, optional): The name of the table or resource (default: "generic_resource").
- `overwrite` (boolean, optional): Whether to overwrite existing schema files.
- `isolation_mode` (boolean, optional): If `True`, targets a local/isolated database instead of the shared INFRA node (`dasafo-shared-db`).
- `requirements` (object, optional): Data volume, read/write ratios, latency targets, and compliance needs.
- `current_schema_path` (string, optional): Path to existing SQL/Schema for re-architecture.

### Output Schema (SkillOutput.result)

- `industrial_status`: (string) "SOLIDIFIED - DATABASE BLUEPRINT GENERATED"
- `architecture_plan`: (string) Detailed strategy for technology selection and modeling.
- `schema_artifacts`: (array) List of generated SQL/JSON schema files.
- `performance_projections`: (object) Estimated latency (s) and throughput (B/s).
- `compliance_report`: (object) Verification of SI mandates and Hybrid Infra alignment.
- `summary`: (string) Human-readable outcome of the specific action.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica técnica mencionada (latencias de consulta, tamaños de tabla, tasas de transferencia, límites de almacenamiento) debe expresarse estrictamente en unidades del SI (**segundos**, **bytes**).

## 🛡️ Industrial Constraints (Zero-Trust)

- **SQL First:** All relational designs must include raw, executable SQL migrations.
- **RLS Enforcement:** For Supabase/Postgres, Row Level Security (RLS) policies must be part of the core schema design.
- **No Data Loss:** Every migration plan must include a verified rollback strategy.
- **Pattern Alignment:** All schemas must follow the `02_ARCHITECTURE_RULES.md` regarding SoC and DTOs.

## 🧠 Strategic Workflow (v4.0-S)

1. **Tech Selection:** Evaluate trade-offs (CAP theorem, cost, operational complexity) to choose the optimal storage engine.
2. **Conceptual Modeling:** Map business entities to a logical data domain (Normalization/Denormalization strategies).
3. **Physical Design:** Specify data types, partitioning, and indexing for production scale.
4. **Security Hardening:** Define RLS, encryption at rest, and access control policies.
5. **Validation:** Execute plan in a sandbox/migration-check before promoting to M3/M4.

---
**ORIGIN:** [database-architect by sickn33](https://skills.sh/sickn33/antigravity-awesome-skills/database-architect)
*Skill v4.0-S | Status: Standardized & Industrialized (Dasafo Edition).*
