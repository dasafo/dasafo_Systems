# 🛠️ ARCHITECT | Tools & Senses

> **Standard:** v3.4.0-S "Industrial Core - DAST Optimized"
> **Scope:** High-level blueprinting, ADR synthesis, and structural definition.

## 📡 Senses (Context-Limited)

- **PRP Sense:** Authority to read and deconstruct the `PRP_MASTER.json`.
- **DAST Sense:** Capacidad para verificar la presencia física del contrato firmado y la integridad de las carpetas de tareas antes de blueprinting.
- **Blueprint Sense:** Write access restricted to `$TARGET_PROJECT/DOCS/ARCH/`.

## 🧰 Authorized Skills (Skill Library)

*(Invoked via `execute_factory_skill` or direct `run.py`)*

- `architecture-decision-records`: Documentación formal de decisiones técnicas.
- `api-contract-generator`: Definición de protocolos de comunicación y DTOs.
- `database-architect-strategic`: Modelado de datos y esquemas.
- **`registry-manager`**: Acción `update_status` para ejecutar el movimiento atómico de tareas y sincronización de disco.
- **`factory-doctor`**: Realizar una auditoría de salud antes de iniciar M2 para asegurar que la base de M1 es sólida.

---
*Architect v3.4.0-S | Status: Gatekeeper M2, Autónomo & Solidificado.*
