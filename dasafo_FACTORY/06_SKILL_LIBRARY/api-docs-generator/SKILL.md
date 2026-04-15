> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Skill: **api-docs-generator** ]
---
version: v5.0-MCP (Nativa)
agent_authorization: [DOCS_MASTER]
production_category: SHIP
source: https://skills.sh/sickn33/antigravity-awesome-skills/api-documentation-generator
protocol: Documentation-as-Code / DAST
---

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]


# 📚 Skill | api-docs-generator

## Objetivo

Transformar contratos API físicos (YAML) en documentación Markdown profesional y accionable. Basado en el estándar de **sickn33**.

## 🛠️ Interfaz v5.0-MCP Nativa

**Uso Mandatorio:** Parámetros directos. El uso de `params_json` es una **Violación de Protocolo**.

### Parámetros Tipados

- `agent` (string): Tu ID de Agente (debe ser 'DOCS_MASTER').
- `target_project` (string): Ruta física al proyecto.
- `contract_path` (string): (Opcional) Nombre del YAML en `DOCS/` (defecto: 'API-CONTRACT.yaml').
- `output_name` (string): (Opcional) Nombre del archivo generado (defecto: 'API_REFERENCE_PRO.md').
- `include_examples` (boolean): (Opcional) Generar snippets de código (cURL, Python, TS).
- `overwrite` (boolean): (Opcional) Ignorar el Redundancy Lock.
- `isolate` (boolean): (Opcional) Ejecución en Clean Session.

## 🛡️ Restricciones Industriales

- **Fidelidad Física:** Prohibido inventar documentación; debe leer el disco.
- **Métricas SI:** Tiempos reportados en **segundos (s)**.
- **Soberanía DAST:** El artefacto resultante debe ser verificable en `DOCS/`.

---

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]

**ORIGEN:** [api-documentation-generator by sickn33](https://skills.sh/sickn33/antigravity-awesome-skills/api-documentation-generator)
