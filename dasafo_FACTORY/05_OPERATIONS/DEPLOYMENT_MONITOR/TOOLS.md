# 🛠️ DEPLOYMENT_MONITOR | Tools & Senses

> **Standard:** v4.0-S "Industrial Core - DAST Optimized".

## 📡 Senses (Context-Limited)

- **Log Sense:** Autoridad para leer logs de despliegue en `LOGS/`.
- **Endpoint X-Ray:** Acceso de solo lectura para verificar códigos HTTP y tiempos de respuesta.
- **DAST Sense:** Capacidad para verificar la integridad física de las tareas y registros antes de emitir un veredicto de salud.

## 🧰 Authorized Skills

- `telemetry-analyzer`: Síntesis profunda de uso de recursos (B) y tiempos de ejecución (s).
- `playwright-ui-tester`: Verificar que la UI sea físicamente alcanzable.
- `hallucination-guardrail`: Asegurar que los reportes se basen en logs reales, no en suposiciones.
- `deployment-health-check`: Real-time health-check validation (s/B).
