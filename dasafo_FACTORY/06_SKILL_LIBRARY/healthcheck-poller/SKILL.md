---
version: 3.2.0-S
agent: DEVOPS_SRE
---

# 💓 Skill | Healthcheck Poller

## Objective
Automated ping and validation for deployed industrial endpoints to ensure continuity and system reliability.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `endpoint` (string): The URL or internal port to check.
- `expected_status` (integer, optional): Default 200.

### Output Schema (SkillOutput.result)
- `status`: (string) "OPTIMAL" | "DOWN".
- `latency_ms`: (integer) Time in milliseconds (SI).
- `incident_id`: (string, optional): ID if healthcheck fails.

### ⚖️ Mandato SI (Sistema Internacional)
La latencia detectada y el tiempo entre pings deben reportarse estrictamente en milisegundos o segundos (unidades del SI).

## Failure Protocol
1.  **Mark:** Flag service as "DOWN" in physical telemetry.
2.  **Telemetry:** Update `$TARGET_PROJECT/PROJECT_TELEMETRY.md` with incident log.
3.  **Notify:** Signal `ORCHESTRATOR` for autonomous fix or urgent human escalation.

---
*Skill v3.2.0-S | Status: Standardized.*
