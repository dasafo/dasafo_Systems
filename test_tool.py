import sys, os
sys.path.append("/home/david/Documents/AI/AGENTES/dasafo_FACTORY")
from dasafo_FACTORY.mcp_tools.hub04_compliance import agentic_thought_secret_scanner

try:
    res = agentic_thought_secret_scanner(
        agent="ORCHESTRATOR",
        target_project="/home/david/Documents/AI/AGENTES/PROJECTS/ContentRepurpose"
    )
    import json
    print(json.dumps(res))
except Exception as e:
    import traceback
    traceback.print_exc()
