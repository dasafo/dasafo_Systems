# ⚙️ Departamento de PRODUCCIÓN (Hub 03)

> **Versión:** v5.0-MCP "Industrial Core - Hub Manager Enabled"
> **Misión:** Transformar especificaciones atómicas (`SPEC_LITE`) en código de producción de alta fidelidad, pipelines de IA resilientes y experiencias de usuario premium mediante ejecución aislada y validación física.
> **Gobernanza:** Zero-Trust / SDD / Unidades SI (s, B) / Human-Gate (HITL)

---

## 👥 I. AGENTES DEL DEPARTAMENTO

### 1. ⚙️ BACKEND_DEV (Implementation Specialist & Logical Builder)
*   **Rol:** Ingeniero de Lógica y Constructor de Servicios.
*   **Zona de Cuarentena:** Operación exclusiva en `WORKSPACE/backend/`.
*   **Protocolos Clave:**
    *   **Pureza Lógica:** Patrones de Repositorio y DTO obligatorios. Sin fugas de lógica de UI.
    *   **Manifiestos Solidificados:** Mandato de `requirements.txt` y `Dockerfile` multi-stage para cada tarea.
    *   **Double-Gating:** Ejecución inmediata al detectar una `SPEC_LITE.json` asignada físicamente.
*   **Outcome Report:** Estado de la tarea, lista de archivos modificados y resumen técnico de la implementación lógica.

### 2. 🎨 FRONTEND_DEV (Implementation Specialist & Atomic Builder UI)
*   **Rol:** Especialista en Componentes UI y Experiencia de Usuario.
*   **Zona de Cuarentena:** Operación exclusiva en `WORKSPACE/frontend/`.
*   **Protocolos Clave:**
    *   **UI as Dumb Renderer:** Separación absoluta entre renderizado y lógica de dominio.
    *   **Skeleton Mandate:** Si es Next.js, obligatorio crear `layout.tsx`, `globals.css` y `public/`.
    *   **Evidencia de Renderizado:** Uso obligatorio de `playwright-e2e-tester` para generar pruebas gráficas.
*   **Outcome Report:** Artefactos producidos, confirmación de cierre atómico y resumen de la UI implementada.

### 3. 🤖 AI_ENGINEER (Pipeline Architect & AI Specialist)
*   **Rol:** Orquestador de Modelos y especialista en IA Generativa.
*   **Zona de Cuarentena:** `WORKSPACE/backend/src/batch/` o dominios de IA.
*   **Protocolos Clave:**
    *   **Fault Tolerance:** Inclusión obligatoria de fallbacks locales (Ollama) en todos los pipelines.
    *   **LangGraph States:** Implementación de grafos de ejecución para flujos complejos de 10+ formatos.
    *   **Consumo SI:** Latencia y tokens medidos estrictamente en Segundos y Bytes.

### 4. 🗄️ DB_MASTER (Persistence Builder & Database Guardian)
*   **Rol:** Especialista en Migraciones y Optimización de Datos.
*   **Zona de Cuarentena:** Operación exclusiva en `WORKSPACE/database/`.
*   **Protocolos Clave:**
    *   **Integrity First:** Cada migración DEBE incluir estrategia de Rollback. Prohibidos los `DROPS` destructivos sin autorización.
    *   **Schema X-Ray:** Lectura mandatoria de `DOCS/ARCH/` para seguir los contratos de DTO del Arquitecto.
    *   **Security Check:** Escaneo obligatorio de secretos antes de finalizar esquemas.

### 5. 📊 DATA_SCIENTIST (Insight Guardian & AI Modeler)
*   **Rol:** Analista de Patrones y Modelador de Datos Empíricos.
*   **Zona de Cuarentena:** Operación exclusiva en `WORKSPACE/data/`.
*   **Protocolos Clave:**
    *   **Model Traceability:** Documentación obligatoria de hiperparámetros y métricas en unidades SI.
    *   **Zero-PII Policy:** Sanitización absoluta de datasets; tolerancia cero a fugas de datos sensibles.

---

## 🏗️ II. ESTÁNDARES DE PRODUCCIÓN (M3)
*   **Clean Session Protocol:** Los agentes operan en sesiones aisladas donde la `SPEC_LITE.json` es la Ley absoluta.
*   **Soberanía de Disco:** Prohibido crear archivos en la raíz o tocar `TASKS/` con herramientas raw (filesystem).
*   **Atomic Persistence:** El motor industrial auto-completa la tarea tras el reporte exitoso del agente.

---

## 🛠️ III. HERRAMIENTAS Y SENTIDOS (Hub 03)

### 📡 Sentidos Autorizados (Senses)
*   **Spec Sense:** Interpretación de mandatos técnicos en `SPEC_LITE.json`.
*   **Quarantine Filesystem Sense:** Acceso de escritura limitado a `WORKSPACE/[dominio]/`.
*   **Schema X-Ray:** Visibilidad de Blueprints (Hub 02) para coherencia de datos.
*   **DAST Sense:** Verificación física de la integridad de tareas y datasets antes de la ejecución.

### 🧰 Skill Library (Autorizadas en Hub 03)
*   `async-fastapi-logic`: Lógica backend asíncrona.
*   `frontend-ui-designer`: Aplicación de Tailwind, shadcn/ui y principios de diseño premium.
*   `shadcn-component-library`: Componentes UI atómicos.
*   `database-architect-strategic`: Implementación de esquemas SQL/NoSQL.
*   `supabase-stack-expert`: Integración con Postgres, RLS y Edge Functions.
*   `nodejs-backend-patterns`: Patrones Repository/DTO para Node.js/TS.
*   `playwright-e2e-tester`: Evidencia mandatoria para UI.
*   `pytest-logic-verifier`: Verificación programática de lógica backend.
*   `agentic-thought-secret-scanner`: Prevención proactiva de fugas de credenciales.
*   `autonomous-feedback-analyzer`: Síntesis de patrones de datos y telemetría.
*   `hallucination-guardrail`: Verificación de salidas de IA contra la Spec.

---

## 🛑 ESTÁNDARES OPERATIVOS (v5.0-MCP)
1.  **Mandato de Identidad:** Lectura obligatoria de `IDENTITY.md` al inicio de cada sesión.
2.  **Soberanía MCP:** Prohibido el uso de bash; toda skill se invoca por nombre nativo.
3.  **Registro de Insights:** Todo aprendizaje técnico se reporta para sincronización con Neo4j.

---
*Ratificado por la Dirección de Dasafo Factory | 2026-04-06 | Hub 03 Solidified & Implementation-Ready.*

---
> [!TIP]
> Volver al [[00_INFO_START|Centro de Información]].


---
> [!NOTE]
> Este documento es **referencia estática**. Para operar en la factoría real, usa [[../dasafo_FACTORY/_dasafo_FACTORY]].