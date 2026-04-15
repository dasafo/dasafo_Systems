import os
import time
from .legacy_database_architect_strategic import execute_db_architect
from .legacy_supabase_stack_expert import execute_supabase_expert

def execute_outcome(target_project: str, agent: str, sub_action: str, **kwargs) -> tuple[dict, list]:
    '''Unified entrypoint for database-outcome-generator - FASE 0 CONECTADA'''
    
    if sub_action == 'database-architect-strategic':
        return execute_db_architect(
            target_project=target_project,
            resource_entity=kwargs.get('resource_entity', 'generic_resource'),
            overwrite=kwargs.get('overwrite', False),
            isolation_mode=kwargs.get('isolation_mode', False)
        )
        
    elif sub_action == 'supabase-stack-expert':
        return execute_supabase_expert(
            target_project=target_project,
            resource_entity=kwargs.get('resource_entity', 'generic_resource'),
            isolation_mode=kwargs.get('isolation_mode', False)
        )
        
    return {"status": "FAILED", "error": f"Unknown sub_action: {sub_action}"}, []
