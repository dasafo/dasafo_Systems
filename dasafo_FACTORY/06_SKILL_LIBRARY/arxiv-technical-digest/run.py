"""
run.py — ArXiv Technical Digest (RESEARCH_AGENT)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Fetches and digests technical papers from ArXiv via API.
"""

from __future__ import annotations
import os
import requests
import xml.etree.ElementTree as ET
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def fetch_arxiv_metadata(arxiv_id: str):
    """Fetches paper metadata from ArXiv."""
    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        namespace = {'atom': 'http://www.w3.org/2005/Atom'}
        entry = root.find('atom:entry', namespace)
        if entry is None:
            return None
        title = entry.find('atom:title', namespace).text.strip()
        summary = entry.find('atom:summary', namespace).text.strip()
        return {"title": title, "summary": summary}
    except Exception as e:
        return {"error": str(e)}

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    agent = "RESEARCH_AGENT"
    skill = "arxiv-technical-digest"
    cid = skill_input.correlation_id

    try:
        # 1. Input Resolution
        arxiv_id = skill_input.params.get("id", "2301.00001")
        target = skill_input.params.get("target_project") or skill_input.target_project or os.environ.get("TARGET_PROJECT")
        
        # 2. Execution
        metadata = fetch_arxiv_metadata(arxiv_id)
        
        if not metadata or "error" in metadata:
            error_msg = metadata.get("error", "Paper not found.")
            return SkillOutput.failure(agent, skill, f"ArXiv Fetch Error: {error_msg}", cid)
        
        digest = f"# 🧠 ArXiv Digest: {metadata['title']} (v3.2.0-S)\n"
        digest += f"**ID:** {arxiv_id} | **Status:** SOLIDIFIED\n\n"
        digest += f"## Abstract\n{metadata['summary']}\n"
        
        artifacts = []
        output_path = None
        
        if target:
            project_path = Path(target).resolve()
            output_dir = project_path / "LOCAL_KNOWLEDGE" / "research"
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path = output_dir / f"Digest-{arxiv_id}.md"
            output_path.write_text(digest, encoding="utf-8")
            artifacts.append(str(output_path))

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "digest": digest,
                "metadata": metadata,
                "path": str(output_path) if output_path else None
            },
            correlation_id=cid,
            artifacts=artifacts
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Critical ArXiv Failure: {str(e)}", cid)
