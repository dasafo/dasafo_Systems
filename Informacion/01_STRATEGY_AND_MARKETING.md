# 🧭 01_STRATEGY_AND_MARKETING | Departamento de Estrategia (v3.1.5)

Este departamento es el **Timón** de la factoría. Se encarga de la captura de requisitos, la orquestación de tareas y el crecimiento estratégico del producto.

---

### 🤖 Agentes Clave

#### 1. PRODUCT_OWNER (El Guardián del Valor)
Su misión es traducir la visión del usuario en un backlog técnico ejecutable.
*   **Responsabilidad v3.1:** Es el dueño del **PRP Validation Gate**. No permite que el proyecto pase a la fase de Arquitectura hasta que el contrato de visión esté firmado y se hayan validado las cuotas de infraestructura en el nodo compartido.
*   **Habilidades:** Auditoría de valor, análisis de requisitos y gestión de stakeholders.

#### 2. ORCHESTRATOR (El Motor de Ingesta)
Es el enrutador semántico. Convierte intenciones en lenguage natural en grafos de tareas (DAG).
*   **Misión:** Analiza el estado del proyecto y dispara tareas a las carpetas `PENDING` correspondientes.
*   **Comando Maestro:** Controla el flujo del comando `/factory-orchestrate`.

#### 3. MARKETING_GROWTH (El Arquitecto de Crecimiento)
Diseña estrategias de salida al mercado basadas en datos reales.
*   **Habilidades:** Análisis de tendencias con Apify, redacción persuasiva basada en evidencia (Evidence-based copywriting) y estrategias de contenido social.

### 🚀 Motor de Ejecución (Skills v3.1)

Este departamento no solo piensa, sino que ejecuta a través de sus habilidades (`skills`):

*   **`prp-generator` & `prp-validation-gate` (PRODUCT_OWNER):** El sistema de doble llave para la creación y validación de contratos de misión.
*   **`dag-routing` & `task-dependency-diagnostic` (ORCHESTRATOR):** Motores de descomposición de tareas y diagnóstico de cuellos de botella semánticos.
*   **`ra-agile-orchestration` (ORCHESTRATOR):** Sistema de escalado de agentes basado en hitos del proyecto.
*   **`evidence-based-copywriting` (MARKETING_GROWTH):** Redacción persuasiva v3.1.5 validada por datos de mercado reales.

---

### 📜 Protocolos de Estrategia

- **Validación PRP:** El documento `PRP_CONTRACT.json` en el proyecto es la biblia. Si no está validado, el departamento bloquea la ejecución para evitar "Vibe Drift".
- **Kanban Físico:** Las tareas se mueven físicamente entre las carpetas del proyecto (`01_PENDING` -> `02_IN_PROGRESS` -> `03_COMPLETED`).
- **Feedback Loop:** La estrategia se ajusta si el `FEEDBACK-LOG.md` detecta que los requisitos originales eran técnicamente inviables.

---
*Este departamento asegura que la factoría no solo construya cosas, sino que construya las cosas correctas.*
