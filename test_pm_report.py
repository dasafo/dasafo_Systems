import sys
sys.path.append("/home/david/Documents/AI/AGENTES/dasafo_FACTORY")
from dasafo_FACTORY.mcp_tools.hub01_strategy import project_management

try:
    res = project_management(
        agent="ORCHESTRATOR",
        target_project="/home/david/Documents/AI/AGENTES/PROJECTS/ContentRepurpose",
        action="standup_report"
    )
    import json
    print(json.dumps(res))
except Exception as e:
    import traceback
    traceback.print_exc()
