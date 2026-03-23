La carpeta **`.agents/`** es el "Puente Visual" entre el sistema de archivos de tu factoría y la interfaz de Antigravity. Es lo que permite que la factoría deje de ser un conjunto de scripts invisibles y se convierta en un equipo táctico seleccionable.

Aquí tienes el desglose de lo que hace cada archivo en esta ubicación:

---

### 🧥 Los Perfiles Nativos (Archivos `.md`)

Cada archivo en la raíz de `.agents/` (ej: `orchestrator.md`, `backend_dev.md`, `security_auditor.md`) actúa como un **Embajador de la Factoría**. 

1.  **Mapeo de Identidad**: Estos archivos le dicen a Antigravity: *"Existe un agente llamado @orchestrator y sus instrucciones maestras están en la carpeta dasafo_FACTORY"*.
2.  **Referencia Cruzada**: Conectan el perfil de chat con las habilidades (`SKILLS`) y herramientas (`TOOLS`) que definimos en la estructura interna.
3.  **Selector de IA**: Permiten que el usuario elija qué "empleado" de la factoría quiere invocar en el chat para una tarea específica.

---

### ⚡ Los Workflows (Directorio `workflows/`)

Esta es la parte más potente para el usuario. Contiene los **Comandos Especiales** o "Atajos de Acción" que puedes escribir directamente en el chat.

*   **`factory-orchestrate.md` (Comando `/factory-orchestrate`)**:
    *   **¿Qué hace?**: Invoca al Orquestador para que analice el estado del proyecto, mueva las piezas del tablero Kanban (las carpetas `01_PENDING`, `02_IN_PROGRESS`, etc.) y genere la siguiente fase de desarrollo.
    *   **Uso**: Es el botón de "Play" para avanzar en el desarrollo.

*   **`factory-audit.md` (Comando `/factory-audit`)**:
    *   **¿Qué hace?**: Activa inmediatamente al Auditor de Seguridad y al QA Tester para que escaneen todo el código en la carpeta `03_COMPLETED`.
    *   **Uso**: Es el "Botón de Pánico" o de control de calidad antes de dar por terminado un hito.

---

### 🔗 La Relación con `dasafo_FACTORY`

Mientras que `dasafo_FACTORY` contiene el **conocimiento profundo** y los **scripts técnicos**, la carpeta `.agents/` contiene la **interfaz de usuario**. 

*   **`dasafo_FACTORY`** = El Motor bajo el capó.
*   **`.agents/`** = El Volante, la Palanca de Cambios y el Salpicadero.

**En resumen:** Esta carpeta es el panel de control. Gracias a estos archivos, puedes dar órdenes complejas a la factoría usando comandos sencillos como `/factory-orchestrate` en lugar de tener que gestionar carpetas y archivos manualmente. Es el paso final que hace que tu sistema sea **Híbrido y Visual**.
