---
version: 3.2.0-S
agent: FRONTEND_DEV
---

# 🌊 Skill | Framer Motion Transitions

## Objective

Deliver a "Surgical & Premium" feel through subtle, high-performance animations and transitions using Framer Motion.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `animation_type` (string, optional): "page" | "hover" | "staggered". Default "page".
- `duration_ms` (integer, optional): Maximum 300ms. Default 200.

### Output Schema (SkillOutput.result)

- `code_snippet`: (string) React code snippet using Framer Motion.
- `vibe_check`: (string) "PREMIUM".

### ⚖️ Mandato SI (Sistema Internacional)

Los tiempos de duración de las animaciones deben reportarse estrictamente en segundos o milisegundos (unidades SI).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Duration Limit:** Enforces a maximum physical duration of `300ms` for system transitions to avoid "sluggish" vibes.
- **Deterministic Snippets:** Code generated is physically contextualized with the `v3.2.0-S` standard header.

## Key Micro-interactions

- **Transitions:** Smooth exit/enter via `AnimatePresence`.
- **States:** Subtle scaling (1.02x) and shadow elevation for interactivity.
- **Reveal:** Staggered revealing for list/data elements.
- **Blur:** Backdrop-blur for premium floating assets (Glassmorphism).

## Constraint

Animations MUST NOT exceed 300ms. Speed is a primary aesthetic dimension.

---
*Skill v3.2.0-S | Status: Standardized.*
