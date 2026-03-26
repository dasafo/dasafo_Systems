# 🎭 Skill | Playwright Visual & Interaction Testing
> **Version:** v3.1.5 "Solidity Guard"
> **Source:** https://playwright.dev/ (Adapted)
> **Agent:** QA_TESTER

## Objective
Validate the visual integrity and interactive responsiveness of the Frontend interfaces.

## Testing Domains
- **Layout Consistency:** Use screenshots to detect style regressions.
- **Micro-interactions:** Verify Framer Motion transitions are within the 300ms limit.
- **Responsiveness:** Test on Desktop (1920x1080), Tablet (iPad), and Mobile (iPhone 13) breakpoints.
- **Data Integrity:** Verify that graphed data matches the raw data from `DB_MASTER` within a 0.01% error margin.

## Workflow
1.  **Launch:** Start the Browser Sandbox.
2.  **Interaction:** Simulate user clicks, drags, and inputs.
3.  **Compare:** Match visual output against the ARCHITECT's design tokens.
