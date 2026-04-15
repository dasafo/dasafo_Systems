import os
import time
from .legacy_build_test_executor import execute_build_test
from .legacy_playwright_e2e_tester import execute_e2e
from .legacy_pytest_logic_verifier import execute_logic_verification

def execute_outcome(target_project: str, agent: str, sub_action: str, **kwargs) -> tuple[dict, list]:
    '''Unified entrypoint for e2e-verification-outcome - FASE 0 CONECTADA'''
    
    if sub_action == 'build-test-executor':
        return execute_build_test(
            target_project=target_project,
            agent=agent,
            action=kwargs.get('action', 'run_build'),
            command=kwargs.get('command', "echo 'Simulating industrial build...'"),
            overwrite=kwargs.get('overwrite', False)
        )
        
    elif sub_action == 'playwright-e2e-tester':
        return execute_e2e(
            target_project=target_project,
            agent=agent,
            action=kwargs.get('action', 'run_e2e'),
            spec_path=kwargs.get('spec_path'),
            url=kwargs.get('url', 'http://localhost:3000')
        )
        
    elif sub_action == 'pytest-logic-verifier':
        return execute_logic_verification(
            target_project=target_project,
            agent=agent,
            action=kwargs.get('action', 'run_test'),
            spec_path=kwargs.get('spec_path'),
            module_path=kwargs.get('module_path')
        )
        
    return {"status": "FAILED", "error": f"Unknown sub_action: {sub_action}"}, []
