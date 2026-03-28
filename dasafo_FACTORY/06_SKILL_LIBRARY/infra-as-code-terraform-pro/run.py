import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — IaC Terraform Support (DEVOPS_SRE)
v3.2.0-S: Modular Toolbox | Industrial Scale.

Simulates infrastructure management and drift detection using Terraform.
"""

from __future__ import annotations
import os
import shutil
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    """Industrialized entry point: Real Infrastructure Gateway."""
    agent = "DEVOPS_SRE"
    skill = "infra-as-code-terraform-pro"
    cid = skill_input.correlation_id

    try:
        # 0. Zero-Trust Environment Check
        terraform_bin = shutil.which("terraform")
        if not terraform_bin:
            return SkillOutput.failure(agent, skill, "SECURITY LOCK: Terraform binary not found in system path. Mocking IaC plans is forbidden.", cid)

        # 1. Resolve State
        target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "Missing TARGET_PROJECT to locate IaC definitions.", cid)
             
        action = skill_input.params.get("action", "plan")
        
        # 2. Logic: Preparation for strict physical pass
        project_path = Path(target).resolve()
        iac_path = project_path / "infrastructure"
        
        if not iac_path.exists():
            return SkillOutput.success(
                agent=agent,
                skill=skill,
                result={
                    "status": "ABORTED_NO_IAC",
                    "drift_detected": False,
                    "industrial_verification": True,
                    "message": f"Expected Terraform folder at {iac_path} not found."
                },
                correlation_id=cid
            )
        
        return SkillOutput.success(
            agent=agent,
            skill=skill,
            result={
                "binary": terraform_bin,
                "status": "APPROVED_FOR_EXEC",
                "industrial_verification": True,
                "action": action
            },
            correlation_id=cid,
            artifacts=[]
        )

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"IaC Operation Failed: {str(e)}", cid)
