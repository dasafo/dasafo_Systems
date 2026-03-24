"""
run.py — Skill: SQL Performance Tuner
Agent: DB_MASTER

Analiza una query SQL, genera el EXPLAIN ANALYZE equivalente y
devuelve recomendaciones de índices según las reglas del SKILL.md.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "00_GLOBAL_KNOWLEDGE"))
from skill_schema import SkillInput, SkillOutput  # noqa: E402


# ── Patrones de detección ────────────────────────────────────────────────────

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
    """Analiza la query y devuelve un diagnóstico con recomendaciones."""
    table = _extract_table_name(query)
    where_cols = _extract_where_columns(query)
    issues: list[str] = []
    recommendations: list[dict] = []
    explain_statement = f"EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)\n{query.strip()};"

    # Detección de N+1 (subquery IN SELECT)
    if _NESTED_SELECT_PATTERN.search(query):
        issues.append("N+1 detectado: subquery dentro de IN(SELECT ...). Refactorizar a JOIN o CTE.")
        recommendations.append({
            "type": "REFACTOR",
            "severity": "HIGH",
            "message": "Reemplazar IN(SELECT ...) con un JOIN o WITH clause (CTE). Reducción esperada: 10x-100x en latencia.",
        })

    # Detección de JSONB sin índice GIN
    if _JSONB_PATTERN.search(query):
        issues.append("Operación JSONB detectada. Se requiere índice GIN.")
        recommendations.append({
            "type": "INDEX",
            "severity": "HIGH",
            "index_type": "GIN",
            "sql": f"CREATE INDEX CONCURRENTLY idx_{table}_jsonb ON {table} USING GIN (jsonb_column);",
            "message": "Usar GIN para operaciones ->> y Full-Text sobre JSONB.",
        })

    # Detección de Full-Text Search sin índice GIN
    if _FTS_PATTERN.search(query):
        issues.append("Full-Text Search detectado. Se requiere índice GIN sobre tsvector.")
        recommendations.append({
            "type": "INDEX",
            "severity": "HIGH",
            "index_type": "GIN",
            "sql": f"CREATE INDEX CONCURRENTLY idx_{table}_fts ON {table} USING GIN (to_tsvector('spanish', content_column));",
            "message": "FTS requiere índice GIN sobre tsvector pre-computado.",
        })

    # Detección de columnas en WHERE sin índice (B-Tree recomendado)
    for col in where_cols:
        recommendations.append({
            "type": "INDEX",
            "severity": "MEDIUM",
            "index_type": "B-TREE",
            "sql": f"CREATE INDEX CONCURRENTLY idx_{table}_{col} ON {table} ({col});",
            "message": f"Columna '{col}' en WHERE sin índice aparente. B-Tree para igualdad/rango.",
        })

    # Sin LIMIT en SELECT
    if not _LIMIT_PRESENT.search(query):
        issues.append("No se detecta LIMIT. En tablas >10k filas puede causar full-table scan.")
        recommendations.append({
            "type": "QUERY_IMPROVEMENT",
            "severity": "MEDIUM",
            "message": "Añadir LIMIT para consultas sobre tablas grandes. BRIN puede ayudar en tablas time-series.",
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
        return SkillOutput.failure(agent, skill, "Param 'query' (SQL string) es requerido.", cid)

    analysis = _analyze_query(query)

    warnings: list[str] = []
    if analysis["compliance"] == "FAIL":
        warnings.append("Se detectaron vulnerabilidades de rendimiento de severidad HIGH. Corregir antes de producción.")

    return SkillOutput(
        success=True,
        agent=agent,
        skill=skill,
        result=analysis,
        warnings=warnings,
        correlation_id=cid,
    )
