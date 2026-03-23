El departamento de **`04_COMPLIANCE_AND_QUALITY`** es la "Aduana de Seguridad" de la factoría. Su misión es garantizar que nada salga a producción si no es 100% seguro, estable y fiel a los requisitos originales.

Aquí tienes el desglose de sus agentes y archivos:

---

### 1. 🧪 QA_TESTER (El Juez de Solidez)
Es el responsable de verificar que el código no solo funcione, sino que cumpla con los estándares de calidad definidos.

*   **`IDENTITY.md`**: Define su rol como un probador implacable, escéptico y orientado al detalle.
*   **`HEARTBEAT.md`**: Un registro del estado de salud de las pruebas del sistema.
*   **`SOUL.md`**: Su filosofía de "Cero Errores" y la importancia de la experiencia de usuario (UX) sin fallos.
*   **`SKILLS/`**: 
    *   **`scoutqa-automated-suites`**: Creación de pruebas automáticas que se ejecutan sin intervención humana.
    *   **`playwright-visual-testing`**: Verificación de que la interfaz se ve bien en todos los navegadores y tamaños de pantalla.
    *   **`hallucination-report-guardrail`**: Un filtro especial para detectar si el código generado incluye funciones que no existen o lógica inventada.

---

### 2. 🛡️ SECURITY_AUDITOR (El Guardián Implacable)
Su misión es proteger el sistema contra ataques externos y asegurar que no haya fugas de información sensible.

*   **`IDENTITY.md`**: Define su personalidad de "Hacker Ético" interno, siempre buscando vulnerabilidades.
*   **`SOUL.md`**: Su compromiso con la privacidad de los datos y la seguridad desde el diseño (Security by Design).
*   **`TOOLS.md`**: Lista de herramientas MCP para escaneo de vulnerabilidades y revisión de dependencias.
*   **`SKILLS/`**:
    *   **`agentic-thought-secret-scanner`**: Capacidad para detectar si algún agente ha dejado una API Key o contraseña hardcodeada en el código.
    *   **`owasp-llm-enforcement`**: Aplicación de los 10 estándares principales de seguridad para aplicaciones web y modelos de lenguaje.
    *   **`nemo-llm-guardrails`**: Implementación de barreras de seguridad de NVIDIA para evitar respuestas o acciones peligrosas de los agentes.

---

### 3. ✍️ DOCS_MASTER (El Redactor Técnico Premium)
Transforma el "código sucio" en documentación limpia, manuales de usuario y referencias API de las que estar orgulloso.

*   **`IDENTITY.md`**: Perfil de comunicador técnico con enfoque en claridad y elegancia.
*   **`SKILLS/`**: 
    *   **`api-docs-generator`**: Creación automática de Swagger/Markdown para las APIs del proyecto.
    *   **`manual-builder`**: Generación de guías de usuario finales basadas en la funcionalidad real implementada.
    *   **`changelog-automator`**: Mantenimiento del historial de cambios de cada proyecto.

---

### 📂 El Filtro de la Factoría

Este departamento es el que interactúa directamente con la carpeta **`05_REJECTED`**. Si el **QA Tester** o el **Security Auditor** encuentran un fallo, mueven la tarea a "Rechazado" y el desarrollador **DEBE** corregirlo antes de intentar moverlo a `04_ARCHIVE`.

**En resumen:** En este departamento, el software se pone a prueba bajo fuego. Sin este equipo, la factoría fabricaría software que podría fallar en manos del usuario o ser hackeado fácilmente. Es el seguro de vida de tu proyecto.
