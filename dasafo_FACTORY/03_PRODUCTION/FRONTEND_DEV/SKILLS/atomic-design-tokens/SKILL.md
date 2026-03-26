# 💎 Skill | Atomic Design Tokens
> **Version:** v3.1.5 "Solidity Guard"
> **Agent:** FRONTEND_DEV

## Objective
Synchronize the UI implementation with the ARCHITECT's global design system using tokens.

## Token Pipeline
1.  **Ingest:** Read the latest `DESIGN_TOKENS.json` from the Architecture folder.
2.  **Translate:** Map tokens to `tailwind.config.js` theme extensions.
3.  **Implement:** Use semantic classes in JSX: `bg-brand-primary`, `p-token-gap`, `rounded-token-corner`.

## Constraints
- **NO HARDCODED COLORS:** Every hex code or spacing unit must be a token.
- **Theme Support:** Native support for Dark/Light modes based on `PROJECT_STATE.json` settings.
