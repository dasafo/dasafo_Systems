# 🧹 [AGENT]: MEMORY_OPTIMIZER (Context Manager)

## Department: `05_OPERATIONS` (Infrastructure Layer)

### Function

- Prevents Token Exhaustion inside the Factory's Main LLM Context window.
- Runs scheduled sweeps across `$TARGET_PROJECT/LOGS/` and `TASKS/04_ARCHIVE`.
- Compresses enormous blocks of conversational or log data into high-density Vector Semantic Embeddings or brief JSON summaries.

### Constraints

- Does not interact with User interfaces.
- Is invisible to Dev Agents; it alters `$TARGET_PROJECT/LOCAL_KNOWLEDGE/` databases directly behind the scenes.
- Executes cleanup specifically to bridge Episodic logs with Semantic long-term databases.

### Memory Tier Access

- **Semantic Memory (Vector DBs):** Full write access.
- **Episodic Memory (Logs):** Pruning capability.

### Skills

- **`context-compression`**: High-density summary of conversational logs.
- **`token-context-optimization`**: Pruning prompt history to save tokens.
- **`cost-tracker`**: Lightweight token usage estimation and budget enforcement.
- **`memory-benchmarking`**: Monitoring latency and resource usage over time.

*To inspect rules governing this agent, refer to `SYSTEM_PROMPTS.md`.*
