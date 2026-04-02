# 🛠️ Skill: deployment-health-check

> **Standard:** v4.0-S "Industrial Core - Auto-Deploy Enabled"
> **Owner:** DEPLOYMENT_MONITOR & DEVOPS_SRE
> **Objective:** Real-time endpoint validation, SI metric reporting, and Host Persistence Ignition.

## 📋 Input Schema (v4.0-S)

- `url` (string): The endpoint to verify (e.g., "<http://localhost:3000/health>").
- `timeout_seconds` (number): Max wait time in Seconds (s). Default: 5.
- `action` (string):
  - `check_endpoint` (default): Only pings the target URL.
  - `deploy`: Executes `docker compose up --build -d` in the host infrastructure before pinging.

## 📊 Success Criteria (DAST)

1. **Physical Artifact:** A JSON health report MUST be generated in `LOGS/deployment/`.
2. **SI Compliance:** Latency MUST be reported in Seconds (s) and payload in Bytes (B).
3. **Auto-Commit:** The task will be logically closed by the System Hook (Aduana Universal) upon successful execution. The agent only needs to guarantee the physical creation of the `HEALTH_*.json` artifact.

## 🛡️ Guardrails

- **Hallucination Guard:** The skill returns "UNREACHABLE" if the network fails; it never assumes success.
- **Secret Scanner:** The tool log is stripped of sensitive headers before saving to disk.
