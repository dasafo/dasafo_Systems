from __future__ import annotations
import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — PRP Validation Gate (PRODUCT_OWNER)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Enforces the mandatory gate between Discovery and Production phases.
"""

import os
import json
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    agent = "PRODUCT_OWNER"
    skill = "prp-validation-gate"
    cid = skill_input.correlation_id

    try:
        # 1. Resolve Target
        target = skill_input.target_project or skill_input.params.get("project") or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "Missing TARGET_PROJECT", cid)
        
        project_path = Path(target).resolve()
        contract_path = project_path / "LOCAL_KNOWLEDGE" / "contracts" / "PRP_CONTRACT.json"
        
        # Fallback to root if not in contracts/
        if not contract_path.exists():
             contract_path = project_path / "PRP_CONTRACT.json"

        # 2. Logic (Gate Verification)
        if not contract_path.exists():
             return SkillOutput.success(agent, skill, {"gate_status": "LOCKED", "signing_status": "MISSING", "reason": f"No PRP contract found at {contract_path}"}, cid)

        prp = json.loads(contract_path.read_text(encoding="utf-8"))
        
        # Check for both formats: prp_status AND signing.status
        signing_status = prp.get("signing", {}).get("status") or prp.get("prp_status", "DRAFT")
        
        gate = "OPEN" if signing_status == "VALIDATED" else "LOCKED"

        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "gate_status": gate,
                "signing_status": signing_status,
                "integrity_score": 1.0,
                "contract_ref": str(contract_path)
            },
            correlation_id=cid,
            artifacts=[str(contract_path)]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"PRP Gate Audit Failed: {str(e)}", cid)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Skill: PRP Validation Gate")
    parser.add_argument("--project", required=True, help="Path to the target project")
    args = parser.parse_args()
    
    skill_input = SkillInput(
        agent="CLI_TOOL",
        skill="prp-validation-gate",
        params={"project": args.project},
        target_project=args.project,
        correlation_id="cli-gate-check"
    )
    
    output = run(skill_input)
    print(output.to_json())
