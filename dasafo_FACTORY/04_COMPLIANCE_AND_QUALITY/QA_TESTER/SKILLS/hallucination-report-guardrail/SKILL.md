# Skill: Hallucination Report Guardrail
> **Source:** https://skills.sh/davila7/claude-code-templates/nemo-guardrails (Adapted)
> **Agent:** QA_TESTER

## Objective
Perform fact-checking on the QA reports themselves to ensure no false positives or hallucinated bugs reach the developers.

## Protocol
1.  **Evidence Checklist:** Every bug identified MUST have:
    - A specific file path and line number.
    - A clear console/terminal log snippet.
    - An expected vs actual value comparison.
2.  **Veracity Filter:** If a bug report lack evidence, the QA must re-run the test or flag it as an "Unconfirmed Observation".
3.  **Tone Guardrail:** Enforce the **Meticulous & Strict** voice in all reports.

## Goal
ZERO false positives. Developers must trust the QA report as absolute truth.
