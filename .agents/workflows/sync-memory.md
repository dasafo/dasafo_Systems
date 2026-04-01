---
description: Activates the MEMORY_OPTIMIZER to extract Golden Rules from logs and sync them to the Neo4j Knowledge Graph (v4.0-S).
---

# Workflow /sync-memory

This flow acts as the factory's "sleep cycle", converting short-term logs into Long-Term Persistence (LTP) to prevent future hallucinations.

1. **Agent:** `MEMORY_OPTIMIZER`
2. **Execution Protocol:** // turbo
3. **Extract & Sync:** Execute the following command:
   `python3 dasafo_FACTORY/skill_engine.py --agent MEMORY_OPTIMIZER --skill autonomous-feedback-analyzer --target-project $TARGET_PROJECT`

**Persisting agentic engrams to Neo4j...**
