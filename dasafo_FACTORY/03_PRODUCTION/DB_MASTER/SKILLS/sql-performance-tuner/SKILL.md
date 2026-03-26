# ⏱️ Skill | SQL Performance Tuner
> **Version:** v3.1.5 "Solidity Guard"
> **Agent:** DB_MASTER

## Objective
Analyze, optimize, and refactor SQL queries to ensure maximum speed and minimal resource usage.

## Performance Protocol
1.  **Analyze:** Always use `EXPLAIN (ANALYZE, BUFFERS)` to see the execution plan.
2.  **Indexing:**
    - Use B-Tree for standard equality/range queries.
    - Use GIN for JSONB and Full-Text Search.
    - Use BRIN for huge sequential tables (time-series).
3.  **N+1 Killer:** Identify and refactor queries with nested loops to use efficient `JOIN`s or `WITH` clauses (CTEs).

## Constraints
NO query should perform a Full Table Scan on tables larger than 10k rows without a documented reason.
