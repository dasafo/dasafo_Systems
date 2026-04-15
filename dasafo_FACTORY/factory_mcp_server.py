"""
Servidor MCP Industrial (v5.0 Nativo) para dasafo_FACTORY.
Punto de entrada: importa los Hubs para registrar herramientas y ejecuta mcp.run().

ADR: La lógica de mcp + aduana_universal vive en mcp_tools/mcp_app.py
para evitar importaciones circulares. Este archivo solo actúa como entrypoint.
"""

# 1. Re-exportar mcp, aduana_universal y app para compatibilidad y patrón Octopus
from mcp_tools.mcp_app import mcp, aduana_universal, app  # noqa: F401

# 2. Importar los hubs para que sus @mcp.tool() se registren al cargar
from mcp_tools import (  # noqa: F401
    core_dast,
    hub01_strategy,
    hub02_arch,
    hub03_prod,
    hub04_compliance,
    hub05_operations,
)

# =====================================================================
# 🧰 HERRAMIENTAS NATIVAS MCP — REGISTRADAS EN LOS HUBS
# =====================================================================
# Las herramientas están registradas modularmente en:
#   - mcp_tools/core_dast.py       → delegate-clean-session, kanban-solidity-gate, etc.
#   - mcp_tools/hub01_strategy.py  → prp-generator, startup-metrics-framework, etc.
#   - mcp_tools/hub02_arch.py      → architecture-decision-records, api-contract-generator, etc.
#   - mcp_tools/hub03_prod.py      → async-fastapi-logic, shadcn-component-library, etc.
#   - mcp_tools/hub04_compliance.py→ factory-audit-pro, agentic-thought-secret-scanner, etc.
#   - mcp_tools/hub05_operations.py→ docker-stack-provisioner, deployment-health-check, etc.

import importlib
import logging

# Configuración de Logging
logger = logging.getLogger("FACTORY_GATEWAY")

# --- CARGA DINÁMICA DEL ENGRANAJE CORE ---
try:
    # Importamos el router y el grafo desde las carpetas estandarizadas
    router_mod = importlib.import_module("00_CORE_ENGINE.router")
    graph_mod = importlib.import_module("00_CORE_ENGINE.graph")
    
    router_engine_selector = router_mod.router_engine_selector
    factory_orchestrator = graph_mod.factory_orchestrator
except Exception as e:
    logger.error(f"CRITICAL: Failed to load Core Engine components: {e}")
    router_engine_selector = None
    factory_orchestrator = None

@app.post("/orchestrate")
async def orchestrate_task(payload: dict):
    """
    Gateway de Orquestación Políglota (v5.1-Octopus).
    Actúa como el Director de Tráfico antes de invocar los motores de razonamiento.
    """
    if not router_engine_selector:
        return {"status": "error", "message": "Core Engine not initialized."}

    # 1. El Router detecta Carga Cognitiva y ROI
    decision = router_engine_selector(payload)
    engine_choice = decision.get("engine_choice", "pev_engine")
    model_endpoint = decision.get("model_endpoint", "CLOUD_LLM")

    print(f"🚦 [ROUTER] Decisión: {engine_choice} | Modelo: {model_endpoint}")

    # 2. Bifurcación Física de Motores
    if engine_choice == "crewai_engine":
        # TODO: Integración física con CrewAI Agent Library
        print("🚀 [CREWAI] Derivando tarea administrativa/lineal...")
        return {
            "status": "success", 
            "engine_used": "CrewAI (Agentic Orchestrator)",
            "model": model_endpoint,
            "result": "Tarea delegada a sub-agentes lineales."
        }
    
    else:
        print(f"🧠 [PEV] Invocando Grafo LangGraph (Session: {payload.get('task_id')})...")
        # Inyectamos el endpoint del modelo decidido por el router
        payload["model_endpoint"] = model_endpoint
        
        # Configuración para el checkpointer de LangGraph (Thread-Safe para Octopus)
        config = {"configurable": {"thread_id": payload.get("task_id", "default_thread")}}
        
        try:
            # Invocamos el motor de razonamiento superior (PEV)
            result = await factory_orchestrator.ainvoke(payload, config)
            return {
                "status": "success", 
                "engine_used": "LangGraph (PEV Engine)",
                "model": model_endpoint,
                "result": result
            }
        except Exception as e:
            logger.error(f"Execution Error in PEV: {e}")
            return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    mcp.run()