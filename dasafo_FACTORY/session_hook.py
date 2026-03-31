import json
import logging
import os
from pathlib import Path

# Configuración de logging industrial
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AduanaUniversal")

# Skills autorizadas para bypass (RCP de proyecto y utilidades de sistema) 
BYPASS_SKILLS = {
    "kanban-solidity-gate",
    "factory-doctor",             # 🚑 Autorizado para RCP de Proyecto
    "agentic-thought-secret-scanner",
    "factory-audit-pro",
    "prp-generator",
    "arxiv-technical-digest",
    "apify-trend-analysis",
    "hallucination-guardrail",
    "autonomous-feedback-analyzer",
    "project-management",
    "deployment-health-check",
    "registry-manager",
    "context-pruning-sieve"
}

def verify_project_state(target_project: str, requested_skill: str, agent: str = None) -> tuple[bool, str]:
    """
    Protocol-Level Session Hook (Aduana Universal v3.4.0-S).
    Implementa DAST (Disk-as-Source-of-Truth) y Double-Gating. 
    """
    
    # 1. Bypass Inmediato 
    if requested_skill in BYPASS_SKILLS:
        return True, "Bypass skill allowed."

    # 2. Verificación de Integridad del Estado 
    state_path = Path(target_project) / "PROJECT_STATE.json"
    if not state_path.exists():
        return False, "Solidity Guard: PROJECT_STATE.json ausente. Operación denegada."
        
    try:
        with open(state_path, "r", encoding="utf-8") as f:
            state_data = json.load(f)
    except Exception as e:
        return False, f"Solidity Guard: Error crítico leyendo PROJECT_STATE.json: {e}"
    
    phases = state_data.get("phases", {})
    if not phases:
        return False, "Solidity Guard: No se definen 'phases' en el estado."

    # --- 3. LÓGICA DE DOUBLE-GATING (Autorización Distribuida) ---
    # Permite que agentes de producción operen si poseen una SPEC_LITE física
    if agent in ["BACKEND_DEV", "FRONTEND_DEV", "DB_MASTER", "DATA_SCIENTIST"]:
        spec_path = Path(target_project) / "TASKS" / "SPEC_LITE.json"
        if spec_path.exists():
            try:
                with open(spec_path, "r") as f:
                    spec = json.load(f)
                    assigned = spec.get("metadata", {}).get("assigned_agent")
                    if assigned == agent:
                        return True, f"Double-Gate: Agente {agent} autorizado por SPEC_LITE física."
            except:
                pass 
    # -----------------------------------------------------------------------

    # 4. Validación de Secuencialidad de Fases
    phase_keys = list(phases.keys())
    in_progress_idx = -1
    in_progress_count = 0

    for i, pk in enumerate(phase_keys):
        if phases[pk] == "IN_PROGRESS":
            in_progress_count += 1
            in_progress_idx = i

    if in_progress_count > 1:
        return False, "Solidity Guard: Multi-fase detectada. Se requiere foco atómico."
        
    if in_progress_idx != -1:
        # Verificar que todas las fases anteriores estén APPROVED
        for i in range(in_progress_idx):
            if phases[phase_keys[i]] != "APPROVED":
                return False, f"Solidity Guard: Bloqueo de fase. {phase_keys[i]} debe estar APPROVED."
                
    if in_progress_count == 0:
         return False, "Solidity Guard: Ninguna fase activa. Use kanban-solidity-gate."

    # --- 5. STARK-SOLIDITY ENFORCEMENT (Verificación Física DAST) ---
    
    # Validación M1: Contrato Maestro
    if phases.get("M1") == "APPROVED":
        if not (Path(target_project) / "PRP_CONTRACT.json").exists():
            return False, "DAST Violation: M1 aprobada pero falta PRP_CONTRACT.json físico."

    # Validación M2: Planos Arquitectónicos
    if phases.get("M2") == "APPROVED":
        arch_docs = list((Path(target_project) / "DOCS" / "ARCH").glob("*.md"))
        if not arch_docs:
            return False, "DAST Violation: M2 aprobada pero no hay evidencia en DOCS/ARCH/."

    # Validación M3/M4: Reportes de Construcción/QA
    current_phase = phase_keys[in_progress_idx]
    if current_phase in ["M3", "M4"] and requested_skill in ["project-management", "kanban-solidity-gate"]:
        if not (Path(target_project) / "LOGS" / "BUILD_REPORT.json").exists():
            return False, f"DAST Violation: Cierre en {current_phase} denegado sin BUILD_REPORT.json."

    return True, "State Validated"