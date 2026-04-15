import time
import json
import os
from pathlib import Path
from .mcp_client import mcp_invoke

def _scan_available_skills() -> list[str]:
    skills_context = []
    skill_lib_path = Path("/home/david/Documents/AI/AGENTES/dasafo_FACTORY/06_SKILL_LIBRARY")
    if skill_lib_path.exists():
        for skill_dir in skill_lib_path.iterdir():
            if skill_dir.is_dir():
                skill_md = skill_dir / "SKILL.md"
                if skill_md.exists():
                    try:
                        content = skill_md.read_text(encoding="utf-8")
                        # Estándar de Divulgación Progresiva: Solo leemos el Nivel 1 (Meta/Desc)
                        split_idx = content.find("<!-- LEVEL_1_END -->")
                        if split_idx != -1:
                            content = content[:split_idx].strip()
                        skills_context.append(content)
                    except: pass
    return skills_context

def node_architect(state: dict) -> dict:
    print(f"[{time.ctime()}] 🏗️ ARCHITECT: Planning execution...")
    available_skills = _scan_available_skills()
    return {
        "plan_docs": f"Plan for {state.get('task_id')}",
        "available_skills_context": available_skills
    }

async def node_author(state: dict) -> dict:
    print(f"[{time.ctime()}] ✍️ AUTHOR: Executing task {state.get('task_id')}...")
    # Integración con Memoria vía mcp_client (que llama a 00_SHARED_MEMORY)
    payload = {
        "target_project": state.get("target_project"),
        "agent": "node_author",
        "sub_action": state.get("required_skill", "backend-logic-outcome"),
        "task_id": state.get("task_id")
    }
    try:
        resultado = await mcp_invoke("delegate-clean-session", payload)
        details = resultado.get("details", resultado)
        return {
            "draft_artifacts": details.get("artifacts_generated", []),
            "execution_stdout": details.get("summary", ""),
            "phase": "review"
        }
    except Exception as e:
        return {"error_trace": str(e), "phase": "security"}

async def node_reviewer(state: dict) -> dict:
    print(f"[{time.ctime()}] 🔎 REVIEWER: Verifying artifacts via DeepEval...")
    payload = {
        "target_project": state.get("target_project"), 
        "agent": "node_reviewer",
        "target_skill": state.get("required_skill", "unknown"),
        "input_payload": str(state.get("plan_docs")),
        "actual_output": str(state.get("draft_artifacts"))
    }
    try:
        # CORRECCIÓN: Usamos la skill que realmente tiene el motor DeepEval (GEval)
        resultado = await mcp_invoke("skill-validation-outcome", payload)
        
        # Obtenemos la métrica GEval entre 0 y 1
        qa_score = resultado.get("similarity_score", 0)
        verdict = qa_score > 0.8 # Umbral del revisor
        
        return {
            "reviewer_pass": verdict, 
            "quality_score": qa_score,
            "revision_count": state.get("revision_count", 0) + 1,
            "review_notes": [resultado.get("reason", "No notes context.")]
        }
    except Exception as e:
        logger.error(f"Reviewer Error: {e}")
        return {"reviewer_pass": False, "quality_score": 0, "error_trace": str(e)}

async def node_security(state: dict) -> dict:
    print(f"[{time.ctime()}] 🛡️ RED_TEAM & AUTO-HEAL: Scanning for violations...")
    
    # 1. Escaneo Zero-Trust estándar
    try:
        scan_res = await mcp_invoke("agentic-thought-secret-scanner", {"target_project": state.get("target_project")})
    except:
        scan_res = {"success": False, "findings": "Scanner invocation failed."}
    
    # 2. Detección de fallos (Si el autor falló o el scanner detectó algo)
    error_trace = state.get("error_trace")
    if error_trace or not scan_res.get("success", True):
        print(f"[{time.ctime()}] 💊 AUTO-HEAL: Error o Violación detectada. Activando Refactorización Semántica...")
        
        heal_payload = {
            "target_project": state.get("target_project"),
            "agent": "FACTORY_EVOLVER",
            "sub_action": "skill-refactor-pro",
            "action": "semantic_heal",  # La nueva acción impulsada por IA
            "target_smell": error_trace or str(scan_res.get("findings"))
        }
        
        # Delegamos a la skill de evolución para que intente parchear el código
        try:
            await mcp_invoke("factory-evolution-outcome", heal_payload)
            print(f"[{time.ctime()}] 🩹 AUTO-HEAL: Parche semántico aplicado. Reintentando...")
            # Bucle: Mandamos de vuelta al Author para que reintente la ejecución
            return {
                "security_verdict": False, 
                "phase": "node_author", # Nombre correcto del nodo en graph.py
                "error_trace": None     # Limpiamos el error para el reintento
            } 
        except Exception as e:
            print(f"[{time.ctime()}] 💀 AUTO-HEAL FATAL: No se pudo sanar el sistema. {e}")
            return {"security_verdict": False, "phase": "end"}

    return {"security_verdict": True, "phase": "end"}
