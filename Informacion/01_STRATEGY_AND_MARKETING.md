El departamento de **`01_STRATEGY_AND_MARKETING`** es el "Centro de Mando" de la factoría. Aquí no se escribe código, sino que se definen los objetivos, se planifican las tareas y se diseña la estrategia de crecimiento.

Aquí tienes el desglose de lo que hace cada agente y sus archivos:

---

### 1. 🏗️ ORCHESTRATOR (El Director de Operaciones)
Es el agente más crítico. Su misión es leer el estado del proyecto y decidir qué agente debe trabajar a continuación, creando las tareas JSON necesarias.

*   **`IDENTITY.md`**: Define su personalidad de gestor eficiente y su capacidad para ver el proyecto de forma global. Es el que aplica el Ciclo TEA.
*   **`TOOLS.md`**: Lista las herramientas permitidas para mover archivos entre carpetas de tareas y validar el pipeline.
*   **`SKILLS/`**: 
    *   **`dag-routing`**: Capacidad para crear grafos de tareas (que la tarea B no empiece hasta que la A esté lista).
    *   **`structured-system-design`**: Habilidad para estructurar misiones complejas en pasos lógicos.

---

### 2. 👑 PRODUCT_OWNER (El Dueño de la Visión)
Es el puente entre tus deseos como usuario y la ejecución técnica. Se encarga de que el producto final sea realmente lo que necesitas.

*   **`IDENTITY.md`**: Define su enfoque en el valor de negocio y la experiencia de usuario (UX).
*   **`SOUL.md`**: Contiene la "filosofía de producto" específica de este rol (calidad sobre cantidad).
*   **`HEARTBEAT.md`**: Un registro de cómo evoluciona la visión del producto a lo largo del tiempo.
*   **`SKILLS/`**:
    *   **`requirements-analysis-framework`**: Metodología para desglosar tus ideas en requisitos técnicos claros.

---

### 3. 📈 MARKETING_GROWTH (El Estratega de Crecimiento)
Este agente entra en juego para que el proyecto no solo funcione, sino que tenga éxito en el mercado.

*   **`IDENTITY.md`**: Su perfil de experto en marketing digital, psicología del consumidor y analítica.
*   **`USER.md`**: Información específica sobre el público objetivo al que se dirige el proyecto.
*   **`TEMPLATE_growth_strategy.md`**: La estructura que sigue para crear planes de marketing coherentes.
*   **`SKILLS/`**:
    *   **`social-content-strategy`**: Planificación de contenido para redes sociales.
    *   **`evidence-based-copywriting`**: Redacción de textos persuasivos basados en datos, no en suposiciones.

---

### 📂 Estructura Común de Archivos en los Agentes
Casi todos los agentes comparten estos archivos:

1.  **`IDENTITY.md`**: El "Quién soy" de la IA.
2.  **`TOOLS.md`**: El "Con qué trabajo" (herramientas MCP específicas).
3.  **`SKILLS/`**: El "Qué sé hacer" (instrucciones detalladas de procedimientos específicos).
4.  **`USER.md` / `SOUL.md`**: El "Para quién trabajo" y el "Bajo qué valores".

**En resumen:** En esta carpeta, el **Product Owner** define el "Qué", el **Marketing Growth** el "Para Quién" y el **Orchestrator** el "Cuándo y por Quién" se ejecuta cada paso. Es la capa pensante antes de la acción.
