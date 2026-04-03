---
version: v4.0-MCP
agent: QA_TESTER / FRONTEND_DEV
source: internal/skill-creator
---

# 🎭 Skill | Playwright E2E Tester (v4.0-MCP)

## Objective

Execute End-to-End (E2E) browser testing using Playwright to ensure UI/UX workflows match the functional criteria established in the `SPEC_LITE.json` contract.

## 🛠️ Interface (v4.0-MCP)

### Input Schema (SkillInput.params)

- `action` (enum): `generate_spec`, `run_e2e`.
- `target_project` (string, mandatory): Absolute path to the project workspace.
- `spec_path` (string, mandatory): Path to the `SPEC_LITE.json` defining the user flow.
- `url` (string, optional): Localhost or staging URL to test.

### Output Schema (SkillOutput.result)

- `e2e_status`: (string) `PASSED` or `FAILED`.
- `report_path`: (string) Path to the physical report in `LOGS/`.
- `video_trace_bytes`: (integer) Size of the generated trace/video in bytes.
- `industrial_status`: (string) "SOLIDIFIED - E2E VERIFIED" | "BLOCKED - E2E FAILED".

### ⚖️ SI Mandate (International System)

The size of network and video traces must be reported in **bytes** (B), and the loading/execution time in **seconds** (s).

## 🛡️ Industrial Constraints (Zero-Trust)

- **Trace Artifacts:** All runs must produce a physical `PLAYWRIGHT_REPORT.json` detailing the network activity and DOM assertions.
- **Contract Parity:** The assertions in the Playwright spec must map 1:1 to the `04_user_stories` in the project's PRPs.
