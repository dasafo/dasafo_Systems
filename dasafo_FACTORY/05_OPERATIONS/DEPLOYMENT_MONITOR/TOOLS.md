# 🛠️ Deployment Monitor | Tools & Senses
>
> **Scope:** Operational monitoring and health-check auditing.

## 📡 Senses (MCP Protocol)
- **Network Sense:** Full bridge to `read_url_content` and `curl` for endpoint validation.
- **Resource Sense:** Terminal access to `docker ps`, `top`, and `df` for saturation monitoring.
- **Filesystem Sense:** Write access to `$TARGET_PROJECT/LOGS/ops/` and `OPERATIONAL_STATUS.md`.

## 🔧 Internal Tools
- **Health_Poller:** (Functional) Asynchronous probe for HTTP and socket availability.
- **Resource_Scanner:** (Simulated) Script to aggregate container metrics across projects.
- **Incident_Framer:** (Simulated) Logic to format Slack/Telegram alerts from raw logs.

---
*Ops Tools v3.1.5 | Status: Solidified.*
