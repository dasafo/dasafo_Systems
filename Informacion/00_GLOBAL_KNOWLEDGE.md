# 🧠 00_GLOBAL_KNOWLEDGE | Cerebro Colectivo (v3.2.0-S)

La carpeta **`00_GLOBAL_KNOWLEDGE`** es el **"Cerebro Colectivo"** o la **Memoria Central** de la factoría. A diferencia del `FEEDBACK-LOG.md` (que registra errores puntuales), esta carpeta contiene las leyes, estándares y definiciones de identidad que son comunes a **TODOS** los proyectos que la factoría ejecute.

Aquí tienes el desglose de para qué sirve cada archivo:

### 🧭 Identidad y Reglas de Negocio

*   **`AGENT_REGISTRY.md` (El Censo de Capacidades):** Define qué puede hacer cada agente, qué herramientas (MCPs) tiene autorizadas y con qué modelo de IA debe ejecutarse (ej: GPT-4o para Backend, Gemini para Research). Es el "listado de empleados" oficial.
*   **`SYSTEM_PROMPTS.md` (El ADN de la IA):** Contiene las plantillas de instrucciones (`prompts`) que se inyectan en cada agente cuando "cobra vida". Asegura que el Orquestador actúe siempre como orquestador y el de Seguridad como un guardián implacable.

### 📐 Estándares de Ingeniería (Numerados por importancia)

*   **`01_CODING_STANDARDS.md` (Calidad de Código):** Define cómo debe escribirse la lógica. Prohíbe nombres de funciones genéricos (como `getData()`), obliga a usar el patrón de "Early Return" y define el sistema de diseño (Atomic Design) para las interfaces.
*   **`02_ARCHITECTURE_RULES.md` (Estructura del Sistema):** Las leyes de separación de capas. Prohíbe mezclar lógica de negocio con la interfaz y define la "Disciplina DTO" (Data Transfer Object) para que los datos viajen de forma segura entre el servidor y el usuario.
*   **`03_SCIENTIFIC_RIGOR.md` (Precisión Física):** Obliga al sistema a trabajar siempre en el Sistema Internacional (SI). Los pesos son kilogramos, las distancias son metros. Prohíbe unidades imperiales para evitar errores catastróficos en proyectos científicos o industriales.
*   **`04_SECURITY_AND_OPS.md` (Seguridad y Despliegue):** Define la política de "Zero Trust". Ningún agente confía en el código del otro. Aquí está la ley de "Chesterton's Fence" (no borrar código sin entender su propósito) y el uso de Docker para que todo sea reproducible en cualquier PC.

### 📈 Métricas y Catálogo

*   **`EVALUATION_METRICS.md` (El Juez de Éxito):** Define cómo medimos si una misión fue exitosa. Evalúa la eficiencia del código, la seguridad y el "Vibe" (la estética y rapidez de la solución).
*   **`CATALOG.md` (Repositorio de Activos):** Un índice de qué proyectos se han hecho y qué "piezas de lego" de código (componentes reutilizables) tiene la factoría disponibles para no inventar la rueda en cada proyecto.

### 🔌 Infraestructura Técnica (El Motor v3.1)

*   **`INFRA/` (Nodo Central de Servicios):** Ubicado en `dasafo_Systems/INFRA`, este nodo centraliza las dependencias pesadas (Neo4j, Postgres, Glances) para toda la factoría. Permite que múltiples proyectos compartan infraestructura de alto rendimiento sin redundancia.
*   **`mcp_agent_factory.py` (La Central MCP):** El servidor que conecta a los agentes con sus habilidades. Es el "cableado" que permite que la IA ejecute código real.
*   **`skill_schema.py` & `skills_runner.md` (El Manual de Habilidades):** Definen cómo se construyen y ejecutan las habilidades (`skills`). Aseguran que cualquier nueva capacidad añadida a la factoría sea compatible con todos los agentes.
*   **`PRP_CONTRACT_TEMPLATE.json` (El Molde de Contratos):** La plantilla maestra para el `PRP_CONTRACT.json`. Garantiza que cada proyecto empiece con objetivos bien definidos.
*   **`SKILLS/` (El Almacén de Habilidades):** Una carpeta que contiene la lógica ejecutable (`run.py`) que todos los agentes comparten. En la **v3.1.5**, todas las habilidades deben seguir el estándar `SkillInput/SkillOutput` y resolver sus rutas de forma dinámica para ser ejecutables desde cualquier punto de la factoría.

---

**En resumen:** Si `dasafo_FACTORY` fuera una empresa real, `00_GLOBAL_KNOWLEDGE` sería el departamento de **Recursos Humanos, el Manual de Procedimientos, el Departamento de Calidad y el Taller de Mantenimiento**, todo en uno. Es lo que garantiza que, aunque uses diferentes IAs, el resultado siempre sea de "Calidad dasafo" y que la factoría sea funcional y autorreparable.
