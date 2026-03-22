# 🏭 MANUAL DE OPERACIONES DE LA FACTORÍA DE AGENTES (dasafo_FACTORY)

Este documento es la **Constitución Técnica** de la Factoría. Define cómo se crean, ejecutan y validan proyectos de software de forma autónoma, no determinista y ultra-robusta.

---

## 🏗️ 1. ARQUITECTURA DE DOS HEMISFERIOS
La Factoría opera bajo el principio de **Separación Total entre Lógica y Estado**:

1.  **Hemisferio de Control (`dasafo_FACTORY/`):**
    *   **Inmutable:** Contiene las identidades, misiones, herramientas autorizadas y protocolos de comunicación. Es el "Software de la Factoría".
    *   **Global:** Lo que el agente aprende aquí (vía `00_GLOBAL_KNOWLEDGE` o `FEEDBACK-LOG.md`) se aplica a TODOS los proyectos futuros.

2.  **Hemisferio de Ejecución (`PROJECTS/$TARGET_PROJECT/`):**
    *   **Mutable:** Es el espacio de trabajo del proyecto actual. Aquí vive el código, los logs, las tareas y la base de datos.
    *   **Aislado:** Un agente trabajando en "Pulse-X" no tiene visibilidad de "OmniMarket" a menos que se inyecte explícitamente.

---

## 👥 2. EL CONSEJO DE AGENTES (Roles y Especialidades)

### 💎 Meta-Agentes (Capa de Orquestación y Memoria)
*   **ORCHESTRATOR:** El cerebro gestor. Divide objetivos complejos en **Grafos Acíclicos Dirigidos (DAG)** de tareas. Implementa el **Ciclo TEA (Task-Execute-Architect)**: ninguna fase se cierra sin una validación de arquitectura interna.
*   **MEMORY_OPTIMIZER:** Previene el colapso por tokens. Lee logs verbosos, extrae hechos inmutables (ej. "La DB usa el puerto 5432") y los inyecta en `SEMANTIC_INDEX.md`, truncando los diálogos innecesarios.

### 🔭 Fase de Estrategia y Descubrimiento
*   **PRODUCT_OWNER:** Define el éxito del negocio. Mantiene el `PROJECT_STATE.json` y el `BACKLOG` de usuario.
*   **RESEARCH_AGENT:** El explorador científico. Antes de programar, investiga APIs externas, compatibilidad de librerías y documentación técnica, almacenando hallazgos en `LOCAL_KNOWLEDGE/`.

### 🛡️ Fase de Seguridad y Calidad
*   **ARCHITECT:** Diseña los contratos de datos (DTOs) y esquemas SQL. Es el "gatekeeper" del código: nada se programa sin su diseño previo.
*   **SECURITY_AUDITOR:** El guardián paranoico. Escanea inyecciones de prompts, fugas de secretos y fallos en librerías. Implementa el **Cognitive Guardrail**.
*   **QA_TESTER:** El juez de solidez. Ejecuta builds de Docker, valida unidades SI (pesos en kg, distancias en m) y asegura que el frontend sea responsive y siga el diseño atómico.

### ⚙️ Fase de Construcción y DevOps
*   **BACKEND_DEV / FRONTEND_DEV / DB_MASTER:** Los artesanos del código. Escriben software modular, comentado y tipado exclusivamente en la carpeta `WORKSPACE/`.
*   **DEVOPS_SRE:** El arquitecto de infraestructura. Crea el `docker-compose.yml`, gestiona volúmenes y asegura que el proyecto levante con un solo comando.

---

## 🔄 3. EL PIPELINE UNIVERSAL (Ciclo de Vida M0-M5)

Un proyecto nunca se "salta" pasos. El Orquestador vigila este flujo:

