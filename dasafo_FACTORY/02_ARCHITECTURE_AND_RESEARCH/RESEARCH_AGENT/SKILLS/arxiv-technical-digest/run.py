"""
run.py — ArXiv Technical Digest (RESEARCH_AGENT)
v3.1.5: Solidity Guard | Industrial Scale.

Fetches and digests technical papers from ArXiv via API.
"""

from __future__ import annotations
import sys
import os
import requests
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

# Add factory knowledge to path
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "00_GLOBAL_KNOWLEDGE"))
from skill_schema import SkillInput, SkillOutput

def fetch_arxiv_metadata(arxiv_id: str):
    """Fetches paper metadata from ArXiv."""
    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        # XML parsing for Atom feed
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
    arxiv_id = skill_input.params.get("id", "2301.00001")
    target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
    
    metadata = fetch_arxiv_metadata(arxiv_id)
    
    if not metadata or "error" in metadata:
        error_msg = metadata.get("error", "Paper not found.")
        return SkillOutput.failure(
            agent=skill_input.agent,
            skill=skill_input.skill,
            error=f"ArXiv Fetch Error: {error_msg}",
            correlation_id=skill_input.correlation_id
        )
    
    digest = f"# 🧠 ArXiv Digest: {metadata['title']} (v3.1.5)\n"
    digest += f"**ID:** {arxiv_id} | **Status:** SOLIDIFIED\n\n"
    digest += f"## Abstract\n{metadata['summary']}\n"
    
    artifact_paths = []
    if target:
        output_path = Path(target) / "LOCAL_KNOWLEDGE" / f"Digest-{arxiv_id}.md"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(digest, encoding="utf-8")
        artifact_paths.append(str(output_path))

    return SkillOutput.success(
        agent=skill_input.agent,
        skill=skill_input.skill,
        data={"digest": digest, "metadata": metadata},
        artifacts=artifact_paths,
        correlation_id=skill_input.correlation_id
    )
