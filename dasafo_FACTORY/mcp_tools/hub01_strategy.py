import importlib.util
from pathlib import Path
import os
from mcp_tools.mcp_app import mcp, aduana_universal

def _load_skill_logic(skill_name: str):
    logic_path = Path(__file__).resolve().parent.parent / "06_SKILL_LIBRARY" / skill_name / "scripts" / "logic.py"
    if not logic_path.exists():
        logic_path = Path(__file__).resolve().parent.parent / "06_SKILL_LIBRARY" / skill_name / "logic.py"
    spec = importlib.util.spec_from_file_location(f"{skill_name.replace('-', '_')}_logic", logic_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

trend_logic = _load_skill_logic("apify-trend-analysis")
social_logic = _load_skill_logic("social-content-strategy")
project_contract_logic = _load_skill_logic("project-contract-outcome")

@mcp.tool(name="project-contract-outcome")
@aduana_universal(skill_name="project-contract-outcome")
def project_contract_outcome(agent: str, target_project: str, sub_action: str = 'prp-generator', isolate: bool = False, **kwargs):
    return project_contract_logic.execute_outcome(target_project, agent, sub_action, **kwargs)

@mcp.tool(name="apify-trend-analysis")
@aduana_universal(skill_name="apify-trend-analysis")
def apify_trend_analysis(agent: str, target_project: str, actor: str, input_data: dict = None, overwrite: bool = False, isolate: bool = False):
    return trend_logic.execute_trend_analysis(target_project, actor, input_data, overwrite)

@mcp.tool(name="social-content-strategy")
@aduana_universal(skill_name="social-content-strategy")
def social_content_strategy(agent: str, target_project: str, action: str = "repurpose", source_content: str = "", platforms: list = None, brand_voice: str = "", overwrite: bool = False, isolate: bool = False):
    return social_logic.execute_social_strategy(target_project, action, source_content, platforms, brand_voice, overwrite)
