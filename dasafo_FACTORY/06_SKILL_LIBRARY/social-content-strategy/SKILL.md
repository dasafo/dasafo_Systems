> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Skill: **social-content-strategy** ]
---
version: v5.0-MCP (Native)
agent_authorization: [MARKETING_GROWTH]
source: https://skills.sh/coreyhaines31/marketingskills/social-content
protocol: Content-Repurposing / DAST
---
<!-- LEVEL_1_END -->



> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]


# 🚀 Skill | social-content-strategy

## Objective

Design and execute high-performance social media marketing strategies by transforming "Pillar Content" into a distributed ecosystem of social assets.

## 🛠️ Interface (v5.0-MCP Native)

**MANDATORY:** Use direct typed arguments. `params_json` is **DEPRECATED**.

### Typed Parameters

- `agent` (string): Your Agent ID (MARKETING_GROWTH).
- `target_project` (string): Absolute path to the marketing workspace.
- `action` (enum): `repurpose_system` (default), `develop_pillars`, `generate_hooks`, `plan_calendar`.
- `source_content` (string): Text, URL, or transcript of the pillar content.
- `platforms` (list): (Optional) Target platforms (default: LinkedIn, X, Instagram, Threads).
- `brand_voice` (string): (Optional) Description of the required tone.
- `overwrite` (boolean): Bypass Redundancy Lock.
- `isolate` (boolean): Execution in Clean Session.

## Internal Mechanics

- **Hook Alignment:** Every social post must be traceable back to the source pillar content. No hallucinations.
- **Batching Mandate:** Strategies must target an efficiency of < 10,800s per week.
- **SI Standards:** All metrics (reading times, publishing latency) strictly in **Seconds (s)** and **Bytes (B)**.
- **DAST Sovereignty:** Strategy artifacts MUST be saved physically in `DOCS/MARKETING/`.

---

> [ ⬆️ Up: [[../MOC_SKILL_LIBRARY]] | 📂 Global: [[../../_dasafo_FACTORY]] ]

**ORIGIN:** [social-content by coreyhaines31](https://skills.sh/coreyhaines31/marketingskills/social-content)
