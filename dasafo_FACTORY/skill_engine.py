"""
skill_engine.py — CLI unificado para ejecutar cualquier skill de dasafo_FACTORY (v3.4.0-S).

ADR: Industrial Core v3.4.0-S. Todas las skills residen en 06_SKILL_LIBRARY/.
El motor carga run.py dinámicamente basándose en el nombre de la skill del Top 18 Hub.
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

def _resolve_run_module(skill: str) -> Path:
    """Devuelve la ruta absoluta al run.py de la skill en la librería central."""
    run_path = SKILL_LIBRARY_DIR / skill / "run.py"
    if not run_path.exists():
        raise FileNotFoundError(
            f"Error Industrial Core: No se encontró run.py para la skill '{skill}'.\n"
            f"Ruta esperada en la librería: {run_path}"
        )
    return run_path

def _load_and_run(run_path: Path, skill_input: SkillInput) -> SkillOutput:
    """Carga dinámicamente run.py (con caché) y ejecuta su función run()."""
    module_name = run_path.parent.name
    
    # Si el módulo no está en caché, lo cargamos desde el disco
    if module_name not in _MODULE_CACHE:
        spec = importlib.util.spec_from_file_location(f"skill_{module_name}", run_path)
        if spec is None or spec.loader is None:
            raise ImportError(f"No se pudo cargar el módulo: {run_path}")
        
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        if not hasattr(module, "run"):
            raise AttributeError(
                f"El módulo {run_path} no tiene una función 'run(input: SkillInput) -> SkillOutput'."
            )
        # Guardamos en caché
        _MODULE_CACHE[module_name] = module

    # Ejecutamos desde la caché
    return _MODULE_CACHE[module_name].run(skill_input)

def execute(
    agent: str,
    skill: str,
    params: dict,
    target_project: Optional[str] = None,
    correlation_id: Optional[str] = None,
    isolate: bool = False,
) -> SkillOutput:
    """Punto de entrada programático. v3.4.0-S compatible."""
    if isolate:
        os.environ["CLEAN_SESSION"] = "True"
    if correlation_id is None:
        correlation_id = str(uuid.uuid4())[:8]

    if target_project is None:
        target_project = os.environ.get("TARGET_PROJECT", ".")

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
        
        # 🧪 Snapshot state before execution (Solidity Guard)
        state_path = Path(target_project) / "PROJECT_STATE.json" if target_project else None
        before_phases = {}
        
        if state_path and state_path.exists():
            try:
                with open(state_path) as f:
                    before_phases = json.load(f).get("phases", {})
            except json.JSONDecodeError as e:
                return SkillOutput.failure(agent, skill, f"Solidity Guard Fatal: PROJECT_STATE.json corrupto. {e}", correlation_id)
            except Exception as e:
                return SkillOutput.failure(agent, skill, f"Solidity Guard Fatal: Error leyendo estado. {e}", correlation_id)

        # Ejecución
        output = _load_and_run(run_path, skill_input)

        # 🧬 Solidity Guard v3.4.0-S: Post-Execution Verification
        if output.success:
            # 1. Physical Artifact Verification
            if output.artifacts:
                missing = []
                for art in output.artifacts:
                    art_path = Path(art)
                    if not art_path.is_absolute():
                        art_path = Path(target_project) / art
                    if not art_path.exists():
                        missing.append(str(art_path))
                if missing:
                    output.success = False
                    output.error = f"Solidity Guard Violation: Artifacts missing from disk: {', '.join(missing)}"
                    return output

            # 2. Phase-Gate Enforcement (Aduana Universal)
            if state_path and state_path.exists():
                try:
                    with open(state_path) as f:
                        after_phases = json.load(f).get("phases", {})
                    
                    before_done = sum(1 for v in before_phases.values() if v == "APPROVED")
                    after_done = sum(1 for v in after_phases.values() if v == "APPROVED")
                    
                    if after_done > before_done + 1:
                        output.success = False
                        output.error = (
                            f"Aduana Solidity Breach: Phase jump detected ({before_done} -> {after_done}). "
                            "Authorization must be physical and sequential in PROJECT_STATE.json."
                        )
                except Exception as e:
                    output.success = False
                    output.error = f"Solidity Guard Fatal: Post-execution check failed. {e}"
        
        return output
        
    except (ValueError, FileNotFoundError, AttributeError, ImportError) as exc:
        return SkillOutput.failure(
            agent=agent,
            skill=skill,
            error=str(exc),
            correlation_id=correlation_id,
        )
    except Exception as exc:
        return SkillOutput.failure(
            agent=agent,
            skill=skill,
            error=f"Unexpected Error v3.4.0-S: {exc}",
            correlation_id=correlation_id,
        )

def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="skill_engine",
        description="Industrial Core Engine - dasafo_FACTORY v3.4.0-S",
    )
    parser.add_argument("--agent", required=True, help="ID del agente que invoca")
    parser.add_argument("--skill", required=True, help="Nombre de la skill en 06_SKILL_LIBRARY")
    parser.add_argument("--input", default="{}", help="Parámetros como JSON string.")
    parser.add_argument("--target-project", default=None, help="Ruta al proyecto activo.")
    parser.add_argument("--correlation-id", default=None, help="ID de correlación.")
    parser.add_argument("--isolate", action="store_true", help="Activar isolation_guard (Clean Session)")
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
        isolate=args.isolate,
    )
    print(output.to_json())
    sys.exit(0 if output.success else 1)
