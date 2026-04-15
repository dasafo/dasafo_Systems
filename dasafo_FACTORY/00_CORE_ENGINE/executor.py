import docker
import os
import time
import logging

logger = logging.getLogger("PEV:EXECUTOR")

def run_agent_container(agent_role: str, task_payload: dict, target_project_path: str):
    """
    Levanta un contenedor efímero para ejecutar una tarea en un entorno estéril (DAST).
    Implementa límites de recursos y aislamiento de carpetas.
    """
    client = docker.from_env()
    
    # Nombre único para el trabajador (FTE: Full-Time Equivalent)
    container_name = f"FTE_{agent_role}_{int(time.time())}"
    
    # Mapeo de volúmenes:
    # 1. El proyecto objetivo (Lectura/Escritura)
    # 2. La librería de skills (Solo Lectura)
    volumes = {
        os.path.abspath(target_project_path): {'bind': '/app/projects', 'mode': 'rw'},
        os.path.abspath("./06_SKILL_LIBRARY/"): {'bind': '/app/skills', 'mode': 'ro'}
    }
    
    try:
        logger.info(f"[*] Desplegando agente {agent_role} en contenedor {container_name}...")
        
        container = client.containers.run(
            image="dasafo/agent-base:latest",
            command=f"python execute_skill.py '{task_payload}'",
            volumes=volumes,
            mem_limit="512m",  # Límite de memoria para evitar fugas de recursos
            cpu_quota=50000,   # 0.5 CPU
            name=container_name,
            remove=True,       # Auto-destrucción al terminar (Efímero)
            detach=False       # Esperamos el resultado (Síncrono para el orquestador)
        )
        
        return container.decode('utf-8')
        
    except Exception as e:
        logger.error(f"🚨 EXECUTOR ERROR: Fallo en el despliegue del agente. {str(e)}")
        raise
