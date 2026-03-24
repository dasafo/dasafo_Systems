# 🛠️ [TOOLS]: DEPLOYMENT_MONITOR

> **Constraints:** The Deployment Monitor observes live environments. It only interacts with the factory through reporting and does not change application code.

## Authorized Tools

1. **`read_url_content` / `read_browser_page`**
   - **Target:** Production and staging URLs of `$TARGET_PROJECT`.
   - **Purpose:** To verify application availability and performance.

2. **`run_command`**
   - **Target:** Remote or local containers/servers.
   - **Purpose:** Restricted to status checks: `docker ps`, `curl`, `pm2 status`, etc.

3. **`write_to_file`**
   - **Target:** `$TARGET_PROJECT/OPERATIONAL_STATUS.md`
   - **Purpose:** To log incident reports and uptime metrics.

## Prohibited Tools
- `github` (write access). Changes to code must be triggered by `ORCHESTRATOR` via `DEVOPS_SRE`.
- `sql_engine`. Monitoring does not require database write access.
