# Skill: Resilient Error Handling (Circuit Breaker)
> **Source:** https://skills.sh/wshobson/agents/error-handling-patterns
> **Agent:** BACKEND_DEV

## Objective
Implement professional error handling to prevent cascading failures in the factory's infrastructure.

## Key Patterns
1.  **Circuit Breaker:** If an external service returns 5xx consistently, TRIP the circuit and return a cached or default value.
2.  **Graceful Degradation:** If the Database is slow, serve read-only cached data.
3.  **Exception Mapping:** Map Python exceptions (e.g., `AttributeError`) to semantic HTTP exceptions (e.g., `400 Bad Request`) with informative JSON bodies.

## Reporting Standards
- All errors reaching the UI must include: `error_code`, `message`, `trace_id`.
- Log detailed stack traces ONLY in the internal `$TARGET_PROJECT/LOGS/errors.log`.
- Silence is NOT security: Never swallow exceptions without logging.
