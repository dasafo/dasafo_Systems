import os
import time
from .legacy_factory_audit_pro import execute_audit
from .legacy_agentic_thought_secret_scanner import execute_scan

def execute_outcome(target_project: str, agent: str, sub_action: str, **kwargs) -> tuple[dict, list]:
    '''Unified entrypoint for security-audit-outcome - FASE 0 CONECTADA'''
    
    if sub_action == 'factory-audit-pro':
        return execute_audit(
            target_project=target_project,
            severity_threshold=kwargs.get('severity_threshold', 'MEDIUM'),
            strict_mode=kwargs.get('strict_mode', False),
            dimensions=kwargs.get('dimensions')
        )
        
    elif sub_action == 'agentic-thought-secret-scanner':
        return execute_scan(
            target_project=target_project,
            network_preflight=kwargs.get('network_preflight', False)
        )
        
    return {"status": "FAILED", "error": f"Unknown sub_action: {sub_action}"}, []
