# Skill: Scikit-Learn Pipeline Master
> **Source:** https://skills.sh/davila7/claude-code-templates/scikit-learn
> **Agent:** DATA_SCIENTIST

## Objective
Build and validate machine learning models using strict Scikit-Learn Pipelines to ensure production readiness.

## Core Capabilities
- **`Pipeline & ColumnTransformer`:** Separate numeric and categorical preprocessing.
- **`Evaluation & Selection`:** Use Stratified Splitting and specific metrics (Precision/Recall/F1) suited for the mission.
- **`Reproducibility`:** Mandatory use of `random_state` in every model.

## Workflow
1.  **EDA:** Perform significance tests using Scipy before modeling.
2.  **Define Pipeline:** Enclose both `StandardScaler` (or equivalent) and `Estimator` in a single Pipeline.
3.  **Validate:** Perform 5-fold cross-validation and document results in `$TARGET_PROJECT/LOGS/experiments/`.
