El departamento de **`02_ARCHITECTURE_AND_RESEARCH`** es el "Laboratorio de Ingeniería" de la factoría. Su misión es validar la viabilidad técnica y diseñar los planos estructurales antes de que los desarrolladores empiecen a escribir código.

Aquí tienes el desglose de sus agentes y archivos:

---

### 1. 📐 ARCHITECT (El Jefe de Diseño de Sistemas)
Este agente es el "Gatekeeper" de la calidad estructural. Nadie programa sin que él haya definido los contratos y esquemas.

*   **`IDENTITY.md`**: Define su rol como autoridad en patrones de diseño, escalabilidad y robustez.
*   **`AGENTS.md`**: Un registro de qué otros agentes técnicos necesita coordinar para que la arquitectura se cumpla.
*   **`SOUL.md`**: Su filosofía de "Arquitectura Limpia" (Clean Architecture) y minimalismo técnico.
*   **`SKILLS/`**: 
    *   **`api-contract-generator`**: Crea las especificaciones (como OpenAPI/Swagger) que el Backend y Frontend deben seguir a rajatabla.
    *   **`system-design`**: Capacidad para diseñar diagramas de flujo y arquitectura de servidores.
    *   **`design-token-definition`**: Asegura que los colores y espacios sean consistentes (Atomic Design).
    *   **`architecture-decision-records`**: Mantiene un diario de **por qué** se eligió una tecnología sobre otra.

---

### 2. 🧪 RESEARCH_AGENT (El Científico de Datos y Tecnología)
Su misión es reducir la incertidumbre técnica mediante la investigación profunda y la validación de hechos.

*   **`IDENTITY.md`**: Define su personalidad de investigador meticuloso, escéptico y orientado a los datos.
*   **`BOOTSTRAP.md`**: Instrucciones sobre cómo iniciar una fase de investigación desde cero.
*   **`TOOLS.md`**: Listado de herramientas MCP de búsqueda web y lectura de documentación técnica.
*   **`SKILLS/`**:
    *   **`deep-semantic-search`**: Habilidad para encontrar información no obvia en grandes volúmenes de datos.
    *   **`arxiv-technical-digest`**: Capacidad para leer y resumir papers científicos o técnicos complejos para aplicarlos al proyecto.
    *   **`hallucination-guardrail`**: Un protocolo interno para verificar que lo que está recomendando es real y no una "alucinación" de la IA.

---

### 📂 Estructura Detallada del Departamento

La estructura sigue la norma de la factoría, con carpetas de **SKILLS** que contienen archivos `SKILL.md` individuales para cada capacidad específica. Esto permite que los agentes "carguen" solo el conocimiento que necesitan para la tarea actual, ahorrando recursos y mejorando la precisión.

**En resumen:** En este departamento, el **Research Agent** descubre el "Cómo es posible" y el **Architect** crea el "Plano Maestro" que todos deben seguir. Sin este departamento, la factoría fabricaría software frágil y desordenado.
