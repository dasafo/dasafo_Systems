# 🏗️ 02_ARCHITECTURE_RULES

## 1. The "Chasis Blindado" Architecture
The Factory is divided into two strict zones:
- **`dasafo_FACTORY/`**: The IMMUTABLE brain. Contains logic, skills, and global knowledge.
- **`PROJECTS/`**: The MUTABLE workspace. Where specific implementations live.

## 2. Boundary Enforcement
- **Domain**: Depends on nothing. Core business rules.
- **Application**: Orchestrates use cases.
- **Infrastructure**: Implements interfaces (DBs, APIs).
- **UI**: Purely visual. Communicates only with the Application layer.

## 3. The PRP Validation Gate
> [!IMPORTANT]
> No production task can start without a signed `PRP_CONTRACT.json` in the project root. This contract defines the "What" before the agents decide the "How".

## 4. Multi-Agent Orchestration
- Use DAG (Directed Acyclic Graph) for task decomposition.
- All inter-agent communication follows the `COMMUNICATION_PROTOCOL`.
- Agents must never share mutable state; they pass serialized DTOs.

## 5. Industrial-Scale Infrastructure (v3.1)
- **Central Node (`INFRA`)**: Heavy services (Neo4j, Postgres, Redis) must be hosted on the shared `INFRA` node to optimize RAM/Disk.
- **`dasafo_network`**: All containers must communicate via the shared `dasafo_network` for secure but unified service access.
- **Resource Quotas**: Every project must enforce RAM/CPU limits to prevent "noisy neighbor" effects on the central node.
