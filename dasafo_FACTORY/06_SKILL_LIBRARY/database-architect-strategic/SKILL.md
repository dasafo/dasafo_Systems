---
version: 3.2.0-S
agent: DB_MASTER
---

# 🏗️ Skill | Strategic Database Architect

## Objective

Provide high-level architecture decisions for data storage, consistency, and scalability across the industrial ecosystem.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `table` (string, optional): Target table name for migration.
- `strategy` (string, optional): "relational" | "vector" | "document". Default "relational".

### Output Schema (SkillOutput.result)

- `sql_migration`: (string) Generated SQL command.
- `blueprint_path`: (string) Path to the saved architecture blueprint.
- `status`: (string) "STABLE".

### ⚖️ Mandato SI (Sistema Internacional)

Las latencias de consulta (p99), el throughput de transacciones (TPS) y el consumo de almacenamiento (bytes) deben expresarse bajo unidades del SI.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Physical Migration:** This skill physically writes `.sql` files to `LOCAL_KNOWLEDGE/architecture/`. If the path is inaccessible, the skill returns `failure`.
- **Stateless Verification:** The DB Master verifies the validity of SQL syntax against a local schema definition before saving.

## Tactical Decisions

- **Normalization:** Only denormalize when benchmarks (SI) prove performance gains.
- **Storage:** Select storage engine based on access patterns (PG, Supabase Vector, JSONB).
- **Disaster Recovery:** SCHEMAS must include PITR and high availability plans.

---
*Skill v3.2.0-S | Status: Standardized.*
