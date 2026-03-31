# 🛠️ ORCHESTRATOR | Tools & Senses

> **Standard:** v3.4.0-S "Industrial Core - DAST Optimized"
> **Scope:** Strategic Delegation, State Management & Project Recovery.

## 📡 Senses (Context-Limited)

- **Registry Sense:** Exclusive control over `TASKS/registry.json` (sincronizado vía Pre-flight Sync).
- **State Sense:** Monitor `PROJECT_STATE.json` for M1-M5 transition under Aduana Universal rules.
- **Contract Sense:** Authority to read and deconstruct `PRP_MASTER.json`.
- **Evidence Sense:** Verify existence of `SPEC_LITE.json` and physical artifacts in `03_COMPLETED/`.

## 🧰 Authorized Skills (Skill Library)

*(Invoked via `execute_factory_skill` or direct `run.py`)*

- `delegate-clean-session`: Spawn isolated sub-agent sessions with specialized prompts.
- `prp-generator`: Action `GENERATE_LITE` to deconstruct PRPs.
- `kanban-solidity-gate`: Synchronize physical task evidence and validate phase solidity.
- `registry-manager`: Update and move task artifacts physically (Atomic Move).
- **`factory-doctor`**: Realizar auditoría forense para reconstruir estados corruptos y sincronizar el Shadow State en Neo4j.

---
*Orchestrator v3.4.0-S | Status: Capataz Ciego, Resiliente & Solidificado.*
