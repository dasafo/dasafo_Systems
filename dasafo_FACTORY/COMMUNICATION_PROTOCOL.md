# 📡 dasafo_FACTORY | Communication Protocol
>
> **Standard:** Sensory Bridge v3.1 "Infraestructura Blindada"
> **Focus:** Shared Resources & Multi-Agent Industrial Orchestration

## 🧩 Communication Layers


### 1. The Sensory Bridge (MCP)

- Agents interact with the physical and digital world through **Senses** (Tools).
- Every tool call is an **Observation**. Every output is a **Perception**.


### 2. AutoShield (Collective Intelligence)

- No agent operates in isolation. All agents MUST query the `FEEDBACK-LOG.md` before execution.
- Discovered patterns must be written back to the factory's immune system.


### 3. The PRP Validation Gate

- **PO Approval:** Mandatory signature of `PRP_CONTRACT.json` before Phase M2 (Architecture).
- **Physical Kanban:** Phase transitions (`M1` to `M5`) are prohibited if the `TASKS/` directory is out of sync with the `PROJECT_STATE.json`.
- **Infrastructure Quotas:** Every project must declare resource limits in `.env` to avoid "Noisy Neighbor" effects on the shared `INFRA` node.
- **Compliance:** All communications must follow the SI unit mandate and SoC rules.


### 4. Telemetry Log

- All agent interactions must be logged in `$TARGET_PROJECT/LOGS/`.
- Format: `[TIMESTAMP] [AGENT] [SKILL] [STATUS] [CORRELATION_ID]`

---
*Communication Protocol v3.1 | Status: Solidified.*
