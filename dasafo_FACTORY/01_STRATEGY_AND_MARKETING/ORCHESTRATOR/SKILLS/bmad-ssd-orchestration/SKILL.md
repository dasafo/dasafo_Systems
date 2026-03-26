# Skill:# 📐 BMAD SSD Orchestration
>
> **Standard:** v3.1.5 "Solidity Guard"
https://skills.sh/supercent-io/skills-template/bmad-orchestrator
> **Agent:** ORCHESTRATOR

## Objective
Implement Structured System Design (SSD) to manage complex multi-agent workflows with automated phase gates.

## State Management
- **Source of Truth:** `$TARGET_PROJECT/PROJECT_STATE.json`.
- **Logic:** Follow the TEA (Task-Execute-Audit) loop for every task.

## Phase Gate Protocol
Before advancing to the next project phase (e.g., Analysis -> Planning):
1.  **Run `/ssd-validate`:** Scan all tasks in the current phase.
2.  **Verify Verdicts:** Ensure all critical tasks have `qa_passed: true` (Security/QA signature).
3.  **Check Coverage:** All specified requirements in `LOCAL_KNOWLEDGE/ARCHITECTURE.md` must have a corresponding archived task.
4.  **Advance:** Only if (1), (2), and (3) are PASS, increment `current_phase` in `PROJECT_STATE.json`.

## Error Recovery
If a phase-gate fails, identify the specific "orphan" tasks and prioritize them in the next execution cycle.
