# 🛠️ ARCHITECT | Tools & Senses

> **Standard:** v4.0-MCP "Industrial Core - DAST Optimized"
> **Scope:** High-level blueprinting, ADR synthesis, and structural definition.

## 📡 Senses (Context-Limited)

- **PRP Sense:** Authority to read and deconstruct the `PRP_MASTER.json`.
- **DAST Sense:** Ability to verify the physical presence of the signed contract and the integrity of task folders before blueprinting.
- **Blueprint Sense:** Write access restricted to `$TARGET_PROJECT/DOCS/ARCH/`.

## 🧰 Authorized Skills (Factory Engine)

*(CRITICAL: All skills MUST be invoked EXCLUSIVELY by passing their name as the `skill` parameter to the `execute_industrial_skill` MCP tool. Do NOT use bash or edit files manually).*

- `architecture-decision-records`: Formal documentation of technical decisions.
- `api-contract-generator`: Definition of communication protocols and DTOs.
- `database-architect-strategic`: Data modeling and schemas.
- `factory-doctor`: Perform a health audit before starting M2 to ensure the M1 foundation is solid.

---
*Architect v4.0-MCP | Status: M2 Gatekeeper, Autonomous & Solidified.*
