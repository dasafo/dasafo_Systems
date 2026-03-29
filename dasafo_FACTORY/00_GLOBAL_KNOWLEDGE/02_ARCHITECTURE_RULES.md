# 🏗️ 02_ARCHITECTURE_RULES
>
> **Standard:** v3.3.1-S "Industrial Core"

## 1. The "Chasis Blindado" Architecture

The Factory is divided into two strict zones:

- **`dasafo_FACTORY/`**: The IMMUTABLE brain. Contains logic, skills, and global knowledge.
- **`PROJECTS/`**: The MUTABLE workspace. Where specific implementations live.

## 2. Boundary Enforcement

- **Domain**: Depends on nothing. Core business rules.
- **Application**: Orchestrates use cases.
- **Infrastructure**: Implements interfaces (DBs, APIs, Storage).
- **UI**: Purely visual. Communicates only with the Application layer via DTOs.

## 3. The PRP Generator & Gate (12-Section Mandate)

> [!IMPORTANT]
> No production task can start without a signed `PRP_CONTRACT.json` generated using the industrial 12-section mandate. This contract defines the "What" before the agents decide the "How".

## 4. Multi-Agent Orchestration

- Use DAG (Directed Acyclic Graph) for task decomposition.
- All inter-agent communication follows the industrialized Top 18 Hub mapping.
- Agents must never share mutable state; they pass serialized DTOs through the aduana.

## 5. Industrial-Scale Infrastructure

- **Central Node (`INFRA`)**: Heavy services (Supabase, Postgres, Redis, Neo4j) must be hosted on the shared `INFRA` node to optimize resource consumption.
- **Resource Quotas**: Every project must enforce RAM/CPU limits via `docker-compose` to prevent noise.

## 6. Architecture Solidity (Zero-Trust)

> [!CAUTION]
> **NO REPORT WITHOUT DISK IO & TASK SYNCHRONIZATION.**
> Task progression must move JSON files from `TASKS/01_PENDING` to `TASKS/03_COMPLETED` via `kanban-solidity-gate`.

- **Artifacts Required:** ADRs, API Contracts, and UI Blueprints in the project's `DOCS/ARCH/` or `LOCAL_KNOWLEDGE/architecture/` directory.
- **Verification Rule (Zero-Trust):** The Orchestrator will REJECT any Phase Promotion if these physical proofs are not present on disk.
- **HITL Signature:** No movement to Phase M3 (Production) is allowed without a manual signature of the `PRP_CONTRACT.json`.

---
*Architecture Rules v3.3.1-S | dasafo_FACTORY.*
