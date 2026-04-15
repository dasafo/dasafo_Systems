import importlib.util
from pathlib import Path
from mcp_tools.mcp_app import mcp, aduana_universal

def _load_skill_logic(skill_name: str):
    logic_path = Path(__file__).resolve().parent.parent / "06_SKILL_LIBRARY" / skill_name / "scripts" / "logic.py"
    if not logic_path.exists(): logic_path = Path(__file__).resolve().parent.parent / "06_SKILL_LIBRARY" / skill_name / "logic.py"
    spec = importlib.util.spec_from_file_location(f"{skill_name.replace('-', '_')}_logic", logic_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

mgmt_outcome_logic = _load_skill_logic("project-management-outcome")
delegate_logic = _load_skill_logic("delegate-clean-session")
backbone_logic = _load_skill_logic("backbone-validation-outcome")

@mcp.tool(name="project-management-outcome")
@aduana_universal(skill_name="project-management-outcome")
def project_management_outcome(agent: str, target_project: str, sub_action: str = 'project-management', isolate: bool = False, **kwargs):
    return mgmt_outcome_logic.execute_outcome(target_project, agent, sub_action, **kwargs)

@mcp.tool(name="delegate-clean-session")
@aduana_universal(skill_name="delegate-clean-session")
def delegate_clean_session(agent: str, target_project: str, spec_path: str = "", agent_type: str = "", current_phase: str = "", isolate: bool = False):
    return delegate_logic.execute_delegation(agent, target_project, spec_path, agent_type, current_phase)

@mcp.tool(name="backbone-validation-outcome")
@aduana_universal(skill_name="backbone-validation-outcome")
def backbone_validation_outcome(agent: str, target_project: str, sub_action: str = 'project-backbone-validator', isolate: bool = False, **kwargs):
    return backbone_logic.execute_outcome(target_project, agent, sub_action, **kwargs)
