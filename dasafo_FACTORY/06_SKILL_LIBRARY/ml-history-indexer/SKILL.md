---
version: 3.2.0-S
agent: MEMORY_OPTIMIZER
---

# 🤖 Skill | ML History Indexer

## Objective

Maintain a searchable, high-performance history of all machine learning experiments, results, and architectural parameters to enable industrial model persistence.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `query` (string, optional): Search term for experiments.
- `time_range_days` (integer, optional): Default 90.

### Output Schema (SkillOutput.result)

- `matched_experiments`: (list) List of serialized experiment metadata.
- `best_performer`: (object, optional): Data of the top-performing model in the range.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica de rendimiento indexada (precisión, F1-score, tiempo de entrenamiento total) debe coincidir con los registros del SI.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Artifact Lock:** Requires physical access to `ML_EXPERIMENT_LOG.md`. Failure to find the log results in an empty result, never a halluncinated history.
- **Physical Verification:** Reports of "best performers" MUST be cross-referenced with the physical `.pth` or `.onnx` artifacts if present.

## Data Processing

1. **Hyperparameter Mapping:** Extract every parameter from the physical `ML_EXPERIMENT_LOG.md`.
2. **Indexing:** Vectorize experiment summaries for semantic recovery.
3. **Analytics:** Compare current results with historical benchmarks to detect regression.

---
*Skill v3.2.0-S | Status: Standardized.*
