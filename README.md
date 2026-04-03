# 🏛️ dasafo_Systems | Multi-Agent AI Software Factory (v5.0-MCP)

[![Status](https://img.shields.io/badge/Status-Industrial_Ready-emerald?style=for-the-badge)](#)
[![Version](https://img.shields.io/badge/Standard-v4.0--MCP_Native_Core-gold?style=for-the-badge)](#)
[![Governance](https://img.shields.io/badge/Governance-Aduana_Universal_MCP-purple?style=for-the-badge)](#)
[![Security](https://img.shields.io/badge/Security-Zero_Trust_Solidity-red?style=for-the-badge)](#)

**dasafo_Systems** is an autonomous engineering ecosystem designed to transform software creation into an industrial, predictable, and highly profitable process. It is not just an AI chat; it is a **mass production infrastructure** governed by 16 specialized agents, physical phase gates, zero-trust protocols, and a native Model Context Protocol (MCP) bridge.

---

## 🚀 Key Innovations in v5.0-MCP

- **🔌 Native MCP Bridge:** Zero terminal access. Agents communicate with the factory engine exclusively via a secure `FastMCP` server, eliminating arbitrary code execution and enforcing strict operational guardrails.
- **🧠 Predictive Memory (Neo4j):** The factory learns from its mistakes. The `QA_TESTER` logs cultural violations, which are synthesized into *Golden Rules* in the Neo4j Knowledge Graph. The Orchestrator injects these rules into future tasks to prevent hallucination loops.
- **⚕️ Industrial Immune System (Auto-Heal):** If a deployment fails due to a port conflict or memory OOM, the system triggers an `EMERGENCY_SPEC`. The `FACTORY_EVOLVER` wakes up, patches the infrastructure autonomously, and redeploys.
- **📈 Financial ROI Engine:** Code is useless if it's not profitable. The `PRODUCT_OWNER` uses the `startup-metrics-framework` to mandate Target CAC, LTV, and Execution Costs before any developer writes a single line of code.

---

## 🏗️ Industrial Ecosystem: The 3 Nodes

The system operates under a tripartite architecture that ensures total isolation and data persistence:

```mermaid
graph TD
    User((Director Ops)) --> Antigravity["🪐 Antigravity IDE (MCP Client)"]
    Antigravity --> Server["🛂 factory_mcp_server.py (Aduana Universal)"]
    Server --> Factory["🧠 dasafo_FACTORY / Core Engine"]
    Factory --> Hub["📡 Top 18 Skill Hub"]
    Server --> Projects["📦 PROJECTS / Workshop"]
    Projects <--> Infra["⚡ INFRA / Power Grid"]

    subgraph Solidity_Guard_v5.0-MCP
        PRP["12-Section Contract"]
        Neo4j["Knowledge Graph (LTP)"]
        Clean["Clean Session Isolation"]
    end
````

### 1\. `dasafo_FACTORY` (The Brain)

The immutable node containing the laws, identities, and executive skills.

- **MCP Server:** `factory_mcp_server.py` acts as the definitive gateway.
- **Top 18 Hub:** Library of 30+ atomic skills (`06_SKILL_LIBRARY`).
- **Agents:** 16 industrial profiles across 5 departments (Strategy, Architecture, Production, Compliance, and Operations).

### 2\. `INFRA` (The Power Grid)

Shared backend services managed via Docker Compose:

- **Relational:** Postgres (`shared-db`) for operational metadata.
- **Semantic:** Neo4j (`kg-db`) for Long-Term Persistence (LTP) and Golden Rules.
- **Cache:** Redis (`cache-node`) for real-time orchestration.
- **Health:** Glances for system resource monitoring.

### 3\. `PROJECTS` (The Workshop)

The space where missions are executed. Each project operates under **Disk-as-Source-of-Truth (DAST)** constraints:

- `DOCS/`: Technical blueprints and human-in-the-loop (HITL) approval records.
- `TASKS/`: Physical record of the industrial Kanban (`registry.json`).
- `WORKSPACE/`: Distributed source code (Frontend/Backend/Shared).
- `LOGS/`: Technical evidence and telemetry for each session.

-----

## ⚙️ The Industrial Engine (DAST Protocol)

Our engine is distinguished by the use of **Disk-as-Source-of-Truth (DAST)** and **Physical State Gates**:

- **Aduana Universal:** Integrated into the MCP server. No skill can be invoked if the project is not in the correct phase or if human physical signatures (`APPROVAL_MX.md`) are missing.
- **Double-Gating:** Agents can execute tasks completely autonomously *if and only if* they detect their assigned `SPEC_LITE.json` physically present on the disk.
- **SI Mandate:** 100% mandatory. Time in **seconds (s)**, resources in **bytes (B)**. No exceptions.

-----

## 🕹️ Command Center (The 14 MCP SOPs)

Interact with the factory using high-level Standard Operating Procedures (SOPs) via your MCP client. You manage the factory; the factory manages the code:

| SOP | Phase | Industrial Action |
| :--- | :--- | :--- |
| **`init-contract`** | M1 | Generates the 12-section master contract with CAC/LTV Projections. |
| **`factory-orchestrate`** | M1-M5 | Deconstructs contracts into Kanban tasks and synchronizes state. |
| **`validate-backbone`** | M2-M3 | Physically verifies framework scaffolding before delegating logic. |
| **`execute-task`** | M3 | Launches an isolated Clean Session with predictive Neo4j Guardrails. |
| **`scan` & `audit`** | M4 | Zero-Trust security scan and Cultural Linter validation. |
| **`provision` & `deploy`**| M5 | Atomic Infrastructure-as-Code provisioning and deployment. |
| **`auto-heal`** | M5 | Triggers the autonomous patching loop for broken deployments. |
| **`sync-memory`** | LTP | Consolidates feedback logs into Neo4j Engrams for future projects. |
| **`kanban-board`** | All | Serves the real-time physical Vibe Kanban on port 3001. |

-----

## 🚀 Quick Start Guide: From Director to Owner

1. **Power Up the Grid:**

    ```bash
    cd INFRA && docker-compose up -d
    ```

2. **Initialize a Mission:**

    ```bash
    cd dasafo_FACTORY && ./init_project.sh ProjectName
    ```

3. **Connect the MCP Engine:**
    Ensure your AI IDE (Antigravity/Claude) is configured to use `factory_mcp_server.py`.

4. **Define the Vision:**

      - Ask the `PRODUCT_OWNER` to execute the `init-contract` SOP.
      - Physically sign the phase transition by updating `DOCS/USER/APPROVAL_M1.md` to `Status: APPROVED`.

5. **Execute & Evolve:**

      - Command the Orchestrator to run `factory-orchestrate` to populate the Kanban.
      - Trigger `validate-backbone` and `execute-task` to watch the factory build your SaaS autonomously.
      - Use `sync-memory` when finished to make the factory smarter for your next project.

-----

<p align="center">
<i>"Industrializing the Future of Autonomous Software Engineering"</i><br>
<b>dasafo_Systems v5.0-MCP | Solidity, Speed, Veracity.</b>
</p>
