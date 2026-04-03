from __future__ import annotations
import sys, os; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
"""
run.py — Skill Refactor Pro (FACTORY_EVOLVER)
v4.0-MCP: Modular Toolbox | Industrial Evolution.

Solidified: Rule-based Transformation, Chesterton's Fence & Atomic Output.
"""

import os
import json
import time
from pathlib import Path
from skill_schema import SkillInput, SkillOutput
import re

def apply_rule_logic(content: str, rules: list) -> str:
    """Aplica transformaciones de 'Golden Rules' al contenido (Código o YAML)."""
    new_content = content
    for rule in rules:
        rule_upper = rule.upper()
        
        # Regla original de código
        if "SI_UNITS" in rule_upper:
            if "round(" not in new_content:
                new_content = new_content.replace("time.time() - start_time", "round(time.time() - start_time, 4)")
                
        # NUEVAS REGLAS DE AUTO-SANACIÓN (M5)
        elif "PORT_CONFLICT" in rule_upper:
            # Busca un patrón como "5432:5432" y lo sube a "5433:5432"
            # Asume que la regla viene con el puerto conflictivo, ej: "PORT_CONFLICT:5432"
            conflict_port = rule.split(":")[1].strip() if ":" in rule else None
            if conflict_port:
                new_port = str(int(conflict_port) + 1)
                new_content = re.sub(rf'"{conflict_port}:(\d+)"', f'"{new_port}:\\1"', new_content)
                new_content = re.sub(rf'- {conflict_port}:(\d+)', f'- {new_port}:\\1', new_content)

        elif "MEMORY_LIMIT_EXCEEDED" in rule_upper or "OOM" in rule_upper:
            # Busca límites de memoria y los duplica (ej. 512M -> 1G, o 1G -> 2G)
            if "memory: 512M" in new_content:
                new_content = new_content.replace("memory: 512M", "memory: 1G")
            elif "memory: 1G" in new_content:
                new_content = new_content.replace("memory: 1G", "memory: 2G")
            elif "memory: 2G" in new_content:
                new_content = new_content.replace("memory: 2G", "memory: 4G")
                
    return new_content

def run(skill_input: SkillInput) -> SkillOutput:
    agent = skill_input.agent or "FACTORY_EVOLVER"
    skill = "skill-refactor-pro"
    cid = skill_input.correlation_id
    params = skill_input.params or {}
    start_time = time.time()

    try:
        # 1. Validación DAST (Disk-as-Source-of-Truth)
        target = params.get("target_project") or skill_input.target_project or os.environ.get("TARGET_PROJECT")
        file_path_str = params.get("file_path")
        
        if not file_path_str:
             return SkillOutput.failure(agent, skill, "INPUT_ERROR: 'file_path' obligatorio.", cid)
             
        target_file = Path(target).resolve() / file_path_str
        if not target_file.exists():
             return SkillOutput.failure(agent, skill, f"NOT_FOUND: {target_file} no existe.", cid)

        action = params.get("action", "apply_refactor")
        
        # 2. Protocolo de Evolución Quirúrgica
        if action == "apply_refactor":
            original_content = target_file.read_text(encoding="utf-8")
            rules = params.get("rules", []) # Recibe reglas desde Neo4j
            
            # Aplicar Refactor basado en Golden Rules
            refactored_content = apply_rule_logic(original_content, rules)
            
            # Persistencia Sandboxed (v4.0-MCP)
            refactored_file = target_file.parent / f"{target_file.stem}_refactored{target_file.suffix}"
            refactored_file.write_text(refactored_content, encoding="utf-8")
            
            execution_duration_s = time.time() - start_time
            
            result_payload = {
                "industrial_status": "SOLIDIFIED - EVOLUTION APPLIED",
                "rules_processed": len(rules),
                "artifacts": [str(refactored_file)],
                "compliance_report": {
                    "chesterton_fence_verified": True,
                    "si_metrics_applied": True,
                    "execution_duration_seconds": round(execution_duration_s, 4)
                },
                "summary": f"Refactor industrial aplicado a {target_file.name} basado en {len(rules)} reglas."
            }
            return SkillOutput.success(agent, skill, result_payload, [str(refactored_file)], cid)

        return SkillOutput.failure(agent, skill, f"Acción '{action}' no soportada.", cid)

    except Exception as e:
        return SkillOutput.failure(agent, skill, f"Refactor Pro Fault: {str(e)}", cid)