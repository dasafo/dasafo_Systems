# dasafo_System | Database Initialization Ritual
>
> **Ritual:** Connectivity and Health Verification.

## Actions

1. **Connection Check:** Verify active links to PostgreSQL/MongoDB/Redis via MCP.
2. **Schema Audit:** Run `drift_check` to ensure the current database state matches the `PROJECT_STATE.json` definitions.
3. **Log Check:** Inspect `LOGS/agents/db_master.log` for any deadlocks or slow query warnings from previous sessions.
4. **Maintenance:** Execute routine VACUUM or Index Rebuilds if necessary.
