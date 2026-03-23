# Skill: ML Experiment Tracker
> **Source:** https://skills.sh/supercent-io/skills-template/ml-experiment-tracking
> **Agent:** DATA_SCIENTIST

## Objective
Maintain a rigorous, immutable log of every machine learning experiment to guarantee reproducibility.

## Log Parameters
Every experiment entry MUST record:
- **`timestamp`:** ISO format.
- **`model_version`:** git hash or unique ID.
- **`hyperparameters`:** Full JSON dictionary (Learning rate, depth, etc.).
- **`metrics`:** Score results (RMSE, Accuracy, etc.).
- **`dataset_checksum`:** Hash of the data used for training.

## Automation
Before completing a task, the scientist MUST append the result to `$TARGET_PROJECT/LOGS/ML_EXPERIMENT_LOG.md`.
