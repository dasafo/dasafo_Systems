from __future__ import annotations
import sys
import os
import time
from pathlib import Path

# Inyección para resolver skill_schema.py desde la raíz de la factoría
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

try:
    from skill_schema import SkillInput, SkillOutput
except ImportError:
    pass # Gestionado por skill_engine.py

def run(skill_input: SkillInput) -> SkillOutput:
    """Project Backbone Validator (v4.0-MCP) - Scaffolding Inspector."""
    start_time = time.time()
    
    agent = skill_input.agent or "ORCHESTRATOR"
    skill = "project-backbone-validator"
    cid = skill_input.correlation_id
    params = skill_input.params or {}
    
    target = params.get("target_project") or skill_input.target_project or os.environ.get("TARGET_PROJECT")
    framework = params.get("framework", "").lower()
    
    if not target or not framework:
        return SkillOutput.failure(agent, skill, "VALIDATION_ERROR: Missing target_project or framework.", cid)
        
    project_path = Path(target).resolve()
    missing_bones = []
    
    # 🏗️ Reglas DAST: El esqueleto mínimo viable por framework
    scaffolding_rules = {
        "nextjs": [
            "WORKSPACE/frontend/package.json",
            "WORKSPACE/frontend/app/layout.tsx", 
            "WORKSPACE/frontend/app/globals.css"
        ],
        "fastapi": [
            "WORKSPACE/backend/requirements.txt",
            "WORKSPACE/backend/main.py"
        ]
    }
    
    expected_files = scaffolding_rules.get(framework)
    if not expected_files:
        return SkillOutput.failure(agent, skill, f"VALIDATION_ERROR: Unknown framework '{framework}'.", cid)
        
    # 🔍 Verificación Física (Zero-Trust)
    for rel_path in expected_files:
        file_path = project_path / rel_path
        if not file_path.exists():
            missing_bones.append(rel_path)
            
    is_ready = len(missing_bones) == 0
    execution_duration_s = round(time.time() - start_time, 4)
    
    if not is_ready:
        summary = f"Scaffolding incomplete for {framework}. Missing core files."
        warnings = [f"Missing backbone file: {f}" for f in missing_bones]
        result_payload = {
            "scaffolding_ready": False,
            "missing_bones": missing_bones,
            "validation_time_s": execution_duration_s,
            "recommendation": f"Run project-seeder/framework-bootstrapper for {framework} before delegating SPEC_LITE."
        }
        # Retornamos success=True a nivel MCP para que el Orquestador lea el resultado, 
        # pero scaffolding_ready=False le indica que NO debe despachar al FRONTEND_DEV aún.
        return SkillOutput.success(agent, skill, result_payload, [], warnings, cid, summary=summary)
        
    result_payload = {
        "scaffolding_ready": True,
        "missing_bones": [],
        "validation_time_s": execution_duration_s,
        "recommendation": "Backbone solidified. Safe to dispatch atomic agents."
    }
    
    return SkillOutput.success(agent, skill, result_payload, [], [], cid, summary=f"{framework} scaffolding validated physically.")