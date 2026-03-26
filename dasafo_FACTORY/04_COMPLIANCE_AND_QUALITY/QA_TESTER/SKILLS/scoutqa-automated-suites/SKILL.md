# 🕵️‍♂️ Skill | ScoutQA Automated Suite Generation
> **Version:** v3.1.5 "Solidity Guard"
> **Source:** https://skills.sh/karpathy/nanochat/scoutqa (Adapted)
> **Agent:** QA_TESTER

## Objective
Automatically generate comprehensive test suites (Unit/Integration) by analyzing source code structure and implicit edge cases.

## Core Process
1.  **Code Discovery:** Use `grep` or `list_dir` to find new modifications in production agents.
2.  **Suite Generation:** Create `test_*.py` or `*.test.ts` files ensuring coverage for:
    - Happy Path (Expected behavior).
    - Unhappy Path (Error states, exceptions).
    - Edge Cases (Null inputs, overflow).
3.  **Execution:** Run the suite using `pytest` or `npm test` and produce a `TEST_REPORT.json` for the ORCHESTRATOR.

## Standards
Rejects any suite with less than 80% code coverage.
