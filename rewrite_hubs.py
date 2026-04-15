import sys
from pathlib import Path

# Note: Only writing to files, completely safely via python.

content_hub01 = """import importlib.util
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
"""

content_hub02 = """import importlib.util
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
"""

content_hub03 = """import importlib.util
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
"""

content_hub04 = """import importlib.util
from pathlib import Path
from mcp_tools.mcp_app import mcp, aduana_universal

def _load_skill_logic(skill_name: str):
    logic_path = Path(__file__).resolve().parent.parent / "06_SKILL_LIBRARY" / skill_name / "scripts" / "logic.py"
    if not logic_path.exists(): logic_path = Path(__file__).resolve().parent.parent / "06_SKILL_LIBRARY" / skill_name / "logic.py"
    spec = importlib.util.spec_from_file_location(f"{skill_name.replace('-', '_')}_logic", logic_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

sec_audit_logic = _load_skill_logic("security-audit-outcome")
e2e_veri_logic = _load_skill_logic("e2e-verification-outcome")
guardrail_logic = _load_skill_logic("hallucination-guardrail")

@mcp.tool(name="security-audit-outcome")
@aduana_universal(skill_name="security-audit-outcome")
def security_audit_outcome(agent: str, target_project: str, sub_action: str = 'factory-audit-pro', isolate: bool = False, **kwargs):
    return sec_audit_logic.execute_outcome(target_project, agent, sub_action, **kwargs)

@mcp.tool(name="e2e-verification-outcome")
@aduana_universal(skill_name="e2e-verification-outcome")
def e2e_verification_outcome(agent: str, target_project: str, sub_action: str = 'build-test-executor', isolate: bool = False, **kwargs):
    return e2e_veri_logic.execute_outcome(target_project, agent, sub_action, **kwargs)

@mcp.tool(name="hallucination-guardrail")
@aduana_universal(skill_name="hallucination-guardrail")
def hallucination_guardrail(agent: str, target_project: str, action: str = "guard", content: str = "", context_path: str = "", strictness: float = 1.0, isolate: bool = False):
    return guardrail_logic.apply_guardrail(target_project, action, content, context_path, strictness)
"""

content_hub05 = """import importlib.util
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
"""

content_core = """import importlib.util
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
"""

base_dir = Path("/home/david/Documents/AI/AGENTES/dasafo_FACTORY/mcp_tools")
(base_dir / "hub01_strategy.py").write_text(content_hub01)
(base_dir / "hub02_arch.py").write_text(content_hub02)
(base_dir / "hub03_prod.py").write_text(content_hub03)
(base_dir / "hub04_compliance.py").write_text(content_hub04)
(base_dir / "hub05_operations.py").write_text(content_hub05)
(base_dir / "core_dast.py").write_text(content_core)

print("Hubs completely refactored to use Outcome tools.")
