from __future__ import annotations
import sys, os
from pathlib import Path
import json
import time
from typing import Dict, Any

# Inyección de ruta para cargar skill_schema
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from skill_schema import SkillInput, SkillOutput

# Intentar importar Neo4j para el Shadow State (LTP)
try:
    from neo4j import GraphDatabase
except ImportError:
    GraphDatabase = None

def run(skill_input: SkillInput) -> SkillOutput:
    agent = skill_input.agent or "FACTORY_EVOLVER"
    skill = "factory-doctor"
    cid = skill_input.correlation_id
    params = skill_input.params or {}
    start_time = time.time()
    
    target = params.get("target_project") or skill_input.target_project or os.environ.get("TARGET_PROJECT")
    if not target:
        return SkillOutput.failure(agent, skill, "SECURITY LOCK: No target project identified for healing.", cid)

    project_path = Path(target).resolve()
    tasks_root = project_path / "TASKS"
    
    try:
        # 1. ESCANEO FORENSE DE TAREAS (Dictadura del Disco)
        new_registry = []
        folders = {"PENDING": "01_PENDING", "IN_PROGRESS": "02_IN_PROGRESS", "COMPLETED": "03_COMPLETED"}
        
        for status, folder_name in folders.items():
            folder_path = tasks_root / folder_name
            if folder_path.exists():
                for task_file in folder_path.glob("*.json"):
                    try:
                        with open(task_file, 'r', encoding='utf-8') as f:
                            task_data = json.load(f)
                            task_data["status"] = status # Sincronización forzada por carpeta
                            new_registry.append(task_data)
                    except Exception:
                        continue

        # 2. RECONSTRUCCIÓN DEL REGISTRY.JSON (Atomic Sync)
        registry_file = tasks_root / "registry.json"
        with open(registry_file, 'w', encoding='utf-8') as f:
            json.dump(new_registry, f, indent=2)
        
        reg_size = registry_file.stat().st_size # SI Units: Bytes

        # 3. DETECCIÓN DE FASE POR ARTEFACTOS (Solidity Logic)
        detected_phase = "M1"
        if (project_path / "LOGS" / "BUILD_REPORT.json").exists():
            detected_phase = "M3"
        elif (project_path / "DOCS" / "ARCH").exists() and any((project_path / "DOCS" / "ARCH").iterdir()):
            detected_phase = "M2"
        elif (project_path / "PRP_CONTRACT.json").exists():
            detected_phase = "M1"

        # 4. SANACIÓN DEL PROJECT_STATE.JSON
        state_file = project_path / "PROJECT_STATE.json"
        new_state = {
            "factory_version": "v4.0-MCP",
            "project_status": "HEALED",
            "current_phase": detected_phase,
            "phases": {
                "M1": "APPROVED" if detected_phase in ["M2", "M3", "M4", "M5"] else "IN_PROGRESS",
                "M2": "APPROVED" if detected_phase in ["M3", "M4", "M5"] else ("IN_PROGRESS" if detected_phase == "M2" else "PENDING"),
                "M3": "APPROVED" if detected_phase in ["M4", "M5"] else ("IN_PROGRESS" if detected_phase == "M3" else "PENDING"),
                "M4": "PENDING", "M5": "PENDING"
            }
        }
        with open(state_file, 'w', encoding='utf-8') as f:
            json.dump(new_state, f, indent=2)

        # 5. SHADOW STATE (Neo4j Integration)
        if params.get("sync_neo4j", True) and GraphDatabase:
            # Aquí se usarían las variables de INFRA/.env cargadas por skill_engine.py
            # (Lógica simplificada para este entorno)
            pass

        execution_time = time.time() - start_time # SI Units: Seconds

        result = {
            "healing_status": "SUCCESS",
            "reconstructed_tasks": len(new_registry),
            "detected_phase": detected_phase,
            "registry_size_bytes": reg_size,
            "execution_time_s": round(execution_time, 4),
            "summary": f"Project healed to phase {detected_phase}. Registry rebuilt with {len(new_registry)} tasks."
        }

        return SkillOutput.success(agent, skill, result, [str(registry_file), str(state_file)], cid)

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Doctor Critical Failure: {str(e)}", cid)