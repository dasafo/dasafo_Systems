# 🛠️ DEPLOYMENT_MONITOR | Tools & Senses (v4.0-MCP)

> **Standard:** v4.0-MCP "Industrial Core - DAST Optimized".

## 📡 Senses (Context-Limited)

- **Log Sense:** Authority to read deployment logs in `LOGS/`.
- **Endpoint X-Ray:** Read-only access to verify HTTP codes and response times.
- **DAST Sense:** Ability to verify the physical integrity of tasks and records.

## 🧰 Authorized Skills (Factory Engine)

*(CRITICAL: All skills MUST be invoked EXCLUSIVELY via the `execute_industrial_skill` MCP Tool).*

- `telemetry-analyzer`: Deep synthesis of resource usage (B) and execution times (s).
- `playwright-ui-tester`: Verify that the UI is physically reachable.
- `hallucination-guardrail`: Ensure that reports are based on real logs.
- `deployment-health-check`: Real-time health-check validation (s/B).

---
*Deployment Monitor v4.0-MCP | Status: Solidified.*
