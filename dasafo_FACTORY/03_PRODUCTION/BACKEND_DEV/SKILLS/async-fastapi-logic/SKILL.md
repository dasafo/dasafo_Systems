# Skill: Async FastAPI & JWT Logic
> **Source:** https://skills.sh/jeffallan/claude-skills/fastapi-expert
> **Agent:** BACKEND_DEV

## Objective
Master high-performance asynchronous logic and secure authentication in FastAPI.

## Constraints (Must-Follow)
- **Async Only:** Always use `async def` for endpoints and I/O bound tasks.
- **JWT Security:** Implement secure authentication using `PyJWT` and OAuth2 password flow.
- **Background Tasks:** Use FastAPI `BackgroundTasks` for non-blocking operations (e.g., sending emails, log cleanup).
- **Environment Safety:** NEVER hardcode secrets. Use `pydantic-settings` to load from `.env`.

## Implementation Strategy
- Use `httpx` for async external API calls.
- Use `SQLAlchemy` (v2.0+) with `asyncpg` for database interaction.
- Enforce **Strict 01_CODING_STANDARDS.md** compliance.
