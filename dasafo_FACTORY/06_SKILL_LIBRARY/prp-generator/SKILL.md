---
version: v4.0-S
agent: PRODUCT_OWNER
source: https://skills.sh/daffy0208/ai-dev-standards/prp-generator
---

# 📝 Skill | PRP & Spec Generator (v4.0-S)

## Objective

Generate industrial-grade requirements artifacts. Supports the dual-track contract system:

- **PRP_MASTER:** 12-section full contract for project discovery (M1).
- **SPEC_LITE:** 4-section atomic specification for isolated task execution.

## 🛠️ Interface (v4.0-S)

### Input Schema (SkillInput.params)

- `action` (enum): `generate_master`, `generate_lite`, `update`, `validate`.
- `project_name` (string, mandatory): Project name or Task ID.
- `problem_description` (string, mandatory): Core goal or task objective.
- `pattern` (enum): `A` (Simple), `B` (New Product), `C` (AI-Native).
- `target_project` (string, mandatory): Absolute path to the project root.

### Output Schema (SkillOutput.result)

- `prp_content`: (string) The full 12-section PRP document.
- `prp_path`: (string) Path to the generated `PRP_CONTRACT.json` or `PRP.md`.
- `solidity_score`: (float) Confidence metric (0.0-1.0) based on section completeness.
- `open_questions`: (array) List of missing or vague requirements.
- `industrial_status`: (string) "SOLIDIFIED - PRP CONTRACT SIGNED".

### ⚖️ SI Mandate (International System)

Any success metrics or technical constraints (latency < 200ms, storage > 50GB) must be strictly expressed in SI units (**seconds**, **bytes**).

## 🛡️ Industrial Constraints (Zero-Trust)

- **The 12-Section Mandate:** A PRP is not valid if any of the 12 industrial sections are empty.
- **Measurable Metrics:** Success criteria MUST include a North Star metric with a specific numerical target (e.g., "Reduction > 40%").
- **Boundary Lock:** The PRP must explicitly define "Out of Scope" to prevent agentic overreach.
- **Physical Sync:** The generated PRP must be saved as a physical JSON artifact (`PRP_CONTRACT.json`) in the project root.

## 🧠 Workflow (v4.0-S)

1. **Information Gathering:** Analyze the problem statement and success criteria.
2. **Decomposition:** Fill the 12 sections: Overview, Problem, Success, Stories, Functional, Non-Functional, Constraints, Data, UI/UX, Risks, Scope, and Questions.
3. **Pattern Selection:** Classify the project complexity (A, B, or C).
4. **Validation:** Check for "vague" requirements or missing technical constraints.
5. **Solidification:** Generate the physical contract and update the `PROJECT_STATE.json` to reflect `Phase: M1`.

---
**ORIGIN:** [PRP Generator by daffy0208](https://skills.sh/daffy0208/ai-dev-standards/prp-generator)
*Skill v4.0-S | Status: Standardized & Industrialized (Dasafo Edition).*
