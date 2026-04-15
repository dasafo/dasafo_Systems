# dasafo_FACTORY/session_hook.py
import json
import logging
import os
from pathlib import Path

# Configuración de logging industrial
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AduanaUniversal_v5.0")

# 🚦 Herramientas autorizadas para saltar la validación de fase (Solo diagnóstico puro)
# IMPORTANTE: Solo herramientas que NO modifican código, logs ni estado del proyecto.
# ADR: skill-refactor-pro, autonomous-feedback-analyzer, context-pruning-sieve,
#      hallucination-guardrail, research-manager REMOVIDOS del bypass (v5.0.4 Security Patch).
BYPASS_SKILLS = {
    "kanban-solidity-gate",            # Diagnóstico: solo lectura del estado
    "factory-doctor",                  # Diagnóstico: recuperación forense (read-only)
    "registry-manager",                # Infraestructura: gestión atómica del registro
    "factory-audit-pro",               # Auditoría: solo lectura
    "project-backbone-validator",      # Validación: solo lectura de estructura
    "deployment-health-check",         # Monitoreo: solo lectura de endpoints
}

def verify_project_state(target_project: str, requested_skill: str, agent: str = None) -> tuple[bool, str]:
    """
    Protocol-Level Session Hook (Aduana Universal v5.0-MCP).
    Implementa DAST (Disk-as-Source-of-Truth) y Double-Gating Nativo. 
    """
    
    # 1. Bypass Inmediato para herramientas de gestión e infraestructura
    if requested_skill in BYPASS_SKILLS:
        return True, "Bypass: Skill de gestión permitida."

    # 2. Verificación de Existencia del Proyecto
    state_path = Path(target_project) / "PROJECT_STATE.json"
    if not state_path.exists():
        return False, "Solidity Guard: PROJECT_STATE.json ausente. El proyecto no ha sido inicializado físicamente."
        
    try:
        with open(state_path, "r", encoding="utf-8") as f:
            state_data = json.load(f)
    except Exception as e:
        return False, f"Solidity Guard: Error crítico leyendo PROJECT_STATE.json: {e}"
    
    phases = state_data.get("phases", {})
    if not phases:
        return False, "Solidity Guard: No se definen 'phases' en el estado del proyecto."

    # --- 3. LÓGICA DE DOUBLE-GATING (Autorización Distribuida v5.0-MCP) ---
    # Permite que un agente opere si posee una SPEC_LITE física asignada en el disco.
    # Lista sincronizada con el AGENT_SKILL_MAPPING.md
    authorized_peons = [
        "ORCHESTRATOR", "PRODUCT_OWNER", "MARKETING_GROWTH",           # Hub 01
        "ARCHITECT", "RESEARCH_AGENT",                                 # Hub 02
        "AI_ENGINEER", "BACKEND_DEV", "FRONTEND_DEV", "DB_MASTER", "DATA_SCIENTIST", # Hub 03
        "QA_TESTER", "SECURITY_AUDITOR", "DOCS_MASTER",                # Hub 04
        "DEVOPS_SRE", "DEPLOYMENT_MONITOR", "FACTORY_EVOLVER", "MEMORY_OPTIMIZER" # Hub 05
    ]

    if agent in authorized_peons:
        tasks_dir = Path(target_project) / "TASKS"
        # Búsqueda prioritaria en IN_PROGRESS (estándar v5.0 Auto-Start)
        possible_specs = [
            tasks_dir / "02_IN_PROGRESS" / "SPEC_LITE.json",
            tasks_dir / "01_PENDING" / "SPEC_LITE.json",
            tasks_dir / "01_PENDING" / "EMERGENCY_SPEC.json",
            tasks_dir / "SPEC_LITE.json"
        ]
        
        for sp in possible_specs:
            if sp.exists():
                try:
                    with open(sp, "r") as f:
                        spec = json.load(f)
                        assigned = spec.get("metadata", {}).get("assigned_agent")
                        # Si el agente es el dueño de la tarea física, se abre la aduana
                        if assigned == agent:
                            return True, f"Double-Gate: Agente {agent} autorizado por evidencia física en {sp.name}."
                except:
                    continue

    # 4. Validación de Secuencialidad de Fases
    phase_keys = list(phases.keys())
    in_progress_idx = -1
    in_progress_count = 0

    for i, pk in enumerate(phase_keys):
        if phases[pk] == "IN_PROGRESS":
            in_progress_count += 1
            in_progress_idx = i

    if in_progress_count > 1:
        return False, "Solidity Guard: Multi-fase detectada. Se requiere foco atómico (solo una fase IN_PROGRESS)."
        
    if in_progress_idx != -1:
        # Bloqueo: No se puede trabajar en una fase si las anteriores no están APPROVED
        for i in range(in_progress_idx):
            if phases[phase_keys[i]] != "APPROVED":
                return False, f"Solidity Guard: Bloqueo de fase. {phase_keys[i]} debe estar APPROVED antes de avanzar."
                
    if in_progress_count == 0:
         return False, "Solidity Guard: Ninguna fase activa. El Director debe activar una fase vía kanban-solidity-gate."

    # --- 5. STARK-SOLIDITY ENFORCEMENT (DAST) ---
    
    # Validación M1: Contrato Maestro físico
    if phases.get("M1") == "APPROVED":
        if not (Path(target_project) / "PRP_CONTRACT.json").exists():
            return False, "DAST Violation: M1 aparece como APPROVED pero falta el PRP_CONTRACT.json físico."

    # Validación M1: Firma Humana Obligatoria
    if phases.get("M1") == "APPROVED":
        approval_file = Path(target_project) / "DOCS" / "USER" / "APPROVAL_M1.md"
        if not approval_file.exists():
            return False, "HITL Violation: Falta APPROVAL_M1.md firmado por el Director en DOCS/USER/."
        
        with open(approval_file, "r") as f:
            if "Status: APPROVED" not in f.read():
                return False, "Solidity Guard: El archivo de aprobación existe pero no ha sido firmado con 'Status: APPROVED'."

    # Validación M2: Planos Arquitectónicos
    if phases.get("M2") == "APPROVED":
        arch_docs = list((Path(target_project) / "DOCS" / "ARCH").glob("*.md"))
        if not arch_docs:
            return False, "DAST Violation: Fase M2 aprobada sin planos técnicos en DOCS/ARCH/."

    return True, "State Validated"