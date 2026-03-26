"""
run.py — AutoShield Feedback Writer (QA_TESTER)
v3.1.5: Solidity Guard | Industrial Scale.

Automated entry of detected errors into the collective memory.
"""

import sys
import os
from pathlib import Path

# Add factory knowledge to path
sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "00_GLOBAL_KNOWLEDGE"))
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """
    Appends a new YAML entry to the global FEEDBACK-LOG.md.
    """
    error_id = skill_input.params.get("id", "FB-NEW")
    pattern = skill_input.params.get("pattern", "Unknown issue detected.")
    severity = skill_input.params.get("severity", "medium")
    agent = skill_input.params.get("affected_agent", "NONE")
    
    # Resolve FEEDBACK-LOG.md path
    factory_root = Path(__file__).resolve().parents[5]
    feedback_log_path = factory_root / "dasafo_FACTORY" / "FEEDBACK-LOG.md"
    
    if not feedback_log_path.exists():
         # Fallback search if department structure differs
         feedback_log_path = factory_root / "FEEDBACK-LOG.md"
         if not feedback_log_path.exists():
            return SkillOutput.failure(
                agent=skill_input.agent,
                skill=skill_input.skill,
                error="FEEDBACK-LOG.md not found in factory root.",
                correlation_id=skill_input.correlation_id
            )
    
    entry = f"\n### [{error_id}] {pattern} (v3.1.5)\n"
    entry += "```yaml\n"
    entry += f"id: {error_id}\n"
    entry += f"severity: {severity}\n"
    entry += f"pattern: \"{pattern}\"\n"
    entry += f"affected_agents: [\"{agent}\"]\n"
    entry += f"validated_standard: \"v3.1.5\"\n"
    entry += "```\n"
    
    with open(feedback_log_path, "a", encoding="utf-8") as f:
        f.write(entry)
        
    return SkillOutput.success(
        agent=skill_input.agent,
        skill=skill_input.skill,
        data={"message": f"Feedback entry {error_id} recorded in {feedback_log_path.name}"},
        correlation_id=skill_input.correlation_id
    )
