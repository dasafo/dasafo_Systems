---
description: Activates the Product Owner to generate the 12-section PRP_MASTER contract with Financial KPIs via MCP.
---

# Workflow /init-contract

This flow forces the **PRODUCT_OWNER** to define the absolute truth and financial viability of the project before any code is written.

1. **Agent:** `PRODUCT_OWNER`
2. **Execution Protocol:** SOP via MCP

3. **Financial Baseline:** Invoca la herramienta MCP **directamente por nombre** con la skill `startup-metrics-framework` (params: business_model, target_audience) para establecer Target CAC, LTV y SI constraints. Analiza la respuesta.

4. **Run PRP Generator:** Con los datos anteriores, invoca las herramientas MCP **directamente por nombre** (ej. `prp-generator`, `delegate-clean-session`) con:
   * `agent`: "PRODUCT_OWNER"
   * **Tool MCP:** `prp-generator`
   * `target_project`: "PROJECTS/$TARGET_PROJECT"
   * **Params:** '{"action": "generate_master", "overwrite": true}'

**Esperar la firma (HITL) del Director en APPROVAL_M1.md antes de dar por finalizada la fase.**
