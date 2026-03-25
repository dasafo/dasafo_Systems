# 🧪 03_SCIENTIFIC_RIGOR

## 1. Zero Trust Policy
Never trust input data. Sanitize and validate at every layer boundary using `skill_schema` or Zod/Pydantic.

## 2. Experimental Method
Every major architectural change must follow:
1. **Hypothesis**: What do we want to solve?
2. **Analysis**: Comparative study of libraries/approaches.
3. **Draft**: ADR (Architectural Decision Record).
4. **Validation**: Automated tests (Pytest/Playwright).

## 3. SI Units & Precision
- Mandatory use of Kelvin for temperature (fallback Celsius), Meters for distance, and Seconds for time.
- Floating point precision must be explicitly handled in scientific calculations.

## 4. Error Logging (AutoShield)
Failures are data. Every error must be caught and distilled into the `FEEDBACK-LOG.md` to prevent systemic recurrence.
