"""
run.py — Database Architect Strategic (DB_MASTER)
Blueprint generator for relational schemas and migrations.
v3.1: Infraestructura Blindada | Industrial Scale.
"""

import os
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """
    Generates a SQL migration or schema blueprint.
    """
    target_project = skill_input.target_project or os.environ.get("TARGET_PROJECT", ".")
    project_path = Path(target_project).resolve()
    
    table_name = skill_input.params.get("table", "new_table")
    
    sql = f"-- Migration: Create {table_name}\n"
    sql += f"CREATE TABLE {table_name} (\n"
    sql += f"    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),\n"
    sql += f"    created_at TIMESTAMPTZ DEFAULT now(),\n"
    sql += f"    vibe_level INT CHECK (vibe_level BETWEEN 0 AND 10),\n"
    sql += f"    project_id UUID REFERENCES projects(id)\n"
    sql += f");\n\n"
    sql += f"ALTER TABLE {table_name} ENABLE ROW LEVEL SECURITY;\n"
    
    return SkillOutput.success(
        agent=skill_input.agent,
        skill=skill_input.skill,
        data={"sql_migration": sql, "target": str(project_path)},
        correlation_id=skill_input.correlation_id
    )
