import json
import logging
import os
from pathlib import Path

# Configurar logging simple
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AduanaUniversal")

# Skills autorizadas para ejecutar incluso si el estado está bloqueado
BYPASS_SKILLS = {
    # 🌟 Puertas y Checklists
    "kanban-solidity-gate",
    "autoshield-preflight-check",
    "prp-validation-gate",
    
    # 📋 Gestión Burocrática (Necesaria para cerrar tareas y desbloquear el proyecto)
    "project-management",
    
    # 🔍 Diagnóstico y Auditoría (Sólo lectura / Pasivas)
    "factory-audit-pro",
    "task-dependency-diagnostic",
    "healthcheck-poller",
    "resource-monitor",
    
    # 📚 Contexto e Investigación (No destructivas)
    "notebooklm-nexus",
    "context-compression",
    "continuous-research"
}

def verify_project_state(target_project: str, requested_skill: str) -> tuple[bool, str]:
    """
    Protocol-Level Session Hook (Aduana Universal v3.2.0-S).
    Verifica que el agente no intente ejecutar código si el proyecto está
    en un estado secuencial inconsistente (Fallo Cerrado).
    """
    
    if requested_skill in BYPASS_SKILLS:
        return True, "Bypass skill allowed."

    state_path = Path(target_project) / "PROJECT_STATE.json"
    
    if not state_path.exists():
        return False, "Solidity Guard: PROJECT_STATE.json no existe en el proyecto destino. Operación denegada."
        
    try:
        with open(state_path, "r", encoding="utf-8") as f:
            state_data = json.load(f)
    except json.JSONDecodeError as e:
        return False, f"Solidity Guard: PROJECT_STATE.json corrupto (inválido JSON). Evidencia: {e}"
    except Exception as e:
        return False, f"Solidity Guard: Error leyendo PROJECT_STATE.json. Evidencia: {e}"
    
    # Evaluar fases
    phases = state_data.get("phases", {})
    if not phases:
        # Podría ser un proyecto nuevo, pero asumimos que debe tener fases para operar.
        return False, "Solidity Guard: PROJECT_STATE.json no define la clave 'phases'."

    phase_keys = list(phases.keys())
    
    # Buscar el primer PENDING
    first_pending_idx = -1
    for i, pk in enumerate(phase_keys):
        if phases[pk] == "PENDING":
            first_pending_idx = i
            break
            
    # Buscar el primer IN_PROGRESS
    in_progress_count = 0
    in_progress_idx = -1
    for i, pk in enumerate(phase_keys):
        if phases[pk] == "IN_PROGRESS":
            in_progress_count += 1
            in_progress_idx = i

    # Reglas de Solidez Industrial
    if in_progress_count > 1:
        return False, "Solidity Guard: Hay más de una fase 'IN_PROGRESS'. Se requiere foco atómico."
        
    if in_progress_idx != -1:
        # Todas las anteriores deben ser APPROVED
        for i in range(in_progress_idx):
            if phases[phase_keys[i]] != "APPROVED":
                return False, f"Solidity Guard: Fase {phase_keys[in_progress_idx]} en progreso, pero la fase anterior {phase_keys[i]} no está APPROVED."
                
    if first_pending_idx != -1:
        # Todas las posteriores (o ella misma) que sean distintas de PENDING son inválidas
        for i in range(first_pending_idx + 1, len(phase_keys)):
            if phases[phase_keys[i]] != "PENDING":
                return False, f"Solidity Guard: Inconsistencia detectada. Fase {phase_keys[first_pending_idx]} es PENDING, pero {phase_keys[i]} es {phases[phase_keys[i]]}."
                
    # Si todo es coherente, validamos que exista al menos una fase en progreso o todo aprobado
    if in_progress_count == 0 and first_pending_idx != -1:
         return False, "Solidity Guard: Ninguna fase está 'IN_PROGRESS', pero hay fases 'PENDING'. Por favor usa kanban-solidity-gate para abrir la siguiente fase."

    return True, "State Validated"

