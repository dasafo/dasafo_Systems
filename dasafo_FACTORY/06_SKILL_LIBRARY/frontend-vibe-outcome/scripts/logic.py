import os
import time
from .legacy_frontend_ui_designer import execute_ui_validation
from .legacy_atomic_design_tokens import execute_atomic_tokens
from .legacy_shadcn_component_library import execute_shadcn_management

def execute_outcome(target_project: str, agent: str, sub_action: str, **kwargs) -> tuple[dict, list]:
    '''Unified entrypoint for frontend-vibe-outcome - FASE 0 CONECTADA'''
    
    if sub_action == 'frontend-ui-designer':
        return execute_ui_validation(
            target_project=target_project,
            component_name=kwargs.get('component_name', 'UnknownComponent'),
            design_vibe=kwargs.get('design_vibe', 'industrial')
        )
        
    elif sub_action == 'atomic-design-tokens':
        return execute_atomic_tokens(
            target_project=target_project,
            action=kwargs.get('action', 'sync'),
            layer=kwargs.get('layer', 'base'),
            name=kwargs.get('name'),
            value=kwargs.get('value'),
            overwrite=kwargs.get('overwrite', False)
        )
        
    elif sub_action == 'shadcn-component-library':
        return execute_shadcn_management(
            target_project=target_project,
            action=kwargs.get('action', 'add'),
            component=kwargs.get('component'),
            overwrite=kwargs.get('overwrite', False)
        )
        
    return {"status": "FAILED", "error": f"Unknown sub_action: {sub_action}"}, []
