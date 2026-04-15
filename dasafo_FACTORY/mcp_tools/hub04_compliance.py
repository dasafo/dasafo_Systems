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

sec_audit_logic = _load_skill_logic("security-audit-outcome")
e2e_veri_logic = _load_skill_logic("e2e-verification-outcome")
guardrail_logic = _load_skill_logic("hallucination-guardrail")
val_logic = _load_skill_logic("skill-validation-outcome")

@mcp.tool(name="skill-validation-outcome")
@aduana_universal(skill_name="skill-validation-outcome")
def skill_validation_outcome(agent: str, target_project: str, target_skill: str, input_payload: str, actual_output: str, min_similarity: float = 0.95, isolate: bool = False):
    return val_logic.validate_outcome(target_project, target_skill, input_payload, actual_output, min_similarity)

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
