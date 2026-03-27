---
version: 3.2.0-S
agent: DEVOPS_SRE
---

# 🖥️ Skill | Server Management

## Objective
Enforce production server operations stability covering process management, real-time monitoring, and frictionless scaling decisions.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `action` (string): "status" | "restart" | "scale".
- `service` (string, optional): Default "factory_node".

### Output Schema (SkillOutput.result)
- `server_uptime_s`: (integer) (SI units).
- `maintenance_verdict`: (string) "NOMINAL" | "REQUIRES_ACTION".
- `active_processes`: (list) List of running industrial containers.

### ⚖️ Mandato SI (Sistema Internacional)
Tiempos de actividad (uptime), latencias de red y consumo de recursos deben reportarse exclusivamente en el SI.

## Core Rules
1.  **Process Management:** Mandate Docker/Systemd for auto-recovery and resource awareness.
2.  **Monitoring:** Continuous tracking of CPU, RAM, Disk, and IO thresholds.
3.  **Logging:** Strict JSON output, rotation and zero-PII leakage policy.
4.  **Scaling:** Decide vertical vs horizontal based on sustained SI metrics.
5.  **Troubleshooting:** Process -> Logs -> Resources -> Network -> Dependencies.

---
*Skill v3.2.0-S | Status: Standardized.*
