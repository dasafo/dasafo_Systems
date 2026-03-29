---
version: 3.3.1-S
agent: PRODUCT_OWNER
source: https://skills.sh/daffy0208/ai-dev-standards/prp-generator
---

# 📝 Skill | PRP Generator (v3.3.1-S)

## Objective

Generate a high-solidity **Product Requirements Prompt (PRP)** that defines the "What" of a project before any code is written. This skill enforces a 12-section structure to eliminate scope creep and ensure measurable success criteria, technical grounding, and pattern classification (A, B, or C).

## 🛠️ Interface (v3.3.1-S)

### Input Schema (SkillInput.params)

- `action` (enum): `init`, `generate`, `update`, `validate`.
- `project_name` (string, mandatory): Short name of the project.
- `problem_description` (string, mandatory): The core problem to solve.
- `pattern` (enum): `A` (Simple Feature), `B` (New Product), `C` (AI-Native System).
- `target_project` (string, mandatory): Absolute path to the project root.

### Output Schema (SkillOutput.result)

- `prp_content`: (string) The full 12-section PRP document.
- `prp_path`: (string) Path to the generated `PRP_CONTRACT.json` or `PRP.md`.
- `solidity_score`: (float) Confidence metric (0.0-1.0) based on section completeness.
- `open_questions`: (array) List of missing or vague requirements.
- `industrial_status`: (string) "SOLIDIFIED - PRP CONTRACT SIGNED".

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica de éxito o restricción técnica (latencia < 200ms, almacenamiento > 50GB) debe expresarse estrictamente en unidades del SI (**segundos**, **bytes**).

## 🛡️ Industrial Constraints (Zero-Trust)

- **The 12-Section Mandate:** A PRP is not valid if any of the 12 industrial sections are empty.
- **Measurable Metrics:** Success criteria MUST include a North Star metric with a specific numerical target (e.g., "Reduction > 40%").
- **Boundary Lock:** The PRP must explicitly define "Out of Scope" to prevent agentic overreach.
- **Physical Sync:** The generated PRP must be saved as a physical JSON artifact (`PRP_CONTRACT.json`) in the project root.

## 🧠 Workflow (v3.3.1-S)

1. **Information Gathering:** Analyze the problem statement and success criteria.
2. **Decomposition:** Fill the 12 sections: Overview, Problem, Success, Stories, Functional, Non-Functional, Constraints, Data, UI/UX, Risks, Scope, and Questions.
3. **Pattern Selection:** Classify the project complexity (A, B, or C).
4. **Validation:** Check for "vague" requirements or missing technical constraints.
5. **Solidification:** Generate the physical contract and update the `PROJECT_STATE.json` to reflect `Phase: M1`.

---
**ORIGIN:** [PRP Generator by daffy0208](https://skills.sh/daffy0208/ai-dev-standards/prp-generator)
*Skill v3.3.1-S | Status: Standardized & Industrialized (Dasafo Edition).*
