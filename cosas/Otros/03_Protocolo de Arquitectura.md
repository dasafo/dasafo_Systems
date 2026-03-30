Protocolo de Arquitectura: Gestión de Memoria Persistente y Optimización de Contexto

1. Fundamentos y Diagnóstico de la Ventana de Contexto

En el ecosistema actual de la ingeniería de software asistida por modelos de lenguaje de gran escala (LLM), la ventana de contexto ha pasado de ser una limitación de capacidad a un desafío de gestión estratégica. Como arquitectos, debemos rechazar la falacia de que "más contexto es mejor". La realidad técnica dicta que el rendimiento de un modelo se degrada proporcionalmente al ruido introducido en su ventana de trabajo; un contexto saturado no es un activo, es un pasivo técnico que induce alucinaciones y omisiones críticas.

El Fracaso de la Compactación Tradicional

La industria ha intentado mitigar la saturación mediante la "compactación" (compaction) o resumen automático. Este enfoque es inherentemente defectuoso por las siguientes razones:

* Pérdida de Fidelidad Arquitectónica: El resumen tiende a eliminar los "porqués" detrás de una decisión de diseño, conservando solo el "qué", lo que destruye la trazabilidad técnica.
* Ruido en Ventanas Masivas: Incluso en modelos con ventanas de 1M de tokens (como Gemini), el fenómeno de "lost in the middle" persiste. El ruido acumulado diluye la atención del modelo sobre las reglas de negocio específicas.

Diagnóstico de Soluciones Industriales Actuales

* RAG (Retrieval-Augmented Generation): Aunque estándar, resulta excesivamente pesado y costoso para la iteración rápida de código, requiriendo infraestructuras de embeddings que añaden latencia.
* Fine-tuning: Demasiado estático. Un modelo reentrenado hoy queda obsoleto con el refactor de mañana.
* Consumo Lineal: Leer archivos completos en cada prompt satura la ventana en pocos turnos, forzando ciclos de compactación prematuros.

Este protocolo propone una transición hacia una arquitectura de capas de memoria orgánica y delegación agéntica, donde el contexto se gestiona con precisión quirúrgica.


--------------------------------------------------------------------------------


2. Implementación de la Capa de Memoria 'Engram'

La capa Engram es un sistema de persistencia experimental diseñado para permitir que la IA aprenda de forma orgánica. No se trata de una base de datos estática, sino de un "sustrato factual" que inyecta conocimiento relevante en el momento preciso.

Arquitectura Técnica y "Sorting por Rareza"

A diferencia de los sistemas RAG tradicionales, Engram utiliza un servidor ligero en Go y SQLite con capacidades de búsqueda de texto completo (FTS). Su innovación radica en el Sorting por Rareza:

* El "Porqué": Los patrones comunes (boilerplate, sintaxis estándar) son ruidosos y de poco valor. Los patrones "raros" representan las decisiones arquitectónicas únicas, los identificadores específicos del proyecto y la lógica de negocio particular. Al priorizar la rareza, Engram actúa como un proxy semántico de baja latencia que recupera la esencia del proyecto sin el peso de una base de datos vectorial.

Memoria Orgánica (Zero-Intervention)

El sistema opera bajo un protocolo de "Intervención Cero". El desarrollador no ejecuta comandos de guardado. Mediante el uso de herramientas como el Model Context Protocol (MCP), el agente identifica autónomamente una "Observación" (ej. "Tailwind 4 no requiere archivo de configuración .js en este entorno") y la commitea a la capa SQLite. Esto permite que el conocimiento persista entre sesiones sin intervención manual.

Comparativa de Eficiencia de Contexto:

Método de Gestión	Uso de Ventana de Contexto	Estado de Precisión
Lectura de Archivos (Legacy)	100%	Degradación crítica / Ruido alto
Compactación (Resumen)	40% - 60%	Pérdida de detalle arquitectónico
Arquitectura Engram	~4%	Nitidez máxima (Pristine)


--------------------------------------------------------------------------------


3. Arquitectura de Subagentes y Orquestación Dinámica

Para mantener la integridad del hilo de ejecución, implementamos una jerarquía de "Capataz y Peones" (Orchestrator & Subagents), fundamentada en el aislamiento de contexto.

El Orquestador (Capataz) y el Protocolo "Clean Slate"

