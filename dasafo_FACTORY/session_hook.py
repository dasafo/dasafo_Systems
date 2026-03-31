import json
import logging
import os
from pathlib import Path

# Configuración de logging industrial
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AduanaUniversal")

# Skills autorizadas para bypass (RCP de proyecto, utilidades de sistema y gestión de ADN) 
BYPASS_SKILLS = {
    "kanban-solidity-gate",       #
    "factory-doctor",             # 🚑 Autorizado para RCP de Proyecto
    "registry-manager",           # 📦 Gestión atómica de tareas
    "agentic-thought-secret-scanner", #
    "factory-audit-pro",          #
    "prp-generator",              #
    "arxiv-technical-digest",     #
    "apify-trend-analysis",       #
    "hallucination-guardrail",    #
    "autonomous-feedback-analyzer", #
    "project-management",         #
    "deployment-health-check",    # 📡 Monitoreo Sentinel
    "context-pruning-sieve",      # 🧠 Optimización de memoria
    "skill-refactor-pro"          # 🧬 Evolución autónoma de ADN (v3.4.0-S)
}

def verify_project_state(target_project: str, requested_skill: str, agent: str = None) -> tuple[bool, str]:
    """
    Protocol-Level Session Hook (Aduana Universal v3.4.0-S).
    Implementa DAST (Disk-as-Source-of-Truth) y Double-Gating para agentes autónomos. 
    """
    
    # 1. Bypass Inmediato para herramientas de gestión e infraestructura
    if requested_skill in BYPASS_SKILLS:
        return True, "Bypass skill allowed."

    # 2. Verificación de Integridad del Estado Físico
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

    # --- 3. LÓGICA DE DOUBLE-GATING (Autorización Distribuida v3.4.0-S) ---
    # Permite que CUALQUIER agente autónomo opere si posee una SPEC_LITE física asignada
    # Se expande la lista para cubrir todos los Hubs de la factoría (01-05)
    authorized_peons = [
        "BACKEND_DEV", "FRONTEND_DEV", "DB_MASTER", "DATA_SCIENTIST", # Producción
        "QA_TESTER", "SECURITY_AUDITOR", "RESEARCH_AGENT",           # Compliance
        "DEVOPS_SRE", "FACTORY_EVOLVER", "MEMORY_OPTIMIZER",         # Operations
        "PRODUCT_OWNER", "MARKETING_GROWTH", "DOCS_MASTER"           # Strategy
    ]

    if agent in authorized_peons:
        spec_path = Path(target_project) / "TASKS" / "SPEC_LITE.json"
        if spec_path.exists():
            try:
                with open(spec_path, "r") as f:
                    spec = json.load(f)
                    assigned = spec.get("metadata", {}).get("assigned_agent")
                    # Si la tarea en el disco está asignada a este agente, se concede bypass de fase
                    if assigned == agent:
                        return True, f"Double-Gate: Agente {agent} autorizado por SPEC_LITE física en disco."
            except:
                pass 
    # -----------------------------------------------------------------------

    # 4. Validación de Secuencialidad de Fases (Foco Atómico)
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