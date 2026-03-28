import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Autonomous Feedback Analyzer (FACTORY_EVOLVER)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Analyzes the FEEDBACK-LOG.md to identify recurring failure patterns.
"""

from __future__ import annotations
import os
import re
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def extract_failure_patterns(log_content: str):
    """Uses regex to identify recurring error IDs and agents in the log."""
    pattern = re.compile(r"### \[(?P<id>FB-\d+)\] (?P<pattern>.*)\n```yaml\n.*?affected_agents: \[(?P<agents>.*?)\]", re.DOTALL)
    matches = pattern.finditer(log_content)
    
    analysis = []
    for match in matches:
        analysis.append({
            "id": match.group("id"),
            "pattern": match.group("pattern").strip(),
            "agents": [a.strip().strip('"') for a in match.group("agents").split(",")]
        })
    return analysis

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    agent = "FACTORY_EVOLVER"
    skill = "autonomous-feedback-analyzer"
    cid = skill_input.correlation_id

    try:
        # 1. Path Resolution
        target = skill_input.params.get("log_path") or os.environ.get("TARGET_PROJECT")
        factory_root = Path(__file__).resolve().parents[4]
        
        feedback_log = None
        if target:
            possible_path = Path(target).resolve() / "FEEDBACK-LOG.md"
            if possible_path.exists():
                feedback_log = possible_path

        if not feedback_log:
            # Search in factory hierarchy
            search_paths = [
                factory_root / "FEEDBACK-LOG.md",
                factory_root / "dasafo_FACTORY" / "FEEDBACK-LOG.md"
            ]
            for p in search_paths:
                if p.exists():
                    feedback_log = p
                    break

        if not feedback_log:
             return SkillOutput.success(
                agent=agent,
                skill=skill,
                result={"status": "PASS", "message": "No FEEDBACK-LOG.md found."},
                correlation_id=cid,
                artifacts=[]
            )

        # 2. Execution
        content = feedback_log.read_text(encoding="utf-8")
        patterns = extract_failure_patterns(content)
        
        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "status": "PASS" if not patterns else "EVOLUTION_REQUIRED",
                "patterns_discovered": len(patterns),
                "analysis": patterns
            },
            correlation_id=cid,
            artifacts=[]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Feedback Analysis Failed: {str(e)}", cid)
