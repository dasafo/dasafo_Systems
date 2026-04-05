---
version: v5.0-MCP (Nativa)
agent_authorization: [PRODUCT_OWNER, ORCHESTRATOR]
production_category: DEFINE
source: https://skills.sh/daffy0208/ai-dev-standards/prp-generator
protocol: Contract-Driven / DAST
---

# 📝 Skill | prp-generator

## Objetivo

Generar artefactos de requisitos industriales siguiendo el sistema de doble contrato: **PRP_MASTER** (12 secciones) para M1 y **SPEC_LITE** (4 secciones) para tareas atómicas.

## 🛠️ Interfaz v5.0-MCP Nativa

**Uso Mandatorio:** Parámetros tipados. El parámetro `params_json` está **DEPRECADO**.

### Parámetros

- `agent` (string): Tu ID de Agente autorizado.
- `target_project` (string): Ruta física al proyecto.
- `action` (enum): `generate_master`, `generate_lite`, `update`, `validate`.
- `project_name` (string): Nombre del proyecto o ID de tarea.
- `problem_description` (string): Meta técnica u objetivo central.
- `spec_data` (object): Datos específicos para `generate_lite`.
- `overwrite` (boolean): Saltar el Redundancy Lock.

## 🛡️ Restricciones Industriales

- **Mandato de las 12 Secciones:** Un PRP no es válido si falta alguna sección.
- **Métricas SI:** Éxitos definidos estrictamente en **segundos (s)** y **bytes (B)**.
- **Sincronización Física:** Los contratos deben persistir físicamente (DAST) en la raíz o en `TASKS/`.

---
**ORIGIN:** [PRP Generator by daffy0208](https://skills.sh/daffy0208/ai-dev-standards/prp-generator)
