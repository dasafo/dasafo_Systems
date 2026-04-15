import os
import time
from .legacy_project_management import execute_management
from .legacy_registry_manager import execute_registry_update
from .legacy_kanban_solidity_gate import execute_gate

def execute_outcome(target_project: str, agent: str, sub_action: str, **kwargs) -> tuple[dict, list]:
    '''Unified entrypoint for project-management-outcome - FASE 0 CONECTADA'''
    
    if sub_action == 'project-management':
        return execute_management(
            target_project=target_project,
            action=kwargs.get('action', 'report'),
            report_data=kwargs.get('report_data'),
            overwrite=kwargs.get('overwrite', False)
        )
        
    elif sub_action == 'registry-manager':
        return execute_registry_update(
            target_project=target_project,
            action=kwargs.get('action', 'update'),
            task_id=kwargs.get('task_id'),
            new_status=kwargs.get('new_status')
        )
        
    elif sub_action == 'kanban-solidity-gate':
        return execute_gate(
            target_project=target_project,
            agent=agent,
            action=kwargs.get('action', 'status'),
            port=kwargs.get('port', 8000)
        )
        
    return {"status": "FAILED", "error": f"Unknown sub_action: {sub_action}"}, []
