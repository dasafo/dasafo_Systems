"""
run.py — Skill: RA-Level Agile Orchestration
Agent: ORCHESTRATOR

Enruta un task al agente/departamento correcto según su nivel de Requirement Analysis (RA-0 a RA-5).
Output: JSON con assigned_agent, pipeline_phase e instructions de despacho.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Permite importar skill_schema desde cualquier CWD
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "00_GLOBAL_KNOWLEDGE"))
from skill_schema import SkillInput, SkillOutput  # noqa: E402

# Mapa RA-level → metadatos de enrutamiento
_RA_ROUTING_MAP = {
    "RA-0": {
        "assigned_agents": ["research_agent"],
        "phase": "00_IDEATION",
        "description": "Ideación inicial. El Research Agent valida la viabilidad técnica.",
        "parallelizable": False,
    },
    "RA-1": {
        "assigned_agents": ["research_agent", "architect"],
        "phase": "00_IDEATION",
        "description": "Discovery profundo. Research + Architect definen el mapa técnico.",
        "parallelizable": True,
    },
    "RA-2": {
        "assigned_agents": ["architect"],
        "phase": "01_DESIGN",
        "description": "Diseño de sistema. Architect produce ARCHITECTURE.md y DTOs.",
        "parallelizable": False,
    },
    "RA-3": {
        "assigned_agents": ["backend_dev", "frontend_dev", "data_scientist", "db_master"],
        "phase": "03_PRODUCTION",
        "description": "Ejecución principal. Producción activa (máx. 3 streams paralelos si el Architect aprobó el diseño desacoplado).",
        "parallelizable": True,
        "max_parallel_streams": 3,
    },
    "RA-4": {
        "assigned_agents": ["qa_tester", "security_auditor"],
        "phase": "04_COMPLIANCE_AND_QUALITY",
        "description": "Testing y seguridad. QA y Security Auditor certifican el entregable.",
        "parallelizable": True,
    },
    "RA-5": {
        "assigned_agents": ["devops_sre", "memory_optimizer"],
        "phase": "05_OPERATIONS",
        "description": "Validado. DevOps despliega y Memory Optimizer archiva el contexto.",
        "parallelizable": False,
    },
}


def run(skill_input: SkillInput) -> SkillOutput:
    agent = skill_input.agent
    skill = skill_input.skill
    cid = skill_input.correlation_id

    task_description = skill_input.params.get("task")
    ra_level = skill_input.params.get("level", "").upper().replace(" ", "-")

    # Validación de entrada
    if not task_description:
        return SkillOutput.failure(agent, skill, "Param 'task' es requerido.", cid)

    if not ra_level:
        return SkillOutput.failure(agent, skill, "Param 'level' es requerido (ej: 'RA-3').", cid)

    if ra_level not in _RA_ROUTING_MAP:
        valid = list(_RA_ROUTING_MAP.keys())
        return SkillOutput.failure(
            agent, skill,
            f"Nivel RA inválido: '{ra_level}'. Válidos: {valid}",
            cid,
        )

    routing = _RA_ROUTING_MAP[ra_level]

    result = {
        "ra_level": ra_level,
        "task": task_description,
        "assigned_agents": routing["assigned_agents"],
        "pipeline_phase": routing["phase"],
        "description": routing["description"],
        "parallelizable": routing["parallelizable"],
        "dispatch_instructions": (
            f"Despachar '{task_description}' a {routing['assigned_agents']} "
            f"en fase {routing['phase']}. "
            + (
                f"Máximo {routing['max_parallel_streams']} streams paralelos."
                if routing.get("max_parallel_streams")
                else ""
            )
        ),
    }

    return SkillOutput(
        success=True,
        agent=agent,
        skill=skill,
        result=result,
        correlation_id=cid,
    )
