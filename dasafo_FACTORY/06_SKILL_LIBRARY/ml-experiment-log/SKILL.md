---
version: 3.2.0-S
agent: DATA_SCIENTIST
---

# 📊 Skill | ML Experiment Tracker

## Objective

Maintain a rigorous, immutable log of every machine learning experiment to guarantee scientific reproducibility and industrial quality.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `experiment_data` (object): Dictionary containing hyperparameters, metrics, and dataset hash.
- `model_id` (string): Unique identifier for the model version.

### Output Schema (SkillOutput.result)

- `log_path`: (string) Path to the `ML_EXPERIMENT_LOG.md`.
- `status`: (string) "REPRODUCIBLE".

### ⚖️ Mandato SI (Sistema Internacional)

Todas las métricas de rendimiento (péridida, precisión, tiempo de entrenamiento, latencia de inferencia) deben reportarse estrictamente bajo el SI.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Immutable Persistence:** All experiment results MUST be physically appended to `ML_EXPERIMENT_LOG.md`.
- **Integrity Lock:** Success requires a valid `dataset_checksum` (hash) to ensure reproducibility. Hallucinating a log entry without a physical model artifact is FORBIDDEN.

## Log Parameters

- **`timestamp`:** ISO format.
- **`model_version`:** Git hash or unique ID.
- **`hyperparameters`:** Full JSON dictionary.
- **`metrics`:** Scores (RMSE, Accuracy, etc.).
- **`dataset_checksum`:** Hash of training data.

---
*Skill v3.2.0-S | Status: Standardized.*
