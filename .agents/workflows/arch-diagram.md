---
description: Requests the Architect to generate updated Mermaid diagrams of the system in real-time (v4.0-S).
---

Workflow /arch-diagram

This flow activates the Architect to visualize the technical architecture under the **v4.0-S** **"Modular Toolbox"** standard.

1. **Agent:** `ARCHITECT`

2. **Execution Protocol:** // turbo

3. **Run Blueprint Generation:** Execute the following command to map the architecture:
`python3 dasafo_FACTORY/skill_engine.py --agent ARCHITECT --skill architecture-decision-records --target-project $TARGET_PROJECT`

4. **Result Reporting:** Verify that the generated Markdown/Mermaid files are physically present in `DOCS/ARCH/`.

**Drawing technical blueprints...**
