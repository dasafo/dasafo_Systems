import importlib.util
from pathlib import Path
import os
from factory_mcp_server import mcp, aduana_universal

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
build_logic = _load_skill_logic("build-test-executor")

# --- HERRAMIENTAS CORE ---

@mcp.tool(name="build-test-executor")
@aduana_universal(skill_name="build-test-executor")
def build_test_executor(
    agent: str, 
    target_project: str, 
    action: str = "run_build", 
    command: str = "echo 'Build...'", 
    overwrite: bool = False,
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [FASE M3] Ejecuta comandos de build/test y genera el Pasaporte de Aduana.
    """
    return build_logic.execute_build_test(
        target_project, agent, action, command, overwrite
    )

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
    action: str = "clean_session", 
    session_id: str = None,
    overwrite: bool = False,
    isolate: bool = False
) -> tuple[dict, list]:
    """
    [CORE] Gestiona la delegación de tareas y la limpieza de sesiones activas.
    """
    return delegation_logic.execute_delegation(
        target_project, agent, action, session_id, overwrite
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
