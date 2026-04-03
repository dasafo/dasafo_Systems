import importlib.util
import time
from pathlib import Path
from factory_mcp_server import mcp, aduana_universal

# --- CARGADOR DINÁMICO DE LÓGICA ---

def _load_skill_logic(skill_name: str):
    """Carga dinámicamente el módulo logic.py de la skill especificada."""
    logic_path = Path(__file__).resolve().parent.parent / "06_SKILL_LIBRARY" / skill_name / "logic.py"
    if not logic_path.exists():
        raise FileNotFoundError(f"LTP_ERROR: No se encontró la lógica para {skill_name} en {logic_path}")
    
    spec = importlib.util.spec_from_file_location(f"{skill_name.replace('-', '_')}_logic", logic_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Inicialización de motores de lógica
feedback_logic = _load_skill_logic("autonomous-feedback-analyzer")
pruning_logic = _load_skill_logic("context-pruning-sieve")
health_logic = _load_skill_logic("deployment-health-check")
docker_logic = _load_skill_logic("docker-stack-provisioner")
refactor_logic = _load_skill_logic("skill-refactor-pro")
terraform_logic = _load_skill_logic("terraform-iac-builder")

# --- HERRAMIENTAS MCP ---

@mcp.tool(name="terraform-iac-builder")
@aduana_universal(skill_name="terraform-iac-builder")
def terraform_iac_builder(
    agent: str, 
    target_project: str, 
    action: str = "scaffold_module", 
    module_name: str = "core_infra", 
    cloud_provider: str = "aws", 
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M5] Provisions industrial Terraform IaC following HashiCorp style and surgical access rules.
    """
    return terraform_logic.execute_terraform_provisioning(
        target_project, action, module_name, cloud_provider
    )
    
@mcp.tool(name="skill-refactor-pro")
@aduana_universal(skill_name="skill-refactor-pro")
def skill_refactor_pro(
    agent: str, 
    target_project: str, 
    file_path: str, 
    action: str = "apply_refactor", 
    rules: list = None, 
    target_smell: str = None, 
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M5] Applies surgical refactoring rules to code or YAML artifacts.
    Enforces SI standards and handles auto-healing transformations.
    """
    return refactor_logic.execute_refactor(
        target_project, file_path, action, rules, target_smell
    )

@mcp.tool(name="docker-stack-provisioner")
@aduana_universal(skill_name="docker-stack-provisioner")
def docker_stack_provisioner(
    agent: str, 
    target_project: str, 
    action: str = "generate_dockerfile", 
    service_name: str = "app", 
    stack_type: str = "node",
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M5] Provisions industrial Docker IaC (Dockerfile/Compose) in WORKSPACE/infra/.
    """
    return docker_logic.execute_provisioning(
        target_project, action, service_name, stack_type
    )

@mcp.tool(name="deployment-health-check")
@aduana_universal(skill_name="deployment-health-check")
def deployment_health_check(
    agent: str, 
    target_project: str, 
    action: str = "check_endpoint", 
    url: str = "http://localhost:3000/health", 
    timeout_seconds: int = 5, 
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M5] Real-time endpoint validation and SI metric reporting.
    Triggers Auto-Healing protocols if a deployment fails.
    """
    cid = f"H-{int(time.time())}"
    
    return health_logic.execute_health_check(
        target_project, action, url, timeout_seconds, cid
    )

@mcp.tool(name="context-pruning-sieve")
@aduana_universal(skill_name="context-pruning-sieve")
def context_pruning_sieve(
    agent: str, 
    target_project: str, 
    target_file: str, 
    action: str = "compact_context", 
    budget_threshold: float = 0.8, 
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M5] Extends context capacity by pruning fluff and optimizing token usage.
    """
    return pruning_logic.execute_pruning(
        target_project, target_file, action, budget_threshold
    )

@mcp.tool(name="autonomous-feedback-analyzer")
@aduana_universal(skill_name="autonomous-feedback-analyzer")
def autonomous_feedback_analyzer(
    agent: str, 
    target_project: str, 
    action: str = "analyze_file", 
    file_path: str = "LOGS/FEEDBACK-LOG.md", 
    raw_text: str = None, 
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M5] Analyzes feedback logs to extract Golden Rules and syncs them with Neo4j (LTP).
    """
    return feedback_logic.execute_feedback_analysis(
        target_project, agent, action, file_path, raw_text
    )