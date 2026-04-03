import importlib.util
from pathlib import Path
import os
from mcp_tools.mcp_app import mcp, aduana_universal

# --- CARGADOR DINÁMICO DE LÓGICA (CORE) ---

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
delegation_logic = _load_skill_logic("delegate-clean-session")
doctor_logic = _load_skill_logic("factory-doctor")
kanban_logic = _load_skill_logic("kanban-solidity-gate")
validator_logic = _load_skill_logic("project-backbone-validator")
registry_logic = _load_skill_logic("registry-manager")
# ADR: build-test-executor se registra exclusivamente en hub04_compliance.py

# --- HERRAMIENTAS CORE ---

@mcp.tool(name="kanban-solidity-gate")
@aduana_universal(skill_name="kanban-solidity-gate")
def kanban_solidity_gate(
    agent: str, 
    target_project: str, 
    action: str = "audit", 
    port: int = 3001,
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [CORE] Aplica la Regla de Cero Pendientes y lanza el dashboard visual.
    """
    return kanban_logic.execute_gate(
        target_project, action, port=port
    )

@mcp.tool(name="delegate-clean-session")
@aduana_universal(skill_name="delegate-clean-session")
def delegate_clean_session(
    agent: str, 
    target_project: str, 
    spec_path: str = None,
    agent_type: str = None,
    current_phase: str = "M3",
    isolate: bool = True
) -> tuple[dict, list]:
    """
    [CORE] Delega una tarea a un sub-agente en sesión aislada con inyección JIT Neo4j.
    
    Args:
        agent: Tu ID (ej. ORCHESTRATOR).
        target_project: Ruta al proyecto (ej. PROJECTS/ContentRepurpose).
        spec_path: Nombre del archivo SPEC_LITE (ej. M3-001.json).
        agent_type: FRONTEND_DEV, BACKEND_DEV, QA_TESTER, etc.
        current_phase: M1-M5 para filtrar Golden Rules.
        isolate: Siempre true para clean sessions.
    """
    return delegation_logic.execute_delegation(
        target_project, spec_path, agent_type, current_phase
    )

@mcp.tool(name="factory-doctor")
@aduana_universal(skill_name="factory-doctor")
def factory_doctor(
    agent: str, 
    target_project: str, 
    action: str = "diagnose", 
    strict_mode: bool = True,
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [CORE] Ejecuta diagnósticos de salud estructural y de dependencias en la factoría.
    """
    return doctor_logic.execute_doctor(
        target_project, agent, action, strict_mode
    )

@mcp.tool(name="project-backbone-validator")
@aduana_universal(skill_name="project-backbone-validator")
def project_backbone_validator(
    agent: str, 
    target_project: str, 
    action: str = "validate_structure", 
    schema_version: str = "v1",
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [CORE] Valida la integridad del backbone y la estructura base del proyecto.
    """
    return validator_logic.execute_validation(
        target_project, agent, action, schema_version
    )

@mcp.tool(name="registry-manager")
@aduana_universal(skill_name="registry-manager")
def registry_manager(
    agent: str, 
    target_project: str, 
    action: str = "update_registry", 
    key_value_pairs: dict = None,
    overwrite: bool = False,
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [CORE] Administra el registro central de proyectos y variables de estado.
    """
    return registry_logic.execute_registry_update(
        target_project, agent, action, key_value_pairs, overwrite
    )
