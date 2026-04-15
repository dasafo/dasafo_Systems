import httpx
import json
import logging
import os
import sys

logger = logging.getLogger("PEV:CORE_CLIENT")

import importlib
try:
    # Hack para importar desde carpeta con nombre numérico
    memory_module = importlib.import_module("00_SHARED_MEMORY.memory_manager")
    memory_manager = memory_module.memory_manager
except Exception as e:
    # Usamos print si el logger falla en la inicialización temprana
    print(f"Failed to load memory manager: {e}")
    memory_manager = None

async def mcp_invoke(skill_name: str, payload: dict) -> dict:
    """
    Invoca una herramienta MCP en el servidor central.
    Implementa el patrón Octopus mediante Session IDs únicos para evitar colisiones.
    """
    headers = {
        "X-Session-ID": f"{payload.get('task_id', 'unknown')}-{payload.get('agent', 'sys')}",
        "Content-Type": "application/json"
    }
    
    async with httpx.AsyncClient(timeout=60.0) as client:
        # El servidor mcp_app.py actúa como el Gateway Industrial
        url = f"http://localhost:8000/tools/{skill_name}"
        try:
            response = await client.post(url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"MCP Call Failed [{skill_name}]: {str(e)}")
            raise
