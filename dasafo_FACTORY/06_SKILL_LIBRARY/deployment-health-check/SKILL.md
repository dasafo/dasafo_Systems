---
version: v5.0-MCP (Native)
agent_authorization: [DEPLOYMENT_MONITOR, DEVOPS_SRE, FACTORY_EVOLVER]
production_category: SHIP
protocol: Auto-Heal / DAST
---

# 🚀 Skill | deployment-health-check

## Objective

Real-time endpoint validation and SI metric reporting. Includes the **Immune System Protocol** to trigger emergency infrastructure patches via FACTORY_EVOLVER.

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use typed arguments. `params_json` is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your Agent ID (DEPLOYMENT_MONITOR, DEVOPS_SRE).
- `target_project` (string): Path to project root.
- `action` (enum): `check_endpoint` (default) | `deploy`.
- `url` (string): Target health URL (default: `http://localhost:3000/health`).
- `timeout_seconds` (integer): Max wait time (default: 5).
- `isolate` (boolean): Execution in Clean Session.

## 🛡️ Industrial Constraints

- **Immune Response:** If `deploy` fails, the skill MUST generate a physical `EMERGENCY_SPEC.json` in `TASKS/01_PENDING/`.
- **SI Standards:** Latency in **Seconds (s)** and payload in **Bytes (B)**.
- **DAST Sovereignty:** Physical JSON report required in `LOGS/deployment/`.

---
*Standard v5.0-MCP | Dasafo Factory Operations Hub.*
