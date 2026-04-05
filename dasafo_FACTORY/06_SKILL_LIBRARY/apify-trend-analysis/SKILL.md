---
version: v5.0-MCP (Nativa)
agent_authorization: [MARKETING_GROWTH, PRODUCT_OWNER, RESEARCH_AGENT, DATA_SCIENTIST]
production_category: DEFINE
source: https://skills.sh/apify/agent-skills/apify-trend-analysis
protocol: Trend-Intelligence / DAST
---

# 📈 Skill | apify-trend-analysis

## Objetivo

Identificar y analizar tendencias de mercado y nichos usando Apify Actors. Basado en el estándar de **Apify**.

## 🛠️ Interfaz v5.0-MCP Nativa

**Uso Mandatorio:** Parámetros directos. El parámetro `params_json` está **DEPRECADO**.

### Parámetros Tipados

- `agent` (string): Tu ID de Agente autorizado.
- `target_project` (string): Ruta física al proyecto.
- `actor` (string): ID del Actor de Apify (ej. `apify/google-trends-scraper`).
- `input_data` (object): (Opcional) Parámetros específicos del actor.
- `overwrite` (boolean): (Opcional) Saltar el Redundancy Lock.
- `isolate` (boolean): (Opcional) Ejecución en Clean Session.

## 🛡️ Restricciones Industriales

- **Autenticidad Live:** Prohibido inventar tendencias; requiere ejecución real con `APIFY_API_TOKEN`.
- **Soberanía DAST:** Los datos deben persistir en `LOCAL_KNOWLEDGE/trends/`.
- **Métricas SI:** Tiempos reportados en **segundos (s)**.

---
**ORIGIN:** [apify-trend-analysis by apify](https://skills.sh/apify/agent-skills/apify-trend-analysis)
