# 🎮 Guía de Experiencia de Usuario: Director de Operaciones (v3.4.0-S)

Con la infraestructura industrial **v3.4.0-S** activa, dejas de picar código para **gestionar departamentos, aprobar contratos y auditar evidencias físicas** en el disco duro.

---

## ⚙️ Fase 0: Ignición (El "Power Grid")

Antes de comandar, preparas la energía vital de la factoría:

1. **Enciendes el Núcleo:** Desde la terminal en `INFRA/`, ejecutas `docker-compose up -d` para levantar la Memoria de Largo Plazo (Neo4j) y la persistencia de datos.
2. **Creas el Cascarón:** Ejecutas `./init_project.sh NombreProyecto`. Esto genera la estructura física de carpetas y establece la **Aduana Universal** en Fase M1 (Discovery).

## 🗣️ Fase 1: El Contrato (Discovery)

Abres **Antigravity** y defines la visión del producto:

1. **Briefing:** Explicas tu idea al **PRODUCT_OWNER** en lenguaje natural.
2. **Generación del PRP:** Comandas `/init-contract`. El agente invoca la skill `prp-generator` y deposita un `PRP_CONTRACT.json` en la raíz, que servirá como la "Constitución" del proyecto. Este contrato ahora incluye obligatoriamente las secciones de **Operations (M5)** y **Evolution (Phase 6)**.

## 🗺️ Fase 2: Hubs y Orquestación Atómica

Aquí es donde el sistema valida si tiene la "maquinaria" necesaria:

1. **Validación de Hubs:** El **ORCHESTRATOR** escanea los archivos `TOOLS.md` de cada departamento (01-05) para confirmar que tiene las skills autorizadas antes de proceder.
2. **Despiece Técnico:** Escribes `/factory-orchestrate`. El Orquestador deconstruye el contrato en tareas atómicas (`SPEC_LITE.json`) y las inyecta en `TASKS/01_PENDING/`.

## 🏭 Fase 3: Producción Autónoma (Double-Gating)

La línea de montaje se mueve por la soberanía del disco duro, no por micro-gestión:

1. **Activación por Presencia:** Gracias al **Double-Gating**, un **BACKEND_DEV** o **FRONTEND_DEV** puede iniciar su trabajo en cuanto detecta físicamente su `SPEC_LITE.json` en el disco.
2. **Clean Sessions:** Cada tarea se ejecuta en una sesión aislada para evitar el *token decay* y las alucinaciones por exceso de contexto.
3. **Cierre Atómico:** El agente usa el `registry-manager` para mover su propia tarea a `03_COMPLETED` tras verificar que el código está escrito físicamente.

## 🛂 Fase 4: Auditoría y Compliance

Nada avanza sin pruebas verificables bajo el **Rigor del Sistema Internacional (SI)**:

1. **Escaneo de Seguridad:** Ejecutas `/scan`. El **SECURITY_AUDITOR** busca secretos y vulnerabilidades en el código.
2. **Métricas Industriales:** Ejecutas `/audit`. El **QA_TESTER** valida que el software cumpla con los criterios de éxito, reportando latencias en **segundos (s)** y pesos en **bytes (B)**.
3. **Bloqueo DAST:** La **Aduana Universal** impide promocionar el proyecto si falta una sola evidencia física (ej. `BUILD_REPORT.json`).

## 🚀 Fase 5: Operaciones y Despliegue (M5)

Activas la maquinaria pesada del **Hub 05_OPERATIONS** para llevar el proyecto a la vida real:

1. **Aprovisionamiento:** Ejecutas `/provision`. El **DEVOPS_SRE** prepara la infraestructura física (Docker/Terraform) en `WORKSPACE/infra/`.
2. **Despliegue Atómico:** Ejecutas `/deploy`. El sistema lanza el build validado hacia el entorno de producción.
3. **Monitoreo Sentinel:** Ejecutas `/health-check`. El **DEPLOYMENT_MONITOR** verifica la salud del endpoint en tiempo real, reportando latencia (s) y tamaño de respuesta (B) en `LOGS/deployment/`.

## 🧬 Fase 6: Evolución de ADN (LTP)

Al terminar, la factoría se vuelve más inteligente procesando incluso los datos de despliegue:

1. **Extracción de Engramas:** El **MEMORY_OPTIMIZER** analiza el log de feedback y los logs de despliegue en `LOGS/deployment/` para guardar las "Golden Rules" en el Grafo de Conocimiento (Neo4j).
2. **Refactor de Skills:** El **FACTORY_EVOLVER** utiliza estas reglas para optimizar las skills en `06_SKILL_LIBRARY/`, reduciendo costes y tiempos para el futuro.

---

## 💡 Resumen: Tu Nuevo Rol como Director

* **Corriges Especificaciones, no Código:** Si algo falla, ajustas la `SPEC_LITE.json` y relanzas la tarea. La factoría se encarga del resto.
* **Soberanía Física:** Tienes la paz mental de que el estado del proyecto en el Kanban es un reflejo exacto de lo que hay en tus archivos.
* **Aprendizaje Perpetuo:** Tu factoría no solo entrega software, sino que acumula experiencia técnica que hereda cada nuevo proyecto.

---
*Manual de Operaciones v3.4.0-S | Director de Operaciones Solidificado*
