# 🌉 Integración Antigravity: El Puente IDE (v3.1.5)

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

1.  **Contexto ($TARGET_PROJECT)**: Antigravity inyecta la ruta del proyecto actual como variable de entorno, permitiendo que la factoría sepa exactamente dónde operar.
2.  **Protocolo "Solidity Guard" (v3.1.5)**: Las habilidades de la factoría usan una interfaz estandarizada que garantiza que cada comando ejecutado desde el IDE sea rastreable, seguro y atómico.
3.  **Puente (.agents / .antigravity)**: Traduce las habilidades técnicas en botones, iconos y flujos visuales.
4.  **Usuario**: Orquesta la producción masiva interactuando con agentes inteligentes que entienden tanto el código como la visión de negocio.

> [!TIP]
> Si cambias un icono en `.antigravity/project-config.json`, se actualizará instantáneamente en tu dashboard. Si cambias una instrucción en `.agents/agent.md`, el agente cambiará su comportamiento en la siguiente interacción.

---
