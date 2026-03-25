"""
run.py — Skill: SQL Performance Tuner
Agent: DB_MASTER

Analyzes a SQL query, generates the equivalent EXPLAIN ANALYZE, and
returns index recommendations based on SKILL.md rules.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Add GLOBAL_KNOWLEDGE to path for skill_schema import
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "00_GLOBAL_KNOWLEDGE"))
from skill_schema import SkillInput, SkillOutput  # noqa: E402


# ── Detection Patterns ────────────────────────────────────────────────────────

_FULL_SCAN_PATTERN = re.compile(
    r"\bSELECT\b.+?\bFROM\b\s+(\w+)(?:\s+\w+)?\s*(?:WHERE\s+.+)?$",
    re.IGNORECASE | re.DOTALL,
)
_WHERE_COLS_PATTERN = re.compile(r"\bWHERE\b\s+(.+?)(?:\bORDER\b|\bGROUP\b|\bLIMIT\b|;|$)", re.IGNORECASE | re.DOTALL)
_JSONB_PATTERN = re.compile(r"->>|->|\?\||\?\&", re.IGNORECASE)
_FTS_PATTERN = re.compile(r"\bto_tsvector\b|\bto_tsquery\b|\b@@\b", re.IGNORECASE)
_NESTED_SELECT_PATTERN = re.compile(r"SELECT.+?FROM.+?WHERE.+?IN\s*\(SELECT", re.IGNORECASE | re.DOTALL)
_ORDER_BY_PATTERN = re.compile(r"\bORDER BY\b\s+(.+?)(?:\bLIMIT\b|;|$)", re.IGNORECASE | re.DOTALL)
_NO_LIMIT_PATTERN = re.compile(r"SELECT.+?FROM.+?(?!LIMIT)", re.IGNORECASE | re.DOTALL)
_LIMIT_PRESENT = re.compile(r"\bLIMIT\b", re.IGNORECASE)


def _extract_table_name(query: str) -> str:
    match = re.search(r"\bFROM\b\s+(\w+)", query, re.IGNORECASE)
    return match.group(1) if match else "unknown_table"


def _extract_where_columns(query: str) -> list[str]:
    match = _WHERE_COLS_PATTERN.search(query)
    if not match:
        return []
    where_clause = match.group(1)
    cols = re.findall(r"\b([a-zA-Z_]\w*)\b\s*(?:=|LIKE|ILIKE|>|<|>=|<=|IN|IS)", where_clause, re.IGNORECASE)
    return list(set(cols))


def _analyze_query(query: str) -> dict:
    """Analyzes the query and returns a diagnosis with recommendations."""
    table = _extract_table_name(query)
    where_cols = _extract_where_columns(query)
    issues: list[str] = []
    recommendations: list[dict] = []
    explain_statement = f"EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)\n{query.strip()};"

    # N+1 Detection (subquery inside IN SELECT)
    if _NESTED_SELECT_PATTERN.search(query):
        issues.append("N+1 detected: subquery inside IN(SELECT ...). Refactor to JOIN or CTE.")
        recommendations.append({
            "type": "REFACTOR",
            "severity": "HIGH",
            "message": "Replace IN(SELECT ...) with a JOIN or WITH clause (CTE). Expected reduction: 10x-100x in latency.",
        })

    # JSONB Operations without GIN index
    if _JSONB_PATTERN.search(query):
        issues.append("JSONB operation detected. GIN index required.")
        recommendations.append({
            "type": "INDEX",
            "severity": "HIGH",
            "index_type": "GIN",
            "sql": f"CREATE INDEX CONCURRENTLY idx_{table}_jsonb ON {table} USING GIN (jsonb_column);",
            "message": "Use GIN for ->> and Full-Text operations over JSONB.",
        })

    # Full-Text Search without GIN index
    if _FTS_PATTERN.search(query):
        issues.append("Full-Text Search detected. GIN index over tsvector required.")
        recommendations.append({
            "type": "INDEX",
            "severity": "HIGH",
            "index_type": "GIN",
            "sql": f"CREATE INDEX CONCURRENTLY idx_{table}_fts ON {table} USING GIN (to_tsvector('english', content_column));",
            "message": "FTS requires GIN index over pre-computed tsvector.",
        })

    # Columns in WHERE without potential index (B-Tree recommended)
    for col in where_cols:
        recommendations.append({
            "type": "INDEX",
            "severity": "MEDIUM",
            "index_type": "B-TREE",
            "sql": f"CREATE INDEX CONCURRENTLY idx_{table}_{col} ON {table} ({col});",
            "message": f"Column '{col}' in WHERE without apparent index. B-Tree recommended for equality/range.",
        })

    # Missing LIMIT on SELECT
    if not _LIMIT_PRESENT.search(query):
        issues.append("No LIMIT detected. Can cause full-table scan on tables >10k rows.")
        recommendations.append({
            "type": "QUERY_IMPROVEMENT",
            "severity": "MEDIUM",
            "message": "Add LIMIT for queries on large tables. BRIN can help for time-series tables.",
        })

    return {
        "table": table,
        "where_columns_detected": where_cols,
        "issues_found": len(issues),
        "issues": issues,
        "explain_statement": explain_statement,
        "recommendations": recommendations,
        "compliance": "PASS" if not any(r["severity"] == "HIGH" for r in recommendations) else "FAIL",
    }


def run(skill_input: SkillInput) -> SkillOutput:
    agent = skill_input.agent
    skill = skill_input.skill
    cid = skill_input.correlation_id

    query = skill_input.params.get("query")
    if not query:
        return SkillOutput.failure(agent, skill, "Param 'query' (SQL string) is required.", cid)

    analysis = _analyze_query(query)

    warnings: list[str] = []
    if analysis["compliance"] == "FAIL":
        warnings.append("HIGH severity performance vulnerabilities detected. Fix before production.")

    return SkillOutput(
        success=True,
        agent=agent,
        skill=skill,
        result=analysis,
        warnings=warnings,
        correlation_id=cid,
    )
