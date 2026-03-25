# 🌉 Integración Antigravity: El Puente IDE (v3.1)

Este documento explica cómo la **dasafo_FACTORY** se comunica con el entorno de desarrollo mediante las carpetas ocultas en la raíz del espacio de trabajo. Estas carpetas actúan como la "capa de presentación" y el "sistema de orquestación" para el usuario humano.

---

### 📂 1. `.agents/` — Los Avatares del IDE
Esta carpeta contiene los archivos de definición que Antigravity utiliza para "renderizar" a nuestros agentes en el chat y el dashboard.

-   **Mapeo de Identidad**: Cada archivo (ej. `orchestrator.md`, `architect.md`) vincula un agente visual con su lógica real en `dasafo_Systems/dasafo_FACTORY/`.
-   **Core Origin**: Dentro de estos archivos verás la línea `core_path`, que indica dónde vive el "alma" técnica del agente.
-   **Workflows**: La subcarpeta `.agents/workflows/` contiene los comandos de barra (Slash Commands) como `/scan` o `/orchestrate`. Estos son los gatillos que disparan las **Skills** de la factoría.

---

### 📂 2. `.antigravity/` — El Cerebro de la Interfaz
Aquí reside la configuración maestra de la experiencia de usuario.

-   **`project-config.json`**: Es el archivo que define:
    -   **Nombres e Iconos**: Qué icono de Google Material Design usa cada agente.
    -   **Capacidades**: Habilita la ejecución paralela, las previsualizaciones de artefactos y el modo auto-plan.
    -   **MCP Entry Point**: Define la ruta al servidor MCP de la factoría, permitiendo que las IAs "toquen" el sistema de archivos y la red.

---

### 🔄 El Flujo de Conexión

1.  **Factoría (Core)**: Define las reglas inmutables y las habilidades técnicas.
2.  **Puente (.agents / .antigravity)**: Traduce esas habilidades en botones, iconos y comandos dentro de tu IDE.
3.  **Usuario**: Interactúa con los "Avatares" sin necesidad de conocer la compleja estructura de rutas internas.

> [!TIP]
> Si cambias un icono en `.antigravity/project-config.json`, se actualizará instantáneamente en tu dashboard. Si cambias una instrucción en `.agents/agent.md`, el agente cambiará su comportamiento en la siguiente interacción.

---
