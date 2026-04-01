# 🎮 Guía de Experiencia de Usuario: Director de Operaciones (v4.0-S)

Con la infraestructura industrial **v4.0-S** activa, dejas de picar código para **gestionar departamentos, aprobar contratos, evaluar métricas financieras y auditar evidencias físicas** en el disco duro.

---

## 🗺️ Mapa de Mando Industrial (Tu Botonera)

Como **Director de Operaciones**, tienes 14 flujos (workflows) en tu arsenal. Úsalos con precisión cronológica:

### ⚡ 1. Comandos de Transición y Estrategia (Macro-Gestión)

*Pedales de aceleración para mover el proyecto entre fases y validar cimientos.*

1. **`/init-contract` (Fase 1 - M1):**
   * **Cuándo:** Tras el briefing inicial con el PRODUCT_OWNER.
   * **Qué hace:** Evalúa la viabilidad financiera (CAC, LTV) mediante `startup-metrics-framework` y sella la conversación creando físicamente el `PRP_CONTRACT.json`. Se usa **una vez** por proyecto.
2. **`/factory-orchestrate` (Transiciones):**
   * **Cuándo:** Para deconstruir el contrato en tareas (M2) o validar si se puede pasar de fase (ej. M2 -> M3).
   * **Qué hace:** Deconstruye especificaciones (`SPEC_LITE.json`) y activa la Aduana Universal.
3. **`/validate-backbone` (Inspector de Andamiaje):**
   * **Cuándo:** Antes de delegar las primeras tareas de código en M3.
   * **Qué hace:** El ORCHESTRATOR verifica físicamente que el esqueleto del framework (Next.js, FastAPI, etc.) exista en el disco para evitar construir en el vacío.

### 🛠️ 2. Comandos Tácticos (Producción)

*Herramientas para la ejecución atómica de tareas.*

1. **`/arch-diagram` (Exclusivo Fase M2):**
   * **Cuándo:** Tras crear las tareas de arquitectura.
   * **Qué hace:** Fuerza el dibujo de planos técnicos (Mermaid) en `DOCS/ARCH/`.
2. **`/execute-task` (El Caballo de Batalla):**
   * **Cuándo:** Siempre que haya tareas en `01_PENDING` (M3).
   * **Qué hace:** Verifica los guardarraíles predictivos en Neo4j y lanza una **Clean Session** aislada para ejecutar una especificación. Es el comando de mayor uso diario.

### 🛂 3. Comandos de Aduana y Calidad (Compliance)

*Inspectores de integridad física y lógica.*

1. **`/scan` (Seguridad):**
   * **Cuándo:** Antes de cerrar tareas de implementación.
   * **Qué hace:** El SECURITY_AUDITOR busca secretos y vulnerabilidades.
2. **`/audit` (Calidad y Métricas SI):**
   * **Cuándo:** Tras un `/scan` limpio.
   * **Qué hace:** El QA_TESTER valida el cumplimiento del contrato en **segundos (s)** y **bytes (B)** y detecta *Cultural Violations*.

### 🚀 4. Comandos de Despliegue y Auto-Sanación (Fase 5: Operaciones)

*Maquinaria pesada para el lanzamiento y curación real.*

1. **`/provision` (Infraestructura):**
   * **Cuándo:** Fase M4 aprobada.
   * **Qué hace:** Prepara Dockerfiles/Terraform en `WORKSPACE/infra/`.
2. **`/deploy` (Lanzamiento):**
   * **Cuándo:** Tras el aprovisionamiento.
   * **Qué hace:** Sube el código al entorno de producción.
3. **`/health-check` (Ojo Sentinel):**
    * **Cuándo:** Con el proyecto "Live".
    * **Qué hace:** Verifica salud y latencia en tiempo real.
4. **`/auto-heal` (Sistema Inmunológico):**
    * **Cuándo:** Si un despliegue falla por bloqueos de red o memoria.
    * **Qué hace:** El DEVOPS_SRE alerta al FACTORY_EVOLVER para que parchee automáticamente la infraestructura.

### 📡 5. Comandos de Monitoreo y Evolución (Radares y Memoria)

*Visibilidad total y persistencia a largo plazo.*

1. **`/sync-memory` (Consolidación LTP):**
    * **Cuándo:** Al finalizar auditorías o despliegues (M4/M5).
    * **Qué hace:** Extrae errores del `FEEDBACK-LOG.md` y los inyecta como nodos de aprendizaje en el Grafo de Neo4j.
