import sys, json, os
sys.path.append("/home/david/Documents/AI/AGENTES/dasafo_FACTORY")
from dasafo_FACTORY.mcp_tools.hub04_compliance import agentic_thought_secret_scanner
from dasafo_FACTORY.mcp_tools.hub01_strategy import project_management

project = "/home/david/Documents/AI/AGENTES/PROJECTS/ContentRepurpose"
agent = "ORCHESTRATOR"

print("--- STEP 1: SECURITY GATE ---")
try:
    res, _ = agentic_thought_secret_scanner(agent=agent, target_project=project)
    print(json.dumps(res, indent=2))
except Exception as e:
    print(f"Error Sec Gate: {e}")

print("\n--- STEP 2: DAG ANALYSIS ---")
try:
    res, _ = project_management(agent=agent, target_project=project, action="analyze_schedule")
    print(json.dumps(res, indent=2))
except Exception as e:
    print(f"Error DAG Analysis: {e}")
