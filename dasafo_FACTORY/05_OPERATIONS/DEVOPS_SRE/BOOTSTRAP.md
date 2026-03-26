# dasafo_System | Operations Startup Ritual
> **Version:** v3.1.5 "Solidity Guard"
>
> **Ritual:** Infrastructure Integrity Check.

## Actions

1. **Container Health Audit:** Execute `docker ps` to ensure all production services (DB, API, Frontend) are running.
2. **Environment Sync:** Verify that `.env` files match the requirements in `PROJECT_STATE.json`.
3. **Resource Inventory:** Check available RAM and Disk space on the host machine.
4. **Log Readiness:** Verify that `LOGS/sessions/` is writable.
5. **Infrastructure State Registry:** Register the current state hash in `INFRA_SOLIDITY_HASH` for cross-agent validation.
