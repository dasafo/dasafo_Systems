---
version: 3.3.0-S
agent: Multiple (ORCHESTRATOR / FACTORY_EVOLVER)
---

# 🔍 Skill | Pattern Recognition

## Objective

Identify recurrent anomalies and fixes across the industrial ecosystem to abstract them into global standards, optimizing the factory's systemic flow.

## 🛠️ Interface (v3.3.0-S)

### Input Schema (SkillInput.params)

- `scope` (string, optional): "global" | "local". Default "global".
- `min_occurrences` (integer, optional): Default 3.

### Output Schema (SkillOutput.result)

- `patterns_identified`: (list) List of recurrent behaviors.
- `proposed_standard`: (string) Draft of a new rule or standard.
- `vibe_check`: (string) "OPTIMIZED".

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica de frecuencia de errores o ahorro de tiempo proyectado por el nuevo estándar debe expresarse en el SI (Hz, segundos).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Evidence Based:** Patterns MUST be derived from physical project logs and `FEEDBACK-LOG.md`. Hallucinating "optimal patterns" without physical evidence is FORBIDDEN.
- **Traceability:** Proposed standards MUST reference the specific log IDs that triggered the generalization.

## Workflow

1. **Anomaly Detection:** Scan multiple project logs and `FEEDBACK-LOG.md` files for repeated manual interventions.
2. **Generalization:** Abstract the specific solution into a project-agnostic global rule.
3. **Standardization:** Propose a modification to `CODING_STANDARDS.md` or `IDENTITY.md`.
4. **Evolution:** Update factory core instructions after human approval (RA-authorized).

---
**ORIGIN:** [pattern-recognition by supercent-io](https://skills.sh/supercent-io/skills-template/pattern-recognition)
*Skill v3.3.0-S | Status: Standardized & Industrialized.*
