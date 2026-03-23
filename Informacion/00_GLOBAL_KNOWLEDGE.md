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

---

**En resumen:** Si `dasafo_FACTORY` fuera una empresa real, `00_GLOBAL_KNOWLEDGE` sería el departamento de **Recursos Humanos, el Manual de Procedimientos y el Departamento de Calidad**, todo en uno. Es lo que garantiza que, aunque uses diferentes IAs, el resultado siempre sea de "Calidad dasafo".
