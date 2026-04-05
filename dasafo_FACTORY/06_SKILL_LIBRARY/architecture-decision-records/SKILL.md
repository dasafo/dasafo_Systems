---
version: v5.0-MCP (Nativa)
agent_authorization: [ARCHITECT]
production_category: PLAN
source: https://skills.sh/wshobson/agents/architecture-decision-records
protocol: Immutable-Log / DAST
---

# 📝 Skill | architecture-decision-records

## Objetivo

Capturar y gestionar decisiones técnicas en un registro formal, searchable y persistente. Basado en el estándar de **wshobson**.

## 🛠️ Interfaz v5.0-MCP Nativa

**Uso Mandatorio:** Parámetros tipados. El parámetro `params_json` ha sido **ELIMINADO**.

### Parámetros

- `agent` (string): Tu ID de Agente (debe ser 'ARCHITECT').
- `target_project` (string): Ruta física al proyecto.
- `action` (enum): `new`, `init`, `list`, `supersede`, `finalize_blueprint`.
- `title` (string): Título descriptivo (Requerido para `new`).
- `context` (string): El problema y las restricciones.
- `decision` (string): La solución elegida y su razonamiento.
- `consequences` (string): Trade-offs e impacto.
- `target_id` (string): ID del ADR a reemplazar (Requerido para `supersede`).
- `overwrite` (boolean): Opcional. Saltar el Redundancy Lock.

## 🛡️ Restricciones Industriales

- **Inmutabilidad Física:** Una vez aceptado, un ADR solo se cambia vía `supersede`.
- **Integridad Secuencial:** Los IDs deben ser estrictamente correlativos (0001, 0002...).
- **Métricas SI:** Cualquier métrica técnica (latencia, almacenamiento) debe expresarse en **segundos (s)** o **bytes (B)**.

---
**ORIGEN:** [architecture-decision-records by wshobson](https://skills.sh/wshobson/agents/architecture-decision-records)