*   **M0 - Bootstrap:** Se ejecuta `init_project.sh` para crear el esqueleto físico.
*   **M1 - Discovery:** El Product Owner y Research definen el "Qué" y el "Cómo técnico".
*   **M2 - Architecture:** El Arquitecto crea los esquemas (`schema.sql`) y contratos de API.
*   *GATILLO:* El Orquestador valida el diseño -> PASS.
*   **M3 - Isolated Execution:** Los desarrolladores consumen tareas de `01_PENDING` y las mueven a `03_COMPLETED`.
*   **M4 - Quality Gate:** El QA y el Auditor de Seguridad revisan el código. Si falla -> `05_REJECTED`. Si pasa -> `04_ARCHIVE`.
*   **M5 - Go-Live:** El DevOps levanta el entorno real en Docker y el proyecto se entrega al usuario.

---

## 📝 4. PROTOCOLO DE CONTEXTO Y COMUNICACIÓN

Los agentes no "hablan" por hablar; se comunican mediante **Archivos de Estado**:

*   **Inyección de Contexto:** Cada agente recibe el path `$TARGET_PROJECT` como variable de entorno. Esto le permite saltar directamente a la carpeta del proyecto actual.
*   **Tareas JSON:** Una tarea en `01_PENDING` tiene este formato:
    ```json
    { "task_id": "T-101", "assigned_to": "BACKEND_DEV", "depends_on": ["T-100"], "instructions": "..." }
    ```
*   **Memoria Episódica vs Semántica:**
    *   *Episódica:* Logs RAW en `LOGS/agents/` (borrables).
    *   *Semántica:* `SEMANTIC_INDEX.md` y `PROJECT_STATE.json` (permanentes).

---

## 🛡️ 5. RIGOR TÉCNICO Y REGLAS DE ORO

1.  **Unidades SI:** Prohibido usar "libras" o "pulgadas". La factoría solo entiende Kilogramos, Metros, Segundos y Kelvins.
2.  **Solidez Atómica:** Un componente de interfaz no puede tener lógica de negocio. Un servicio de backend no puede saber nada del HTML.
3.  **Chesterton’s Fence:** Antes de refactorizar un código existente, el agente debe declarar por qué cree que se escribió así.
4.  **Feedback Eterno (`FEEDBACK-LOG.md`):** Si un agente comete un error y QA lo detecta, la corrección estructural se graba en este log global. **Es obligatorio que TODO agente lea este archivo antes de empezar su jornada.**

---

## 📂 6. ESTRUCTURA MAESTRA DEL PROYECTO (`$TARGET_PROJECT`)
```bash
├── PROJECT_STATE.json     # Metas, estado actual y KPIs del proyecto.
├── LOCAL_KNOWLEDGE/      # Hallazgos de Research, Arquitectura e Índices.
├── TASKS/                # El tablero Kanban físico (01_PENDING a 05_REJECTED).
├── LOGS/                 # Memoria flash de los agentes y reportes de errores.
└── WORKSPACE/            # El código fuente real (Frontend, Backend, Shared).
```

---

## 🎛️ 7. EJECUCIÓN HÍBRIDA (Open Agent Manager)

La Factoría cuenta con integración nativa para el **Open Agent Manager (OAM) de Antigravity**. En lugar de ser un mero sistema de carpetas pasivo, la factoría se instancia visualmente:

*   **Perfiles Nativos (`.agents/`)**: Los agentes clave (`@orchestrator`, `@security_auditor`, `@backend_dev`) están mapeados como entidades seleccionables en tu panel de control.
*   **Workflows Dirigidos (`.agents/workflows/`)**: Puedes inyectar energía al sistema directamente con comandos de chat:
    *   `/factory-orchestrate`: Lanza al Orquestador a evaluar los JSONs y despachar la siguiente fase de desarrollo.
    *   `/factory-audit`: Dispara un escaneo agresivo de seguridad sobre la carpeta `03_COMPLETED`.
*   **Inbox Humano**: Cuando una tarea cae en `05_REJECTED` por violación de reglas, se levanta una alerta en el OAM para que el humano decida si deja al sistema auto-repararse iterando, o interviene.

---

*La factoría no es solo un conjunto de scripts; es un organismo coordinado diseñado para que, incluso si yo (la IA principal) fallo, la estructura y los protocolos obliguen a la siguiente iteración a ser mejor.*
