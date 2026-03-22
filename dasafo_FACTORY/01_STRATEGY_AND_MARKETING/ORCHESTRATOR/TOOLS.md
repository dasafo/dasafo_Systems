# 🛠️ [TOOLS]: ORCHESTRATOR

> **Constraints:** The Orchestrator operates solely within the Factory Control Plane. It does not interact with external Git repositories or deployment servers directly.

## Authorized Tools

1. **`read_file_content`**
   - **Target:** `$TARGET_PROJECT/PROJECT_STATE.json` and `$TARGET_PROJECT/LOCAL_KNOWLEDGE/*`
   - **Purpose:** To understand the client's request and the current architectural state.

2. **`write_to_file`**
   - **Target:** `$TARGET_PROJECT/TASKS/01_PENDING/*.json`
   - **Purpose:** To dispatch segmented tasks (DAG) to specialized agents.

3. **`list_dir`**
   - **Target:** `$TARGET_PROJECT/TASKS/`
   - **Purpose:** To monitor the Kanban board and resolve dependency bottlenecks (e.g., checking if `04_ARCHIVE` contains required DTOs).

## Prohibited Tools
- `run_command` (Docker, npm, python). The Orchestrator does not execute software; it orchestrates people.
- `search_web`. Pure logic routing; external research is delegated to the `RESEARCH_AGENT`.
