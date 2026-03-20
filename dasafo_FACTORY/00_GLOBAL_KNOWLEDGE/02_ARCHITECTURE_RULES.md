# 02. Architecture Rules
> **Objective:** Preserve the Separation of Concerns (SoC) law so the agency can operate in parallel without colliding.

## 1. Strict Separation of Responsibilities
Never mix Business Logic, Data Layer, and UI in the same module.
- **UI (Interface):** Is *dumb*. It only draws data and emits events.
- **Business Logic:** Is *blind*. It doesn't know if it's on the web, in a terminal, or on a mobile device.
- **Data Layer:** Is *isolated*. It only handles persistence and relationships.

## 2. DTO (Data Transfer Object) Discipline
- Internal domain models (SQLAlchemy, Prisma) MUST NEVER cross layer boundaries.
- Any data going to the UI must pass through an explicit transformation (DTOs or Pydantic schemas).

## 3. Dependency Agnosticism
- Critical third-party libraries must be isolated using internal interfaces or wrappers. The core never depends directly on external APIs that could be deprecated.

## 4. Event-Driven Architecture (Temporal Decoupling)
- Avoid synchronous coupling for long-running processes between agents.
- Prefer publishing events (`AnomalyDetected`, `TaskCompleted`) instead of making prolonged blocking network calls. 
- *If an agent fails, the chain should not collapse immediately.*
