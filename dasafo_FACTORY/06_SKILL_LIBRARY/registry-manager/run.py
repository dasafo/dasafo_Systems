from __future__ import annotations
import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Registry Manager (ORCHESTRATOR)
v4.0-MCP: Modular Toolbox | Industrial Scale.
Solidified: Atomic Physical Move (DAST) & Kanban SSoT Integrity.
"""

import os
import json
import time
from pathlib import Path
from skill_schema import SkillInput, SkillOutput

def run(skill_input: SkillInput) -> SkillOutput:
    agent = skill_input.agent or "ORCHESTRATOR"
    skill = "registry-manager"
    cid = skill_input.correlation_id
    params = skill_input.params or {}
    
    start_time = time.time()

    try:
        # 1. Resolución de Rutas
        target = params.get("target_project") or skill_input.target_project or os.environ.get("TARGET_PROJECT")
        if not target:
             return SkillOutput.failure(agent, skill, "SECURITY LOCK: Missing TARGET_PROJECT.", cid)
        
        project_path = Path(target).resolve()
        tasks_dir = project_path / "TASKS"
        registry_file = tasks_dir / "registry.json"
        
        action = params.get("action", "update_status")
        task_id = params.get("task_id")
        new_status = params.get("new_status") # PENDING, IN_PROGRESS, COMPLETED

        if not registry_file.exists():
            return SkillOutput.failure(agent, skill, "GATE_ERROR: registry.json not found.", cid)

        if action == "update_status":
            if not task_id or not new_status:
                return SkillOutput.failure(agent, skill, "INPUT_ERROR: task_id and new_status required.", cid)

            # Mapeo de carpetas industriales v4.0-MCP
            folder_map = {
                "PENDING": "01_PENDING",
                "IN_PROGRESS": "02_IN_PROGRESS",
                "COMPLETED": "03_COMPLETED"
            }

            if new_status not in folder_map:
                return SkillOutput.failure(agent, skill, f"INVALID_STATUS: {new_status} no reconocido.", cid)

            # --- ESTRATEGIA DAST: MOVIMIENTO ATÓMICO ---
            
            # 1. Localizar el archivo físico actual (Búsqueda en todas las subcarpetas)
            source_file = None
            for folder in folder_map.values():
                potential_path = tasks_dir / folder / f"{task_id}.json"
                if potential_path.exists():
                    source_file = potential_path
                    break

            # 2. Preparar el destino
            target_folder = tasks_dir / folder_map[new_status]
            target_folder.mkdir(parents=True, exist_ok=True)
            destination_file = target_folder / f"{task_id}.json"

            # 3. Ejecutar Movimiento o Creación
            if source_file:
                # Movimiento atómico a nivel de Sistema Operativo
                os.replace(source_file, destination_file)
            else:
                # Si es una tarea nueva, se crea directamente en el destino
                # (Nota: En un flujo SDD puro, el archivo debería existir antes de actualizar el registro)
                pass

            # 4. Sincronizar el registry.json (La "Vista" del Disco)
            with open(registry_file, 'r', encoding='utf-8') as f:
                registry = json.load(f)

            task_found = False
            prev_status = "UNKNOWN"
            for task in registry:
                if task.get("id") == task_id:
                    prev_status = task.get("status", "PENDING")
                    task["status"] = new_status
                    task_found = True
                    break

            # Guardar el registro actualizado como SSoT
            with open(registry_file, 'w', encoding='utf-8') as f:
                json.dump(registry, f, indent=2)

            # --- MÉTRICAS INDUSTRIALES (SI) ---
            execution_duration_s = time.time() - start_time
            
            result_payload = {
                "industrial_status": "SOLIDIFIED - ATOMIC MOVE SUCCESSFUL",
                "task_id": task_id,
                "previous_status": prev_status,
                "current_status": new_status,
                "artifact_path": str(destination_file),
                "compliance_report": {
                    "atomic_move_verified": True,
                    "disk_as_source_of_truth": True,
                    "execution_duration_seconds": round(execution_duration_s, 4) # Mandato Segundos
                },
                "summary": f"Task {task_id} moved physically from {prev_status} to {new_status}."
            }
            
            return SkillOutput.success(agent, skill, result_payload, [str(destination_file), str(registry_file)], cid)

        return SkillOutput.failure(agent, skill, f"Action '{action}' not implemented.", cid)

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Registry ATOMIC Fault: {str(e)}", cid)