import importlib.util
import time
from pathlib import Path
from mcp_tools.mcp_app import mcp, aduana_universal

def _load_skill_logic(skill_name: str):
    logic_path = Path(__file__).resolve().parent.parent / "06_SKILL_LIBRARY" / skill_name / "scripts" / "logic.py"
    if not logic_path.exists(): logic_path = Path(__file__).resolve().parent.parent / "06_SKILL_LIBRARY" / skill_name / "logic.py"
    spec = importlib.util.spec_from_file_location(f"{skill_name.replace('-', '_')}_logic", logic_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

health_logic = _load_skill_logic("deployment-health-check")
iac_logic = _load_skill_logic("iac-provisioning-outcome")
ephemeral_logic = _load_skill_logic("ephemeral-code-execution")
evolution_logic = _load_skill_logic("factory-evolution-outcome")
feedback_logic = _load_skill_logic("autonomous-feedback-analyzer")

@mcp.tool(name="iac-provisioning-outcome")
@aduana_universal(skill_name="iac-provisioning-outcome")
def iac_provisioning_outcome(agent: str, target_project: str, sub_action: str = 'docker-stack-provisioner', isolate: bool = False, **kwargs):
    return iac_logic.execute_outcome(target_project, agent, sub_action, **kwargs)

@mcp.tool(name="factory-evolution-outcome")
@aduana_universal(skill_name="factory-evolution-outcome")
def factory_evolution_outcome(agent: str, target_project: str, sub_action: str = 'skill-refactor-pro', isolate: bool = False, **kwargs):
    return evolution_logic.execute_outcome(target_project, agent, sub_action, **kwargs)

@mcp.tool(name="ephemeral-code-execution")
@aduana_universal(skill_name="ephemeral-code-execution")
def ephemeral_code_execution(agent: str, target_project: str, language: str = "python", code_payload: str = "", timeout_s: int = 30, isolate: bool = False):
    return ephemeral_logic.execute_ephemeral_code(target_project, agent, language, code_payload, timeout_s, isolate)

@mcp.tool(name="deployment-health-check")
@aduana_universal(skill_name="deployment-health-check")
def deployment_health_check(agent: str, target_project: str, action: str = "check_endpoint", url: str = "http://localhost:3000/health", timeout_seconds: int = 5, isolate: bool = False):
    return health_logic.execute_health_check(target_project, action, url, timeout_seconds, f"H-{int(time.time())}")

@mcp.tool(name="autonomous-feedback-analyzer")
@aduana_universal(skill_name="autonomous-feedback-analyzer")
def autonomous_feedback_analyzer(agent: str, target_project: str, action: str = "analyze_file", file_path: str = "LOGS/FEEDBACK-LOG.md", raw_text: str = None, isolate: bool = False):
    return feedback_logic.execute_feedback_analysis(target_project, agent, action, file_path, raw_text)
