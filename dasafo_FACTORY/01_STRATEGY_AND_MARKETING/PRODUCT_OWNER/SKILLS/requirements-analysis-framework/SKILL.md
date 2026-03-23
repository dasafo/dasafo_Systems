# Skill: Requirements Analysis (Vague to Validated)
> **Source:** https://skills.sh/jwynia/agent-skills/requirements-analysis
> **Agent:** PRODUCT_OWNER

## Objective
Diagnose the current state of a request and move it from a "vague intent" to "validated requirements" before commissioning technical work.

## Diagnostic States (RA Level)
1.  **RA0: No Problem Statement.** (Action: Find the 'Why' before the 'How').
2.  **RA1: Solution-First Thinking.** (Action: Focus on the need, not the tool yet).
3.  **RA2: Vague Needs.** (Action: Use the 'Disappoint Test' - what would make you sad?).
4.  **RA3: Hidden Constraints.** (Action: Dig for time, skills, and legacy integrations).
5.  **RA4: Scope Creep Prevention.** (Action: Define what is EXPLICITLY NOT in scope).
6.  **RA5: Validated.** (Action: Proceed to $TARGET_PROJECT/TASKS/01_PENDING).

## Core Questions per Phase
- **Discovery:** Who has this problem? Why hasn't it been solved?
- **Clarification:** What's the minimum viable version?
- **Constraints:** What would kill the project?
- **Scope:** What would we cut if forced?

## Definition of Done (PO Layer)
A requirement is only "Done" when it reaches **RA5** and is documented in `LOCAL_KNOWLEDGE/PROJECT_CHARTER.md`.
