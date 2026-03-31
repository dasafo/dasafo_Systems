# 🛠️ Skill: deployment-health-check
>
> **Standard:** v3.4.0-S "Industrial Core"
> **Owner:** DEPLOYMENT_MONITOR
> **Objective:** Real-time endpoint validation and SI metric reporting.

## 📋 Input Schema (v3.4.0-S)

- `url` (string): The endpoint to verify (e.g., "<https://api.project.com/health>").
- `timeout_seconds` (number): Max wait time in Seconds (s). Default: 5.
- `action` (string): `check_endpoint` (default).

## 📊 Success Criteria (DAST)

1. **Physical Artifact:** A JSON health report MUST be generated in `LOGS/deployment/`.
2. **SI Compliance:** Latency MUST be reported in Seconds (s) and payload in Bytes (B).
3. **Atomic Move:** The task must be closed via `registry-manager` upon completion.

## 🛡️ Guardrails

- **Hallucination Guard:** The skill returns "UNREACHABLE" if the network fails; it never assumes success.
- **Secret Scanner:** The tool log is stripped of sensitive headers before saving to disk.

---
*Generated for dasafo_FACTORY v3.4.0-S*
