import importlib.util
from pathlib import Path
from mcp_tools.mcp_app import mcp, aduana_universal

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
tokens_logic = _load_skill_logic("atomic-design-tokens")
fastapi_logic = _load_skill_logic("async-fastapi-logic")
ui_logic = _load_skill_logic("frontend-ui-designer")
node_patterns_logic = _load_skill_logic("nodejs-backend-patterns")
pytest_logic = _load_skill_logic("pytest-logic-verifier")
shadcn_logic = _load_skill_logic("shadcn-component-library")
supabase_logic = _load_skill_logic("supabase-stack-expert")

# --- HERRAMIENTAS MCP ---

@mcp.tool(name="supabase-stack-expert")
@aduana_universal(skill_name="supabase-stack-expert")
def supabase_stack_expert(
    agent: str, 
    target_project: str, 
    action: str = "audit_schema", 
    sql_script: str = None, 
    overwrite: bool = False, 
    isolation_mode: bool = False,
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M3] Advanced database engineering for Supabase/Postgres.
    Optimizes performance, security (RLS), and schema design.
    """
    return supabase_logic.execute_supabase_audit(
        target_project, action, sql_script, overwrite, isolation_mode
    )

@mcp.tool(name="shadcn-component-library")
@aduana_universal(skill_name="shadcn-component-library")
def shadcn_component_library(
    agent: str, 
    target_project: str, 
    action: str = "add", 
    component: str = None, 
    overwrite: bool = False, 
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M3] Industrial management of Shadcn/UI components. 
    Enforces atomic design and Tailwind token consistency.
    """
    return shadcn_logic.execute_shadcn_management(
        target_project, action, component, overwrite
    )

@mcp.tool(name="pytest-logic-verifier")
@aduana_universal(skill_name="pytest-logic-verifier")
def pytest_logic_verifier(
    agent: str, 
    target_project: str, 
    spec_path: str, 
    action: str = "run_test", 
    module_path: str = None, 
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M3] Generates and executes Python tests based on Spec-Lite criteria.
    Verifies that implementation matches the business logic contract.
    """
    return pytest_logic.execute_logic_verification(
        target_project, agent, action, spec_path, module_path
    )

@mcp.tool(name="nodejs-backend-patterns")
@aduana_universal(skill_name="nodejs-backend-patterns")
def nodejs_backend_patterns(
    agent: str, 
    target_project: str, 
    module_name: str = "core",
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M3] Enforces industrial Node.js patterns (Repository, DTOs, Service Layer) for a module.
    """
    return node_patterns_logic.execute_patterns(
        target_project, module_name
    )

@mcp.tool(name="frontend-ui-designer")
@aduana_universal(skill_name="frontend-ui-designer")
def frontend_ui_designer(
    agent: str, 
    target_project: str, 
    component_name: str = "UnknownComponent", 
    design_vibe: str = "industrial",
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M3] Validates the frontend design system (Tailwind/Shadcn) before generating React components.
    """
    return ui_logic.execute_ui_validation(
        target_project, component_name, design_vibe
    )

@mcp.tool(name="async-fastapi-logic")
@aduana_universal(skill_name="async-fastapi-logic")
def async_fastapi_logic(
    agent: str, 
    target_project: str, 
    action: str = "scaffold", 
    domain_name: str = None, 
    route_name: str = None, 
    method: str = "GET", 
    overwrite: bool = False, 
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M3] Scaffolds and implements async FastAPI logic following DDD patterns.
    """
    return fastapi_logic.execute_fastapi_logic(
        target_project, action, domain_name, route_name, method, overwrite
    )

@mcp.tool(name="atomic-design-tokens")
@aduana_universal(skill_name="atomic-design-tokens")
def atomic_design_tokens(
    agent: str, 
    target_project: str, 
    action: str = "init", 
    layer: str = "primitive", 
    name: str = None, 
    value: str = None, 
    overwrite: bool = False, 
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M3] Synchronizes UI Design Tokens (CSS/JSON) following the Atomic Design hierarchy.
    """
    return tokens_logic.execute_atomic_tokens(
        target_project, action, layer, name, value, overwrite
    )