# 📚 00_GLOBAL_KNOWLEDGE
>
> **Version:** v3.2.0-S "Modular Toolbox"
> **Scope:** Shared intelligence and industrial standards for all Factory agents.

## 🏗️ Repository Structure

| Compartment | Purpose | Status |
| :--- | :--- | :--- |
| `01_CODING_STANDARDS.md` | Logic, Solidity, and Vibe rules. | **ACTIVE** |
| `02_ARCHITECTURE_RULES.md` | Boundaries, DTOs, and SoC. | **ACTIVE** |
| `03_SCIENTIFIC_RIGOR.md` | SI Units, Error handling, and Physics. | **ACTIVE** |
| `04_SECURITY_AND_OPS.md` | Zero-Trust, Secrets, and IaC. | **ACTIVE** |
| `SYSTEM_PROMPTS.md` | The Global Soul (Meta-Prompt). | **ACTIVE** |
| `CATALOG.md` | Index of all skills in `06_SKILL_LIBRARY/`. | **SYNCED** |
| `TEMPLATES/` | Industrial boilerplate for contracts & reports. | **MODULAR** |

## 🕹️ Operational Rules

1. **Modular Toolbox:** All skills reside in `06_SKILL_LIBRARY/` and are invoked via `skill_engine.py`.
2. **SSoT:** The only sources of truth are the 3 Pillars (`00`, `01`, `02`) and the physical `PROJECT_STATE.json` of each project.
3. **Traceability:** Every change must be recorded in the project's `FEEDBACK-LOG.md`.

---
*Industrial Knowledge Base v3.2.0-S | dasafo_FACTORY.*
