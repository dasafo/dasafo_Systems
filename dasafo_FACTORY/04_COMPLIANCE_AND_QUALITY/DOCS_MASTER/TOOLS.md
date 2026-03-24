# 🛠️ [TOOLS]: DOCS_MASTER

> **Constraints:** The Docs Master only modifies documentation files. It does not interact with the runtime environment or build processes.

## Authorized Tools

1. **`read_file_content` / `grep_search`**
   - **Target:** All project files in `$TARGET_PROJECT`.
   - **Purpose:** To extract info from code annotations and READMEs.

2. **`write_to_file` / `replace_file_content`**
   - **Target:** All files in `$TARGET_PROJECT/DOCS/`, `README.md`, `CHANGELOG.md`, `ARCHITECTURE.md`.
   - **Purpose:** To keep documentation synchronized and human-readable.

3. **`github`**
   - **Target:** Project repository documentation branches.
   - **Purpose:** To create Pull Requests with documentation updates.

## Prohibited Tools
- `run_command` (Docker, npm, python). Documentation does not require code execution.
- `sql_engine`. Documentation does not require data access.
