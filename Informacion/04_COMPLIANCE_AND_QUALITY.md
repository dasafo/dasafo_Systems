# 🛡️ 04_COMPLIANCE_AND_QUALITY | Los Porteros de la Calidad y Seguridad (v3.2.0-S)

Este departamento es el responsable de que nada salga de la factoría si no es **Seguro**, **Correcto** y está **Bien Documentado**. Actúa como el sistema inmune de la factoría, filtrando implacablemente cualquier desviación de los estándares industriales.

En la versión **v3.2.0-S "Modular Toolbox"**, la calidad se rige por la **Tolerancia Cero** a errores de infraestructura, la **Seguridad Zero-Trust** y la transparencia mediante el **ADR Law**.

---

### 🤖 Agentes Clave y Roles (v3.2.0-S)

#### 1. QA_TESTER 🧪 (Arquitecto de Verificación y Sistema Inmune)
Asegura la estabilidad absoluta mediante pruebas rigurosas, destructivas y automatizadas.
*   **Pruebas de Espectro Completo:** Valida flujos de extremo a extremo (E2E) desde la interfaz (UX) hasta la integridad de la base de datos (DB).
*   **Verificación Destructiva:** Intenta romper el sistema activamente para descubrir modos de fallo no obvios.
*   **Gobernanza AutoShield:** Es el operador principal del `autoshield-feedback-writer` para actualizar la memoria colectiva de la factoría.
*   **Mandato de Métricas:** Verifica que todos los outputs técnicos sigan el mandato de **Unidades SI** y los KPIs de rendimiento.

#### 2. SECURITY_AUDITOR 🛡️ (Arquitecto de Seguridad y Guardián Zero-Trust)
Escanea el código en busca de vulnerabilidades y secretos expuestos para garantizar la inmunidad absoluta.
*   **Escaneo de Secretos:** Identifica proactivamente claves de API expuestas y datos sensibles (PII) mediante el `agentic-thought-secret-scanner`.
*   **Modelado de Amenazas:** Analiza los planos arquitectónicos en busca de antipatrones de seguridad (ej. Inyección SQL, RLS inseguro).
*   **Guardia de Dependencias:** Monitorea librerías externas y el nodo `INFRA` en busca de vulnerabilidades (CVE) y fugas de aislamiento.
*   **Tolerancia Cero:** Rechaza cualquier tarea o commit que active una alerta de alta severidad.

#### 3. DOCS_MASTER 📖 (Comunicador Técnico y Guardián de la Estandarización)
Convierte la complejidad técnica en documentación premium y manuales profesionales.
*   **Redacción Técnica High-End:** Mantiene los archivos `README.md`, `ARCHITECTURE.md` y `CHANGELOG.md` con una estructura elocuente y clara.
*   **Puente Lingüístico:** Asegura que la lógica interna permanezca 100% en inglés (EN) mientras mantiene los manuales de usuario en español (ES).
*   **Documentación de API:** Genera y audita esquemas de Swagger/OpenAPI y guías técnicas.
*   **Ley de ADR:** Asegura que cada cambio arquitectónico tenga un registro correspondiente (ADR) en el conocimiento local del proyecto.

---

### 🚀 Motor Ejecutivo: Skills de Cumplimiento v3.2.0-S

El departamento de cumplimiento opera mediante el **Modular Toolbox**, utilizando habilidades de filtrado agresivo:

*   **Validación de Calidad (QA_TESTER):**
    *   `browser-visual-validation`: Pruebas de regresión visual y comparación de interfaces.
    *   `playwright-visual-testing`: Automatización de navegadores de extremo a extremo.
    *   `requirements-validation-audit`: Verificación del código contra las especificaciones del contrato **PRP**.
*   **Seguridad Blindada (SECURITY_AUDITOR):**
    *   `agentic-thought-secret-scanner`: Motor de escaneo rudo para detectar secretos y fugas de datos.
    *   `nemo-llm-guardrails`: Aplicación de seguridad en la IA y protección contra inyecciones de prompts.
    *   `owasp-llm-enforcement`: Validación contra los estándares OWASP Top 10 para modelos de lenguaje.
*   **Comunicación Estándar (DOCS_MASTER):**
    *   `api-docs-generator`: Generación automática de especificaciones técnicas OpenAPI.
    *   `user-experience-copywriter`: Redacción técnica centrada en el usuario y onboarding.

---

### ✅ Filtros de Calidad y Seguridad v3.2.0-S
- **Validation Gate:** El QA Tester tiene el poder de bloquear el paso a producción de cualquier componente que no cumpla el contrato.
- **Security Checkpoints:** Cada tarea en `03_COMPLETED` es auditada por el Security Auditor antes de ser movida al archivo histórico.
- **Autoshield Preflight:** Es obligatorio ejecutar `autoshield-preflight-check` antes de cualquier ciclo de auditoría o generación de documentación.
- **Mandato ADR:** Ninguna decisión técnica estructural es válida sin su correspondiente Registro de Decisión Arquitectónica (ADR).

---
*Información de Calidad y Cumplimiento v3.2.0-S | dasafo_Systems.*
