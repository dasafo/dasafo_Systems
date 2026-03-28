# ⚙️ 01_THE_ENGINE | The Motor Executive

> **Standard:** v3.2.0-S "Modular Toolbox"
> **Focus:** Operations, Pipeline & Phase-Gate Protocol (Aduana Universal)

---

## 🛣️ 1. Universal Pipeline (M1-M5 Maturity)

The 5-phase journey mandated for every industrial project.

### 🔍 M1: Discovery

- **Owner:** `PRODUCT_OWNER`
- **Output:** `PRP_CONTRACT.json` (Status: `signed`).
- **Signature Gate:** `PROJECT_STATE.json -> "M1": "APPROVED"`.

### 📐 M2: Architecture

- **Owner:** `ARCHITECT`
- **Output:** Blueprint artifacts + `TASKS/registry.json`.
- **Signature Gate:** `PROJECT_STATE.json -> "M2": "APPROVED"`.

### ⚙️ M3: Production

- **Owner:** `BACKEND_DEV` / `FRONTEND_DEV`
- **Output:** Functional code (100% SoC) + Verified Tests.
- **Signature Gate:** `PROJECT_STATE.json -> "M3": "APPROVED"`.

### 🧪 M4: Compliance

- **Owner:** `QA_TESTER` / `DOCS_MASTER`
- **Output:** Security Audit + Audit Signatures.
- **Signature Gate:** `PROJECT_STATE.json -> "M4": "APPROVED"`.

### 🔄 M5: Operations

- **Owner:** `DEVOPS_SRE` / `FACTORY_EVOLVER`
- **Output:** Deployment + Global Semantic Index.
- **Signature Gate:** `PROJECT_STATE.json -> "M5": "APPROVED"`.

---

## 🛡️ 2. Phase-Gate Protocol (Aduana Universal)

### 🚫 Anti-Chat Rule (No-Trust Policy)

**El chat es para coordinar; el sistema de archivos es para autorizar.**

Cualquier "OK" o aprobación en el historial de chat es **percibido** pero **no vinculante**. Los agentes tienen prohibido promocionar de fase sin una verificación física del metal.

### 🛂 El Flujo de Aduana (Step-by-Step)

1. **Cierre Técnico:** El agente de fase completa todas sus tareas en `TASKS/registry.json`.
2. **Petición de Firma:** El agente solicita formalmente al Humano la revisión de los artefactos generados.
3. **Firma Física (Humano):** El usuario debe abrir físicamente **`PROJECT_STATE.json`** y cambiar el estado de la fase actual de `"PENDING"` a `"APPROVED"`.
4. **Validación Sensorial (Agente):** El agente orquestador utiliza su sentido `filesystem` para leer el archivo. Solo si detecta físicamente `"APPROVED"`, se habilita la transición a la siguiente fase.

---

## 📡 3. MCP Senses Protocol (The Sensory Bridge)

### 🧠 The Sensory Philosophy

Agents do not "run commands"; they **perceive** and **act** through the Sensory Bridge (MCP).

### 📡 Core Senses

- **Filesystem Sense:** Read/Write/Search within `$TARGET_PROJECT`.
  - **Constraint:** Mandatory check of `PROJECT_STATE.json` before any Phase Promotion.
- **GitHub Sense:** PR creation, issue tracking, and code reviews.
  - **Constraint:** Use semantic commit messages (feat, fix, refactor).
- **NotebookLM Sense:** Deep research and source synthesis (Phases M1/M2).
- **Custom Skills (`run.py`):** Executable logic tailored for specific agent roles.
  - **Constraint:** Todas las habilidades residen en **`06_SKILL_LIBRARY/`**. Los agentes las invocan modularmente. Mandatory execution of `kanban-solidity-gate` for phase transitions (Checks **TASKS/registry.json** as SSoT) and state-gate (linked to **PROJECT_STATE.json**).

---

## 🏗️ 4. Operations Manual (Synergy & Synergy)

### 🔄 Global Operational Events

- **Atomic Reflection (❤️):** Agents update their operational performance in their internal `IDENTITY.md` every major task.
- **Pre-Flight Check (🛸):** Mandatory `autoshield-preflight-check` before destructive actions.
- **Shared Infra Health:** Verify `INFRA` via Glances (Port 61208) before Phase M3.
- **Stateless Execution:** Los agentes deben ser capaces de reconstruir su intención actual leyendo `PROJECT_STATE.json`, sin depender del historial de chat previo.

---

*01_THE_ENGINE v3.2.0-S | Status: Solidified.*
