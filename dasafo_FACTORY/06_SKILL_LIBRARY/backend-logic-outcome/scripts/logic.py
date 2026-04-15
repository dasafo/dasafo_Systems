import os
import time
from .legacy_async_fastapi_logic import execute_fastapi_logic
from .legacy_nodejs_backend_patterns import execute_patterns

def execute_outcome(target_project: str, agent: str, sub_action: str, **kwargs) -> tuple[dict, list]:
    '''Unified entrypoint for backend-logic-outcome - FASE 0 CONECTADA'''
    
    if sub_action == 'async-fastapi-logic':
        return execute_fastapi_logic(
            target_project=target_project,
            action=kwargs.get('action', 'scaffold'),
            domain_name=kwargs.get('domain_name'),
            route_name=kwargs.get('route_name'),
            method=kwargs.get('method', 'GET'),
            overwrite=kwargs.get('overwrite', False)
        )
        
    elif sub_action == 'nodejs-backend-patterns':
        return execute_patterns(
            target_project=target_project,
            module_name=kwargs.get('module_name', 'core')
        )
        
    return {"status": "FAILED", "error": f"Unknown sub_action: {sub_action}"}, []
