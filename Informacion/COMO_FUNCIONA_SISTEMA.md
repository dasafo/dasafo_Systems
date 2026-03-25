# 🏛️ ¿Cómo funciona dasafo_Systems? (v3.1)

**dasafo_Systems** no es solo una carpeta de archivos; es un **Ecosistema Industrial de IA** diseñado para escalar el desarrollo de software con precisión militar y una estética premium.

El sistema funciona mediante la interacción de dos grandes motores: la **Factoría** y los **Proyectos**.

---

## 1. El Cerebro: `dasafo_FACTORY`
Es el lugar donde residen las **reglas inmutables** y el **motor ejecutivo**.

- **Identidades:** Define el "alma" y los valores de cada agente (ej. el Arquitecto es minimalista, el QA es implacable).
- **Habilidades (Skills):** Son los "módulos de ejecución" funcionales. No son solo texto; contienen lógica real (`run.py`) para realizar tareas (ej. escanear secretos, generar APIs).
- **Protocolos:** Las leyes de física del sistema. Cómo se habla (`COMMUNICATION_PROTOCOL`), cómo se escala (`UNIVERSAL_PIPELINE`) y cómo se aprende de los errores (`FEEDBACK-LOG`).

## 2. El Vivero de Servicios: `INFRA/`

Ubicado en la raíz de `dasafo_Systems`, este nodo proporciona servicios compartidos de alto rendimiento.

- **Central Knowledge Graph (Neo4j):** Memoria de grafos persistente para todos los proyectos.
- **Relational Hub (Postgres):** Almacenamiento estructurado industrial.
- **Real-time Health (Glances):** Monitoreo centralizado de recursos.

## 3. El Taller: `PROJECTS/`
Es el lugar donde ocurre la **acción mutable**. Cada proyecto es una instancia independiente.

- **WORKSPACE:** Donde vive el código real del cliente.
- **TASKS:** El sistema de carpetas Kanban (`PENDING`, `IN_PROGRESS`, `COMPLETED`, `ARCHIVE`). El trabajo se mueve físicamente entre estas carpetas.
- **LOCAL_KNOWLEDGE:** El diario de investigación y arquitectura específico de ese proyecto.

---

### 🔄 El Ciclo de Vida: El "Universal Pipeline"

Para que un proyecto sea exitoso en **dasafo_Systems**, debe pasar por este flujo obligatorio:

1.  **Firma del Contrato (PRP):** El usuario y la IA acuerdan el "Qué" (la visión). No se escribe código sin un `PRP_CONTRACT.json` validado.
2.  **Investigación y Planos (Research & Architect):** Los agentes analizan la viabilidad y diseñan los esquemas técnicos. Todo se documenta antes de construir.
3.  **Construcción Atómica (Production):** Los desarrolladores de Backend y Frontend escriben código limpio, tipado y visualmente impresionante.
4.  **Filtro de Seguridad y Calidad (QA & Security):** Cada tarea terminada es auditada para asegurar que no hay secretos expuestos y que los requisitos se cumplen al 100%.
5.  **Lanzamiento (Go-Live):** El equipo de DevOps automatiza el despliegue en contenedores Docker y deja el sistema monitorizado.

---

### 🧠 Memoria Colectiva (AutoShield)

Lo que hace a **dasafo_Systems** único es que el sistema **aprende de sí mismo**.
- Si un agente falla en una tarea, la razón se graba en el `FEEDBACK-LOG.md` de la Factoría.
- Al siguiente segundo, **todos** los agentes de **todos** los proyectos ya saben cómo evitar ese error.

### 🕹️ Cómo interactuar con el Sistema

Tú eres el **Director de Orquesta**.
- Usas el comando `/factory-orchestrate` para avanzar el proyecto.
- Usas el comando `/scan` para auditar la seguridad.
- Los agentes te preguntarán solo en los puntos críticos de decisión (Decision Gates).

---

### 🚀 Guía de Inicio Rápido: Puesta en Marcha (v3.1)

Para iniciar una misión real en la factoría, sigue estos pasos:

1.  **Infraestructura**: Antes de nada, asegúrate de que el nodo central está activo: `cd dasafo_Systems/INFRA && docker-compose up -d`.
2.  **Inicialización**: Desde la carpeta `dasafo_FACTORY`, ejecuta `./init_project.sh NombreProyecto`.
3.  **Selección del Agente**: En tu IDE (Agent Manager), selecciona al **Orchestrator** (icono de router).
4.  **Activación**: Envía el comando `/factory-orchestrate` o solicita: *"Inicia la misión del proyecto [NombreProyecto]"*.
5.  **Validación del Contrato**: Abre el archivo `PROJECTS/NombreProyecto/PRP_CONTRACT.json`, revísalo y firma poniendo el campo `"user_approval": true`.

**¡Listo! La factoría comenzará a trabajar de forma autónoma siguiendo el Universal Pipeline.**

---
**dasafo_Systems: Construyendo el futuro de la ingeniería autónoma, un commit a la vez.**
