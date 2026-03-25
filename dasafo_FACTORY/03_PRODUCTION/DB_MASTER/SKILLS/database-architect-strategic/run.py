"""
run.py — Skill: Database Architect Strategic
Agent: DB_MASTER

Decides between SQL, NoSQL, or Vector Store based on account project brief.
Returns a reasoned decision following the SKILL.md decision tree.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Add GLOBAL_KNOWLEDGE to path for skill_schema import
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "00_GLOBAL_KNOWLEDGE"))
from skill_schema import SkillInput, SkillOutput  # noqa: E402


def _evaluate_signals(brief: dict) -> dict:
    """
    Decision Tree: SQL vs NoSQL vs Vector.
    Based on project brief signals.
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
            "engine": "pgvector (inside Supabase/PostgreSQL)",
            "rationale": "Project requires semantic search or AI features. pgvector allows storing embeddings directly in Postgres without additional external services.",
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
                "Relational data and/or ACID transactions detected. "
                "PostgreSQL is the factory standard (Supabase). "
                + ("JSONB + GIN available for semi-structured fields." if needs_flexibility else "")
            ),
        }

    # NoSQL / Document Store
    if needs_flexibility and needs_scale and not needs_transactions:
        decision["nosql"] = {
            "recommended": True,
            "engine": "Supabase JSONB columns or Redis for caching",
            "rationale": (
                "Flexible schema + high write scale without strict ACID requirements. "
                "Prefer JSONB columns in Postgres to keep service count low, "
                "or Redis as L2 cache."
            ),
        }

    # Time Series
    if time_series:
        decision.setdefault("sql", {})
        decision["sql"]["time_series_note"] = (
            "For massive time-series data, consider date-range partitioning + BRIN indexes."
        )

    # Full-Text
    if needs_full_text:
        decision.setdefault("sql", {})
        decision["sql"]["fts_note"] = (
            "Full-Text Search via to_tsvector + GIN index. ElasticSearch not required if volume <10M docs."
        )

    # Default: if no clear signals
    if not decision:
        decision["sql"] = {
            "recommended": True,
            "engine": "PostgreSQL via Supabase",
            "rationale": "No special signals detected. PostgreSQL as minimum complexity option for the factory stack.",
        }

    return {
        "decision": decision,
        "primary_recommendation": _pick_primary(decision),
        "brief_analyzed": brief,
    }


def _pick_primary(decision: dict) -> str:
    """Selects primary store if multiple are recommended."""
    if "sql" in decision and "vector_store" in decision:
        return "PostgreSQL + pgvector (unified solution)"
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
                "Param 'brief' (dict) is required. Valid signals: "
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
