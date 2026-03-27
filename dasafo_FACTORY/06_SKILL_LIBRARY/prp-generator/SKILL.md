---
version: 3.2.0-S
agent: PRODUCT_OWNER
---

# 📄 Skill | PRP Generator

## Objective
Transform raw user vision strings into structured, industrial-grade `PRP_CONTRACT.json` blueprints, following the Dasafo Factory standards.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `project_name` (string): Name of the new mission.
- `objective` (string): Industrial vision or breakthrough goal.

### Output Schema (SkillOutput.result)
- `prp_blueprint`: (object) The generated JSON structure.
- `blueprint_path`: (string) Absolute path to the contract.
- `status`: "DRAFTED".

### ⚖️ Mandato SI (Sistema Internacional)
Cualquier métrica incluida en el PRP (tiempos de latencia, presupuesto en bytes, precisión del 99.9%) debe expresarse en unidades del SI.

## Functional Protocol
1.  **Extraction:** Identify constraints, goals, and KPIs from the Product Owner's context.
2.  **Templating:** Use global schemas to ensure 1:1 compliance with the Factory Core.
3.  **Drafting:** Generate a versioned contract in `$TARGET_PROJECT/LOCAL_KNOWLEDGE/contracts/`.
4.  **Security Gate:** Insert mandatory `SOLIDITY_AUDIT` marker in the blueprint.

---
*Skill v3.2.0-S | Status: Standardized.*
