---
description: Automated ping and response validation for deployed endpoints.
---

# 💓 Skill | Healthcheck Poller
> **Version:** v3.1.5 "Solidity Guard"

1. **Endpoint Target:** Read the deployment configuration from `DEVOPS_SRE` (e.g., Docker port or URL).
2. **Ping Execution:** Run a silent `curl -I` or equivalent check on the endpoint.
3. **Response Validation:** Verify that the status code is `200 OK` or expected.
4. **Failure Protocol:** If status is `5xx`, `4xx` or timeout:
   - Mark the service as "DOWN".
   - Create an incident log in `PROJECT_TELEMETRY.md`.
   - Notify the Orchestrator for urgent redeployment/fix.
