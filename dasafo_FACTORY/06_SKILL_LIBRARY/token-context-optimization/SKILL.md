---
version: 3.2.0-S
agent: MEMORY_OPTIMIZER
---

# 🧠 Skill | Token & Context Optimization

## Objective
Optimize the LLM context window by deduplicating, compressing, and structurally migrating project data, ensuring industrial token efficiency and high cognitive density.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `compression_mode` (string, optional): "table" | "imperative". Default "table".
- `prune_logs_days` (integer, optional): Default 7.

### Output Schema (SkillOutput.result)
- `tokens_saved`: (integer) Count of tokens reduced.
- `migration_summary`: (list) Facts moved to Global vs Local knowledge.
- `efficiency_ratio`: (float) (0.0-1.0).

### ⚖️ Mandato SI (Sistema Internacional)
Toda métrica de ahorro (bytes de disco liberados, tokens economizados) debe reportarse en el SI.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Cognitive Density Lock:** Compression MUST NOT result in the loss of ADR critical facts. Verify against `ARCHITECTURE.md` checksum before pruning.
- **Physical Migration:** Moved facts MUST be physically verified in their new destination (Global/Local Knowledge) before being deleted from logs.

## Optimization Phases

1. **Deduplication:** Scan `$TARGET_PROJECT/LOGS/` and delete repetitions already defined in `00_GLOBAL_KNOWLEDGE/`.
2. **Structural Migration:**
   - Global facts -> `dasafo_FACTORY/00_GLOBAL_KNOWLEDGE/`.
   - Project facts -> `$TARGET_PROJECT/LOCAL_KNOWLEDGE/ARCHITECTURE.md`.
3. **High-Density Compression:** Transform verbose prose into Markdown Tables for maximum token-per-fact density.
4. **Cleanup:** Prune purely conversational or debug/verbose lines that provide zero long-term architectural value.

---
*Skill v3.2.0-S | Status: Standardized.*
