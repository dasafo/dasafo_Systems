---
version: 3.2.0-S
agent: DB_MASTER
---

# 🟢 Skill | Supabase Live Validation

## Objective
Connect to Supabase via industrial MCP to validate physical schema integrity, RLS policies, and data constraints against the Architect's blueprints with zero drift tolerance.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `reference_schema_path` (string): Absolute path to the expected SQL/Blueprints.
- `severity_threshold` (string, optional): "LOW" | "MEDIUM" | "HIGH". Default "HIGH".

### Output Schema (SkillOutput.result)
- `schema_drift_detected`: (boolean).
- `drift_summary`: (list) Missing tables, column mismatch, or RLS failure.
- `verdict`: (string) "PASS" | "BLOCK_DEPLOYMENT".

### ⚖️ Mandato SI (Sistema Internacional)
Tiempos de latencia de conexión (ms) y tamaños de tabla (Megabytes) deben reportarse exclusivamente en el SI.

## Validation Protocol
1.  **Reference Loading:** Read expected schema from `$TARGET_PROJECT/LOCAL_KNOWLEDGE/`.
2.  **Live Inspection:** Query Supabase `information_schema` for real-time table structures.
3.  **Drift Audit:** Compare Columns, Types, Foreign Keys, and Indexes (case-insensitive).
4.  **Security Audit:** Confirm RLS policies are ACTIVE on sensitive tables.
5.  **Rejection Gate:** Block deployment if CRITICAL or HIGH mismatches are detected.

---
*Skill v3.2.0-S | Status: Standardized.*
