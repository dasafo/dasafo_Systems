# 🛠️ [TOOLS]: MEMORY_OPTIMIZER

> **Constraints:** This agent operates invisibly in the background. It only reads logs and writes to vector stores or memory index files.

## Authorized Tools

1. **`list_dir` & `read_file_content`**
   - **Target:** `$TARGET_PROJECT/LOGS/agents/*`
   - **Purpose:** To read raw, verbose conversational logs and debugging outputs.

2. **`write_to_file` & `multi_replace_file_content`**
   - **Target:** `$TARGET_PROJECT/LOCAL_KNOWLEDGE/SEMANTIC_INDEX.md`
   - **Purpose:** To write compressed summaries and extract hard architectural facts from chatty logs.

3. **`run_command` (Vector Integration)**
   - **Purpose:** Authorized to run scripts that push embedded JSON data to NoSQL/Vector databases (e.g., Pinecone, Supabase Vector) for long-term semantic search.

## Prohibited Tools
- Modification of `$TARGET_PROJECT/WORKSPACE/*`. Modifying code is strictly forbidden.
