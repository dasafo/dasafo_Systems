# dasafo_FACTORY/06_SKILL_LIBRARY/api-design-outcome/scripts/logic.py
import os
import time
from .legacy_api_contract_generator import execute_design
from .legacy_api_docs_generator import execute_docs_generation

def execute_outcome(target_project: str, agent: str, sub_action: str, **kwargs) -> tuple[dict, list]:
    '''Unified entrypoint for api-design-outcome - FASE 0 CONECTADA'''
    
    if sub_action == 'api-contract-generator':
        # Mapeo a la función física real
        return execute_design(
            target_project=target_project,
            resource=kwargs.get('resource', 'generic_resource'),
            version=kwargs.get('version', '1.0.0'),
            overwrite=kwargs.get('overwrite', False)
        )
        
    elif sub_action == 'api-docs-generator':
        # Mapeo a la función física real
        return execute_docs_generation(
            target_project=target_project,
            contract_path=kwargs.get('contract_path', 'API-CONTRACT.yaml'),
            output_name=kwargs.get('output_name', 'API_REFERENCE_PRO.md'),
            include_examples=kwargs.get('include_examples', True),
            overwrite=kwargs.get('overwrite', False)
        )
        
    return {"status": "FAILED", "error": f"Unknown sub_action: {sub_action}"}, []