# 🏗️ Skill | FastAPI Repository Pattern
> **Version:** v3.1.5 "Solidity Guard"
> **Agent:** BACKEND_DEV

## Objective
Implement a structured, scalable application architecture using the Repository and Service patterns in FastAPI.

## Key Patterns
- **Service Layer:** All complex business logic MUST reside in `/services/`.
- **Repository Pattern:** Database access logic MUST be isolated in `/repositories/` to allow for easy mocking/testing.
- **Dependency Injection:** Use FastAPI `Depends()` for service and repo instantiation.

## Workflow
1.  **Structure:** Create the `/app` folder with `main.py`, `models/`, `schemas/`, `api/`, `services/`, and `repositories/`.
2.  **DTO Compliance:** Use Pydantic schemas (from the Architect's DTOs) for all request/response validation.
3.  **Clean Code:** Follow PEP 8 and use type hinting exclusively.
