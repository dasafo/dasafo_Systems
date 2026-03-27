---
version: 3.2.0-S
agent: BACKEND_DEV
---

# 🛡️ Skill | Resilient Error Handling

## Objective
Implement professional-grade error handling patterns (Circuit Breaker, Retries) to prevent cascading failures and ensure industrial system stability.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)
- `service_name` (string): Target external service to wrap.
- `max_retries` (integer, optional): Default 3.

### Output Schema (SkillOutput.result)
- `wrapper_code`: (string) The generated Python resilient block.
- `circuit_breaker_status`: (string) "DEPLOYED".

### ⚖️ Mandato SI (Sistema Internacional)
Los tiempos de espera (timeout) y retrasos (delay) entre reintentos deben expresarse en segundos o milisegundos (unidades SI).

## Key Patterns
1.  **Circuit Breaker:** Trip the circuit on repeated 5xx errors to protect the ecosystem.
2.  **Exception Mapping:** Map technical exceptions to semantic industrial errors with internal trace IDs.
3.  **Zero Swallow:** Swallow NO exceptions without logging.
4.  **Logging:** Persistent logging of stack traces in `$TARGET_PROJECT/LOGS/errors.log`.

---
*Skill v3.2.0-S | Status: Standardized.*
