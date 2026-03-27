# 🛠️ Deployment Monitor | Tools & Senses

> **Standard:** v3.2.0-S Modular Toolbox
> **Scope:** Production health monitoring, incident reporting, and resource tracking.

## 📡 Senses (MCP Protocol)

- **Terminal Sense:** Execution of healthcheck commands (curl, glances, etc.).
- **Filesystem Sense:** Access to `$TARGET_PROJECT/LOGS/` and `PROJECT_STATE.json`.
- **Memory Sense:** Monitoring of resource usage patterns via the bridge.

## 🧰 Authorized Skills (Skill Library)
*(Invoked via `execute_factory_skill`)*

- `healthcheck-poller`: Scheduled verification of service status.
- `incident-reporter`: Structured reporting of system failures.
- `resource-monitor`: Real-time tracking of CPU/RAM/Disk metrics.
- `autoshield-preflight-check`: Mandatory pre-execution validation.
- `kanban-solidity-gate`: Mandatory gate for updating task status in the Registry SSoT.

---
*Deployment Monitor v3.2.0-S | Status: Modularized.*
