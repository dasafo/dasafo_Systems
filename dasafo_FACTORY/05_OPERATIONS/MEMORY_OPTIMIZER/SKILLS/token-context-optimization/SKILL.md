---
description: Optimizing the LLM context window by deduplicating and compressing episodic project data.
---

# 🧠 Token & Context Optimization
> **Status:** v3.1.5 "Solidity Guard" | **Focus:** Industrial Efficiency Synthesis

Based on the [Claude-brewcode Memory Optimizer](https://skills.sh/kochetkov-ma/claude-brewcode/memory-optimize) standard.

## Phase 1: Context Loading & Deduplication
1. Scan `$TARGET_PROJECT/LOGS/` and `TASKS/04_ARCHIVE/`.
2. Cross-reference with `dasafo_FACTORY/00_GLOBAL_KNOWLEDGE/`.
3. **Action:** Delete any memory entry or log repetition that is already defined in the Global Knowledge base (Redundancy check).

## Phase 2: Structural Migration
- If a fact in the logs applies to ALL projects → Move to `dasafo_FACTORY/00_GLOBAL_KNOWLEDGE/`.
- If a fact is an architectural decision for THIS project only → Move to `$TARGET_PROJECT/LOCAL_KNOWLEDGE/ARCHITECTURE.md`.
- **Goal:** Keep the active execution context focused only on the *current task*.

## Phase 3: High-Density Compression
- Convert verbose descriptions into **imperative one-liners**.
- Transform multiple related log entries into **Markdown Tables**. Tables are significantly more token-efficient than prose for LLMs.
- Example: 
  - *Before:* "The agent noticed that the database port was wrong and changed it to 5432 after three failed attempts."
  - *After:* `| Fix | DB Port corrected to 5432 |`
