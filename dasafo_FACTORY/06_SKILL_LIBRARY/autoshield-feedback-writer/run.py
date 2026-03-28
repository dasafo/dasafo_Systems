import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — AutoShield Feedback Writer (QA_TESTER)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Automated entry of detected errors into the collective memory.
"""

from __future__ import annotations
import os
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    agent = "QA_TESTER"
    skill = "autoshield-feedback-writer"
    cid = skill_input.correlation_id

    try:
        # 1. Input Extraction
        error_id = skill_input.params.get("id", "FB-NEW")
        pattern = skill_input.params.get("pattern", "Unknown issue detected.")
        severity = skill_input.params.get("severity", "medium")
        affected_agent = skill_input.params.get("affected_agent", "UNKNOWN")
        golden_rule = skill_input.params.get("golden_rule", "Follow system standards.")
        
        # 2. Path Resolution
        factory_root = Path(__file__).resolve().parents[4]
        feedback_log_path = factory_root / "FEEDBACK-LOG.md"
        
        if not feedback_log_path.exists():
            feedback_log_path = factory_root / "dasafo_FACTORY" / "FEEDBACK-LOG.md"

        if not feedback_log_path.exists():
             return SkillOutput.failure(agent, skill, "FEEDBACK-LOG.md not found in factory root.", cid)
        
        # 3. Entry Formatting
        entry = f"\n### [{error_id}] {pattern} (v3.2.0-S)\n"
        entry += "```yaml\n"
        entry += f"id: {error_id}\n"
        entry += f"severity: {severity}\n"
        entry += f"pattern: \"{pattern}\"\n"
        entry += f"golden_rule: \"{golden_rule}\"\n"
        entry += f"affected_agents: [\"{affected_agent}\"]\n"
        entry += f"validated_standard: \"v3.2.0-S\"\n"
        entry += "```\n"
        
        # 4. Persistence
        with open(feedback_log_path, "a", encoding="utf-8") as f:
            f.write(entry)
            
        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "message": f"Feedback entry {error_id} recorded.",
                "path": str(feedback_log_path)
            },
            correlation_id=cid,
            artifacts=[str(feedback_log_path)]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Feedback Recording Failed: {str(e)}", cid)