2. **`/kanban-board`:** Levanta la interfaz gráfica en puerto 3001.
3. **`/factory-status`:** Reporte de salud, bloqueos y estado de Hubs en texto.

---

## 🏗️ Ciclo de Vida: Guía Paso a Paso

### ⚙️ Fase 0: Ignición (El "Power Grid")

Antes de comandar, preparas la energía vital de la factoría:

1. **Enciendes el Núcleo:** Desde la terminal en `INFRA/`, ejecutas `docker-compose up -d` para levantar Neo4j y la persistencia de datos.
2. **Creas el Cascarón:** Ejecutas `./init_project.sh NombreProyecto`. Esto genera la estructura física de carpetas y establece la **Aduana Universal** en la versión **v4.0-S**.

### 🗣️ Fase 1: El Contrato y Finanzas (Discovery)

Abres **Antigravity** y defines la visión del producto:

1. **Briefing y Finanzas:** Explicas tu idea al **PRODUCT_OWNER**. El Orquestador evalúa el CAC y LTV objetivo.
2. **Sello del PRP:** Comandas `/init-contract`. El agente deposita el `PRP_CONTRACT.json` en la raíz. Este contrato ahora incluye obligatoriamente las métricas de negocio, secciones de **Operations (M5)** y **Evolution (Phase 6)**.

### 🗺️ Fase 2: Hubs, Orquestación Atómica y Andamiaje

Aquí el sistema valida su "maquinaria" y cimientos:

1. **Despiece Técnico:** Escribes `/factory-orchestrate`. El Orquestador deconstruye el contrato en tareas (`SPEC_LITE.json`) en `TASKS/01_PENDING/`.
2. **Prueba de Carga Estructural:** Ejecutas `/validate-backbone` para garantizar que la estructura física (Next.js/Node.js) existe en el disco antes de llamar a los desarrolladores.

### 🏭 Fase 3: Producción Autónoma y Prevención de Errores

La línea de montaje se mueve por la soberanía del disco:

1. **Guardarraíles Preventivos:** Al usar `/execute-task`, el ORCHESTRATOR consulta Neo4j para inyectar reglas anti-alucinación basadas en fallos pasados del framework.
2. **Clean Sessions:** Cada tarea se ejecuta en una sesión aislada, evitando el *token decay*.
3. **Cierre Atómico:** El agente usa el `registry-manager` para mover su tarea a `03_COMPLETED` tras verificar la escritura del código.

### 🛂 Fase 4: Auditoría y Compliance (Rigor SI)

Nada avanza sin pruebas verificables:

1. **Seguridad:** Ejecutas `/scan`. El **SECURITY_AUDITOR** busca secretos y vulnerabilidades.
2. **Calidad:** Ejecutas `/audit`. El **QA_TESTER** valida el cumplimiento, reportando en **segundos (s)** y **bytes (B)** y registrando violaciones arquitectónicas.
3. **Bloqueo DAST:** La **Aduana Universal** impide promocionar el proyecto si falta una sola evidencia (ej. `BUILD_REPORT.json`).

### 🚀 Fase 5: Operaciones, Despliegue y Auto-Sanación (M5)

Activas el **Hub 05_OPERATIONS**:

1. **Aprovisionamiento y Despliegue:** Ejecutas `/provision` seguido de `/deploy`.
2. **Monitoreo Sentinel:** Ejecutas `/health-check`.
3. **Resiliencia Autónoma:** Si el `/deploy` o `/health-check` falla, invocas `/auto-heal`. El sistema creará una Spec de emergencia y reparará los puertos o memoria bloqueada por sí solo.

### 🧬 Fase 6: Evolución de ADN (LTP)

Al terminar, la factoría "aprende" permanentemente:

1. **Consolidación de Memoria:** Ejecutas `/sync-memory` para que el **MEMORY_OPTIMIZER** mande todas las lecciones aprendidas al grafo de Neo4j.
2. **Refactor de Skills:** El **FACTORY_EVOLVER** optimiza las skills en `06_SKILL_LIBRARY/` para futuros proyectos.

---

## 💡 Resumen: Tu Nuevo Rol como Director

* **Corriges Especificaciones, no Código.** Si algo falla, ajustas la `SPEC_LITE.json` y relanzas.
* **Soberanía Física (DAST):** El estado del Kanban es un reflejo exacto del disco.
* **Aprendizaje Perpetuo:** Tu factoría acumula experiencia técnica y financiera que hereda cada nuevo proyecto.

---
*Manual de Operaciones v4.0-S | Director de Operaciones Solidificado*
