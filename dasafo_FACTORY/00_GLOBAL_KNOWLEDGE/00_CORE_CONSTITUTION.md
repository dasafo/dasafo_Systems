# 📜 Dasafo Factory | Core Constitution

> **Standard:** v4.0-S "SDD Optimized Core"
> **Governance:** Zero-Trust / Spec Driven Development / Clean Sessions.

## 🏗️ I. The Law of the Spec (SDD)

1. **Spec Over Everything:** No work is initiated without a physical `PRP_MASTER.json` (Phase M1) or `SPEC_LITE.json` (Execution).
2. **Phase Isolation:** Transition between M1-M5 is physically gated by artifact presence in the file system.
3. **Outcome Mandate:** Every task must end with a 3-point "Zero Fluff" Outcome Report detailing `status`, `artifacts`, and `summary`.

## 🧠 II. Context Isolation (Clean Sessions)

1. **Memory Sovereignty:** Implementation agents operate under `CLEAN_SESSION=True`. They only read the `context_pointers` authorized by the Orchestrator.
2. **No-Noise Policy:** The global `FEEDBACK-LOG` is a technical substrate, not a conversation history. It must be pruned by the `MEMORY_OPTIMIZER`.
3. **Artifact-First:** Agents communicate via changes in the file system, not through long conversational threads.

## 🛡️ III. Zero-Trust & Solidity

1. **Surgical Access:** Agents have no write permissions outside their technical domain or the project's logic layers.
2. **Solidity Gate:** No phase is considered complete without a verified `kanban-solidity-gate` check and a `SECURITY_AUDITOR` clearance.
3. **Chesterton's Fence:** No legacy code is deleted without an ADR (Architecture Decision Record) explaining the "Why".
4. **Backbone Mandate:** No atomic implementation agent (e.g., FRONTEND_DEV, BACKEND_DEV) shall be dispatched without prior physical validation of the framework's scaffolding via the `project-backbone-validator`.

## 📊 IV. Industrial Metrics (SI Standards)

1. **Temporal Precision:** All time-based metrics must be expressed in Seconds (s).
2. **Resource Precision:** All size-based metrics must be expressed in Bytes (B).

## 🏗️ V. Hybrid Infrastructure Mandate (LTP)

1. **Long-Term Persistence (LTP):** Every agentic learning, critical failure, or architectural decision MUST be recorded in the shared Knowledge Graph (`kg-db` / Neo4j).
2. **Execution Isolation:** Source files and temporary artifacts belong to the local `target_project`. Execution is ephemeral, knowledge is permanent.
3. **Service Discovery:** Skills must first look for the hostname `dasafo-shared-db` for relational operations and `dasafo-shared-kg` for semantics.
4. **INFRA Metrics:** Monitoring (via Glances/Core) must report latencies in seconds (s) and resource consumption in bytes (B).

---

*Ratified: 2026-03-30 | Dasafo Factory v4.0-S.*
