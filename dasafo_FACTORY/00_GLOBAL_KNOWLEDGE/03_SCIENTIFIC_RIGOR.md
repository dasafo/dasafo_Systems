# 🔬 03. Scientific Rigor
>
> **Standard:** v3.3.1-S "Industrial Core"

## 1. Zero Trust Policy

Never trust input data. Sanitize and validate at every layer boundary using strongly typed contracts and schemas. All industrial skills MUST validate their input against the authorized registry.

### 2. Versioning Beyond Code

* **Artifact Lifecycle:** Data, models, and simulation results are physical artifacts.
* **Traceability:** Every model training session must tag the exact version of the training dataset.
* **Temporal Decoupling:** Long-running processes should communicate via asynchronous events to prevent sync-lock between agents.

## 3. Experimental Method

Every major architectural change must follow:

1. **Hypothesis**: What do we want to solve?
2. **Analysis**: Comparative study via technical research (e.g., `tech-stack-evaluator`).
3. **Draft**: ADR (Architectural Decision Record).
4. **Validation**: Automated tests and Solidity Gate verification.

## 4. SI Units & Precision

- Mandatory use of **Seconds (s)** for time and **Bytes (B)** for data size in all performance and resource reports.
- Floating point precision must be explicitly handled in scientific calculations.

## 5. Error Logging (AutoShield)

Failures are data. Every error must be caught and distilled into the `FEEDBACK-LOG.md` using the unified `FEEDBACK_SCHEMA.json` to prevent systemic recurrence.

---
*Scientific Rigor v3.3.1-S | dasafo_FACTORY.*
