---
name: dasafo-orchestrator
description: The master execution engine using LangGraph State Machine to enforce the PEV (Plan-Execute-Verify) control loop.
version: v5.1-MCP
role: Hub Manager & Strategic Director
nodes:
  - ARCHITECT_PLANNER
  - FEATURE_AUTHOR
  - ADVERSARIAL_REVIEWER
  - SECURITY_RED_TEAM
---

# 🏛️ ORCHESTRATOR | The PEV Executor

> [ ⬆️ Up: [[../MOC_STRATEGY]] | 📂 Index: [[MOC_ORCHESTRATOR]] ]

This directory houses the unified **LangGraph State Machine** that powers the Factory's Orchestrator. We have strictly moved from monolithic, rigid prompt instructions to a programmatic, persistent, agentic graph based on the **Plan-Execute-Verify (PEV)** methodology.

## 🧠 The PEV State Machine Nodes

The Orchestrator defines execution workflows by navigating through four autonomous, specialized roles:

1. **ARCHITECT (The Planner Node):** 
   Reads project specifications (`PRP_MASTER.json`), retrieves LTP insights from the Graph database, and calculates the DAG topological plan. Generates the `Execution Plan` and expected `Required Context`.
2. **AUTHOR (The Feature Author Node):** 
   Receives the execution plan. Uses the 15 Outcome-Driven MCP macro-skills to generate features, invoke endpoints, format infrastructure, and mutate disk states. Outputs structured `Artifacts`.
3. **REVIEWER (Adversarial Node):** 
   Tests the generated artifact logically to ensure no principles of industrial standard (DAST, Null-state visual resilience, atomic transitions) have been broken.
   *If Failure criteria met*, routes back to the **Author** Node via edge loop.
4. **RED_TEAM (Security Node):** 
   Reviews output for raw Zero-Trust violations, hardcoded credentials, and infrastructure boundaries (RLS enabled, isolation mode respected).
   *If Failure criteria met*, overrides the architecture completely, routing back to the **Architect** Node.

## ⚙️ The Parallel Execution Loop (DAG Integration)

When mapping tasks, the Orchestrator leverages its tools natively through Python:
* Generates emergencies (`FACTORY_EVOLVER` preemptive overrides).
* Injects Neo4j rules natively before the graph starts.
* Checkpoints the entire PEV progression in SQLite/Disk so that inter-agent crash looping does not result in total amnesia.

## 🧰 Authorized Macro-Skills (Node Accessible)
- `project-contract-outcome`
- `project-management-outcome`
- `iac-provisioning-outcome`
- `ephemeral-code-execution`
- `base-knowledge-extraction` (LTP)
- `backbone-validation-outcome`
- `delegate-clean-session` (For specific multi-agent branching)

---
*Orchestrator v5.1-MCP | Status: LangGraph Stateful Hub Manager.*
