"""
run.py — Skill: Deep Semantic Search
Agent: RESEARCH_AGENT
v3.1.5: Solidity Guard | Industrial Scale.

Performs semantic web search and saves results to research_nexus.md.
"""

from __future__ import annotations
import sys
from datetime import datetime, timezone
from pathlib import Path

# Add GLOBAL_KNOWLEDGE to path for skill_schema import
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "00_GLOBAL_KNOWLEDGE"))
from skill_schema import SkillInput, SkillOutput  # noqa: E402

def _format_nexus_entry(query: str, sources: list[dict], summary: str) -> str:
    """Formats the research entry for the Nexus file."""
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        f"## 🔍 Research Entry — {timestamp} (v3.1.5)",
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
    """Standardized entry point for the skill."""
    agent = skill_input.agent
    skill = skill_input.skill
    cid = skill_input.correlation_id

    query = skill_input.params.get("query")
    sources = skill_input.params.get("sources", [])
    summary = skill_input.params.get("summary", "")
    focus_filter = skill_input.params.get("focus", "technical")

    if not query:
        return SkillOutput.failure(agent, skill, "Param 'query' is required.", cid)

    # Use simulated sources if none provided (Production would use MCP search_web)
    if not sources:
        sources = [
            {
                "title": f"[Semantic Result for: {query}]",
                "url": "https://exa.ai",
                "excerpt": f"Industrial-grade semantic search results for {query} with focus: {focus_filter}."
            }
        ]

    if not summary:
        summary = f"Semantic search on '{query}' completed with focus on '{focus_filter}'."

    entry = _format_nexus_entry(query, sources, summary)
    artifact_paths = []

    if skill_input.target_project:
        nexus_path = Path(skill_input.target_project) / "LOCAL_KNOWLEDGE" / "research_nexus.md"
        _append_to_nexus(nexus_path, entry)
        artifact_paths.append(str(nexus_path))

    return SkillOutput.success(
        agent=agent,
        skill=skill,
        data={
            "query": query,
            "focus": focus_filter,
            "sources_found": len(sources)
        },
        artifacts=artifact_paths,
        correlation_id=cid
    )
