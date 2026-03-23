# Skill: Premium Dashboard Architecture
> **Source:** https://skills.sh/supercent-io/skills-template/nextjs-premium-dashboard
> **Agent:** FRONTEND_DEV

## Objective
Build high-level, responsive administrative interfaces using Next.js App Router and professional layouts.

## Core Templates
- **Standard Layout:** SideBar (collapsible), TopBar (breadcrumbs/user), and MainContent.
- **Skeleton Strategy:** Implement custom loading states for every data-fetching component.
- **Error Boundaries:** Wrap critical UI sections to prevent full-page crashes.
- **Responsive Guard:** Ensure all dashboards are usable on Mobile, Tablet (Portrait/Landscape), and Desktop.

## Workflow
1.  **Scaffold:** Use the factory's Next.js template in `/WORKSPACE/frontend/`.
2.  **Navigation:** Implement semantic breadcrumbs using `next/navigation`.
3.  **Data Fetching:** Prefer Server Components for speed, with Suspense for non-blocking UI.
