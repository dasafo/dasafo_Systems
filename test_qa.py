import sys
import json
import logging
sys.path.append("/home/david/Documents/AI/AGENTES/dasafo_FACTORY")
from dasafo_FACTORY.mcp_tools.hub04_compliance import audit_logic
from dasafo_FACTORY.mcp_tools.hub03_prod import pytest_logic

target_project = "/home/david/Documents/AI/AGENTES/PROJECTS/ContentRepurpose"
agent = "QA_TESTER"

print("--- 1. FACTORY AUDIT PRO ---")
try:
    audit_res, _ = audit_logic.execute_audit(
        target_path=target_project,
        agent=agent,
        dimensions=["Anti-Patterns", "SoC_Violations"],
        severity_threshold="P3",
        strict_mode=True
    )
    print(json.dumps(audit_res, indent=2))
except Exception as e:
    import traceback
    traceback.print_exc()

print("\n--- 2. PYTEST LOGIC VERIFIER ---")
try:
    test_res, _ = pytest_logic.execute_logic_verification(
        target_project=target_project,
        agent=agent,
        action="run_test", # assuming standard logic wrapper allows this
        spec_path="TASKS/03_COMPLETED/M3-003.json",
        module_path="WORKSPACE/backend/src/application/use_cases/batch_repurpose.py"
    )
    print(json.dumps(test_res, indent=2))
except Exception as e:
    import traceback
    traceback.print_exc()
