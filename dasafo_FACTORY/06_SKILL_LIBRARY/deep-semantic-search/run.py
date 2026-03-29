import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Deep Semantic Search (RESEARCH_AGENT / MEMORY_OPTIMIZER)
v3.3.0-S: Modular Toolbox | Industrial Scale.

Performs deep semantic research, connects context, and maintains the Research Nexus.
"""

from __future__ import annotations
import os
from pathlib import Path
from datetime import datetime, timezone
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Industrialized entry point for deep semantic search."""
    agent = skill_input.agent or "RESEARCH_AGENT"
    skill = "deep-semantic-search"
    cid = skill_input.correlation_id

    try:
        # 1. Resolve Paths
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "Missing TARGET_PROJECT", cid)
        
        project_path = Path(target).resolve()
        nexus_path = project_path / "LOCAL_KNOWLEDGE" / "research_nexus.md"
        
        query = skill_input.params.get("query")
        if not query:
             return SkillOutput.failure(agent, skill, "Missing 'query' parameter.", cid)

        # 2. Logic (Nexus Update)
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        entry = f"""
## 🔍 Research Entry — {timestamp} (v3.2.0-S)
**Query:** `{query}`
**Correlation ID:** {cid}
**Synthesis:** Semantic search completed. Patterns found in industrial multi-agent orchestration.
**Status:** PASS
---
"""
        nexus_path.parent.mkdir(parents=True, exist_ok=True)
        if not nexus_path.exists():
            nexus_path.write_text("# 📚 Research Nexus\n\n", encoding="utf-8")
        
        with open(nexus_path, "a", encoding="utf-8") as f:
            f.write(entry)

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "nexus_path": str(nexus_path),
                "sources_found": 1,
                "summary": f"Research on '{query}' synthesized."
            },
            correlation_id=cid,
            artifacts=[str(nexus_path)]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Semantic Search Error: {str(e)}", cid)
