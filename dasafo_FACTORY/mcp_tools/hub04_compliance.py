import importlib.util
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
scanner_logic = _load_skill_logic("agentic-thought-secret-scanner")
docs_logic = _load_skill_logic("api-docs-generator")
build_logic = _load_skill_logic("build-test-executor")
audit_logic = _load_skill_logic("factory-audit-pro")
guardrail_logic = _load_skill_logic("hallucination-guardrail")
playwright_logic = _load_skill_logic("playwright-e2e-tester")

# --- HERRAMIENTAS MCP ---

@mcp.tool(name="playwright-e2e-tester")
@aduana_universal(skill_name="playwright-e2e-tester")
def playwright_e2e_tester(
    agent: str, 
    target_project: str, 
    action: str = "run_e2e", 
    spec_path: str = None, 
    url: str = "http://localhost:3000",
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M4] Executes browser-based E2E tests and generates industrial trace reports.
    """
    return playwright_logic.execute_e2e(
        target_project, agent, action, spec_path, url
    )

@mcp.tool(name="hallucination-guardrail")
@aduana_universal(skill_name="hallucination-guardrail")
def hallucination_guardrail(
    agent: str, 
    content: str, 
    target_project: str = None, 
    action: str = "check_fact", 
    context_path: str = None, 
    strictness: float = 0.8,
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [TRANSVERSAL] Enforces factual integrity and output safety using programmable guardrails.
    """
    return guardrail_logic.execute_guardrail(
        content, action, context_path, strictness
    )

@mcp.tool(name="factory-audit-pro")
@aduana_universal(skill_name="factory-audit-pro")
def factory_audit_pro(
    agent: str, 
    target_project: str, 
    dimensions: list = None, 
    severity_threshold: str = "P3", 
    strict_mode: bool = True,
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M4] Performs an industrial-grade quality audit and anti-pattern scan.
    """
    return audit_logic.execute_audit(
        target_project, agent, dimensions, severity_threshold, strict_mode
    )

@mcp.tool(name="build-test-executor")
@aduana_universal(skill_name="build-test-executor")
def build_test_executor(
    agent: str, 
    target_project: str, 
    action: str = "run_build", 
    command: str = "echo 'Simulating build...'", 
    overwrite: bool = False, 
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M3] Executes build/test commands and generates the mandatory Aduana Passport (BUILD_REPORT.json).
    """
    return build_logic.execute_build_test(
        target_project, agent, action, command, overwrite
    )

@mcp.tool(name="api-docs-generator")
@aduana_universal(skill_name="api-docs-generator")
def api_docs_generator(
    agent: str, 
    target_project: str, 
    contract_path: str = "API-CONTRACT.yaml", 
    output_name: str = "API_REFERENCE_PRO.md", 
    include_examples: bool = True, 
    overwrite: bool = False, 
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M4] Genera documentación profesional (Markdown) a partir de contratos OpenAPI.
    Basado en: https://skills.sh/sickn33/antigravity-awesome-skills/api-documentation-generator
    """
    return docs_logic.execute_docs_generation(
        target_project, contract_path, output_name, include_examples, overwrite
    )

@mcp.tool(name="agentic-thought-secret-scanner")
@aduana_universal(skill_name="agentic-thought-secret-scanner")
def agentic_thought_secret_scanner(
    agent: str, 
    target_project: str, 
    network_preflight: bool = False, 
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M4] Escáner Zero-Trust basado en Credential Scanner. 
    Busca secretos y claves API expuestas.
    """
    return scanner_logic.execute_scan(
        target_project, network_preflight
    )