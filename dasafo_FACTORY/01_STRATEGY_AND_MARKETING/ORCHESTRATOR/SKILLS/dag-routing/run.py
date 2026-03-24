"""
run.py — Skill: DAG Routing & Task Decomposition
Agent: ORCHESTRATOR

Lee un intent y lo descompone en tareas JSON escritas en TASKS/01_PENDING/ del TARGET_PROJECT.
Cada tarea incluye: task_id, assigned_to, depends_on, instructions.
"""

from __future__ import annotations

import json
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "00_GLOBAL_KNOWLEDGE"))
from skill_schema import SkillInput, SkillOutput  # noqa: E402


def _build_task_id(prefix: str = "T") -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    short_id = str(uuid.uuid4())[:4].upper()
    return f"{prefix}-{timestamp}-{short_id}"


def _write_task_file(pending_dir: Path, task: dict) -> Path:
    """Escribe un task JSON en 01_PENDING/ y devuelve la ruta."""
    pending_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{task['task_id']}.json"
    task_path = pending_dir / filename
    task_path.write_text(json.dumps(task, indent=2, ensure_ascii=False), encoding="utf-8")
    return task_path


def run(skill_input: SkillInput) -> SkillOutput:
    agent = skill_input.agent
    skill = skill_input.skill
    cid = skill_input.correlation_id

    intent = skill_input.params.get("intent")
    phases = skill_input.params.get("phases")  # opcional: lista de fases manuales

    if not intent and not phases:
        return SkillOutput.failure(
            agent, skill,
            "Se requiere al menos 'intent' (string) o 'phases' (lista de fases) en params.",
            cid,
        )

    # Si el usuario no proporciona fases explícitas, usamos el DAG estándar de la factory
    if not phases:
        phases = [
            {
                "phase_name": "DESIGN",
                "parallel": False,
                "tasks": [
                    {
                        "assigned_to": "ARCHITECT",
                        "instructions": f"Diseñar la arquitectura técnica para: {intent}",
                        "depends_on": [],
                    }
                ],
            },
            {
                "phase_name": "PRODUCTION",
                "parallel": True,
                "tasks": [
                    {
                        "assigned_to": "BACKEND_DEV",
                        "instructions": f"Implementar la lógica de servidor para: {intent}",
                        "depends_on": ["DESIGN"],
                    },
                    {
                        "assigned_to": "FRONTEND_DEV",
                        "instructions": f"Implementar la interfaz de usuario para: {intent}",
                        "depends_on": ["DESIGN"],
                    },
                ],
            },
            {
                "phase_name": "QA",
                "parallel": False,
                "tasks": [
                    {
                        "assigned_to": "QA_TESTER",
                        "instructions": f"Validar la entrega completa para: {intent}",
                        "depends_on": ["PRODUCTION"],
                    }
                ],
            },
        ]

    # Determinamos el directorio de escritura
    target_project = skill_input.target_project or ""
    pending_dir = Path(target_project) / "TASKS" / "01_PENDING" if target_project else Path("TASKS/01_PENDING")

    written_files: list[str] = []
    all_tasks: list[dict] = []

    for phase in phases:
        phase_name = phase.get("phase_name", "UNKNOWN")
        for task_def in phase.get("tasks", []):
            task_id = _build_task_id(prefix=phase_name[:3].upper())
            task = {
                "task_id": task_id,
                "assigned_to": task_def.get("assigned_to", "UNASSIGNED"),
                "phase": phase_name,
                "parallel": phase.get("parallel", False),
                "depends_on": task_def.get("depends_on", []),
                "instructions": task_def.get("instructions", ""),
                "created_at": datetime.now(timezone.utc).isoformat(),
                "correlation_id": cid,
                "status": "PENDING",
            }
            task_path = _write_task_file(pending_dir, task)
            written_files.append(str(task_path))
            all_tasks.append(task)

    return SkillOutput(
        success=True,
        agent=agent,
        skill=skill,
        result={
            "intent": intent,
            "total_tasks_created": len(all_tasks),
            "tasks": all_tasks,
        },
        artifacts=written_files,
        correlation_id=cid,
    )
