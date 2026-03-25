# 🏭 dasafo_FACTORY | Chasis Blindado v2.1

La carpeta **`dasafo_FACTORY`** es el "Motor de Inteligencia" (el cerebro) de todo tu ecosistema. Su función principal es separar **cómo se trabaja** (las reglas y roles) de **lo que se hace** (los proyectos específicos).

En esta versión **v2.1 "Chasis Blindado"**, la factoría ha alcanzado un estado de madurez industrial, con procesos de validación automáticos y un sistema de aprendizaje continuo.

---

### 🧠 ¿Qué es y qué hace? (Agnosticismo de Proyecto)

Es una **Factoría de IA Apátrida (Stateless)**. Los agentes no guardan el código en su interior, sino que "entran al taller", leen las reglas de la factoría y ejecutan la misión en la carpeta del proyecto correspondiente.

*   **Contrato PRP (Puerta de Validación):** Ningún agente escribe código sin que el usuario haya firmado el contrato de visión (PRP). Esto garantiza que el "Qué" esté claro antes del "Cómo".
*   **AutoShield v2.0 (Bucle de Feedback):** Si un agente comete un error, se documenta en formato YAML en el `FEEDBACK-LOG.md`. Todos los agentes futuros leen este log para evitar repetir errores costosos.
*   **Sistemas de Sensores (MCP Senses):** La factoría ahora mapea explícitamente sus sentidos (browsers, bases de datos, APIs de Github) para interactuar con el mundo físico de forma estructurada.
*   **Mandato de Inglés Técnico:** Aunque esta documentación de alto nivel es en español, todo el código interno y la lógica técnica están en inglés para cumplir con estándares globales de ingeniería.

---

### 🏛️ Estructura por Departamentos (v2.1)

La factoría está organizada en **5 departamentos especializados**:

| Departamento | Agentes y Misión | Innovaciones v2.1 |
| :--- | :--- | :--- |
| **`00_GLOBAL_KNOWLEDGE`** | Leyes Universales y `skill_schema`. | Contrato PRP centralizado y Esquema de Feedback. |
| **`01_STRATEGY`** | `ORCHESTRATOR`, `PRODUCT_OWNER`. | Validación estricta del contrato PRP antes de la fase de Arquitectura. |
| **`02_ARCHITECTURE`** | `ARCHITECT`, `RESEARCH_AGENT`. | Búsqueda semántica profunda y registro de decisiones (ADR). |
| **`03_PRODUCTION`** | `BACKEND`, `FRONTEND`, `DB`, `DATA`. | Código 100% tipado y alineado con el Diseño Atómico. |
| **`04_COMPLIANCE`** | `QA_TESTER`, `SECURITY`, `DOCS`. | Auditoría de secretos (Gitleaks) y validación visual con Playwright. |
| **`05_OPERATIONS`** | `DEVOPS`, `MEMORY`, `EVOLVER`. | Evolución autónoma del sistema y optimización de contexto. |

---

### 🕹️ Archivos Maestro de la Factoría

*   **`init_project.sh` (v2.1)**: Inicializa el esqueleto del proyecto, forzando la creación del primer `PRP_CONTRACT.json`.
*   **`GLOBAL_SOUL.md`**: El "Alma" de la factoría. Consolida la ética, el minimalismo y el rigor de todos los agentes en un solo lugar.
*   **`COMMUNICATION_PROTOCOL.md`**: Define cómo fluyen los mensajes y las tareas entre agentes (Discovery -> Architecture -> Execution -> QA).
*   **`AGENT_REGISTRY.md`**: El libro de registro oficial que define qué habilidades (Skills) tiene cada agente y qué herramientas MCP puede usar.
*   **`MCP_SENSES_PROTOCOL.md`**: El mapa sensorial de la factoría (qué agentes pueden "ver" la web o "tocar" la base de datos).

---

### 🕹️ Comandos de Poder

*   **`/factory-orchestrate`**: Invoca al Orquestador para mover el tablero Kanban y avanzar de fase.
*   **`/scan` / `/factory-audit`**: Lanza un escaneo agresivo de seguridad y calidad sobre el código producido.

**Filosofía:** *"Moverse rápido de una forma que los agentes del futuro puedan entender, extender y confiar. El sistema debe permanecer estable bajo una evolución multi-agente continua."*
