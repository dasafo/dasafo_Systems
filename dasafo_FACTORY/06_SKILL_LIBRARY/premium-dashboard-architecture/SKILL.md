---
version: 3.2.0-S
agent: FRONTEND_DEV
---

# 🏗️ Skill | Premium Dashboard Architecture

## Objective

Design and implement high-performance administrative interfaces using "Atomic Vibe" patterns, ensuring visual excellence and resilience.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `layout_type` (string, optional): "sidebar" | "topbar" | "minimal". Default "sidebar".
- `project_path` (string, optional): Absolute path for scaffolding.

### Output Schema (SkillOutput.result)

- `scaffold_status`: (string) "CREATED".
- `components_list`: (list) List of generated UI blocks.

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica de rendimiento del dashboard (LCP, FID, CLS) debe reportarse en segundos o milisegundos (unidades SI).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Atomic Integrity:** Scaffolding MUST use the global semantic design tokens. Hardcoding hex colors or pixel values is FORBIDDEN.
- **Physical Scaffold:** Logic skeletons MUST be physically written to the repository before success.

## Core Standard

1. **Layout:** Professional SideBar + Breadcrumbs + Main Content area.
2. **Solidity:** Mandatory use of Skeleton loaders for every data component.
3. **UI Resilience:** Every component MUST handle Loading, Error, and Empty states.
4. **Glassmorphism:** Enforce backdrop-blur and semantic tokens for depth.

---
*Skill v3.2.0-S | Status: Standardized.*
