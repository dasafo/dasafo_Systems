import os
import json
import time
import datetime
from pathlib import Path

# Logic: Industrial PRP & Spec Generation Engine (v5.0-MCP)
# Supports: Dual-Track Contract System (PRP_MASTER / SPEC_LITE)

def calculate_solidity(data: dict) -> float:
    """Calculates the score based on the completion of the 12 industrial sections."""
    reqs = data.get("requirements", {})
    if not reqs: return 0.0
    sections = [
        "01_overview", "02_problem", "03_success_criteria", "04_user_stories",
        "05_functional", "06_non_functional", "07_constraints", "08_data",
        "09_ui_ux", "10_risks", "11_out_of_scope", "12_open_questions"
    ]
    filled = 0
    for s in sections:
        val = reqs.get(s)
        if val and val not in ["Required", [], {}]:
            filled += 1
    return round(filled / len(sections), 2)

def update_project_state(project_path: Path, phase: str):
    """Physically updates the PROJECT_STATE.json phase marker."""
    state_path = project_path / "PROJECT_STATE.json"
    if state_path.exists():
        state = json.loads(state_path.read_text(encoding="utf-8"))
        state["current_phase"] = phase
        state.setdefault("phases", {})[phase] = "IN_PROGRESS"
        state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")

def execute_prp_generation(
    target_project: str,
    action: str = "generate_master",
    project_name: str = None,
    problem_description: str = None,
    spec_data: dict = None,
    overwrite: bool = False
) -> tuple[dict, list]:
    """Pure logic for requirement contract solidification (v5.0-MCP)."""
    start_time = time.time()
    project_path = Path(target_project).resolve()
    templates_dir = Path(__file__).parent / "templates"
    artifacts = []

    if action in ["generate_master", "update"]:
        if not project_name or not problem_description:
            raise ValueError("Missing project_name or problem_description.")
        
        prp_file = project_path / "PRP_CONTRACT.json"
        if prp_file.exists() and not overwrite and action == "generate_master":
            raise FileExistsError(f"REDUNDANCY LOCK: {prp_file.name} exists in root.")

        template_path = templates_dir / "PRP_MASTER_TEMPLATE.json"
        template = json.loads(template_path.read_text(encoding="utf-8"))

        template["metadata"].update({
            "project_name": project_name,
            "created_at": datetime.datetime.now().isoformat()
        })
        template["requirements"]["02_problem"] = problem_description
        
        prp_file.write_text(json.dumps(template, indent=2, ensure_ascii=False), encoding="utf-8")
        artifacts.append(str(prp_file))
        update_project_state(project_path, "M1")
        solidity = calculate_solidity(template)

        res = {
            "industrial_status": "SOLIDIFIED - PRP CONTRACT SIGNED",
            "solidity_score": solidity,
            "summary": f"PRP_CONTRACT.json solidified with score: {solidity}."
        }

    elif action == "generate_lite":
        spec_file = project_path / "TASKS" / "SPEC_LITE.json"
        spec_file.parent.mkdir(parents=True, exist_ok=True)
        
        template_path = templates_dir / "SPEC_LITE_TEMPLATE.json"
        template = json.loads(template_path.read_text(encoding="utf-8"))

        if spec_data:
            # DAST Fusion: Inject data into the template
            if "metadata" in spec_data: template["metadata"].update(spec_data["metadata"])
            if "technical_goal" in spec_data: template["specification"]["01_objective"] = spec_data["technical_goal"]
            if "requirements" in spec_data: template["specification"]["02_success_evidence"] = spec_data["requirements"]

        spec_file.write_text(json.dumps(template, indent=2, ensure_ascii=False), encoding="utf-8")
        artifacts.append(str(spec_file))
        res = {"industrial_status": "SOLIDIFIED - SPEC LITE READY", "summary": "SPEC_LITE generated in TASKS/"}

    res["compliance_report"] = {
        "si_metrics_applied": True,
        "execution_duration_seconds": round(time.time() - start_time, 4)
    }
    return res, artifacts