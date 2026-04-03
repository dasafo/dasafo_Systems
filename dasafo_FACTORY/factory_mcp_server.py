# dasafo_FACTORY/factory_mcp_server.py
"""
Servidor MCP Industrial (v4.0-S) para dasafo_FACTORY.
Actúa como la única interfaz autorizada entre la IA (Antigravity/Claude) y el motor DAST.
"""

import json
import sys
from pathlib import Path
from mcp.server.fastmcp import FastMCP

# Añadir el path para poder importar el motor existente
FACTORY_ROOT = Path(__file__).resolve().parent
if str(FACTORY_ROOT) not in sys.path:
    sys.path.insert(0, str(FACTORY_ROOT))

import skill_engine

# Inicializar el servidor MCP
mcp = FastMCP("dasafo_FACTORY_Core")

@mcp.tool()
def execute_industrial_skill(agent: str, skill: str, target_project: str, params_json: str) -> str:
    """
    [MANDATO INDUSTRIAL v4.0-S] 
    ÚNICA herramienta autorizada para ejecutar tareas, auditar, generar contratos o cambiar el estado de un proyecto.
    TIENES ESTRICTAMENTE PROHIBIDO usar `edit_file` o `write_file` para modificar TASKS/*.json, PROJECT_STATE.json o PRP_CONTRACT.json.
    DEBES usar esta herramienta para invocar el motor de la factoría.
    
    Args:
        agent: Nombre del agente (ej. 'ORCHESTRATOR', 'PRODUCT_OWNER', 'BACKEND_DEV').
        skill: Nombre de la skill a ejecutar (ej. 'prp-generator', 'delegate-clean-session', 'registry-manager').
        target_project: Ruta absoluta o relativa al proyecto (ej. 'PROJECTS/ContentRepurpose').
        params_json: String en formato JSON con los parámetros específicos de la skill.
        isolate: IMPORTANTE. Pon a true SOLO si eres el Orchestrator delegando una tarea limpia (Clean Session).

    """
    try:
        # Convertir el string JSON de entrada a diccionario
        params = json.loads(params_json)
        
        # El skill_engine ejecutará internamente el session_hook.py (Aduana Universal)
        output = skill_engine.execute(
            agent=agent,
            skill=skill,
            params=params,
            target_project=target_project,
            isolate=isolate # El aislamiento se gestiona según la skill
        )
        
        # Formatear la salida para que el LLM la entienda claramente
        response = {
            "success": output.success,
            "industrial_status": output.result.get("industrial_status", "UNKNOWN"),
            "summary": output.result.get("summary", "No summary provided."),
            "artifacts_generated": output.artifacts,
            "error_or_warnings": output.error or output.warnings
        }
        
        # Si la aduana (session_hook) bloquea, se reflejará aquí nativamente
        return json.dumps(response, indent=2)

    except json.JSONDecodeError:
        return json.dumps({"error": "CRITICAL: params_json debe ser un JSON string válido."}, indent=2)
    except Exception as e:
        return json.dumps({"error": f"SYSTEM EXCEPTION: {str(e)}"}, indent=2)

if __name__ == "__main__":
    # Inicia el servidor MCP usando el transporte estándar (stdio) para que Antigravity lo conecte
    mcp.run()