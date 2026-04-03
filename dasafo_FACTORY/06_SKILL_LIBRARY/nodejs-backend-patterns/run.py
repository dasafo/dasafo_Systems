from __future__ import annotations
import sys
import os
import time
from pathlib import Path

# Inyección para resolver dependencias de la factoría
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

try:
    from skill_schema import SkillInput, SkillOutput
except ImportError:
    pass

def run(skill_input: SkillInput) -> SkillOutput:
    """Node.js Backend Patterns (v4.0-MCP) - Architecture Enforcer."""
    start_time = time.time()
    
    agent = skill_input.agent or "BACKEND_DEV"
    skill = "nodejs-backend-patterns"
    cid = skill_input.correlation_id
    params = skill_input.params or {}
    
    target = params.get("target_project") or skill_input.target_project or os.environ.get("TARGET_PROJECT")
    module_name = params.get("module_name", "core").lower()
    
    if not target:
        return SkillOutput.failure(agent, skill, "ARCH_ERROR: Missing target_project.", cid)
        
    project_path = Path(target).resolve()
    backend_path = project_path / "WORKSPACE" / "backend"
    
    # 🔍 Verificación Física: ¿Es esto realmente un proyecto Node.js?
    pkg_json_path = backend_path / "package.json"
    execution_duration_s = round(time.time() - start_time, 4)
    
    if not pkg_json_path.exists():
        summary = "No package.json found in WORKSPACE/backend/. Cannot apply Node.js patterns to a non-JS environment."
        result_payload = {
            "is_node_environment": False,
            "error": summary,
            "execution_time_s": execution_duration_s
        }
        # Devolvemos success=True para el MCP, pero con advertencias claras para el agente
        return SkillOutput.success(agent, skill, result_payload, [], [summary], cid, summary=summary)

    # Si el entorno es válido, proveemos el enrutamiento arquitectónico estricto
    result_payload = {
        "is_node_environment": True,
        "scaffold_paths": {
            "controller": f"WORKSPACE/backend/controllers/{module_name}.controller.ts",
            "service": f"WORKSPACE/backend/services/{module_name}.service.ts",
            "repository": f"WORKSPACE/backend/repositories/{module_name}.repository.ts",
            "dto": f"WORKSPACE/backend/dtos/{module_name}.dto.ts"
        },
        "testing_mandate": f"MANDATORY: Generate tests at WORKSPACE/backend/tests/{module_name}.test.ts",
        "execution_time_s": execution_duration_s
    }
    
    return SkillOutput.success(
        agent, skill, result_payload, [], [], cid, 
        summary=f"Node.js environment verified. Enforcing Service/Repository architecture for module '{module_name}'."
    )