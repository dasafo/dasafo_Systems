---
description: Activates the Deployment_Monitor to verify real-time health and SI metrics of the live project (v4.0-S).
---

# Workflow /health-check

This flow validates that the deployment is reachable and performing under industrial standards.

1. **Agent:** `DEPLOYMENT_MONITOR`
2. **Execution Protocol:** // turbo
3. **Run Health Check:** `python3 dasafo_FACTORY/skill_engine.py --agent DEPLOYMENT_MONITOR --skill deployment-health-check --target-project $TARGET_PROJECT`

4. **SI Verification:** Ensure latency is reported in **seconds (s)** and response size in **bytes (B)**.

**Monitoring industrial pulse...**
