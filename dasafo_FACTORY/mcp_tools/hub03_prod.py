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

api_design_logic = _load_skill_logic("api-design-outcome")
backend_logic = _load_skill_logic("backend-logic-outcome")
frontend_vibe_logic = _load_skill_logic("frontend-vibe-outcome")

@mcp.tool(name="api-design-outcome")
@aduana_universal(skill_name="api-design-outcome")
def api_design_outcome(agent: str, target_project: str, sub_action: str = 'api-contract-generator', isolate: bool = False, **kwargs):
    return api_design_logic.execute_outcome(target_project, agent, sub_action, **kwargs)

@mcp.tool(name="backend-logic-outcome")
@aduana_universal(skill_name="backend-logic-outcome")
def backend_logic_outcome(agent: str, target_project: str, sub_action: str = 'async-fastapi-logic', isolate: bool = False, **kwargs):
    return backend_logic.execute_outcome(target_project, agent, sub_action, **kwargs)

@mcp.tool(name="frontend-vibe-outcome")
@aduana_universal(skill_name="frontend-vibe-outcome")
def frontend_vibe_outcome(agent: str, target_project: str, sub_action: str = 'frontend-ui-designer', isolate: bool = False, **kwargs):
    return frontend_vibe_logic.execute_outcome(target_project, agent, sub_action, **kwargs)
