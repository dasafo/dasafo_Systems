# 🛠️ DEPLOYMENT_MONITOR | Tools & Senses

> **Standard:** v4.0-S "Industrial Core - DAST Optimized".

## 📡 Senses (Context-Limited)

- **Log Sense:** Authority to read deployment logs in `LOGS/`.
- **Endpoint X-Ray:** Read-only access to verify HTTP codes and response times.
- **DAST Sense:** Ability to verify the physical integrity of tasks and records before issuing a health verdict.

## 🧰 Authorized Skills

- `telemetry-analyzer`: Deep synthesis of resource usage (B) and execution times (s).
- `playwright-ui-tester`: Verify that the UI is physically reachable.
- `hallucination-guardrail`: Ensure that reports are based on real logs, not assumptions.
- `deployment-health-check`: Real-time health-check validation (s/B).