El Orquestador mantiene el hilo conductor y la visión estratégica. Bajo este protocolo, el Orquestador tiene prohibido leer archivos directamente. Su contexto debe permanecer "pristino" para evitar la saturación. Su única función es delegar.

Subagentes (Peones): Unidades de Ejecución Desechables

Cada tarea se delega a un subagente en una sesión independiente. Aplicamos el principio de "Sesión nueva, vida nueva":

* Aislamiento de Ruido: Al ser unidades efímeras, los subagentes operan sin el historial de chat acumulado, lo que garantiza una implementación de código limpia y precisa.
* Delegación Dinámica: El subagente recibe la instrucción, ejecuta y devuelve un resumen al Orquestador, muriendo tras la tarea.

Selección Estratégica de Modelos

La eficiencia de costos y razonamiento se logra mediante la orquestación multi-modelo:

* Gemini 1.5 Pro: Preferido para las fases de Exploración y Planificación debido a su inigualable ratio de razonamiento/costo en ventanas grandes.
* Claude 3.5 Opus: Reservado exclusivamente para Razonamiento Estructural de Alto Nivel y resolución de conflictos arquitectónicos complejos.
* Claude 3.5 Sonnet / GPT-4o: Los "workhorses" para la Implementación y Debugging, donde la velocidad y la precisión sintáctica son primordiales.


--------------------------------------------------------------------------------


4. Protocolo de Gestión y Registro de 'Skills'

Las Skills son capacidades modulares (herramientas) que los agentes cargan bajo demanda. El Skill Registry actúa como un catálogo centralizado para evitar el "sobrecalentamiento" del contexto mediante la carga perezosa (lazy loading).

* Segmentación del Conocimiento: Prescribimos el uso de archivos .enmd específicos por dominio. Un subagente trabajando en la carpeta /ui solo cargará las skills de componentes y estilos, ignorando la lógica de /api. Esto elimina la posibilidad de que el agente intente aplicar patrones de servidor en el cliente.
* Carga Dinámica: El subagente consulta en Engram qué habilidades requiere antes de ejecutarlas, asegurando que solo el herramental necesario ocupe espacio en su memoria activa.


--------------------------------------------------------------------------------


5. Ciclo de Trabajo SDD (Spec Driven Development)

El framework SDD transforma el "Vibe Coding" en ingeniería de software rigurosa. Engram actúa aquí como el repositorio de especificaciones, eliminando la necesidad de archivos temporales.

Las 9 Fases del Flujo SDD:

1. Inicialización: Definición de objetivos.
2. Exploración: Análisis del terreno (codebase).
3. Propuesta: Solución conceptual.
4. Especificación: Documentación técnica en Engram.
5. Diseño: Arquitectura de componentes.
6. Tareas: Desglose atómico de trabajo.
7. Implementación: Codificación (preferiblemente TDD).
8. Verificación (Guardian Angel): Aquí es donde el Guardian Angel (GGA) valida el código contra "desviaciones culturales". Engram provee la memoria cultural para detectar si un archivo está en la carpeta incorrecta o si viola una norma de nomenclatura interna que un linter estándar ignoraría.
9. Resumen: Consolidación de aprendizajes en la capa de memoria persistente.


--------------------------------------------------------------------------------


6. Sincronización, Exportación y Mitigación de Deuda de Contexto

El valor estratégico de este protocolo reside en la eliminación de la "Deuda de Contexto" y el "Impuesto de Onboarding".

Protocolo de Sincronización (engram sync)

La memoria del proyecto no debe morir con la sesión del desarrollador. El comando engram sync genera un Manifiesto Contextual:

* Contextual Manifest: Un archivo comprimido que contiene las observaciones, decisiones y bugs históricos.
* Eliminación del "Yo del Pasado": Al importar un manifiesto de Engram, un nuevo desarrollador (o una IA en una nueva sesión) hereda instantáneamente meses de contexto arquitectónico. La IA ya "sabe" por qué se eligió una librería específica o qué errores evitar, eliminando las semanas de fricción inicial.

Visión de Memoria Corporativa

Aspiramos a un Servidor de Engram centralizado. En este paradigma, la memoria del proyecto es un activo compartido en la nube, permitiendo una sincronización en tiempo real de la "intuición" agéntica entre todos los miembros del equipo.

Al implementar este protocolo, trascendemos las limitaciones físicas de los LLM, construyendo un sistema donde la IA no solo asiste, sino que evoluciona junto con el proyecto de forma profesional, estructurada y, sobre todo, persistente.

