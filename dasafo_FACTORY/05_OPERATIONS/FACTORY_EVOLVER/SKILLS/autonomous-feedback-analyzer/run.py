"""
run.py — Autonomous Feedback Analyzer (FACTORY_EVOLVER)
v3.1.5: Solidity Guard | Industrial Scale.

Analyzes the FEEDBACK-LOG.md to identify recurring failure patterns.
"""

from __future__ import annotations
import sys
import re
from pathlib import Path

# Add factory knowledge to path
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "00_GLOBAL_KNOWLEDGE"))
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
    # Resolve FEEDBACK-LOG.md path
    factory_root = Path(__file__).resolve().parents[4]
    feedback_log = factory_root / "FEEDBACK-LOG.md"
    
    if not feedback_log.exists():
        # Fallback check
        feedback_log = factory_root / "dasafo_FACTORY" / "FEEDBACK-LOG.md"

    if not feedback_log.exists():
        return SkillOutput.success(
            agent=skill_input.agent,
            skill=skill_input.skill,
            data={"status": "EMPTY", "message": "No FEEDBACK-LOG.md found. Evolution pulse is stable."},
            correlation_id=skill_input.correlation_id
        )

    try:
        content = feedback_log.read_text(encoding="utf-8")
        patterns = extract_failure_patterns(content)
        
        return SkillOutput.success(
            agent=skill_input.agent,
            skill=skill_input.skill,
            data={
                "status": "PASS",
                "patterns_discovered": len(patterns),
                "analysis": patterns
            },
            correlation_id=skill_input.correlation_id
        )
    except Exception as e:
        return SkillOutput.failure(skill_input.agent, skill_input.skill, f"Analysis Error: {str(e)}", skill_input.correlation_id)
