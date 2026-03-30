---
description: Generates a visual report of project progress, including Kanban state and Infrastructure v3.4.0-S health.
---

# Workflow /factory-status

This flow generates a consolidated health and status report for the current project context.

1. **Agent:** `DEPLOYMENT_MONITOR`
2. **Execution Protocol**: // turbo
3. **Run Pulse Check**: Execute the following command for a real-time status:
   `python3 dasafo_FACTORY/skill_engine.py --agent DEVOPS_SRE --skill project-management --target-project PROJECTS/$TARGET_PROJECT`

4. **Status Mapping**: Extract task metrics from `PROJECTS/$TARGET_PROJECT/TASKS` and compile into a visual report.

**Capturing industrial project pulse...**
