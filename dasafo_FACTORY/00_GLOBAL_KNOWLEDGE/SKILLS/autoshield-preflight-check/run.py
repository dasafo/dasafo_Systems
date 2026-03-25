"""
run.py — AutoShield Preflight Check
Universal pre-execution skill to inject collective memory into agent context.
"""

import os
import re
import yaml
from pathlib import Path
from typing import Any, Dict, List

# Standard input/output schema for factory skills
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """
    Parses FEEDBACK-LOG.md and returns relevant golden rules for the current agent.
    """
    agent_id = skill_input.agent.lower()
    
    # Resolve FEEDBACK-LOG.md path (3 levels up from this run.py)
    # 00_GLOBAL_KNOWLEDGE/SKILLS/autoshield-preflight-check/run.py -> dasafo_FACTORY/
    factory_root = Path(__file__).resolve().parent.parent.parent.parent
    feedback_log_path = factory_root / "FEEDBACK-LOG.md"
    
    if not feedback_log_path.exists():
        return SkillOutput.success(
            agent=skill_input.agent,
            skill=skill_input.skill,
            data={"rules": [], "message": "No FEEDBACK-LOG.md found. Proceeding with clean slate."},
            correlation_id=skill_input.correlation_id
        )

    try:
        content = feedback_log_path.read_text(encoding="utf-8")
        
        # Extract YAML blocks: ```yaml ... ```
        yaml_blocks = re.findall(r"```yaml\n(.*?)\n```", content, re.DOTALL)
        
        relevant_rules = []
        for block in yaml_blocks:
            try:
                data = yaml.safe_load(block)
                if not data: continue
                
                # Filtering logic
                is_affected = agent_id in [a.lower() for a in data.get("affected_agents", [])]
                is_critical = data.get("severity", "").lower() in ["critical", "high"]
                
                if is_affected or is_critical:
                    rule_id = data.get("id", "FB-UNKNOWN")
                    rule_text = data.get("pattern", "No pattern description found.")
                    severity = data.get("severity", "medium").upper()
                    relevant_rules.append(f"[{rule_id}] {severity} — \"{rule_text}\"")
            
            except Exception:
                continue # Skip malformed YAML blocks

        # Format output
        if not relevant_rules:
            output_msg = "No specific rules found for this agent. Follow standard protocols."
        else:
            header = "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n🛡️ AUTOSHIELD PREFLIGHT ACTIVE\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            footer = f"\nTotal rules loaded: {len(relevant_rules)}\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            output_msg = header + "The following rules MUST be respected:\n\n" + "\n".join(relevant_rules) + footer

        return SkillOutput.success(
            agent=skill_input.agent,
            skill=skill_input.skill,
            data={
                "rules": relevant_rules,
                "formatted_output": output_msg
            },
            correlation_id=skill_input.correlation_id
        )

    except Exception as e:
        return SkillOutput.failure(
            agent=skill_input.agent,
            skill=skill_input.skill,
            error=f"Error parsing FEEDBACK-LOG: {str(e)}",
            correlation_id=skill_input.correlation_id
        )
