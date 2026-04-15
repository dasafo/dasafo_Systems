# dasafo_FACTORY/06_SKILL_LIBRARY/arxiv-technical-digest/logic.py
import os
import time
import json
from pathlib import Path
from datetime import datetime

# Logic based on: https://skills.sh/jezweb/claude-skills/arxiv-digest

def execute_digest(
    target_project: str, 
    query: str, 
    max_results: int = 5, 
    overwrite: bool = False
) -> tuple[dict, list]:
    """Pure logic for fetching and digesting ArXiv papers (v5.0-MCP)."""
    start_time = time.time()
    
    # Requirement: arxiv library must be installed
    import arxiv 

    project_path = Path(target_project).resolve()
    storage_dir = project_path / "LOCAL_KNOWLEDGE" / "research"
    storage_dir.mkdir(parents=True, exist_ok=True)

    # Execution
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )

    digest_data = []
    for result in search.results():
        digest_data.append({
            "title": result.title,
            "summary": result.summary,
            "pdf_url": result.pdf_url,
            "published": result.published.isoformat(),
            "authors": [author.name for author in result.authors]
        })

    # DAST Sovereignty: Save physical evidence
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"digest_{timestamp}.json"
    output_path = storage_dir / file_name

    if output_path.exists() and not overwrite:
        raise FileExistsError(f"REDUNDANCY LOCK: {file_name} already exists.")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(digest_data, f, indent=2, ensure_ascii=False)

    execution_duration_s = time.time() - start_time
    
    result_payload = {
        "industrial_status": "KNOWLEDGE_DIGESTED",
        "papers_found": len(digest_data),
        "storage_path": str(output_path),
        "execution_duration_seconds": round(execution_duration_s, 4)
    }

    return result_payload, [str(output_path)]