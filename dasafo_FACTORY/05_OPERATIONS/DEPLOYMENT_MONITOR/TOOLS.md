# 🛠️ DEPLOYMENT_MONITOR | Tools & Senses

> **Standard:** v3.4.0-S "SDD Implementation"
> **Scope:** Real-time monitoring, log analysis, and health-check validation.

## 📡 Senses (Context-Limited)
- **Log Sense:** Authority to read deployment logs in `$TARGET_PROJECT/LOGS/`.
- **Endpoint X-Ray:** Read-only access to verify HTTP Status Codes and response times.
- **Spec Sense:** Read access to `SPEC_LITE.json` to verify against expected health thresholds.

## 🧰 Authorized Skills (Skill Library)
*(Lazy loaded only when mandated by the Spec)*

### 📊 Monitoring & Telemetry
- `telemetry-analyzer`: Deep synthesis of resource usage (B/s) and execution times (s).
- `playwright-ui-tester`: (In Smoke-Test mode) Verify that the deployed UI is physically reachable.

### 🛡️ Guardrails
- `hallucination-guardrail`: Mandatory verification to ensure health reports are backed by real logs, not assumptions.

---
*Deployment Monitor v3.4.0-S | Status: Resurrected & Industrialized.*
