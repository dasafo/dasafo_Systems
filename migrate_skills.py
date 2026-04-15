import os
import shutil
from pathlib import Path

FACTORY_DIR = Path("/home/david/Documents/AI/AGENTES/dasafo_FACTORY/06_SKILL_LIBRARY")
MCP_TOOLS_DIR = Path("/home/david/Documents/AI/AGENTES/dasafo_FACTORY/mcp_tools")

# Schema: NEW_OUTCOME_NAME: [LIST OF OLD SKILL NAMES TO MERGE]
MIGRATION_SCHEMA = {
    "project-contract-outcome": ["prp-generator", "startup-metrics-framework"],
    "tech-research-outcome": ["architecture-decision-records", "research-manager", "arxiv-technical-digest"],
    "backbone-validation-outcome": ["project-backbone-validator"],
    "api-design-outcome": ["api-contract-generator", "api-docs-generator"],
    "backend-logic-outcome": ["async-fastapi-logic", "nodejs-backend-patterns"],
    "frontend-vibe-outcome": ["frontend-ui-designer", "atomic-design-tokens", "shadcn-component-library"],
    "security-audit-outcome": ["factory-audit-pro", "agentic-thought-secret-scanner"],
    "e2e-verification-outcome": ["build-test-executor", "playwright-e2e-tester", "pytest-logic-verifier"],
    "iac-provisioning-outcome": ["docker-stack-provisioner", "terraform-iac-builder"],
    "factory-evolution-outcome": ["skill-refactor-pro", "context-pruning-sieve", "factory-doctor"],
    "project-management-outcome": ["project-management", "registry-manager", "kanban-solidity-gate"]
}

def generate_unified_logic(new_skill, old_skills):
    code = "import os\nimport time\n"
    for old in old_skills:
        code += f"from .legacy_{old.replace('-', '_')} import *  # Imported legacy logic\n"
        
    code += f"""
# Outcome Logic for {new_skill}
def execute_outcome(target_project: str, agent: str, sub_action: str, **kwargs) -> tuple[dict, list]:
    '''Unified entrypoint for {new_skill}'''
    artifacts = []
    result = {{"status": "consolidated execution started"}}
    
    # Delegator
"""
    for old in old_skills:
        code += f"    if sub_action == '{old}':\n"
        code += f"        return {{'sub_action': '{old}', 'msg': 'legacy mapping required'}}, []\n"
    
    code += "    return result, artifacts\n"
    return code

for new_skill, old_skills in MIGRATION_SCHEMA.items():
    new_skill_dir = FACTORY_DIR / new_skill
    scripts_dir = new_skill_dir / "scripts"
    
    # Create new structure
    scripts_dir.mkdir(parents=True, exist_ok=True)
    
    # SKILL.md
    skill_content = f"---\nname: {new_skill}\ndescription: Consolidated outcome macro-skill for {', '.join(old_skills)}\n---\n# {new_skill}\n\nOutcome tool."
    (new_skill_dir / "SKILL.md").write_text(skill_content)
    
    # Migrate old logic files
    for old in old_skills:
        old_dir = FACTORY_DIR / old
        old_logic = old_dir / "logic.py"
        if old_logic.exists():
            clean_name = old.replace('-', '_')
            shutil.copy(old_logic, scripts_dir / f"legacy_{clean_name}.py")
            # We don't delete old_dir yet to be safe
            
    # Generate unified logic.py
    (scripts_dir / "logic.py").write_text(generate_unified_logic(new_skill, old_skills))

print("Migration step 1 complete. New folders created.")
