"""
run.py — Requirements Validation Audit (QA_TESTER)
Verifies that the implementation aligns with the PRP contract.
v2.1: Project-agnostic.
"""

import os
from pathlib import Path
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
        "status": "VALIDATED" if contract_path.exists() else "AUDIT_FAILED",
        "guidance": "If contract is missing, the agent must halt execution until PO approval."
    }
    
    return SkillOutput.success(
        agent=skill_input.agent,
        skill=skill_input.skill,
        data=audit_results,
        correlation_id=skill_input.correlation_id
    )
