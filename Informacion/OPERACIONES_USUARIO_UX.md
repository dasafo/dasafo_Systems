# 🎮 Guía de Experiencia de Usuario: Director de Operaciones (v4.0-S)

Con la infraestructura industrial **v4.0-S** activa, dejas de picar código para **gestionar departamentos, aprobar contratos y auditar evidencias físicas** en el disco duro.

---

## 🗺️ Mapa de Mando Industrial (Tu Botonera)

Como **Director de Operaciones**, tienes 11 flujos (workflows) en tu arsenal. Úsalos con precisión cronológica:

### ⚡ 1. Comandos de Transición (Macro-Gestión)
*Pedales de aceleración para mover el proyecto entre fases.*

1. **`/init-contract` (Fase 1 - M1):**
   * **Cuándo:** Tras el briefing inicial con el PRODUCT_OWNER.
   * **Qué hace:** Sella la conversación creando físicamente el `PRP_CONTRACT.json`. Se usa **una vez** por proyecto.
2. **`/factory-orchestrate` (Transiciones):**
   * **Cuándo:** Para deconstruir el contrato en tareas (M2) o validar si se puede pasar de fase (ej. M2 -> M3).
   * **Qué hace:** Deconstruye especificaciones (`SPEC_LITE.json`) y activa la Aduana Universal.

### 🛠️ 2. Comandos Tácticos (Producción)
*Herramientas para la ejecución atómica de tareas.*

3. **`/arch-diagram` (Exclusivo Fase M2):**
   * **Cuándo:** Tras crear las tareas de arquitectura.
   * **Qué hace:** Fuerza el dibujo de planos técnicos (Mermaid) en `DOCS/ARCH/`.
4. **`/execute-task` (El Caballo de Batalla):**
   * **Cuándo:** Siempre que haya tareas en `01_PENDING` (M3).
   * **Qué hace:** Lanza una **Clean Session** aislada para ejecutar una especificación. Es el comando de mayor uso diario.

### 🛂 3. Comandos de Aduana y Calidad (Compliance)
*Inspectores de integridad física y lógica.*

5. **`/scan` (Seguridad):**
   * **Cuándo:** Antes de cerrar tareas de implementación.
   * **Qué hace:** El SECURITY_AUDITOR busca secretos y vulnerabilidades.
6. **`/audit` (Calidad y Métricas SI):**
   * **Cuándo:** Tras un `/scan` limpio.
   * **Qué hace:** El QA_TESTER valida el cumplimiento del contrato en **segundos (s)** y **bytes (B)**.

### 🚀 4. Comandos de Despliegue (Fase 5: Operaciones)
*Maquinaria pesada para el lanzamiento real.*

7. **`/provision` (Infraestructura):**
   * **Cuándo:** Fase M4 aprobada.
   * **Qué hace:** Prepara Dockerfiles/Terraform en `WORKSPACE/infra/`.
8. **`/deploy` (Lanzamiento):**
   * **Cuándo:** Tras el aprovisionamiento.
   * **Qué hace:** Sube el código al entorno de producción.
9. **`/health-check` (Ojo Sentinel):**
   * **Cuándo:** Con el proyecto "Live".
   * **Qué hace:** Verifica salud y latencia en tiempo real.

### 📡 5. Comandos de Monitoreo (Radares)
*Visibilidad total sin alterar archivos.*

10. **`/kanban-board`:** Levanta la interfaz gráfica en puerto 3001.
11. **`/factory-status`:** Reporte de salud, bloqueos y estado de Hubs en texto.

---

## 🏗️ Ciclo de Vida: Guía Paso a Paso

### ⚙️ Fase 0: Ignición (El "Power Grid")

Antes de comandar, preparas la energía vital de la factoría:

