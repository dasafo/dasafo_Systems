# 📜 Dasafo Factory | Core Constitution

> [ ⬆️ Up: [[MOC_GLOBAL]] | 📂 Index: [[MOC_GLOBAL]] ]

> **Standard:** v5.0-MCP "Native Industrial Core"
> **Governance:** Zero-Trust / Spec Driven Development / Clean Sessions.

## 🏗️ I. The Law of the Spec (SDD)

1. **Spec Over Everything:** No work is initiated without a physical `PRP_MASTER.json` (Phase M1) or `SPEC_LITE.json` (Execution).
2. **Phase Isolation:** Transition between M1-M5 is physically gated by artifact presence in the file system.
3. **Outcome Mandate:** Every task must end with a 3-point "Zero Fluff" Outcome Report detailing `status`, `artifacts`, and `summary`.
4. **Human-Gate Sovereignty:** No phase transition (M1 to M5) is valid or authorized without the presence of a human-signed approval artifact in the `DOCS/USER/APPROVAL_MX.md` path. Failure to comply with this is considered a critical Cultural Violation.

## 🧠 II. Context Isolation (Clean Sessions)

1. **Memory Sovereignty:** Implementation agents operate under `CLEAN_SESSION=True`. They only read the `context_pointers` authorized by the Orchestrator.
2. **No-Noise Policy:** The global `FEEDBACK-LOG` is a technical substrate, not a conversation history. It must be pruned by the `MEMORY_OPTIMIZER`.
3. **Artifact-First:** Agents communicate via changes in the file system, not through long conversational threads.

## 🛡️ III. Zero-Trust & Solidity

1. **The MCP Mandate:** The use of terminal commands (bash/sh) or direct python execution is strictly forbidden for factory operations. Agents MUST invoke their authorized MCP tools **directly by name** (e.g., `prp-generator`, `delegate-clean-session`, `kanban-solidity-gate`). The tools are natively registered in the `dasafo_FACTORY_Core_v5.0` FastMCP server.
2. **Surgical Access:** Generic filesystem MCP tools (`write_file`, `edit_file`) are restricted strictly to the agent's assigned `WORKSPACE/[domain]/` directory.
3. **Solidity Gate:** No phase is considered complete without a verified `kanban-solidity-gate` check via MCP and a `SECURITY_AUDITOR` clearance.
4. **Chesterton's Fence:** No legacy code is deleted without an ADR explaining the "Why".
5. **Backbone Mandate:** No atomic implementation agent shall be dispatched without prior physical validation of the scaffolding via `project-backbone-validator`.
6. **Guardian Angel Mandate:** All human engineers MUST operate with the local DAST Pre-Commit Hook active (`.githooks/guardian.py`). Bypassing local security checks to force a commit is a critical Cultural Violation.

## 📊 IV. Industrial Metrics (SI Standards)

1. **Temporal Precision:** All time-based metrics must be expressed in Seconds (s).
2. **Resource Precision:** All size-based metrics must be expressed in Bytes (B).

## 🏗️ V. Hybrid Infrastructure Mandate (LTP)

1. **Long-Term Persistence (LTP):** Every agentic learning, critical failure, or architectural decision MUST be recorded in the shared Knowledge Graph (`kg-db` / Neo4j).
2. **Execution Isolation:** Source files and temporary artifacts belong to the local `target_project`. Execution is ephemeral, knowledge is permanent.
3. **Service Discovery:** Skills must first look for the hostname `dasafo-shared-db` for relational operations and `dasafo-shared-kg` for semantics.
4. **INFRA Metrics:** Monitoring (via Glances/Core) must report latencies in seconds (s) and resource consumption in bytes (B).

## 🧬 VI. The 19-Skill Production Taxonomy (Appendix)

To eradicate "Vibe Coding" and align with Senior Engineering workflows, all MCP skills and delegated tasks MUST fall into one of the following strict execution states:

* **DEFINE:** Strategy, metric baseline, and contract formulation.
* **PLAN:** Architectural blueprints, database schemas, and DAG mapping.
* **BUILD:** Atomic implementation of logic, UI, and design tokens.
* **VERIFY:** Test-Driven validations, E2E tracing, and Guardrail checks.
* **REVIEW:** Security audits, context pruning, and forensic healing.
* **SHIP:** Infrastructure provisioning, deployment, and live-telemetry.

Any task that attempts to "BUILD" and "SHIP" in the same atomic `SPEC_LITE.json` violates the separation of concerns and must be rejected by the Orchestrator.

## 🕸️ VII. Knowledge Connectivity & Navigation (The Weave)

1. **Anti-Orphan Mandate:** No `.md` file shall exist without functional connectivity. Every note must be integrated into the project's semantic graph.
2. **Navigation Header:** All documentation files MUST start with a standardized navigation header:
   ```markdown
   [ ⬆️ Up: [[Parent_MOC]] | 🔙 Back: [[Previous_Context]] | 📂 Index: [[MOC_GLOBAL]] ]
   ```
3. **Wiki-Link Injection:** When generating documentation or reports, Agents MUST use `[[filename]]` for every internal reference to other project artifacts.
4. **MOC Protocol:** Every directory MUST contain a `_MOC.md` or `_INDEX.md` file that lists and links all sub-artifacts in that domain.
5. **Semantic Anchors:** End every major documentation file with a `### 🧬 Related Engrams` section containing at least 3 relevant `[[ ]]` links to sibling notes.

---

*Ratified: 2026-04-13 | Dasafo Factory v5.0.3-MCP (Connectivity Patch).*
