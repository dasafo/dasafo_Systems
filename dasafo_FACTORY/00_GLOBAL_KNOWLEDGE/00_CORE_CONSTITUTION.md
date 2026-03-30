# 🏛️ 00_CORE_CONSTITUTION
>
> **Version:** v3.4.0-S "SDD Optimized Core"
> **Scope:** The ONLY global context injected into all Factory Agents.
> **Mandate:** Read once, execute flawlessly.

## I. THE PRIME DIRECTIVES (Zero-Trust & Disk IO)

1. **Words are Wind, Disk IO is Truth:** No agent can claim task completion without physical JSON artifacts moved via `kanban-solidity-gate`. Progression through M1-M5 phases requires strict physical synchronization.
2. **The "Clean Session" Mandate:** The `ORCHESTRATOR` is blind to source code. Code generation, inspection, and debugging MUST be delegated to sub-agents executing in isolated, fresh context windows.
3. **Lazy Loading:** Agents must ONLY load the specific skills from the Top 18 Hub required for their immediate task. Loading unnecessary skills is a breach of token economy.
4. **No Code Without Spec (SDD):** Implementation agents are forbidden from writing production code without a pre-approved `PRP_CONTRACT.json` or Specification document outlining the exact contract and architecture.

## II. ARCHITECTURE: CHASIS BLINDADO

The Factory operates under a strict two-zone physical boundary:

- **`dasafo_FACTORY/` (Immutable):** Contains this constitution, skills, and logic. Modifying `06_SKILL_LIBRARY/` requires explicit Human-In-The-Loop (HITL) approval.
- **`PROJECTS/` (Mutable Workspace):** Strict 4-layer separation (Domain, Application, Infrastructure, UI). Domain models NEVER cross boundaries. Cross-layer communication mandates explicit **DTOs** and zero-trust data sanitization.

## III. UNIVERSAL STANDARDS

1. **Language:** Code logic, variables, and technical logs MUST be in **English**. Documentation in `DOCS/` may be in Spanish if requested by the USER.
2. **SI Units:** All telemetry, resource reporting, and performance metrics MUST use **Seconds (s)** and **Bytes (B)**.
3. **Zero Hardcoding:** Absolute paths and hardcoded secrets are strictly forbidden. Use environment variables and relative paths anchored to `$TARGET_PROJECT`.
4. **DOCS Protocol:** All architectural blueprints, user manuals, and specifications must strictly reside within the `DOCS/` hierarchy. Root-level documentation is an architectural breach.
5. **Containerization Strictness:** "Works on my machine" is an invalid state. All implementations must be strictly containerized and defined in a `docker-compose.yml` file. Use multi-stage builds for minimal image size.
6. **Destructive Mutation Guard (Chesterton's Fence):** Agents are strictly FORBIDDEN from deleting, refactoring, or modifying legacy code/configurations unless explicitly instructed by the current Spec and documenting the exact dependency chain affected.

## IV. ERROR HANDLING & MEMORY (Engram Protocol)

Failures are data. Do not pollute the active context window with historical errors. All project errors must be serialized using `FEEDBACK_SCHEMA.json` and delegated to the `MEMORY_OPTIMIZER` for rare-pattern indexing (Engram sorting).

---
*Constitution v3.4.0-S | dS_FACTORY: Optimized for Spec Driven Development.*
