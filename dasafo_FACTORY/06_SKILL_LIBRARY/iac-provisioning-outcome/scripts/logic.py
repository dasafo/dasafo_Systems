import os
import time
from .legacy_docker_stack_provisioner import execute_provisioning
from .legacy_terraform_iac_builder import execute_terraform_provisioning

def execute_outcome(target_project: str, agent: str, sub_action: str, **kwargs) -> tuple[dict, list]:
    '''Unified entrypoint for iac-provisioning-outcome - FASE 0 CONECTADA'''
    
    if sub_action == 'docker-stack-provisioner':
        return execute_provisioning(
            target_project=target_project,
            action=kwargs.get('action', 'provision'),
            service_name=kwargs.get('service_name'),
            stack_type=kwargs.get('stack_type', 'standard')
        )
        
    elif sub_action == 'terraform-iac-builder':
        return execute_terraform_provisioning(
            target_project=target_project,
            action=kwargs.get('action', 'apply'),
            cloud_provider=kwargs.get('cloud_provider', 'aws'),
            module_name=kwargs.get('module_name', 'base')
        )
        
    return {"status": "FAILED", "error": f"Unknown sub_action: {sub_action}"}, []
