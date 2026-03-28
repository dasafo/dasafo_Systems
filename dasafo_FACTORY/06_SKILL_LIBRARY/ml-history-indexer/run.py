import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — ML History Indexer (MEMORY_OPTIMIZER)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Indexes historical ML experiments for semantic search and performance comparison.
"""

from __future__ import annotations
import os
import re
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Industrialized entry point: Physical ML Indexer."""
    agent = "MEMORY_OPTIMIZER"
    skill = "ml-history-indexer"
    cid = skill_input.correlation_id

    try:
        # 1. Resolve Path
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "Missing TARGET_PROJECT", cid)
        
        project_path = Path(target).resolve()
        log_file = project_path / "LOGS" / "ML_EXPERIMENT_LOG.md"
        
        # 2. Logic: Physical Scan
        if not log_file.exists():
             return SkillOutput.success(agent, skill, {"matched_experiments": [], "status": "NO_HISTORY", "industrial_verification": True}, cid)
        
        content = log_file.read_text(encoding="utf-8")
        
        # Naive regex parsing to find physical experiments logged by `ml-experiment-log`
        # Looks for lines like `- **Model ID:** v1.0`
        experiments = []
        model_matches = re.finditer(r"-\s\*\*Model\sID:\*\*\s(.*?)\n", content)
        for m in model_matches:
            experiments.append({"id": m.group(1).strip()})

        status = "INDEXED" if experiments else "EMPTY_LOG"

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "matched_experiments": experiments,
                "status": status,
                "industrial_verification": True
            },
            correlation_id=cid,
            artifacts=[str(log_file)]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"History Indexing Failed: {str(e)}", cid)
