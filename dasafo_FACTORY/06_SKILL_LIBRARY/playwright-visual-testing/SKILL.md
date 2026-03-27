---
version: 3.2.0-S
agent: QA_TESTER
---

# 🎭 Skill | Playwright Visual Testing

## Objective
Validate the visual and interactive integrity of Frontend interfaces through automated pixel-perfect comparison and micro-interaction auditing.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `url` (string): Target endpoint to test.
- `breakpoints` (list, optional): ["desktop", "tablet", "mobile"]. Default ["desktop"].
- `pixel_threshold` (float, optional): Maximum allowed difference. Default 0.05.

### Output Schema (SkillOutput.result)
- `test_status`: (string) "PASSED" | "FAILED".
- `diff_screenshots`: (list) Paths to visual diff artifacts.
- `interaction_report`: (object) Stats of transition durations (SI).

### ⚖️ Mandato SI (Sistema Internacional)
Las duraciones de las transiciones (Framer Motion) deben reportarse estrictamente en milisegundos (ms) y no exceder los 300ms de límite industrial.

## Testing Domains
- **Resilience:** Verify layout consistency across all breakpoints.
- **Micro-interactions:** Audit `framer-motion` timings for "Premium Feel".
- **Data Integrity:** Cross-check graphed values against `DB_MASTER` raw records (error < 0.01%).

---
*Skill v3.2.0-S | Status: Standardized.*
