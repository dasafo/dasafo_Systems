"""
PRP & Spec Generator (v3.4.0-S) - Industrial Implementation.
Product Requirements Prompt and Atomic Spec generation.
"""
from __future__ import annotations
import os
import json
from enum import Enum
import datetime
from pathlib import Path
from typing import List, Optional, Dict, Any
from skill_schema import SkillInput, SkillOutput

class PRPAction(str, Enum):
    GENERATE_MASTER = "generate_master"
    GENERATE_LITE = "generate_lite"
    UPDATE = "update"
    VALIDATE = "validate"

def load_template(filename: str) -> Dict[str, Any]:
    """Helper to load standard industrial templates from the local directory."""
    template_path = Path(__file__).parent / "templates" / filename
    try:
        with open(template_path, "r") as f:
            return json.load(f)
    except Exception as e:
        # Emergency fallback if templates are missing
        return {"error": f"Template {filename} not found: {e}"}

def run(request: SkillInput) -> SkillOutput:
    """Industrial execution engine for project contract definition."""
    params = request.params
    action = params.get("action")
    project_name = params.get("project_name", "Unknown")
    problem_description = params.get("problem_description", "")
    pattern = params.get("pattern", "B")
    target_project = Path(request.target_project) if request.target_project else Path(".")
    
    logs = [f"Starting {action} for {project_name}"]
    
    # 1. Project directory setup
    target_project.mkdir(parents=True, exist_ok=True)
    
    # 2. Logic processing based on action
    if action == PRPAction.GENERATE_MASTER:
        prp_file = target_project / "PRP_CONTRACT.json"
        
        prp_data = load_template("PRP_MASTER_TEMPLATE.json")
        
        # Inject dynamic project data into the Master template
        prp_data["metadata"].update({
            "project_name": project_name,
            "pattern": pattern,
            "created_at": datetime.date.today().isoformat()
        })
        prp_data["requirements"]["02_problem"] = problem_description
        
        with open(prp_file, 'w', encoding='utf-8') as f:
            json.dump(prp_data, f, indent=2)
            
        logs.append(f"Generated PRP_MASTER at {prp_file}")
        
        return SkillOutput.success(
            agent=request.agent,
            skill=request.skill,
            result={
                "status": "SOLIDIFIED",
                "prp_path": str(prp_file),
                "solidity_score": 1.0
            }
        )

    elif action == PRPAction.GENERATE_LITE:
        task_id = project_name # Reuse field for ID
        lite_file = target_project / "TASKS" / f"SPEC_{task_id}.json"
        lite_file.parent.mkdir(parents=True, exist_ok=True)
        
        lite_data = load_template("SPEC_LITE_TEMPLATE.json")
        
        # Inject dynamic task data into the Lite template
        lite_data["metadata"].update({
            "task_id": task_id,
            "assigned_agent": params.get("agent_type", "Required"),
            "context_pointers": params.get("context_pointers", [])
        })
        lite_data["specification"]["01_objective"] = problem_description
        
        with open(lite_file, 'w', encoding='utf-8') as f:
            json.dump(lite_data, f, indent=2)
            
        logs.append(f"Generated SPEC_LITE at {lite_file}")
        
        return SkillOutput.success(
            agent=request.agent,
            skill=request.skill,
            result={
                "status": "SOLIDIFIED",
                "prp_path": str(lite_file),
                "solidity_score": 1.0
            }
        )

    return SkillOutput.failure(request.agent, request.skill, f"Unknown action: {action}")
