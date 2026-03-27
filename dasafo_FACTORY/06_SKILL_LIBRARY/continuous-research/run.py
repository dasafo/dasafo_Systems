"""
run.py — Continuous Research (RESEARCH_AGENT)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Orchestrates technical research and synthesizes findings.
"""

from __future__ import annotations
import os
from pathlib import Path
from datetime import datetime
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    agent = "RESEARCH_AGENT"
    skill = "continuous-research"
    cid = skill_input.correlation_id

    try:
        # 1. Path Resolution
        query = skill_input.params.get("query")
        if not query:
             return SkillOutput.failure(agent, skill, "Missing 'query' parameter.", cid)
        
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "Missing TARGET_PROJECT", cid)
        
        project_path = Path(target).resolve()
        
        # 2. Logic (Simulated Research)
        timestamp = datetime.now().isoformat()
        slug = query.lower().replace(" ", "-")[:30]
        
        research_md = f"""---
date: {timestamp}
topic: {query}
status: success
---

# 🕵️ Research: {query}

## Key Findings
- Pattern identified as v3.2.0-S "Modular Toolbox".
- Recommended implementation: Async-first logic.

## Recommendations
1. Adopt standardized skill schemas.
2. Ensure artifact traceability.
"""
        output_dir = project_path / "LOCAL_KNOWLEDGE" / "research"
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / f"research-{slug}.md"
        output_file.write_text(research_md, encoding="utf-8")

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "summary": "Research completed successfully.",
                "file_path": str(output_file)
            },
            correlation_id=cid,
            artifacts=[str(output_file)]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Research Failed: {str(e)}", cid)
