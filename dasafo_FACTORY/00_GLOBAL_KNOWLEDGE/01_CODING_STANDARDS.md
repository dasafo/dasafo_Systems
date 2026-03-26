# 💎 01_CODING_STANDARDS
## 💻 01. Coding Standards
>
> **Standard:** v3.1.5 "Solidity Guard"

## 1. Principles
- **Atomic Vibe**: UI components must be stunning, responsive, and tokenized.
- **Structural Solidity**: Strict separation of concerns (SoC). Business logic is blind to the UI.
- **Immutability**: Data is immutable by default. Pure functions are the gold standard.

## 2. Global Mandates
- **Language**: All internal code, comments, and logic strings MUST be in **English**. Human-facing overview docs in `Informacion/` may be in Spanish.
- **SI Units**: Always use International System units (meters, kilograms, seconds, kWh). No imperial units allowed.
- **Zero Hardcoding**: Never hardcode paths or secrets. Use relative paths or environment variables (`TARGET_PROJECT`).

## 3. Formatting
- **Python**: PEP8 compliant. Explicit type hinting required.
- **Markdown**: Lint-clean (MD022, MD032, MD040).
- **CSS**: Vanilla CSS preferred for flexibility. Use semantic tokens (`var(--color-danger)`).

## 4. Documentation
- Use GitHub Alerts (`> [!IMPORTANT]`) for critical implementations.
- Every function must have a clear, descriptive name (e.g., `calculate_invoice_total` vs `process`).
