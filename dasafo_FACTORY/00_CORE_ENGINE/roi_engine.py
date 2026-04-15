# dasafo_FACTORY/00_CORE_ENGINE/roi_engine.py
import logging

logger = logging.getLogger("PEV:ROI_ENGINE")

COST_LIMIT_PER_TASK = 0.50  # 0.50 USD máximo por subtarea (Threshold Industrial)

def estimate_roi(task_description: str, complexity_score: int):
    """
    Calcula si una tarea debe ejecutarse en la nube (Claude 3.5) o localmente (Ollama/Llama-3).
    Basado en coste proyectado y densidad cognitiva requerida.
    """
    # Estimación rápida de tokens (entrada + salida esperada)
    est_tokens = len(task_description) * 1.5 
    
    # Precio aproximado Claude 3.5 Sonnet: $3.00 / 1M tokens (Input) / $15.00 (Output) -> Avg $0.015/1k
    estimated_cost = (est_tokens / 1000) * 0.015 
    
    logger.info(f"[*] ROI Engine: Evaluando tarea. Coste Est: ${estimated_cost:.4f}, Complexity: {complexity_score}")

    # Regla 1: Techo de Gasto
    if estimated_cost > COST_LIMIT_PER_TASK:
        return "LOCAL_LLM", f"COST_LOCK: Tarea demasiado costosa (${estimated_cost:.2f}). Usando motor local."
    
    # Regla 2: Densidad Cognitiva
    if complexity_score < 3: # Escala 1-10
        return "LOCAL_LLM", "TASK_TRIVIAL: Complejidad baja detectada. Derivando a Llama-3 local."
        
    # Regla 3: Potencia Brutal
    return "CLOUD_LLM", "HIGH_REASONING: Complejidad alta. Usando motor Claude 3.5 Sonnet."
