from langgraph.graph import StateGraph, END
from .pev_state import OrchestratorState
from .pev_nodes import node_author, node_reviewer, node_security, node_architect
from .router import router_engine_selector

# Definición del flujo global de la factoría (StateGraph v5.1)
workflow = StateGraph(OrchestratorState)

# Registro de Nodos
workflow.add_node("node_architect", node_architect)
workflow.add_node("node_author", node_author)
workflow.add_node("node_reviewer", node_reviewer)
workflow.add_node("node_security", node_security)

# Configuración del Grafo
workflow.set_entry_point("node_architect")

# Bordes
workflow.add_edge("node_architect", "node_author")
workflow.add_edge("node_author", "node_reviewer")

def dark_factory_condition(state: dict):
    """
    Decide si avanzar a la siguiente fase sin permiso humano (v5.1-Dark).
    """
    qa_score = state.get("quality_score", 0)
    security_breach_count = state.get("security_breaches", 0)

    if qa_score > 0.85 and security_breach_count == 0:
        print(f"[*] DARK_FACTORY: Calidad {qa_score:.2f} óptima. Procediendo sin gate humano.")
        return "AUTO_PROCEED" 
    
    print(f"[*] DARK_FACTORY: Alerta detectada. Bloqueando para intervención humana.")
    return "HUMAN_INTERVENTION"

# Implementación de nodos de Gate (Placeholders para la demo)
def node_wait_for_user(state: dict):
    print("[-] STANDBY: Esperando aprobación manual del Director...")
    return {"phase": "user_gate"}

def node_next_phase(state: dict):
    print("[+] ADVANCE: Transicionando a la siguiente fase del DAG...")
    return {"phase": "next_milestone"}

# Registro de Nodos de Control
workflow.add_node("node_wait_for_user", node_wait_for_user)
workflow.add_node("node_next_phase", node_next_phase)

# Bucle condicional Dark Factory
workflow.add_conditional_edges(
    "node_reviewer",
    dark_factory_condition,
    {
        "AUTO_PROCEED": "node_next_phase", 
        "HUMAN_INTERVENTION": "node_wait_for_user"
    }
)

workflow.add_edge("node_next_phase", "node_security")
workflow.add_edge("node_wait_for_user", END)
workflow.add_edge("node_security", END)

# Compilador
factory_orchestrator = workflow.compile()
