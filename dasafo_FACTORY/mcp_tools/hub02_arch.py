import importlib.util
from pathlib import Path
from factory_mcp_server import mcp, aduana_universal

# --- CARGADOR DINÁMICO DE LÓGICA (CAPA 3) ---

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
arch_logic = _load_skill_logic("api-contract-generator")
adr_logic = _load_skill_logic("architecture-decision-records")
arxiv_logic = _load_skill_logic("arxiv-technical-digest")
db_logic = _load_skill_logic("database-architect-strategic")
research_logic = _load_skill_logic("research-manager")

# --- HERRAMIENTAS DE LA CAPA 3 ---

@mcp.tool(name="research-manager")
@aduana_universal(skill_name="research-manager")
def research_manager(
    agent: str, 
    target_project: str, 
    report_name: str, 
    content: str, 
    category: str = "RESEARCH",
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M2] Safely persists technical research and architectural investigations to the project's DOCS hierarchy.
    """
    return research_logic.execute_research(
        target_project, report_name, content, category
    )
    
@mcp.tool(name="database-architect-strategic")
@aduana_universal(skill_name="database-architect-strategic")
def database_architect_strategic(
    agent: str, 
    target_project: str, 
    action: str = "design_schema", 
    resource_entity: str = "generic_resource", 
    overwrite: bool = False, 
    isolation_mode: bool = False,
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M2] Expert database architecture and strategic data modeling.
    """
    return db_logic.execute_db_architect(
        target_project, action, resource_entity, overwrite, isolation_mode
    )

@mcp.tool(name="arxiv-technical-digest")
@aduana_universal(skill_name="arxiv-technical-digest")
def arxiv_technical_digest(
    agent: str, 
    target_project: str, 
    query: str, 
    max_results: int = 5, 
    overwrite: bool = False, 
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M2] Fetches and digests academic papers from ArXiv for technical feasibility research.
    Based on: https://skills.sh/jezweb/claude-skills/arxiv-digest
    """
    return arxiv_logic.execute_digest(
        target_project, query, max_results, overwrite
    )

@mcp.tool(name="architecture-decision-records")
@aduana_universal(skill_name="architecture-decision-records")
def architecture_decision_records(
    agent: str, 
    target_project: str, 
    action: str = "new", 
    title: str = None, 
    context: str = None, 
    decision: str = None, 
    consequences: str = None, 
    target_id: str = None, 
    overwrite: bool = False, 
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M2] Gestiona el registro inmutable de decisiones arquitectónicas (ADR).
    Basado en: https://skills.sh/wshobson/agents/architecture-decision-records
    """
    return adr_logic.execute_adr(
        target_project, action, title, context, decision, consequences, target_id, overwrite
    )

@mcp.tool(name="api-contract-generator")
@aduana_universal(skill_name="api-contract-generator")
def api_contract_generator(
    agent: str, 
    target_project: str, 
    resource: str = "generic_resource", 
    version: str = "1.0.0", 
    overwrite: bool = False, 
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M2] Diseña contratos de API (OpenAPI 3.1) bajo el mandato Design-First.
    Basado en: https://skills.sh/jeffallan/claude-skills/api-designer
    """
    return arch_logic.execute_design(
        target_project, resource, version, overwrite
    )