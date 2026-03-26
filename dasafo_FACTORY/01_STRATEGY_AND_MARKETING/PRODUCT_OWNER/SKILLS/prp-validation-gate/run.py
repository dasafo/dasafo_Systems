"""
run.py — Skill: PRP Validation Gate
Agent: PRODUCT_OWNER
v3.1.5: Solidity Guard | Industrial Scale.

Validates the integrity and signing status of the PRP contract.
"""

from __future__ import annotations
import sys
import json
import os
from pathlib import Path

# Add factory knowledge to path
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "00_GLOBAL_KNOWLEDGE"))
from skill_schema import SkillInput, SkillOutput

def validate_prp_integrity(prp_data: dict):
    """Performs industrial validation pass on the contract."""
    required_keys = {"mission_id", "project_name", "governance", "signing"}
    missing = required_keys - set(prp_data.keys())
    
    if missing:
        return False, f"Missing critical contract sections: {missing}"
    
    if prp_data.get("governance") != "Dasafo Factory v3.1.5 Solidity Guard":
        return False, f"Legacy Governance detected: {prp_data.get('governance')}. Required: v3.1.5."
    
    return True, "PRP Integrity Verified."

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
    
    if not target:
        return SkillOutput.failure(skill_input.agent, skill_input.skill, "No TARGET_PROJECT set.", skill_input.correlation_id)

    contract_path = Path(target) / "PRP_CONTRACT.json"
    if not contract_path.exists():
         return SkillOutput.failure(skill_input.agent, skill_input.skill, "PRP_CONTRACT.json not found.", skill_input.correlation_id)

    try:
        with open(contract_path, 'r', encoding="utf-8") as f:
            prp = json.load(f)
        
        valid, msg = validate_prp_integrity(prp)
        if not valid:
            return SkillOutput.failure(skill_input.agent, skill_input.skill, msg, skill_input.correlation_id)
        
        return SkillOutput.success(
            agent=skill_input.agent,
            skill=skill_input.skill,
            data={"status": "PASS", "message": msg, "contract": prp},
            correlation_id=skill_input.correlation_id
        )
    except Exception as e:
        return SkillOutput.failure(skill_input.agent, skill_input.skill, f"JSON Error: {str(e)}", skill_input.correlation_id)
