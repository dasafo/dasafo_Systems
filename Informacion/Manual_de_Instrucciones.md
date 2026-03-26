# 🏛️ ¿Cómo funciona dasafo_Systems? (v3.1.5)

**dasafo_Systems** no es solo una carpeta de archivos; es un **Ecosistema Industrial de IA** diseñado para escalar el desarrollo de software con precisión militar y una estética premium.

El sistema funciona mediante la interacción de dos grandes motores: la **Factoría** y los **Proyectos**.

---

## 1. El Cerebro: `dasafo_FACTORY`
Es el lugar donde residen las **reglas inmutables** y el **motor ejecutivo**.

- **Identidades:** Define el "alma" y los valores de cada agente (ej. el Arquitecto es minimalista, el QA es implacable).
- **Habilidades (Skills):** Son los "módulos de ejecución" funcionales. No son solo texto; contienen lógica real (`run.py`) para realizar tareas (ej. escanear secretos, generar APIs).
- **Protocolos:** Las leyes de física del sistema. Cómo se habla (`COMMUNICATION_PROTOCOL`), cómo se escala (`UNIVERSAL_PIPELINE`) y cómo se aprende de los errores (`FEEDBACK-LOG`).
- **Requisito Técnico v3.1.5:** Todas las habilidades (`run.py`) deben incluir la resolución de ruta `sys.path.insert(0, ...)` para importar `skill_schema` de forma segura en entornos distribuidos.

## 🔒 Industrial Security & Solidity (v3.1.1)
El sistema opera bajo un modelo de "Zero Trust":
- **Acoplamiento Estricto:** No se genera código sin una tarea del Kanban en `02_DONE`.
- **Log-First:** Toda acción crítica debe precederse de una entrada en `/LOGS`.
- **Dead Man's Switch:** El paso a Arquitectura está bloqueado sin firma humana.

## 2. El Vivero de Servicios: `INFRA/`

Ubicado en la raíz de `dasafo_Systems`, este nodo proporciona servicios compartidos de alto rendimiento.

- **Central Knowledge Graph (Neo4j):** Memoria de grafos persistente para todos los proyectos.
- **Relational Hub (Postgres):** Almacenamiento estructurado industrial.
- **Real-time Health (Glances):** Monitoreo centralizado de recursos.

## 3. El Taller: `PROJECTS/`
Es el lugar donde ocurre la **acción mutable**. Cada proyecto es una instancia independiente.

- **WORKSPACE:** Donde vive el código real (backend, frontend, shared).
- **TASKS (Industrial Kanban):** Estructura física numerada para automatización:
    - `01_PENDING`: Misiones en espera.
    - `02_IN_PROGRESS`: Trabajo activo por un agente.
    - `03_COMPLETED`: Tareas validadas por el Auditor.
    - `04_ARCHIVE`: Memoria histórica del proyecto.
    - `05_REJECTED`: Tareas descartadas o duplicadas.
- **LOCAL_KNOWLEDGE:** El diario de investigación, arquitectura y el `SEMANTIC_INDEX.md`.
- **LOGS (Telemetry):** Trazabilidad granular en carpetas:
    - `/agents`: Diálogos y razonamiento.
    - `/sessions`: Trazas de ejecución temporal.
    - `/reports`: Salidas de auditoría y QA.
    - `/incidents`: Registro de fallos y brechas de seguridad.

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

### 🔍 Agentes de "Puerta" vs "Producción"

Aunque la factoría tiene 16 agentes, tú solo interactúas directamente con las **3 Puertas de Acceso** principales para iniciar misiones:

1.  **ORCHESTRATOR** 👑: El director universal. Úsalo cuando tengas una idea general y necesites que la factoría la descomponga en tareas y asigne agentes.
2.  **PRODUCT_OWNER** 📋: El estratega documental. Úsalo cuando ya tengas la visión clara y necesites aterrizarla en un contrato **PRP** ejecutable.
3.  **RESEARCH_AGENT** 🔍: El explorador técnico. Úsalo si antes de planificar nada necesitas investigar la viabilidad tecnológica o el mercado.

*El resto de agentes (Backend, Frontend, DB, QA, etc.) son especializados y suelen ser invocados de forma autónoma por los agentes de cabecera.*

---

### 🕹️ Cómo interactuar con el Sistema

Tú eres el **Director de Orquesta**. Los agentes responden a comandos específicos (Slash Commands) que disparan flujos de trabajo predefinidos. **Nota: Estos comandos son "Anytime Tools" y pueden ejecutarse en cualquier fase del proyecto:**

- **`/factory-orchestrate`** 👑: El comando maestro. Verifica que los JSON de `01_PENDING` se muevan a `03_COMPLETED` siguiendo el pipeline industrial. Úsalo para activar el motor de la factoría.
- **`/scan`** 🛡️: Activa al **Security Auditor** para buscar secretos y vulnerabilidades. Úsalo tras cualquier cambio sensible.
- **`/factory-status`** 📊: Genera un reporte visual del progreso (Kanban y salud de Infraestructura). Úsalo para ver la "foto" actual.
- **`/arch-diagram`** 📐: Solicita al **Architect** diagramas Mermaid actualizados del sistema en tiempo real.
- **`/audit`** 🧪: Pide al **QA_Tester** una revisión exhaustiva de la tarea actual antes de su cierre.

---

### 🚀 Guía de Inicio Rápido: Puesta en Marcha (v3.1)

Para iniciar una misión real en la factoría, sigue estos pasos exactos eligiendo el **Agente de Puerta** adecuado:

1.  **Infraestructura**: Asegúrate de que el nodo central está activo: `cd dasafo_Systems/INFRA && docker-compose up -d`.
2.  **Inicialización**: En `dasafo_FACTORY`, ejecuta `./init_project.sh NombreProyecto`.
3.  **Activación Estratégica**: 
    - **Caso A (Solo Idea General)**: Llama al **ORCHESTRATOR** 👑 para que descomponga la misión.
    - **Caso B (Visión Clara/SaaS)**: Llama directamente al **PRODUCT_OWNER** 📋. Pídele: *"Ejecuta `prp-generator` y rellena el contrato basado en esta visión: [Tu Visión]"*.
    - **Caso C (Duda Técnica)**: Llama al **RESEARCH_AGENT** 🔍 para validar la tecnología antes de planificar.
4.  **Firma del Contrato**: Abre `PROJECTS/NombreProyecto/LOCAL_KNOWLEDGE/PRP_CONTRACT.json`.
    - Revisa los objetivos y el alcance.
    - Cambia `"prp_status": "draft"` → `"signed"`.
    - Pon `"user_approval": true` y la fecha en `validated_at`.
5.  **Despegue Industrial**: Avisa al agente: *"PRP firmado. Continúa con Architecture"*. El **ORCHESTRATOR** tomará el mando automáticamente para mover las tareas en el Kanban.

---
**dasafo_Systems: Construyendo el futuro de la ingeniería autónoma, un commit a la vez.**
