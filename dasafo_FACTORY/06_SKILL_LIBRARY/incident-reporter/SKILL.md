---
version: 3.2.0-S
agent: DEVOPS_SRE
---

# 📡 Skill | Incident Reporter

## Objective
Translate raw industrial connectivity failures into actionable intelligence for the factory, ensuring rapid triage and resolution by the Orchestrator.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `target_url` (string): The endpoint or service that failed.
- `error_code` (integer): HTTP status or system error code.
- `priority` (string, optional): "URGENT" | "HIGH" | "MEDIUM". Default "HIGH".

### Output Schema (SkillOutput.result)
- `incident_id`: (string) Unique ID for the incident (INC-YYYYMMDD-HHMM).
- `incident_path`: (string) Absolute path to the incident log.
- `status`: (string) "REPORTED".

### ⚖️ Mandato SI (Sistema Internacional)
Los reportes de tiempo de inactividad (downtime) y latencia de respuesta durante el incidente deben expresarse estrictamente en segundos o milisegundos (unidades del SI).

## 🧠 Protocol
1.  **Detect:** Triggered by `healthcheck-poller` failures.
2.  **Evidence:** Capture target URL, error code, and last agent operating in the context.
3.  **Format:** Generate a structured incident report for the `ORCHESTRATOR`.
4.  **Notify:** Persist report to `$TARGET_PROJECT/LOGS/incidents/` and trigger relay.

---
*Skill v3.2.0-S | Status: Standardized.*
