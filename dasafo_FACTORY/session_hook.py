import json
import logging
import os
from pathlib import Path

# Configurar logging simple
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AduanaUniversal")

# Skills autorizadas para ejecutar incluso si el estado está bloqueado (Top 18 Hub)
BYPASS_SKILLS = {
    # 🌟 Puertas y Checklists
    "kanban-solidity-gate",
    "agentic-thought-secret-scanner",
    "factory-audit-pro",
    "prp-generator",
    
    # 🔍 Diagnóstico e Investigación (No destructivas)
    "arxiv-technical-digest",
    "apify-trend-analysis",
    "hallucination-guardrail",
    "autonomous-feedback-analyzer",
    
    # 📋 Gestión Burocrática (Necesaria para cerrar tareas y desbloquear el proyecto)
    "project-management"
}

def verify_project_state(target_project: str, requested_skill: str, agent: str = None) -> tuple[bool, str]:
    """
    Protocol-Level Session Hook (Aduana Universal v3.4.0-S).
    Verifica que el agente no intente ejecutar código si el proyecto está
    en un estado secuencial inconsistente (Fallo Cerrado).
    Añadido v3.4.0-S: Sincronización con el esqueleto DOCS/ y Top 18 Hub.
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
        return False, "Solidity Guard: PROJECT_STATE.json no define la clave 'phases'."

    phase_keys = list(phases.keys())
    
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
                
    if in_progress_count == 0:
         # Verificar si hay fases pendientes posteriores a una APPROVED
         return False, "Solidity Guard: Ninguna fase está 'IN_PROGRESS'. Por favor usa kanban-solidity-gate para abrir la siguiente fase."

    # --- STARK-SOLIDITY ENFORCEMENT (v3.4.0-S) ---
    # Si la skill es de gestión de tareas (cierre), validamos evidencia técnica de build en fases correspondientes.
    if requested_skill in ["project-management", "kanban-solidity-gate"]:
        current_phase = phase_keys[in_progress_idx] if in_progress_idx != -1 else None
        
        # Las fases técnicas (Producción/M3, Compliance/M4) requieren proof.
        if current_phase in ["M3", "M4"]:
            build_proof = Path(target_project) / "LOGS" / "BUILD_REPORT.json"
            if not build_proof.exists():
                return False, f"Stark-Solidity Violation (v3.4.0-S): Intento de cierre en {current_phase} sin BUILD_REPORT.json en LOGS/. Operación Bloqueada."
    # ---------------------------------------------

    return True, "State Validated"
