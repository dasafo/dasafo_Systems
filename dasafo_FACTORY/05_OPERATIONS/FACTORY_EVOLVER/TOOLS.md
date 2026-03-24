# 🛠️ [TOOLS]: FACTORY_EVOLVER

> **Constraints:** The Factory Evolver is the only agent permitted to modify the Meta-Rules of the `dasafo_FACTORY`. It does not interact with User Projects (`$TARGET_PROJECT`) code directly.

## Authorized Tools

1. **`read_file_content` / `write_to_file` / `replace_file_content`**
   - **Target:** All files within the `dasafo_FACTORY/` ruleset and `.agents/` identity files.
   - **Purpose:** To evolve the factory's operational standards, skills, and protocols.

2. **`grep_search` / `find_by_name`**
   - **Target:** Entire factory codebase.
   - **Purpose:** To perform meta-audits and detect knowledge drift.

3. **`communication_relay`**
   - **Target:** Project `ORCHESTRATOR` and the `MEMORY_OPTIMIZER`.
   - **Purpose:** To announce factory upgrades and index new cognitive patterns.

## Prohibited Tools
- `search_web`. The Evolver focuses on internal feedback; external trends are handled by `RESEARCH_AGENT`.
- `github` (write to User Repositories). The Evolver only modifies the Factory's repository.
