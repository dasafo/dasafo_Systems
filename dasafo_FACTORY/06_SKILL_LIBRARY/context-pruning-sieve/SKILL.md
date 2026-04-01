---
version: v4.0-S
agent: MEMORY_OPTIMIZER
source: https://skills.sh/sickn33/antigravity-awesome-skills/context-optimization
---

# 🧠 Skill | Context Pruning Sieve (v4.0-S)

## Objective

Extend the effective capacity of agent context windows through strategic compaction, observation masking, and KV-cache optimization. This skill prevents Token Decay and reduces operational latency/costs.

## 🛠️ Interface (v4.0-S)

### Input Schema (SkillInput.params)

- `action` (enum): `compact_context`, `mask_observations`, `optimize_cache_order`.
- `target_project` (string, mandatory): Absolute path to the project workspace.
- `target_file` (string, mandatory): Path to the session log or context file to optimize (e.g., `LOGS/sessions/current.json`).
- `budget_threshold` (float, optional): Token utilization threshold to trigger optimization (Default: 0.8).

### Output Schema (SkillOutput.result)

- `optimization_status`: (string) `COMPACTED`, `MASKED`, or `REORDERED`.
- `original_size_bytes`: (integer) Initial file size in bytes (SI Mandate).
- `optimized_size_bytes`: (integer) Final file size in bytes (SI Mandate).
- `compaction_ratio`: (float) Percentage of reduction achieved.
- `artifacts_produced`: (array) Path to the optimized physical artifact.
- `industrial_status`: (string) "SOLIDIFIED - CONTEXT PRUNED".

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica de reducción de contexto o tamaño de archivo debe expresarse estrictamente en **bytes** (B). El tiempo de ejecución del algoritmo de compresión debe medirse en **segundos** (s).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Observation Masking:** "Observation masking replaces verbose tool outputs with compact references.". Raw tool outputs over 500 bytes MUST be masked if older than 3 turns.
- **Cache-Friendly Ordering:** "Place stable elements first (system prompt, tool definitions), then frequently reused elements, then unique elements last.".
- **Non-Destructive Pruning:** The original context file must be preserved. Output must be saved to a new file (e.g., `*_optimized.json`).
