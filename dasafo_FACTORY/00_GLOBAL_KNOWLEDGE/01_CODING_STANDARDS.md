# 💎 01_CODING_STANDARDS

## 💻 01. Coding Standards
>
> **Standard:** v3.3.1-S "Industrial Core"

## 1. Principles

- **Atomic Vibe**: UI components must be stunning, responsive, and tokenized. Respect semantic tokens strictly.
- **Structural Solidity**: Strict separation of concerns (SoC). Business logic is blind to the UI; UI is a dumb renderer.
- **Immutability**: Treat data as immutable by default. Prefer pure functions and explicit state transitions.

## 2. Global Mandates

- **Language**: All internal code, comments, and logic strings MUST be in **English**. Documentation in `DOCS/` or `Informacion/` may be in Spanish if requested by the USER.
- **SI Units**: Always use International System units (meters, kilograms, seconds, kWh). No imperial units allowed.
- **Zero Hardcoding**: Never hardcode paths or secrets. Use relative paths or environment variables.
- **Early Return Pattern**: Avoid deep nesting. Prefer flat, predictable logic.

## 3. Formatting

- **Python**: PEP8 compliant. Explicit type hinting required.
- **Markdown**: Lint-clean (MD022, MD032, MD040). Headings must have proper blank lines.
- **CSS**: Vanilla CSS for maximum flexibility. Use semantic tokens (`Colors.danger`, `Spacing.large`).

## 4. Documentation

- Use GitHub Alerts (`> [!IMPORTANT]`) for critical implementations.
- Every function must have a clear, descriptive name reflecting its specific responsibility (SRP).

---
*Coding Standards v3.3.1-S | dasafo_FACTORY.*
