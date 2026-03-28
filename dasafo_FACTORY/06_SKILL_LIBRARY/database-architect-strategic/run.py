import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Strategic Database Architect (DB_MASTER)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Generates SQL migrations and strategic data blueprints.
"""

from __future__ import annotations
import os
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def generate_blueprint(table_name: str, strategy: str) -> str:
    """Generates SQL content based on strategy."""
    if strategy == "vector":
        return f"""-- Vector Migration: {table_name}
CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE {table_name} (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    embedding vector(1536),
    content TEXT,
    metadata JSONB DEFAULT '{{}}'
);
CREATE INDEX ON {table_name} USING ivfflat (embedding vector_cosine_ops);
"""
    elif strategy == "document":
        return f"""-- Document Migration: {table_name}
CREATE TABLE {table_name} (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    data JSONB NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);
CREATE INDEX idx_{table_name}_data ON {table_name} USING GIN (data);
"""
    else: # Relational (Standard)
        return f"""-- Relational Migration: {table_name} | v3.2.0-S
CREATE TABLE {table_name} (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMPTZ DEFAULT now(),
    metadata JSONB DEFAULT '{{}}',
    project_id UUID
);
ALTER TABLE {table_name} ENABLE ROW LEVEL SECURITY;
"""

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    # Dynamic identity for industrial traceability
    agent = skill_input.agent or "DB_MASTER"
    skill = skill_input.skill or "database-architect-strategic"
    cid = skill_input.correlation_id

    try:
        # 1. Path Resolution
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "Mission Blocked: TARGET_PROJECT is missing.", cid)
        
        project_path = Path(target).resolve()
        table_name = skill_input.params.get("table", "new_table")
        strategy = skill_input.params.get("strategy", "relational").lower()
        
        # 2. Logic (Migration Generation)
        sql = generate_blueprint(table_name, strategy)

        # 3. Persistence
        # Aligning with LOCAL_KNOWLEDGE architecture defined in 02_THE_REGISTRY.md
        blueprint_dir = project_path / "LOCAL_KNOWLEDGE" / "architecture"
        blueprint_dir.mkdir(parents=True, exist_ok=True)
        
        sql_file = blueprint_dir / f"migration_{table_name}_{cid}.sql"
        sql_file.write_text(sql, encoding="utf-8")

        # 4. Success Return with artifacts for Solidity Guard
        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "sql_migration": sql,
                "blueprint_path": str(sql_file),
                "strategy_applied": strategy,
                "status": "STABLE"
            },
            correlation_id=cid,
            artifacts=[str(sql_file)]
        )

    except Exception as e:
        # Resilient Error Handling
        return SkillOutput.failure(agent, skill, f"Critical DB Architect Failure: {str(e)}", cid)