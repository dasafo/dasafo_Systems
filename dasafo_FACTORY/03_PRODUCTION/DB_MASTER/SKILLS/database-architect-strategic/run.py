"""
run.py — Skill: Database Architect Strategic
Agent: DB_MASTER

Decide entre SQL, NoSQL o Vector Store según el brief del proyecto.
Devuelve una decisión razonada con el árbol de decisión del SKILL.md.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "00_GLOBAL_KNOWLEDGE"))
from skill_schema import SkillInput, SkillOutput  # noqa: E402


def _evaluate_signals(brief: dict) -> dict:
    """
    Árbol de decisión: SQL vs NoSQL vs Vector.
    Basado en señales del brief del proyecto.
    """
    needs_relations = brief.get("relational_data", False)
    needs_transactions = brief.get("acid_transactions", False)
    needs_full_text = brief.get("full_text_search", False)
    needs_embeddings = brief.get("semantic_search", False) or brief.get("ai_features", False)
    needs_flexibility = brief.get("schema_flexibility", False)
    needs_scale = brief.get("high_write_scale", False)
    time_series = brief.get("time_series", False)

    decision: dict = {}

    # Vector Store
    if needs_embeddings:
        decision["vector_store"] = {
            "recommended": True,
            "engine": "pgvector (dentro de Supabase/PostgreSQL)",
            "rationale": "El proyecto requiere búsqueda semántica o features de IA. pgvector permite almacenar embeddings directamente en Postgres sin servicio externo adicional.",
            "setup_sql": (
                "CREATE EXTENSION IF NOT EXISTS vector;\n"
                "CREATE TABLE embeddings (id BIGSERIAL PRIMARY KEY, content TEXT, embedding VECTOR(1536));\n"
                "CREATE INDEX ON embeddings USING ivfflat (embedding vector_cosine_ops);"
            ),
        }

    # SQL (PostgreSQL/Supabase)
    if needs_relations or needs_transactions:
        decision["sql"] = {
            "recommended": True,
            "engine": "PostgreSQL via Supabase",
            "rationale": (
                "Datos relacionales y/o transacciones ACID detectadas. "
                "PostgreSQL es la opción estándar de la factory (Supabase). "
                + ("JSONB + GIN disponible para campos semi-estructurados." if needs_flexibility else "")
            ),
        }

    # NoSQL / Document Store
    if needs_flexibility and needs_scale and not needs_transactions:
        decision["nosql"] = {
            "recommended": True,
            "engine": "Supabase JSONB columns o Redis para caché",
            "rationale": (
                "Esquema flexible + alta carga de escrituras sin necesidad de ACID estricto. "
                "Usar columnas JSONB en Postgres (preferido para mantener un solo servicio) "
                "o Redis como caché L2."
            ),
        }

    # Time Series
    if time_series:
        decision.setdefault("sql", {})
        decision["sql"]["time_series_note"] = (
            "Para series temporales masivas, considerar particionado por rango de fechas + índices BRIN."
        )

    # Full-Text
    if needs_full_text:
        decision.setdefault("sql", {})
        decision["sql"]["fts_note"] = (
            "Full-Text Search con to_tsvector + índice GIN. No requiere ElasticSearch si el volumen <10M docs."
        )

    # Default: si no hay señales claras
    if not decision:
        decision["sql"] = {
            "recommended": True,
            "engine": "PostgreSQL via Supabase",
            "rationale": "Sin señales especiales detectadas. PostgreSQL como opción de mínima complejidad para el stack de la factory.",
        }

    return {
        "decision": decision,
        "primary_recommendation": _pick_primary(decision),
        "brief_analyzed": brief,
    }


def _pick_primary(decision: dict) -> str:
    """Elige el store principal si hay múltiples recomendados."""
    if "sql" in decision and "vector_store" in decision:
        return "PostgreSQL + pgvector (solución unificada)"
    if "vector_store" in decision:
        return "Vector Store (pgvector)"
    if "sql" in decision:
        return "PostgreSQL (Supabase)"
    if "nosql" in decision:
        return "NoSQL / JSONB / Redis"
    return "PostgreSQL (default)"


def run(skill_input: SkillInput) -> SkillOutput:
    agent = skill_input.agent
    skill = skill_input.skill
    cid = skill_input.correlation_id

    brief = skill_input.params.get("brief")
    if not brief or not isinstance(brief, dict):
        return SkillOutput.failure(
            agent, skill,
            (
                "Param 'brief' (dict) es requerido. Señales válidas: "
                "relational_data, acid_transactions, full_text_search, semantic_search, "
                "schema_flexibility, high_write_scale, time_series, ai_features."
            ),
            cid,
        )

    result = _evaluate_signals(brief)

    return SkillOutput(
        success=True,
        agent=agent,
        skill=skill,
        result=result,
        correlation_id=cid,
    )
