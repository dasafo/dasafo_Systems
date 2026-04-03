import importlib.util
from pathlib import Path
import os
from mcp_tools.mcp_app import mcp, aduana_universal

# --- CARGADOR DINÁMICO DE LÓGICA (LAYER 3) ---

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
trend_logic = _load_skill_logic("apify-trend-analysis")
mgmt_logic = _load_skill_logic("project-management")
prp_logic = _load_skill_logic("prp-generator")
social_logic = _load_skill_logic("social-content-strategy")
startup_logic = _load_skill_logic("startup-metrics-framework")

# --- HERRAMIENTAS DEL HUB 01 ---

@mcp.tool(name="startup-metrics-framework")
@aduana_universal(skill_name="startup-metrics-framework")
def startup_metrics_framework(
    agent: str, 
    target_project: str, 
    business_model: str, 
    target_audience: str = "General", 
    estimated_execution_s: float = 1.5,
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M1] Traduce métricas de ejecución técnica (s, B) en KPIs de negocio SaaS (CAC, LTV, ROI).
    Indispensable para definir los criterios de éxito financiero en el PRP_MASTER.
    """
    return startup_logic.execute_financial_analysis(
        target_project, business_model, target_audience, estimated_execution_s
    )

@mcp.tool(name="prp-generator")
@aduana_universal(skill_name="prp-generator")
def prp_generator(
    agent: str, 
    target_project: str, 
    action: str = "generate_master", 
    project_name: str = None, 
    problem_description: str = None, 
    spec_data: dict = None, 
    overwrite: bool = False, 
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M1] Genera contratos industriales PRP_MASTER y especificaciones SPEC_LITE atómicas.
    """
    return prp_logic.execute_prp_generation(
        target_project, action, project_name, problem_description, spec_data, overwrite
    )


@mcp.tool(name="project-management")
@aduana_universal(skill_name="project-management")
def project_management(
    agent: str, 
    target_project: str, 
    action: str = "standup_report", 
    report_data: dict = None, 
    overwrite: bool = False,
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M1] Coordina el estado del proyecto, genera reportes de progreso y registra hitos en disco.
    """
    return mgmt_logic.execute_management(
        target_project, agent, action, report_data, overwrite
    )


@mcp.tool(name="apify-trend-analysis")
@aduana_universal(skill_name="apify-trend-analysis")
def apify_trend_analysis(
    agent: str, 
    target_project: str, 
    actor: str, 
    input_data: dict = None, 
    overwrite: bool = False, 
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M1] Analiza tendencias de mercado y nichos utilizando Apify Actors.
    """
    return trend_logic.execute_trend_analysis(
        target_project, actor, input_data, overwrite
    )


@mcp.tool(name="social-content-strategy")
@aduana_universal(skill_name="social-content-strategy")
def social_content_strategy(
    agent: str, 
    target_project: str, 
    action: str = "repurpose_system", 
    source_content: str = "Generic pillar content base.", 
    platforms: list = None, 
    brand_voice: str = "Professional & Provocative", 
    overwrite: bool = False, 
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M1/M6] Transforma contenido pilar en activos sociales multi-plataforma.
    Alineado con el mandato SI (segundos, bytes).
    """
    return social_logic.execute_social_strategy(
        target_project, action, source_content, platforms, brand_voice, overwrite
    )