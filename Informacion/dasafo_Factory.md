# 🏭 dasafo_FACTORY | Solidity Guard v3.1.5

La carpeta **`dasafo_FACTORY`** es el "Motor de Inteligencia" (el cerebro) de todo tu ecosistema. Su función principal es separar **cómo se trabaja** (las reglas y roles) de **lo que se hace** (los proyectos específicos).

En esta versión **v3.1.5 "Solidity Guard"**, la factoría ha alcanzado un estado de madurez industrial, con una arquitectura de servicios compartidos y un sistema de aprendizaje continuo.

---

### 🧠 ¿Qué es y qué hace? (Agnosticismo de Proyecto)

Es una **Factoría de IA Apátrida (Stateless)**. Los agentes no guardan el código en su interior, sino que "entran al taller", leen las reglas de la factoría y ejecutan la misión en la carpeta del proyecto correspondiente.

*   **Contrato PRP (Puerta de Validación):** Ningún agente escribe código sin que el usuario haya firmado el contrato de visión (PRP). Esto garantiza que el "Qué" esté claro antes del "Cómo".
*   **AutoShield v3.1 (Bucle de Feedback):** Si un agente comete un error, se documenta en formato YAML en el `FEEDBACK-LOG.md`. Todos los agentes futuros leen este log para evitar repetir errores costosos, incluyendo patrones de infraestructura.
*   **Sistemas de Sensores (MCP Senses):** La factoría ahora mapea explícitamente sus sentidos (browsers, bases de datos, APIs de Github) para interactuar con el mundo físico de forma estructurada.
*   **Mandato de Inglés Técnico:** Aunque esta documentación de alto nivel es en español, todo el código interno y la lógica técnica están en inglés para cumplir con estándares globales de ingeniería.

---

### 🏛️ Estructura por Departamentos (v3.1)

La factoría está organizada en **5 departamentos especializados**:

| Departamento | Agentes y Misión | Innovaciones v3.1 |
| :--- | :--- | :--- |
| **`00_GLOBAL_KNOWLEDGE`** | Leyes Universales y `skill_schema`. | Contrato PRP centralizado y Esquema de Feedback. |
| **`01_STRATEGY`** | `ORCHESTRATOR`, `PRODUCT_OWNER`. | Validación estricta del contrato PRP antes de la fase de Arquitectura. |
| **`02_ARCHITECTURE`** | `ARCHITECT`, `RESEARCH_AGENT`. | Búsqueda semántica profunda y registro de decisiones (ADR). |
| **`03_PRODUCTION`** | `BACKEND`, `FRONTEND`, `DB`, `DATA`. | Código 100% tipado y alineado con el Diseño Atómico. |
| **`04_COMPLIANCE`** | `QA_TESTER`, `SECURITY`, `DOCS`. | Auditoría de secretos (Gitleaks v3.1.5) y validación visual avanzada. |
| **`05_OPERATIONS`** | `DEVOPS`, `MEMORY`, `EVOLVER`. | Nodo `INFRA` compartido y análisis de patrones AutoShield v3.1.5. |

---

### 🚀 Motor de Ejecución: Power Skills (v3.1)

La factoría no solo piensa, sino que entrega resultados automáticos mediante habilidades críticas:

*   **Estrategia Automática**: Generación de contratos PRP e inversión de intenciones a tareas (DAG).
*   **Diseño de Ingeniería**: Creación de registros de decisión técnica (ADR) y búsqueda profunda de tecnología.
*   **Producción Premium**: Generadores de Boilerplate de API y sistemas de diseño atómico visual.
*   **Calidad Blindada**: Escaneo de seguridad interno y auditorías automáticas de cumplimiento.
*   **Operaciones Autónomas**: AutoShield v3.1 para aprendizaje de errores y monitorización de infraestructura centralizada.

---

### 🕹️ Archivos Maestro de la Factoría (v3.1)

*   **`init_project.sh`**: Inicializa el esqueleto del proyecto, forzando la creación del primer `PRP_CONTRACT.json`.
*   **`ACTIVE_MISSIONS.json`**: El registro en tiempo real de todos los proyectos activos en la factoría.
*   **`FACTORY_VERSION.md`**: El historial de versiones. Actualmente en **v3.1 "Infraestructura Blindada"**.
*   **`FEEDBACK-LOG.md`**: El motor de AutoShield. Consolida los errores aprendidos para evitar redundancias.
*   **`GLOBAL_SOUL.md`**: El "Alma" de la factoría. Consolida la ética, el minimalismo y el rigor de todos los agentes.
*   **`GLOBAL_USER.md`**: Define el perfil y las expectativas del usuario para que los agentes resuenen con sus necesidades.
*   **`COMMUNICATION_PROTOCOL.md`**: Define cómo fluyen los mensajes y las tareas entre agentes (Discovery -> Architecture -> Execution -> QA).
*   **`MCP_SENSES_PROTOCOL.md`**: El mapa sensorial de la factoría (browsers, filesystem, bases de datos).
*   **`OPERATIONS_MANUAL.md`**: La guía de mantenimiento técnico para administradores de la factoría.
*   **`UNIVERSAL_PIPELINE.md`**: El mapa detallado de las 5 fases de vida de cualquier proyecto.

---

### 🕹️ Comandos de Poder

*   **`/factory-orchestrate`**: Invoca al Orquestador para mover el tablero Kanban y avanzar de fase.
*   **`/scan` / `/factory-audit`**: Lanza un escaneo agresivo de seguridad y calidad sobre el código producido.

**Filosofía:** *"Moverse rápido de una forma que los agentes del futuro puedan entender, extender y confiar. El sistema debe permanecer estable bajo una evolución multi-agente continua."*
