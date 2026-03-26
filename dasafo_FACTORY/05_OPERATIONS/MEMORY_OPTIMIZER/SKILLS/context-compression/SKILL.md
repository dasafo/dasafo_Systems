---
description: How to safely compress episodic logs into semantic memory without losing critical technical facts.
---

# 🧠 Context Compression
> **Status:** v3.1.5 "Solidity Guard" | **Focus:** Industrial Semantic Memory

1. **Sweep Episodic Logs:** Periodically scan `$TARGET_PROJECT/LOGS/agents/*.log`.
2. **Extract Facts:** Ignore "conversational fluff", agent greetings, and repetitive error loops. Isolate:
   - Final decisions (e.g., "We chose PostgreSQL over MySQL").
   - Schemas and explicit DTOs.
   - Fixed bugs and their root causes (e.g., "CORS was failing, fixed via FastMCP proxy").
3. **Format & Embed:** Combine these facts into a structured JSON or Markdown file (`SEMANTIC_INDEX.md`).
4. **Truncate:** Once the semantic extraction is verified, truncate the episodic log file to free up Token Context Window for the active agents.
