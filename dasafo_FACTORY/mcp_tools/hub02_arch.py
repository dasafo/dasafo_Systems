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

db_logic = _load_skill_logic("database-outcome-generator")
tech_research_logic = _load_skill_logic("tech-research-outcome")

@mcp.tool(name="database-outcome-generator")
@aduana_universal(skill_name="database-outcome-generator")
def database_outcome_generator(agent: str, target_project: str, resource_entity: str = "generic_resource", overwrite: bool = False, isolation_mode: bool = False, isolate: bool = False):
    return db_logic.execute_database_outcome(target_project, agent, resource_entity, overwrite, isolation_mode)

@mcp.tool(name="tech-research-outcome")
@aduana_universal(skill_name="tech-research-outcome")
def tech_research_outcome(agent: str, target_project: str, sub_action: str = 'research-manager', isolate: bool = False, **kwargs):
    return tech_research_logic.execute_outcome(target_project, agent, sub_action, **kwargs)
