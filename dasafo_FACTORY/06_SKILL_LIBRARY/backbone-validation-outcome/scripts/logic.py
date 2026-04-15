import os
import time
from .legacy_project_backbone_validator import execute_backbone_validation

def execute_outcome(target_project: str, agent: str, sub_action: str, **kwargs) -> tuple[dict, list]:
    '''Unified entrypoint for backbone-validation-outcome - FASE 0 CONECTADA'''
    
    if sub_action == 'project-backbone-validator':
        return execute_backbone_validation(
            target_project=target_project,
            action=kwargs.get('action', 'validate'),
            schema_version=kwargs.get('schema_version', 'v5.0-MCP')
        )
        
    return {"status": "FAILED", "error": f"Unknown sub_action: {sub_action}"}, []
