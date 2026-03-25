"""
run.py — AutoShield Feedback Writer (QA_TESTER)
Automated entry of detected errors into the collective memory (v2.1).
"""

from skill_schema import SkillInput, SkillOutput
from pathlib import Path
import os

def run(skill_input: SkillInput) -> SkillOutput:
    """
    Appends a new YAML entry to the global FEEDBACK-LOG.md.
    """
    error_id = skill_input.params.get("id", "FB-NEW")
    pattern = skill_input.params.get("pattern", "Unknown issue detected.")
    severity = skill_input.params.get("severity", "medium")
    agent = skill_input.params.get("affected_agent", "NONE")
    
    # Resolve FEEDBACK-LOG.md path
    # 04_COMPLIANCE_AND_QUALITY/QA_TESTER/SKILLS/autoshield-feedback-writer/run.py -> dasafo_FACTORY/
    factory_root = Path(__file__).resolve().parent.parent.parent.parent.parent
    feedback_log_path = factory_root / "FEEDBACK-LOG.md"
    
    if not feedback_log_path.exists():
        return SkillOutput.failure(
            agent=skill_input.agent,
            skill=skill_input.skill,
            error="FEEDBACK-LOG.md not found in factory root.",
            correlation_id=skill_input.correlation_id
        )
    
    entry = f"\n### [{error_id}] {pattern}\n"
    entry += "```yaml\n"
    entry += f"id: {error_id}\n"
    entry += f"severity: {severity}\n"
    entry += f"pattern: \"{pattern}\"\n"
    entry += f"affected_agents: [\"{agent}\"]\n"
    entry += "categories: [\"testing\", \"quality\"]\n"
    entry += "```\n"
    
    with open(feedback_log_path, "a", encoding="utf-8") as f:
        f.write(entry)
        
    return SkillOutput.success(
        agent=skill_input.agent,
        skill=skill_input.skill,
        data={"message": f"Feedback entry {error_id} recorded successfully."},
        correlation_id=skill_input.correlation_id
    )
