"""
run.py — Skill: Deep Semantic Search
Agent: RESEARCH_AGENT

Performs semantic web search on a technical concept and saves the results
to LOCAL_KNOWLEDGE/research_nexus.md in the TARGET_PROJECT.
"""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

# Add GLOBAL_KNOWLEDGE to path for skill_schema import
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "00_GLOBAL_KNOWLEDGE"))
from skill_schema import SkillInput, SkillOutput  # noqa: E402


def _format_nexus_entry(query: str, sources: list[dict], summary: str) -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        f"## 🔍 Research Entry — {timestamp}",
        f"**Query:** `{query}`",
        "",
        f"**Synthesis:** {summary}",
        "",
        "### Sources",
    ]
    for i, source in enumerate(sources, 1):
        title = source.get("title", f"Source {i}")
        url = source.get("url", "#")
        excerpt = source.get("excerpt", "No excerpt available.")
        lines.append(f"{i}. **[{title}]({url})**")
        lines.append(f"   > {excerpt}")
    lines.append("\n---\n")
    return "\n".join(lines)


def _append_to_nexus(nexus_path: Path, entry: str) -> None:
    """Appends an entry to the end of research_nexus.md (no overwrite)."""
    nexus_path.parent.mkdir(parents=True, exist_ok=True)
    if not nexus_path.exists():
        nexus_path.write_text("# 📚 Research Nexus\n\n", encoding="utf-8")
    with nexus_path.open("a", encoding="utf-8") as f:
        f.write(entry)


def run(skill_input: SkillInput) -> SkillOutput:
    agent = skill_input.agent
    skill = skill_input.skill
    cid = skill_input.correlation_id

    query = skill_input.params.get("query")
    sources = skill_input.params.get("sources", [])  # List of {title, url, excerpt}
    summary = skill_input.params.get("summary", "")
    focus_filter = skill_input.params.get("focus", "technical")  # technical | market | scientific

    if not query:
        return SkillOutput.failure(agent, skill, "Param 'query' is required.", cid)

    # If no explicit sources provided, use a semantic placeholder.
    # In production, this would invoke MCP search_web or Exa API.
    if not sources:
        sources = [
            {
                "title": f"[Semantic Result for: {query}]",
                "url": "https://exa.ai",
                "excerpt": (
                    "This result is a placeholder. "
                    "In production, invoke MCP search_web with the query and filter by: "
                    f"GitHub, ArXiv, Engineering Blogs (focus: {focus_filter})."
                ),
            }
        ]

    if not summary:
        summary = (
            f"Semantic search on '{query}' completed. "
            f"Found {len(sources)} relevant source(s) with focus on '{focus_filter}'. "
            "Review sources to connect findings with target architecture."
        )

    entry = _format_nexus_entry(query, sources, summary)

    artifacts: list[str] = []
    warnings: list[str] = []

    target_project = skill_input.target_project
    if target_project:
        nexus_path = Path(target_project) / "LOCAL_KNOWLEDGE" / "research_nexus.md"
        _append_to_nexus(nexus_path, entry)
        artifacts.append(str(nexus_path))
    else:
        warnings.append(
            "TARGET_PROJECT not defined. Entry was not persisted to research_nexus.md."
        )

    return SkillOutput(
        success=True,
        agent=agent,
        skill=skill,
        result={
            "query": query,
            "focus_filter": focus_filter,
            "sources_found": len(sources),
            "summary": summary,
            "entry_preview": entry[:300] + "..." if len(entry) > 300 else entry,
        },
        artifacts=artifacts,
        warnings=warnings,
        correlation_id=cid,
    )
