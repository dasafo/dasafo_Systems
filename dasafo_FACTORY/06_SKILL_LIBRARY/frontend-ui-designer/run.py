from __future__ import annotations
import sys
import os
import time
from pathlib import Path

# Inyección de dependencias de la Factoría
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

try:
    from skill_schema import SkillInput, SkillOutput
except ImportError:
    pass

def run(skill_input: SkillInput) -> SkillOutput:
    """Frontend UI Designer (v4.0-S) - Design System Enforcer."""
    start_time = time.time()
    
    agent = skill_input.agent or "FRONTEND_DEV"
    skill = "frontend-ui-designer"
    cid = skill_input.correlation_id
    params = skill_input.params or {}
    
    target = params.get("target_project") or skill_input.target_project or os.environ.get("TARGET_PROJECT")
    component_name = params.get("component_name", "UnknownComponent")
    
    if not target:
        return SkillOutput.failure(agent, skill, "DESIGN_ERROR: Missing target_project.", cid)
        
    project_path = Path(target).resolve()
    frontend_path = project_path / "WORKSPACE" / "frontend"
    
    # 🔍 Verificación Física (Zero-Trust) del Design System
    design_markers = [
        frontend_path / "tailwind.config.ts",      # O .js
        frontend_path / "components.json",         # Shadcn config
        frontend_path / "package.json"
    ]
    
    missing_systems = [str(m.name) for m in design_markers if not m.exists() and not (frontend_path / "tailwind.config.js").exists()]
    
    execution_duration_s = round(time.time() - start_time, 4)
    
    if missing_systems:
        summary = f"Design system missing dependencies: {', '.join(missing_systems)}. Cannot guarantee aesthetic output."
        # No bloqueamos la ejecución del agente (success=True), pero le advertimos que el chasis visual no está listo.
        result_payload = {
            "design_system_verified": False,
            "missing_dependencies": missing_systems,
            "scaffold_path": str(frontend_path / "components" / "ui"),
            "execution_time_s": execution_duration_s
        }
        return SkillOutput.success(agent, skill, result_payload, [], [summary], cid, summary=summary)

    # Si todo está en orden
    result_payload = {
        "design_system_verified": True,
        "missing_dependencies": [],
        "scaffold_path": str(frontend_path / "components" / "ui"),
        "execution_time_s": execution_duration_s
    }
    
    return SkillOutput.success(
        agent, skill, result_payload, [], [], cid, 
        summary=f"Design system verified. Ready to architect {component_name}."
    )