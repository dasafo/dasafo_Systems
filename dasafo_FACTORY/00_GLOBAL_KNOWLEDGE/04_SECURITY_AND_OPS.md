# 04. Security, Logs & Operations (OPS)
> **Objective:** A traceable, atomic, and infallible deployment through Zero-Trust policies.

## 1. Chesterton's Fence Law (Safe Refactoring)
Before an agent proceeds to delete or drastically modify fully functional core logic:
1. They must determine **why** it was created.
2. State its assumed purpose.
3. Understand its dependencies.
*Never delete code whose role within the project you haven't completely mapped out.*

## 2. Reproducible Environments (Infra-as-Code)
- "It works on my machine" is an invalid argument for this agency.
- Every environment must be reproducible at the code level (`Dockerfile`, `requirements.txt`, `pyproject.toml`, `package.json`).
- Raw dependencies must be *pinned* to strict versions to prevent drifts.

## 3. Zero-Trust & Sanitization
- Never trust user input (whether in GUI interfaces or external API JSONs).
- Sanitize at the boundaries (CORS, Middlewares, Validators). 
- Secrets (API Keys, DB passwords) must be hidden in `.env`, referenced remotely. Never *hardcoded*.

## 4. Early Observability (Structured Logging)
- `console.log("reached here")` is banned for production systems.
- Use structured logs that provide context. Every backend error must include: `useCase`, `entityId`, `correlationId`, `errorDetails`. An SRE must be able to trace the full lifespan of a failing request.
- **Concurrency Guard:** All writes to `EXECUTION_LOG.md` MUST be protected by the `EXECUTION_LOG.lock` mutex as defined in the Communication Protocol.
