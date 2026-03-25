# Skill: Requirements Validation Audit
> **Source:** https://skills.sh/jwynia/agent-skills/requirements-analysis (Adapted)
> **Agent:** QA_TESTER

## Objective
Act as the "Devil's Advocate" to ensure that the implementation matches the PRODUCT_OWNER's RA level requirements.

## Audit Workflow
1.  **Traceability:** Map each test case to a specific goal in `PROJECT_STATE.json`.
2.  **Compliance Check:**
    - Is the feature solving the intended problem?
    - Are the SI units consistent across the entire flow?
    - Does it follow the 'dasafo_FACTORY' ethical and scientific guidelines?
3.  **V-Model Pass:** If a requirement is at RA5 (Validated), the QA MUST provide 100% test coverage for its acceptance criteria before marking the task as DONE.

## Output
Reports documented in `$TARGET_PROJECT/LOGS/QA_AUDIT_{DATE}.md`.
