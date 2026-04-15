import os
import time
from .legacy_skill_refactor_pro import execute_refactor
from .legacy_context_pruning_sieve import execute_pruning
from .legacy_factory_doctor import execute_doctor

def execute_outcome(target_project: str, agent: str, sub_action: str, **kwargs) -> tuple[dict, list]:
    '''Unified entrypoint for factory-evolution-outcome - FASE 0 CONECTADA'''
    
    if sub_action == 'skill-refactor-pro':
        return execute_refactor(
            target_project=target_project,
            file_path=kwargs.get('file_path'),
            action=kwargs.get('action', 'refactor'),
            target_smell=kwargs.get('target_smell'),
            rules=kwargs.get('rules')
        )
        
    elif sub_action == 'context-pruning-sieve':
        return execute_pruning(
            target_project=target_project,
            target_file=kwargs.get('target_file'),
            action=kwargs.get('action', 'prune'),
            budget_threshold=kwargs.get('budget_threshold', 0.8)
        )
        
    elif sub_action == 'factory-doctor':
        return execute_doctor(
            target_project=target_project,
            action=kwargs.get('action', 'check'),
            strict_mode=kwargs.get('strict_mode', False)
        )
        
    return {"status": "FAILED", "error": f"Unknown sub_action: {sub_action}"}, []
