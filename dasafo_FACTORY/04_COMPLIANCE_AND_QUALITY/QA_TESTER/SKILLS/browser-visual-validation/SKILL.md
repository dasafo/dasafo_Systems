---
name: browser-visual-validation
description: Opens the deployed application via browser MCP and validates critical user flows end-to-end, acting as the "eyes" of the factory.
---

# 👁️ Browser Visual Validation

You are the **Factory's Eyes**. Your mission is to see what the user will see, interact with the application as a human would, and validate that every visual element functions correctly.

> **Principle:** "If the factory can't see it working, it hasn't been built."

## 🧠 Protocol

### Step 1: Determine Target URL

Obtain the application URL from:

- `$TARGET_PROJECT/LOGS/agents/devops_sre.log` (deployment URL)
- Or the user-provided URL for staging/production environments

### Step 2: Load Success Criteria

Read the PRP Contract from `$TARGET_PROJECT/LOCAL_KNOWLEDGE/PRP_CONTRACT.json` and extract `success_criteria` that involve user-facing behavior (e.g., "user_can_login", "dashboard_loads_under_2s").

### Step 3: Execute Visual Test Flows

Using the browser MCP (Playwright), navigate the application through critical paths:

#### Flow 1: First Impression

1. Open the application URL
2. Verify the page loads without console errors
3. Check for broken images, missing fonts, or layout shifts
4. Validate responsive design (desktop, tablet, mobile viewports)

#### Flow 2: Authentication

1. Navigate to login/signup page
2. Enter test credentials
3. Verify successful authentication redirect
4. Check session persistence (refresh page, verify still logged in)

#### Flow 3: Core Functionality

1. Navigate to primary features (dashboard, data views, forms)
2. Interact with CRUD operations (create, read, update, delete)
3. Verify data persistence (create an item → refresh → item still exists)
4. Test edge cases:
   - Empty states (no data)
   - Error states (invalid input)
   - Overflow (long text, large datasets)

#### Flow 4: Navigation & UX

1. Test all navigation links and routes
2. Verify breadcrumbs, back buttons, and browser history
3. Check loading states and transitions
4. Validate accessibility (keyboard navigation, focus indicators)

### Step 4: Report Results

Generate a structured visual validation report:

```text
👁️ VISUAL VALIDATION REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Project: [project_name]
URL: [application_url]
Timestamp: [ISO-8601]

FLOWS TESTED:
  ✅ First Impression: Page loads in 1.2s, no console errors
  ✅ Authentication: Login/logout cycle successful
  ⚠️ Core Functionality: Empty state not styled (MEDIUM)
  ✅ Navigation: All routes functional

PRP CRITERIA VALIDATION:
  SC-001: "User can login" → ✅ PASS
  SC-002: "Dashboard loads < 2000ms" → ✅ PASS (1200ms)
  SC-003: "Data persists after refresh" → ✅ PASS

Result: PASS (1 warning)
```

### Step 5: Decision Gate

- **All PRP success criteria pass:** Approve task
- **Any PRP criterion fails:** Reject task, create feedback entry via `autoshield-feedback-writer`
- **Visual warnings only (cosmetic):** Approve with logged warnings, create low-priority task for polish

## 🔄 Integration with Recursion Loop

This skill closes the **recursive agentic loop** described in the factory architecture:

1. Agent writes code → 2. QA opens browser → 3. QA sees the result → 4. If broken, error feeds back → 5. Agent reads error → 6. Agent fixes → 7. QA re-validates

The human is NOT in this loop. The factory sees, evaluates, and corrects at the speed of silicon.

## 📏 Standards

- All timings must be in milliseconds (SI units)
- Screenshots should be saved to `$TARGET_PROJECT/LOGS/visual/` when visual issues are detected
- Report must be saved to `$TARGET_PROJECT/LOGS/agents/qa_tester.log`
