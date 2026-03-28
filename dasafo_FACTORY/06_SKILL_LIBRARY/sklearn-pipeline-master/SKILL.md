---
version: 3.2.0-S
agent: DATA_SCIENTIST
---

# 🧪 Skill | Scikit-Learn Pipeline Master

## Objective

Build and validate high-integrity machine learning models using Scikit-Learn Pipelines to ensure production reliability and feature-drift protection.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `model_type` (string): "RandomForest" | "XGBoost" | "LogisticRegression".
- `n_folds` (integer, optional): Default 5.

### Output Schema (SkillOutput.result)

- `mean_f1_score`: (float) Cross-validated metric.
- `pipeline_viz`: (string) Structure of the `ColumnTransformer`.
- `reproducibility_check`: (boolean) True (verified `random_state`).

### ⚖️ Mandato SI (Sistema Internacional)

Toda métrica de rendimiento de modelo (latencia de inferencia en segundos, tamaño del pickle en bytes) debe reportarse en el SI.

## 🛡️ Industrial Constraints (Zero-Trust)

- **State Lock:** Mandatory fixing of `random_state` at every stochastic step. Reporting results from non-deterministic pipelines is FORBIDDEN.
- **Physical Save:** Models MUST be physically saved to `MODELS/` with an associated `METADATA.json` explaining training SI metrics.

## Workflow

1. **Exploration:** Perform Scipy significance tests before modeling.
2. **Orchestration:** Enclose `StandardScaler`, `OneHotEncoder`, and `Estimator` in a single immutable Pipeline.
3. **Cross-Validation:** Execute Stratified K-Fold to document stability in `$TARGET_PROJECT/LOGS/experiments/`.
4. **Reproducibility:** Fix `random_state` at every stochastic step.

---
*Skill v3.2.0-S | Status: Standardized.*
