"""
run.py — Skill: Task Dependency Diagnostic
Agent: ORCHESTRATOR

Escanea TASKS/01_PENDING/ y TASKS/02_IN_PROGRESS/ del TARGET_PROJECT.
Detecta: stale locks (>30min sin modificar), dependencias circulares, tareas bloqueadas.
Output: reporte JSON + DEPENDENCY_DIAGNOSTIC.md.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "00_GLOBAL_KNOWLEDGE"))
from skill_schema import SkillInput, SkillOutput  # noqa: E402

STALE_LOCK_THRESHOLD_MINUTES = 30


def _load_tasks_from_dir(directory: Path) -> list[dict]:
    """Carga todos los archivos .json de un directorio de tareas."""
    if not directory.exists():
        return []
    tasks = []
    for task_file in directory.glob("*.json"):
        try:
            data = json.loads(task_file.read_text(encoding="utf-8"))
            data["_file_path"] = str(task_file)
            data["_modified_at"] = datetime.fromtimestamp(
                task_file.stat().st_mtime, tz=timezone.utc
            ).isoformat()
            tasks.append(data)
        except (json.JSONDecodeError, OSError):
            pass  # Archivo corrupto, ignorar con warning
    return tasks


def _detect_stale_locks(in_progress: list[dict]) -> list[dict]:
    """Detecta tareas en progreso sin modificación en más de STALE_LOCK_THRESHOLD_MINUTES."""
    stale = []
    now = datetime.now(timezone.utc)
    for task in in_progress:
        modified_at_str = task.get("_modified_at", "")
        try:
            modified_at = datetime.fromisoformat(modified_at_str)
            idle_minutes = (now - modified_at).total_seconds() / 60
            if idle_minutes > STALE_LOCK_THRESHOLD_MINUTES:
                stale.append({
                    "task_id": task.get("task_id", "UNKNOWN"),
                    "assigned_to": task.get("assigned_to", "UNKNOWN"),
                    "idle_minutes": round(idle_minutes, 1),
                    "diagnosis": "STALE_LOCK",
                    "action": "PURGE_LOCK",
                })
        except (ValueError, TypeError):
            pass
    return stale


def _detect_blocked_tasks(pending: list[dict], resolved_phases: set[str]) -> list[dict]:
    """Detecta tareas en pending cuyos depends_on no han sido resueltos."""
    blocked = []
    for task in pending:
        unresolved_deps = [
            dep for dep in task.get("depends_on", [])
            if dep not in resolved_phases
        ]
        if unresolved_deps:
            blocked.append({
                "task_id": task.get("task_id", "UNKNOWN"),
                "assigned_to": task.get("assigned_to", "UNKNOWN"),
                "unresolved_dependencies": unresolved_deps,
                "diagnosis": "BLOCKED",
                "action": "WAIT_OR_ESCALATE",
            })
    return blocked


def _detect_circular_deps(pending: list[dict]) -> list[str]:
    """Detección simple de dependencias circulares por análisis de grafos DFS."""
    # Construimos un grafo: phase → tasks que dependen de ella
    dep_graph: dict[str, list[str]] = {}
    for task in pending:
        phase = task.get("phase", task.get("task_id", "UNKNOWN"))
        deps = task.get("depends_on", [])
        dep_graph[phase] = deps

    visited: set[str] = set()
    rec_stack: set[str] = set()
    circular: list[str] = []

    def dfs(node: str) -> bool:
        visited.add(node)
        rec_stack.add(node)
        for neighbor in dep_graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                circular.append(f"Ciclo detectado: {node} → {neighbor}")
                return True
        rec_stack.discard(node)
        return False

    for node in list(dep_graph.keys()):
        if node not in visited:
            dfs(node)

    return circular


def _write_diagnostic_report(target_dir: Path, report: dict) -> Path:
    """Escribe DEPENDENCY_DIAGNOSTIC.md en el proyecto objetivo."""
    target_dir.mkdir(parents=True, exist_ok=True)
    report_path = target_dir / "DEPENDENCY_DIAGNOSTIC.md"

    lines = [
        "# 🔍 Dependency Diagnostic Report",
        f"> Generated: {report['generated_at']}",
        "",
        f"## Summary",
        f"- **Pending tasks:** {report['total_pending']}",
        f"- **In-progress tasks:** {report['total_in_progress']}",
        f"- **Stale locks:** {len(report['stale_locks'])}",
        f"- **Blocked tasks:** {len(report['blocked_tasks'])}",
        f"- **Circular dependencies:** {len(report['circular_dependencies'])}",
        "",
    ]

    if report["stale_locks"]:
        lines.append("## ⏰ Stale Locks (Action: PURGE)")
        for lock in report["stale_locks"]:
            lines.append(f"- `{lock['task_id']}` → {lock['assigned_to']} (idle {lock['idle_minutes']}min)")
        lines.append("")

    if report["blocked_tasks"]:
        lines.append("## 🚧 Blocked Tasks (Action: WAIT/ESCALATE)")
        for blocked in report["blocked_tasks"]:
            deps = ", ".join(blocked["unresolved_dependencies"])
            lines.append(f"- `{blocked['task_id']}` → waiting for: {deps}")
        lines.append("")

    if report["circular_dependencies"]:
        lines.append("## 🔄 Circular Dependencies (Action: HUMAN INTERVENTION)")
        for cycle in report["circular_dependencies"]:
            lines.append(f"- {cycle}")
        lines.append("")

    if not any([report["stale_locks"], report["blocked_tasks"], report["circular_dependencies"]]):
        lines.append("## ✅ All Clear — No blockages detected.")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


def run(skill_input: SkillInput) -> SkillOutput:
    agent = skill_input.agent
    skill = skill_input.skill
    cid = skill_input.correlation_id

    target_project = skill_input.target_project or skill_input.params.get("target_project", "")
    tasks_root = Path(target_project) / "TASKS" if target_project else Path("TASKS")

    pending = _load_tasks_from_dir(tasks_root / "01_PENDING")
    in_progress = _load_tasks_from_dir(tasks_root / "02_IN_PROGRESS")
    done_phases = {task.get("phase", "") for task in _load_tasks_from_dir(tasks_root / "03_DONE")}

    stale_locks = _detect_stale_locks(in_progress)
    blocked_tasks = _detect_blocked_tasks(pending, done_phases)
    circular_deps = _detect_circular_deps(pending + in_progress)

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_pending": len(pending),
        "total_in_progress": len(in_progress),
        "stale_locks": stale_locks,
        "blocked_tasks": blocked_tasks,
        "circular_dependencies": circular_deps,
        "overall_health": "OK" if not any([stale_locks, blocked_tasks, circular_deps]) else "ISSUES_DETECTED",
    }

    artifacts: list[str] = []
    if target_project:
        report_path = _write_diagnostic_report(Path(target_project), report)
        artifacts.append(str(report_path))

    warnings: list[str] = []
    if not target_project:
        warnings.append("TARGET_PROJECT no definido. El reporte no fue escrito a disco.")

    return SkillOutput(
        success=True,
        agent=agent,
        skill=skill,
        result=report,
        artifacts=artifacts,
        warnings=warnings,
        correlation_id=cid,
    )
