"""
skill_engine.py — CLI unificado para ejecutar cualquier skill de dasafo_FACTORY (v3.4.0-S).
ADR: Industrial Core v3.4.0-S. Implementa DAST (Disk-as-Source-of-Truth) y Double-Gating.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
import uuid
import time
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

# Path resolution for v3.4.0-S (Modular Toolbox)
FACTORY_ROOT = Path(__file__).resolve().parent
SKILL_LIBRARY_DIR = FACTORY_ROOT / "06_SKILL_LIBRARY"

# Inject root in sys.path for skill_schema imports
if str(FACTORY_ROOT) not in sys.path:
    sys.path.insert(0, str(FACTORY_ROOT))

try:
    from skill_schema import SkillInput, SkillOutput
except ImportError:
    from .skill_schema import SkillInput, SkillOutput

# Caché en memoria para evitar I/O de disco
_MODULE_CACHE = {}

def pre_flight_sync(target_project: str):
    """
    Sincronización Atómica (DAST): El Disco manda sobre el Registro.
    Asegura que el registry.json refleje la realidad física antes de cualquier ejecución.
    """
    project_path = Path(target_project)
    tasks_root = project_path / "TASKS"
    registry_file = tasks_root / "registry.json"
    
    if not tasks_root.exists() or not registry_file.exists():
        return

    folders = {"PENDING": "01_PENDING", "IN_PROGRESS": "02_IN_PROGRESS", "COMPLETED": "03_COMPLETED"}
    physical_tasks = []

    for status, folder_name in folders.items():
        folder_path = tasks_root / folder_name
        if folder_path.exists():
            for task_file in folder_path.glob("*.json"):
                try:
                    with open(task_file, 'r', encoding='utf-8') as f:
                        task_data = json.load(f)
                        task_data["status"] = status  # Forzamos el estado según la carpeta física 
                        physical_tasks.append(task_data)
                except: continue

    with open(registry_file, 'w', encoding='utf-8') as f:
        json.dump(physical_tasks, f, indent=2)

def inject_infra_env(target_project: Optional[str] = None) -> bool:
    """
    Inyección de Permisos de Fase (Double-Gating).
    Carga variables de INFRA e inyecta la fase autorizada actual en el entorno.
    """
    infra_env = FACTORY_ROOT.parent / "INFRA" / ".env"
    if infra_env.exists():
        load_dotenv(infra_env)
    
    # --- Punto 3: Double-Gating Authorization ---
    if target_project:
        state_path = Path(target_project) / "PROJECT_STATE.json"
        if state_path.exists():
            try:
                with open(state_path) as f:
                    state = json.load(f)
                    # El agente recibe permiso explícito de la fase actual detectada en disco 
                    os.environ["CURRENT_AUTHORIZED_PHASE"] = state.get("current_phase", "M1")
            except:
                os.environ["CURRENT_AUTHORIZED_PHASE"] = "M1"
    return True

def _resolve_run_module(skill: str) -> Path:
    run_path = SKILL_LIBRARY_DIR / skill / "run.py"
    if not run_path.exists():
        raise FileNotFoundError(f"Error Industrial Core: No se encontró run.py para '{skill}'.")
    return run_path

def _load_and_run(run_path: Path, skill_input: SkillInput) -> SkillOutput:
    module_name = run_path.parent.name
    if module_name not in _MODULE_CACHE:
        spec = importlib.util.spec_from_file_location(f"skill_{module_name}", run_path)
        if spec is None or spec.loader is None:
            raise ImportError(f"No se pudo cargar el módulo: {run_path}")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        _MODULE_CACHE[module_name] = module
    return _MODULE_CACHE[module_name].run(skill_input)

def execute(
    agent: str,
    skill: str,
    params: dict,
    target_project: Optional[str] = None,
    correlation_id: Optional[str] = None,
    isolate: bool = False,
) -> SkillOutput:
    """Punto de entrada con Guardián de Solidez y Sincronización v3.4.0-S."""
    
    if target_project is None:
        target_project = os.environ.get("TARGET_PROJECT", ".")

    # 🔄 1. Sincronización Pre-flight (DAST)
    pre_flight_sync(target_project)

    # 🔌 2. Inyectar conectividad INFRA y Permisos de Fase (Double-Gating)
    inject_infra_env(target_project)

    if isolate:
        os.environ["CLEAN_SESSION"] = "True"
    if correlation_id is None:
        correlation_id = str(uuid.uuid4())[:8]

    skill_input = SkillInput(
        agent=agent,
        skill=skill,
        params=params,
        target_project=target_project,
        correlation_id=correlation_id,
        isolation_guard=bool(os.environ.get("CLEAN_SESSION", False))
    )

    try:
        run_path = _resolve_run_module(skill)
        
        # 🧪 Snapshot antes de ejecución
        state_path = Path(target_project) / "PROJECT_STATE.json"
        before_phases = {}
        if state_path.exists():
            with open(state_path) as f:
                before_phases = json.load(f).get("phases", {})

        # 🚀 Ejecución de Skill
        output = _load_and_run(run_path, skill_input)

        # 🧬 Solidity Guard v3.4.0-S: Verificación Post-Ejecución 
        if output.success:
            # Verificación de Artefactos Físicos
            if output.artifacts:
                for art in output.artifacts:
                    art_path = Path(art) if Path(art).is_absolute() else Path(target_project) / art
                    if not art_path.exists():
                        output.success = False
                        output.error = f"Solidity Guard: Artefacto ausente en disco: {art_path}"
                        return output

            # Validación de Salto de Fase
            if state_path.exists():
                with open(state_path) as f:
                    after_phases = json.load(f).get("phases", {})
                
                before_done = sum(1 for v in before_phases.values() if v == "APPROVED")
                after_done = sum(1 for v in after_phases.values() if v == "APPROVED")
                
                if after_done > before_done + 1:
                    output.success = False
                    output.error = f"Solidity Breach: Salto de fase detectado ({before_done} -> {after_done})."
        
        return output
        
    except Exception as exc:
        return SkillOutput.failure(agent, skill, f"Error v3.4.0-S: {exc}", correlation_id)


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
        isolate=args.isolate,
    )
    print(output.to_json())
    sys.exit(0 if output.success else 1)