1. **Enciendes el Núcleo:** Desde la terminal en `INFRA/`, ejecutas `docker-compose up -d` (`sudo systemctl start docker` primero si es necesario) para levantar Neo4j y la persistencia de datos.
2. **Creas el Cascarón:** Ejecutas `./init_project.sh NombreProyecto`. Esto genera la estructura física de carpetas y establece la **Aduana Universal** en Fase M1 (Discovery).

### 🗣️ Fase 1: El Contrato (Discovery)
Abres **Antigravity** y defines la visión del producto:
1. **Briefing:** Explicas tu idea al **PRODUCT_OWNER**.
2. **Sello del PRP:** Comandas `/init-contract`. El agente deposita el `PRP_CONTRACT.json` en la raíz. Este contrato ahora incluye obligatoriamente las secciones de **Operations (M5)** y **Evolution (Phase 6)**.

### 🗺️ Fase 2: Hubs y Orquestación Atómica
Aquí el sistema valida su "maquinaria":
1. **Validación de Hubs:** El **ORCHESTRATOR** escanea los `TOOLS.md` de cada departamento (01-05) para confirmar skills autorizadas.
2. **Despiece Técnico:** Escribes `/factory-orchestrate`. El Orquestador deconstruye el contrato en tareas (`SPEC_LITE.json`) en `TASKS/01_PENDING/`.

### 🏭 Fase 3: Producción Autónoma (Double-Gating)
La línea de montaje se mueve por la soberanía del disco:
1. **Activación por Presencia:** Gracias al **Double-Gating**, un desarrollador puede iniciar su trabajo en cuanto detecta su `SPEC_LITE.json` física.
2. **Clean Sessions:** Cada tarea (ej. mediante `/execute-task`) se ejecuta en una sesión aislada, evitando el *token decay*.
3. **Cierre Atómico:** El agente usa el `registry-manager` para mover su tarea a `03_COMPLETED` tras verificar la escritura del código.

### 🛂 Fase 4: Auditoría y Compliance (Rigor SI)
Nada avanza sin pruebas verificables:
1. **Seguridad:** Ejecutas `/scan`. El **SECURITY_AUDITOR** busca secretos y vulnerabilidades.
2. **Calidad:** Ejecutas `/audit`. El **QA_TESTER** valida el cumplimiento, reportando en **segundos (s)** y **bytes (B)**.
3. **Bloqueo DAST:** La **Aduana Universal** impide promocionar el proyecto si falta una sola evidencia (ej. `BUILD_REPORT.json`).

### 🚀 Fase 5: Operaciones y Despliegue (M5)
Activas el **Hub 05_OPERATIONS**:
1. **Aprovisionamiento:** Ejecutas `/provision`. El **DEVOPS_SRE** prepara Docker/Terraform en `WORKSPACE/infra/`.
2. **Despliegue Atómico:** Ejecutas `/deploy`. El sistema lanza el build validado al entorno real.
3. **Monitoreo Sentinel:** Ejecutas `/health-check`. El **DEPLOYMENT_MONITOR** verifica latencia (s) y tamaño (B) en `LOGS/deployment/`.

### 🧬 Fase 6: Evolución de ADN (LTP)
Al terminar, la factoría "aprende":
1. **Extracción de Engramas:** El **MEMORY_OPTIMIZER** analiza logs de feedback y de despliegue para guardar "Golden Rules" en Neo4j.
2. **Refactor de Skills:** El **FACTORY_EVOLVER** optimiza las skills en `06_SKILL_LIBRARY/` para futuros proyectos.

---

## 💡 Resumen: Tu Nuevo Rol como Director

* **Corriges Especificaciones, no Código.** Si algo falla, ajustas la `SPEC_LITE.json` y relanzas.
* **Soberanía Física (DAST):** El estado del Kanban es un reflejo exacto del disco.
* **Aprendizaje Perpetuo:** Tu factoría acumula experiencia técnica que hereda cada nuevo proyecto.

---
*Manual de Operaciones v4.0-S | Director de Operaciones Solidificado*
