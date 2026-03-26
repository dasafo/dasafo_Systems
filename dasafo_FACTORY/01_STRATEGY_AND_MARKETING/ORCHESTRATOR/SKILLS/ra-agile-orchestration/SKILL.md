# Skill: RA# 🏃 RA Agile Orchestration
>
> **Standard:** v3.1.5 "Solidity Guard"
ORCHESTRATOR

## Objective
Dynamically route and prioritize tasks based on their Requirement Analysis (RA) level (RA0-RA5).

## Orchestration Logic
- **RA-0 to RA-2 (Ideación):** Assign to `RESEARCH_AGENT` and `ARCHITECT` for discovery and feasibility studies.
- **RA-3 (Execution):** Dispatch to `03_PRODUCTION` (BE, FE, DS, DB) for primary implementation.
- **RA-4 (Testing/Security):** Move task to `04_COMPLIANCE_AND_QUALITY` (QA, SECURITY) for rigorous certification.
- **RA-5 (Validated):** Mark task for `DEVOPS_SRE` deployment and `MEMORY_OPTIMIZER` archival.

## Parallelization
Allow up to 3 parallel RA-3 streams if the `ARCHITECT` has approved the decoupled design.
