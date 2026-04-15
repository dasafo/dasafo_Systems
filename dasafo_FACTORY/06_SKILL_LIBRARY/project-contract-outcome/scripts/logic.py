import os
import time
from .legacy_prp_generator import execute_prp_generation
from .legacy_startup_metrics_framework import execute_financial_analysis

def execute_outcome(target_project: str, agent: str, sub_action: str, **kwargs) -> tuple[dict, list]:
    '''Unified entrypoint for project-contract-outcome - FASE 0 CONECTADA'''
    
    if sub_action == 'prp-generator':
        return execute_prp_generation(
            target_project=target_project,
            project_name=kwargs.get('project_name'),
            problem_description=kwargs.get('problem_description'),
            action=kwargs.get('action', 'init'),
            spec_data=kwargs.get('spec_data'),
            overwrite=kwargs.get('overwrite', False)
        )
        
    elif sub_action == 'startup-metrics-framework':
        return execute_financial_analysis(
            target_project=target_project,
            business_model=kwargs.get('business_model', 'SaaS'),
            target_audience=kwargs.get('target_audience', 'Developers'),
            estimated_execution_s=kwargs.get('estimated_execution_s', 0.0)
        )
        
    return {"status": "FAILED", "error": f"Unknown sub_action: {sub_action}"}, []
