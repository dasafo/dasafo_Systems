---
version: 3.2.0-S
agent: DB_MASTER
---

# ⏱️ Skill | SQL Performance Tuner

## Objective

Analyze, optimize, and refactor complex SQL queries to ensuring minimum resource latency and maximum throughput in the factory's data layer.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `query` (string): The raw SQL string to analyze.
- `analyze` (boolean, optional): Set true for real execution plan. Default false.

### Output Schema (SkillOutput.result)

- `execution_plan`: (string) Markdown block of `EXPLAIN` output.
- `optimization_strategy`: (string) "Indexing" | "Refactoring" | "Caching".
- `estimated_speedup`: (float) (e.g., 2.5x).

### ⚖️ Mandato SI (Sistema Internacional)

Los costes de ejecución de las consultas deben reportarse en milisegundos (ms) y el uso de búfer en bytes/megabytes (SI).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Evidence Based:** Optimization proposals MUST include a physical `EXPLAIN ANALYZE` dump before and after changes.
- **Safety Gate:** Rejects any refactoring that bypasses established RLS policies.

## Performance Protocol

1. **Diagnostics:** Use `EXPLAIN (ANALYZE, BUFFERS)` to isolate bottlenecks.
2. **Industrial Indexing:**
   - **B-Tree:** Standard ranges.
   - **GIN:** JSONB / Full-Text Search.
   - **BRIN:** Multi-terabyte time-series data.
3. **Join Refactoring:** Eliminate N+1 patterns via CTEs or lateral joins.
4. **Constraint:** Reject any query performing a Full Table Scan on >10k rows.

---
*Skill v3.2.0-S | Status: Standardized.*
