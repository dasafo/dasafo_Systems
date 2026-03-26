"""
run.py — Skill: PRP Generator
Agent: PRODUCT_OWNER
v3.1.5: Solidity Guard | Industrial Scale.

Generates the preliminary Project Requirements Document (PRP) contract.
"""

from __future__ import annotations
import sys
import json
import os
from pathlib import Path
from datetime import datetime

# Add factory knowledge to path
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "00_GLOBAL_KNOWLEDGE"))
from skill_schema import SkillInput, SkillOutput

def generate_prp_blueprint(project_name: str, objective: str):
    """Builds the formal PRP JSON structure."""
    return {
        "mission_id": f"MISSION-{datetime.now().strftime('%Y%m%d-%H%M')}",
        "project_name": project_name,
        "objective": objective,
        "governance": "Dasafo Factory v3.1.5 Solidity Guard",
        "requirements": {
            "functional": ["Agentic Orchestration", "Zero-Trust Security"],
            "non_functional": ["Premium UI/UX", "Modular Solidity"]
        },
        "signing": {
            "status": "PENDING_PO_APPROVAL",
            "timestamp": None
        }
    }

def run(skill_input: SkillInput) -> SkillOutput:
    """Standardized entry point for the skill."""
    project_name = skill_input.params.get("project_name", "UNKNOWN_PROJECT")
    objective = skill_input.params.get("objective", "No objective defined yet.")
    target = skill_input.target_project or os.environ.get("TARGET_PROJECT")
    
    prp = generate_prp_blueprint(project_name, objective)
    
    artifact_paths = []
    if target:
        output_path = Path(target) / "PRP_CONTRACT.json"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding="utf-8") as f:
            json.dump(prp, f, indent=2)
        artifact_paths.append(str(output_path))

    return SkillOutput.success(
        agent=skill_input.agent,
        skill=skill_input.skill,
        data={"prp_blueprint": prp},
        artifacts=artifact_paths,
        correlation_id=skill_input.correlation_id
    )
