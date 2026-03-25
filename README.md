# dasafo_Systems | Multi-Agent AI Factory v3.1

<p align="center">
  <img src="https://img.shields.io/badge/Architecture-Stateless_Agents-0ea5e9?style=for-the-badge" alt="Architecture Badge">
  <img src="https://img.shields.io/badge/Standards-SI_Units-emerald?style=for-the-badge" alt="Standards Badge">
  <img src="https://img.shields.io/badge/Design-Atomic_Vibe-purple?style=for-the-badge" alt="Design Badge">
  <img src="https://img.shields.io/badge/Security-Zero_Trust-red?style=for-the-badge" alt="Security Badge">
</p>

## 🚀 Overview

**dasafo_Systems** is a high-performance, stateless AI Multi-Agent Factory designed for mass-scaling software projects with surgical precision. This version (**v3.1 "Infraestructura Blindada"**) introduces a centralized services node, industrial-scale resource quotas, and enhanced observability.

Built on the pillars of **Rigor**, **Solidity**, and **Vibe**, the factory allows for parallelized execution by multiple agents while enforcing strict isolation, mandatory **PRP Contract** validation, and **AutoShield v3.1** error prevention.

---

## 🏛️ System Architecture

The ecosystem is strictly divided into two immiscible hemispheres:

### 1. The Infrastructure Node (`INFRA/`) [NEW]
The centralized "Vivero" of shared services.
- **Neo4j**: Central Knowledge Graph for all projects.
- **Postgres**: Relational operational storage.
- **Glances**: Health and performance monitoring.

### 2. The Factory Engine (`dasafo_FACTORY/`)
The immutable "Brain" of the agency. It contains the identities, skills, and protocols that govern every agent.
- **`00_GLOBAL_KNOWLEDGE`**: The Factory OS. Universal laws, coding standards, and the `skill_schema`.
- **`01_STRATEGY` to `05_OPERATIONS`**: Departmental silos containing specialized agents (e.g., `ORCHESTRATOR`, `ARCHITECT`, `BACKEND_DEV`).
- **`GLOBAL_SOUL.md`**: Centralized ethics and operational values.
- **`COMMUNICATION_PROTOCOL.md`**: The laws of physics for agent interaction and task passing.

### 3. Information & Documentation (`Informacion/`)
High-level summaries and guides for human-agent onboarding, maintained in **Spanish** for accessibility.

---

## ⚡ Executive Power Skills (v2.1)

The factory is not just a set of rules; it is an **Executive Engine** capable of autonomous output:

- **Strategy Engine**: Automatic PRP Contract generation & Intent-to-DAG conversion.
- **Architectural Tools**: Automated ADR generation & deep-semantic tech research.
- **Production Masters**: API Boilerplate generators & Atomic Design System engines.
- **Compliance Gates**: Internal secret scanning & recursive PRP audit validation.
- **Operations Stability**: AutoShield v3.1 self-healing & centralized infra monitoring.

---

## ⚙️ The Universal Pipeline (v2.1)

Every project sequentially clears these phases:

1. **Phase 0 (Discovery & PRP):** Establishing the mission. No agent proceeds until the user signs the `PRP_CONTRACT.json` (Vision-What, not How).
2. **Phase 1 (Architecture & Research):** Deep semantic research (ADRs, schemas). No code is written until the "Master Plan" is approved.
3. **Phase 2 (Isolated Execution):** Production agents write code strictly inside `$TARGET_PROJECT/WORKSPACE/`.
4. **Phase 3 (QA & Security Gate):** Mandatory Playwright tests and secret scanning. Errors are logged to **AutoShield v3.1** (YAML) for collective learning.
5. **Phase 4 (Go-Live):** `DEVOPS_SRE` orchestrates the deployment via Docker and monitors health via Glances.

---

## 💎 Core Values (v2.1)

- **Zero-Trust Security:** Secret scanning and prompt-injection guards are mandatory.
- **Atomic Design:** UI must be premium (Dark mode, neon accents, glassmorphism).
- **English-only Mandate:** All internal code, logic, and technical documentation are in English.
- **Shared Infrastructure:** Maximize efficiency by reusing the `INFRA` node while enforcing container isolation.
- **Recursive Evolution:** `FACTORY_EVOLVER` continuously optimizes the system based on AutoShield feedback.

---

## 🛠️ Getting Started

### 1. Launch Infrastructure
```bash
cd dasafo_Systems/INFRA
docker-compose up -d
```

### 2. Initialize Project
```bash
cd dasafo_FACTORY
./init_project.sh ProjectName
```

### 3. Inject Context
```bash
export TARGET_PROJECT="/absolute/path/to/ProjectName"
```

### 4. Kick-Off
Invoke the Orchestrator via the `/factory-orchestrate` command to start the Discovery phase.

---

<p align="center">
  <i>"Move fast in a way that future agents can understand, extend, and trust."</i>
</p>
