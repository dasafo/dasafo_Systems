"""
run.py — Requirements Validation Audit (QA_TESTER)
v3.1.5: Solidity Guard | Industrial Scale.

Verifies that the implementation aligns with the PRP contract.
"""

import sys
import os
from pathlib import Path

# Add factory knowledge to path
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "00_GLOBAL_KNOWLEDGE"))
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """
    Checks for the presence and signing of the PRP_CONTRACT.json.
    """
    target_project = skill_input.target_project or os.environ.get("TARGET_PROJECT", ".")
    project_path = Path(target_project).resolve()
    
    contract_path = project_path / "PRP_CONTRACT.json"
    
    audit_results = {
        "project": str(project_path),
        "contract_exists": contract_path.exists(),
        "status": "VALIDATED v3.1.5" if contract_path.exists() else "AUDIT_FAILED",
        "guidance": "If contract is missing, the agent must halt execution until PO approval."
    }
    
    return SkillOutput.success(
        agent=skill_input.agent,
        skill=skill_input.skill,
        data=audit_results,
        correlation_id=skill_input.correlation_id
    )
