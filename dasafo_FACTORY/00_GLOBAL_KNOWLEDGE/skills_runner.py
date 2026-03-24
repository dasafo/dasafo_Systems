"""
skills_runner.py — CLI unificado para ejecutar cualquier skill de dasafo_FACTORY.

ADR: Se usa importlib para cargar run.py dinámicamente según agente+skill,
evitando hardcodear rutas. Esto permite añadir nuevas skills sin modificar este archivo.

Uso:
    python skills_runner.py --agent orchestrator --skill ra-agile-orchestration \
        --input '{"task": "Create login page", "level": "RA-3"}'
    
    python skills_runner.py --agent db_master --skill sql-performance-tuner \
        --input '{"query": "SELECT * FROM users"}'
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
import uuid
from pathlib import Path
from typing import Optional

# GLOBAL_KNOWLEDGE_DIR: directorio donde vive este script (00_GLOBAL_KNOWLEDGE/)
# FACTORY_ROOT: directorio padre dasafo_FACTORY/ — base para las rutas de agentes
GLOBAL_KNOWLEDGE_DIR = Path(__file__).resolve().parent
FACTORY_ROOT = GLOBAL_KNOWLEDGE_DIR.parent
sys.path.insert(0, str(GLOBAL_KNOWLEDGE_DIR))

from skill_schema import SkillInput, SkillOutput  # noqa: E402

# Mapa: alias_agente → ruta relativa a FACTORY_ROOT de su carpeta SKILLS/
AGENT_SKILLS_MAP: dict[str, str] = {
    "orchestrator":     "01_STRATEGY_AND_MARKETING/ORCHESTRATOR/SKILLS",
    "product_owner":    "01_STRATEGY_AND_MARKETING/PRODUCT_OWNER/SKILLS",
    "marketing_growth": "01_STRATEGY_AND_MARKETING/MARKETING_GROWTH/SKILLS",
    "architect":        "02_ARCHITECTURE_AND_RESEARCH/ARCHITECT/SKILLS",
    "research_agent":   "02_ARCHITECTURE_AND_RESEARCH/RESEARCH_AGENT/SKILLS",
    "backend_dev":      "03_PRODUCTION/BACKEND_DEV/SKILLS",
    "frontend_dev":     "03_PRODUCTION/FRONTEND_DEV/SKILLS",
    "data_scientist":   "03_PRODUCTION/DATA_SCIENTIST/SKILLS",
    "db_master":        "03_PRODUCTION/DB_MASTER/SKILLS",
    "docs_master":      "04_COMPLIANCE_AND_QUALITY/DOCS_MASTER/SKILLS",
    "qa_tester":        "04_COMPLIANCE_AND_QUALITY/QA_TESTER/SKILLS",
    "security_auditor": "04_COMPLIANCE_AND_QUALITY/SECURITY_AUDITOR/SKILLS",
    "devops_sre":       "05_OPERATIONS/DEVOPS_SRE/SKILLS",
    "memory_optimizer": "05_OPERATIONS/MEMORY_OPTIMIZER/SKILLS",
    "deployment_monitor": "05_OPERATIONS/DEPLOYMENT_MONITOR/SKILLS",
    "factory_evolver":  "05_OPERATIONS/FACTORY_EVOLVER/SKILLS",
}


def _resolve_run_module(agent: str, skill: str) -> Path:
    """Devuelve la ruta absoluta al run.py de la skill solicitada."""
    agent_key = agent.lower()
    if agent_key not in AGENT_SKILLS_MAP:
        raise ValueError(
            f"Agente desconocido: '{agent}'. "
            f"Agentes disponibles: {list(AGENT_SKILLS_MAP.keys())}"
        )
    skills_dir = FACTORY_ROOT / AGENT_SKILLS_MAP[agent_key]
    run_path = skills_dir / skill / "run.py"
    if not run_path.exists():
        raise FileNotFoundError(
            f"No se encontró run.py para la skill '{skill}' del agente '{agent}'.\n"
            f"Ruta esperada: {run_path}"
        )
    return run_path


def _load_and_run(run_path: Path, skill_input: SkillInput) -> SkillOutput:
    """Carga dinámicamente run.py y ejecuta su función run(SkillInput) → SkillOutput."""
    spec = importlib.util.spec_from_file_location("skill_module", run_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"No se pudo cargar el módulo: {run_path}")
    module = importlib.util.module_from_spec(spec)
    # Permite que run.py importe skill_schema sin repetir sys.path
    sys.path.insert(0, str(run_path.parent.parent.parent.parent))
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    if not hasattr(module, "run"):
        raise AttributeError(
            f"El módulo {run_path} no tiene una función 'run(input: SkillInput) -> SkillOutput'."
        )
    return module.run(skill_input)  # type: ignore[return-value]


def execute(
    agent: str,
    skill: str,
    params: dict,
    target_project: Optional[str] = None,
    correlation_id: Optional[str] = None,
) -> SkillOutput:
    """
    Punto de entrada programático (sin CLI). Útil para llamadas inter-agente.
    """
    if correlation_id is None:
        correlation_id = str(uuid.uuid4())[:8]

    if target_project is None:
        target_project = os.environ.get("TARGET_PROJECT")

    skill_input = SkillInput(
        agent=agent,
        skill=skill,
        params=params,
        target_project=target_project,
        correlation_id=correlation_id,
    )

    try:
        run_path = _resolve_run_module(agent, skill)
        return _load_and_run(run_path, skill_input)
    except (ValueError, FileNotFoundError, AttributeError, ImportError) as exc:
        return SkillOutput.failure(
            agent=agent,
            skill=skill,
            error=str(exc),
            correlation_id=correlation_id,
        )
    except Exception as exc:  # noqa: BLE001
        return SkillOutput.failure(
            agent=agent,
            skill=skill,
            error=f"Error inesperado: {type(exc).__name__}: {exc}",
            correlation_id=correlation_id,
        )


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="skills_runner",
        description="Motor de ejecución de Skills de dasafo_FACTORY.",
    )
    parser.add_argument("--agent", required=True, help="ID del agente (ej: orchestrator)")
    parser.add_argument("--skill", required=True, help="Nombre de la skill (ej: ra-agile-orchestration)")
    parser.add_argument(
        "--input",
        default="{}",
        help="Parámetros de la skill como JSON string (ej: '{\"task\": \"...\"}').",
    )
    parser.add_argument(
        "--target-project",
        default=None,
        help="Ruta al proyecto activo. Sobrescribe $TARGET_PROJECT.",
    )
    parser.add_argument("--correlation-id", default=None, help="ID de correlación para trazabilidad.")
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    try:
        params = json.loads(args.input)
    except json.JSONDecodeError as e:
        print(json.dumps({"success": False, "error": f"--input no es JSON válido: {e}"}))
        sys.exit(1)

    output = execute(
        agent=args.agent,
        skill=args.skill,
        params=params,
        target_project=args.target_project,
        correlation_id=args.correlation_id,
    )
    print(output.to_json())
    sys.exit(0 if output.success else 1)
