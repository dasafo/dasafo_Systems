# Skill: Architecture Decision Records (ADR)
> **Source:** https://skills.sh/wshobson/agents/architecture-decision-records
> **Agent:** ARCHITECT

## Objective
Establish a formal, immutable log of technical decisions, explaining the "Why" behind the "How" for every $TARGET_PROJECT.

## Workflow
1.  **Draft:** Create an ADR when a significant tech stack or structural choice is made.
2.  **Format:** Use the MADR format (Context, Alternatives, Decision, Consequences).
3.  **Persist:** Save in `$TARGET_PROJECT/LOCAL_KNOWLEDGE/architecture/ADR-XXX.md`.
4.  **Index:** Maintain a `README.md` index in the same folder with the current status of each ADR (Accepted, Deprecated, Proposed).

## Lifecycle States
- **Proposed:** Under review by the PO or Orchestrator.
- **Accepted:** The definitive standard for the current mission.
- **Deprecated:** Recorded history of why we moved away from a specific pattern.
