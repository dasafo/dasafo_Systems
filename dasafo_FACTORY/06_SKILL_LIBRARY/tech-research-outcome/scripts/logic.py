import os
import time
from .legacy_architecture_decision_records import execute_adr
from .legacy_research_manager import execute_research
from .legacy_arxiv_technical_digest import execute_digest

def execute_outcome(target_project: str, agent: str, sub_action: str, **kwargs) -> tuple[dict, list]:
    '''Unified entrypoint for tech-research-outcome - FASE 0 CONECTADA'''
    
    if sub_action == 'architecture-decision-records':
        return execute_adr(
            target_project=target_project,
            agent=agent,
            action=kwargs.get('action', 'new'),
            title=kwargs.get('title'),
            context=kwargs.get('context'),
            decision=kwargs.get('decision'),
            consequences=kwargs.get('consequences'),
            target_id=kwargs.get('target_id'),
            overwrite=kwargs.get('overwrite', False)
        )
        
    elif sub_action == 'research-manager':
        return execute_research(
            target_project=target_project,
            report_name=kwargs.get('report_name', 'RESEARCH_REPORT.md'),
            content=kwargs.get('content', '# Technical Research Report'),
            category=kwargs.get('category', 'RESEARCH')
        )
        
    elif sub_action == 'arxiv-technical-digest':
        return execute_digest(
            target_project=target_project,
            query=kwargs.get('query', ''),
            max_results=kwargs.get('max_results', 5),
            overwrite=kwargs.get('overwrite', False)
        )
        
    return {"status": "FAILED", "error": f"Unknown sub_action: {sub_action}"}, []
