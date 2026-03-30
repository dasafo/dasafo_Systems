---
version: 3.3.1-S
agent: MARKETING_GROWTH
source: https://skills.sh/coreyhaines31/marketingskills/social-content
---

# 🚀 Skill | Social Content Strategy (v3.4.0-S)

## Objective

Design and execute high-performance social media marketing strategies through content pillars, hook optimization, and multi-platform repurposing. This skill transforms "Pillar Content" (blogs, videos, podcasts) into a distributed ecosystem of social assets while maintaining brand voice and engagement loops.

## 🛠️ Interface (v3.4.0-S)

### Input Schema (SkillInput.params)

- `action` (enum): `develop_pillars`, `generate_hooks`, `repurpose_system`, `plan_calendar`.
- `target_project` (string, mandatory): Absolute path to the marketing workspace.
- `source_content` (string, optional): Text, URL, or transcript of the pillar content.
- `platforms` (array, optional): Default `["LinkedIn", "Twitter/X", "Instagram", "Threads"]`.
- `brand_voice` (string, optional): Description of the required tone (e.g., "Professional & Provocative").

### Output Schema (SkillOutput.result)

- `content_pillars`: (array) Core themes and topics identified.
- `platforms_output`: (object) Adapted content for each platform (Hooks, Threads, Posts).
- `batching_schedule`: (string) Proposed weekly distribution logic.
- `repurposing_flow`: (array) List of assets extracted from the pillar.
- `industrial_status`: (string) "SOLIDIFIED - CONTENT STRATEGY READY".

### ⚖️ Mandato SI (Sistema Internacional)

Cualquier métrica de rendimiento (tiempos de lectura, latencia de publicación, tasas de engagement, cuotas de almacenamiento de assets) debe expresarse estrictamente en el SI (**segundos**, **bytes**).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Hook-to-Pillar Alignment:** Every social post must be traceable back to a point in the source pillar content. Hallucinating marketing claims is PROHIBITED.
- **Platform Specificity:** No cross-posting without adaptation. The skill must enforce specific formatting for each platform (e.g., Markdown for LinkedIn, Short Threads for X).
- **Batching Mandate:** All proposed strategies must follow the "Batching Strategy" (targeting efficiency < 10,800s per week).
- **Physical Metadata:** The content calendar and pillars must be saved as physical JSON/MD artifacts in `DOCS/MARKETING/`.

## 🧠 Strategic Workflow (v3.4.0-S)

1. **Pillar Analysis:** Extract 3-5 key insights from the source content.
2. **Hook Generation:** Create curiosity, story, and value hooks for each insight.
3. **Adaptation:** Transform insights into platform-native formats (LinkedIn posts, Twitter threads, etc.).
4. **Calendar Distribution:** Schedule assets across the week to maximize distribution spread.
5. **Engagement Planning:** Define a "Daily Engagement Routine" (< 1,800s) to support the content.

---
**ORIGIN:** [social-content by coreyhaines31](https://skills.sh/coreyhaines31/marketingskills/social-content)
*Skill v3.4.0-S | Status: Standardized & Industrialized (Dasafo Edition).*
