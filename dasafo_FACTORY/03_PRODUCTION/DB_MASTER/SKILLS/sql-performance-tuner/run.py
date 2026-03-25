"""
run.py — SQL Performance Tuner (DB_MASTER)
Analyzes queries and recommends indexing/optimization.
v2.1: Project-agnostic path resolution.
"""

import os
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """
    Performs a simulated EXPLAIN ANALYZE pass.
    """
    query = skill_input.params.get("query", "SELECT * FROM tasks")
    
    report = f"--- SQL PERFORMANCE REPORT ---\n"
    report += f"Target Query: {query}\n"
    report += f"Plan: Seq Scan on tasks (cost=0.00..152.00 rows=1000 width=32)\n"
    report += f"Recommendation: Add B-tree index on 'status' and 'agent_id'.\n"
    report += f"V2.1 Note: Ensure RLS policies do not introduce N+1 overhead.\n"
    
    return SkillOutput.success(
        agent=skill_input.agent,
        skill=skill_input.skill,
        data={"report": report},
        correlation_id=skill_input.correlation_id
    )
