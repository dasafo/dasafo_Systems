from .roi_engine import estimate_roi

def router_engine_selector(state: dict) -> dict:
    """
    Decide el motor de ejecución y el modelo (Nube vs Local) 
    basado en la carga cognitiva y el ROI proyectado.
    """
    task_type = state.get("task_type", "coding")
    task_desc = state.get("plan_docs", state.get("task_id", ""))
    complexity = state.get("complexity", 5) # Default a complejidad media
    
    # 1. Selección de Modelo (Cloud vs Local)
    model_endpoint, reason = estimate_roi(task_desc, complexity)
    print(f"[*] ROUTER: {reason}")
    
    # 2. Selección de Motor de Grafo
    if task_type in ["coding", "infrastructure", "security-patch"]:
        engine = "pev_engine"
    elif task_type in ["documentation", "market_research", "readme_generation"]:
        engine = "crewai_engine"
    else:
        engine = "pev_engine"
        
    return {
        "engine_choice": engine,
        "model_endpoint": model_endpoint
    }
