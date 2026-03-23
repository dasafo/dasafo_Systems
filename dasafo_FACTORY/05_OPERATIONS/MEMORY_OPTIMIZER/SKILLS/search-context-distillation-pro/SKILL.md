# Skill: Search Context Distillation Pro
> **Source:** https://skills.sh/exa-awesome-skills/context-search (Adapted)
> **Agent:** MEMORY_OPTIMIZER

## Objective
Filter and compress bulky agent logs into dense, high-value architectural and factual summaries.

## Procedure
1.  **Semantic Clustering:** Identify related lines of thought in raw logs using keyword proximity.
2.  **Fact Extraction:** Isolate ADRs (Architectural Decision Records), Bug fixes, and Environment changes.
3.  **Distillation:** Rewrite the raw discourse into a structured Markdown or JSON format for the `SEMANTIC_INDEX.md`.
4.  **Noiseless Pruning:** Delete purely conversational or debug/verbose lines that provide no long-term value.

## Constraints
NEVER delete a log until its summary has been validated by an internal checksum.
