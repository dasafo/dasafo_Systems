---
version: v5.0-MCP (Nativa)
agent_authorization: [ARCHITECT]
production_category: PLAN
source: https://skills.sh/jeffallan/claude-skills/api-designer
protocol: Design-First / DAST
---

# 📡 Skill | api-contract-generator

## Objetivo

Diseñar y mantener contratos de API industriales (OpenAPI 3.1) siguiendo la metodología **Design-First**. Basado en el estándar **api-designer**.

## 🛠️ Interfaz v5.0-MCP Nativa

**Uso Mandatorio:** Argumentos directos. El parámetro `params_json` está **DEPRECADO**.

### Parámetros Tipados

- `agent` (string): Tu ID de Agente (debe ser 'ARCHITECT').
- `target_project` (string): Ruta física al proyecto.
- `resource` (string): (Opcional) Nombre del recurso a modelar (ej. 'user', 'order').
- `version` (string): (Opcional) Versión de la API (defecto: '1.0.0').
- `overwrite` (boolean): (Opcional) Saltar el Redundancy Lock.
- `isolate` (boolean): (Opcional) Ejecución en Clean Session.

## 🛡️ Restricciones Industriales

- **RESTful Enforcement:** Solo URIs orientadas a recursos. Verbos en URIs prohibidos.
- **Soberanía DAST:** El contrato DEBE persistir físicamente en `DOCS/API-CONTRACT.yaml`.
- **Métricas SI:** Tiempos reportados en **segundos (s)**.

---
**ORIGEN:** [api-designer by jeffallan](https://skills.sh/jeffallan/claude-skills/api-designer)
