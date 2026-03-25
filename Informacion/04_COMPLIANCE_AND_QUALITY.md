# 🛡️ 04_COMPLIANCE_AND_QUALITY | Los Porteros de la Calidad

Este departamento es el responsable de que nada salga de la factoría si no es **Seguro**, **Correcto** y está **Bien Documentado**.

---

### 🤖 Agentes Clave

#### 1. QA_TESTER (El Validador de Requisitos)
Asegura que el código hace lo que el Product Owner dijo que debía hacer.
*   **Habilidades v2.1:** Tests automáticos con Playwright, auditorías de validación de requisitos y reportes de alucinaciones.
*   **Misión:** Si el QA no da el visto bueno, la tarea regresa a Producción (Phase 05_REJECTED).

#### 2. SECURITY_AUDITOR (El Guardián Zero-Trust)
Escanea el código en busca de vulnerabilidades y secretos expuestos.
*   **Herramientas:** Escaneo agresivo de secretos (`agentic-thought-secret-scanner`), cumplimiento de OWASP y mitigación de inyecciones de prompts.
*   **Misión:** Cero tolerancia con API keys hardcodeadas o dependencias vulnerables.

#### 3. DOCS_MASTER (El Traductor Técnico)
Convierte la complejidad técnica en manuales claros y profesionales.
*   **Habilidades:** Generador de docs de API, redactor técnico senior y estratega de documentación para el usuario final.

### 🚀 Motor de Ejecución (Skills v2.1)

Este departamento garantiza el cumplimiento y la calidad mediante sus habilidades (`skills`) ejecutables:

*   **`requirements-validation-audit` (QA_TESTER):** Capacidad para auditar si el código desarrollado cumple estrictamente con el contrato PRP firmado.
*   **`internal-secrets-search` (SECURITY_AUDITOR):** Motor de escaneo profundo que busca secretos y vulnerabilidades en la lógica interna.
*   **`documentation-generation` (DOCS_MASTER):** Herramienta automática para generar manuales y guías técnicas de alta calidad.

---

### ✅ El Filtro de Calidad

- **Validation Gate:** El QA Tester tiene el poder de bloquear el paso a "Go-Live" de cualquier componente.
- **Security Checkpoints:** Cada tarea completada en `03_COMPLETED` es auditada por el Security Auditor antes de ser archivada.
- **Documentación Viva:** El Docs Master asegura que cada cambio en la arquitectura se refleje instantáneamente en los manuales.

---
*La calidad no es un accidente, es el resultado de un filtrado implacable.*
