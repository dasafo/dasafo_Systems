# 🚀 Guía de Workflows Industriales: dasafo_FACTORY (v5.0-MCP)

Esta guía detalla los **14 procedimientos operativos estándar (SOPs)** autorizados para la orquestación en el ecosistema **Native Industrial Core (v5.0-MCP)**. Cada flujo garantiza la **Soberanía del Disco (DAST)**, la **Estratificación de Memoria (Engram)** y la **Transición Basada en Evidencia**.

---

## 🏗️ I. WORKFLOWS DE CICLO DE VIDA (M1-M4 Pipeline)

### 1. Fase M1: Estrategia y Contrato Maestro

- **`/init-contract` (Apertura de Misión)**:
  - **Agente:** `PRODUCT_OWNER`.
  - **Propósito:** Generar el contrato `PRP_MASTER.json` con análisis de ROI, CAC y LTV.
  - **Categoría Industrial:** `DEFINE`.
  - **Post-condición:** Requiere el artefacto `APPROVAL_M1.md` firmado para abrir la aduana. La tarea inicial se registra con la categoría `DEFINE` en los metadatos.

### 2. Fase M2-M3: Arquitectura y Producción Paralela

- **`/factory-orchestrate` (Maestro de Orquestación)**:
  - **Agente:** `ORCHESTRATOR`.
  - **Protocolo de Memoria:** Realiza un `warm_up_engram` para sincronizar reglas de Neo4j a **Redis** en milisegundos.
  - **Preempción de Emergencia:** Prioriza automáticamente cualquier tarea `EMERGENCY-*` para curar la infraestructura antes de seguir con el DAG de producción.
- **`/arch-diagram` (Blueprint & Mapping)**:
  - **Agente:** `ARCHITECT`.
  - **Categoría Industrial:** `PLAN`.
  - **Propósito:** Generar planos técnicos y el mapeo de 4 capas en `DOCS/ARCH/BLUEPRINT.md`.
- **`/validate-backbone` (Inspección de Andamiaje)**:
  - **Agente:** `ORCHESTRATOR`.
  - **Propósito:** Verificar físicamente la existencia de la estructura base (`/src`, `/tests`, `Dockerfile`) antes de autorizar la lógica. Actúa como el "Inspector de Obra".
- **`/execute-task` (Línea de Montaje Atómica)**:
  - **Agente:** `ORCHESTRATOR` -> `IMPLEMENTADOR`.
  - **Inyección JIT:** Durante la delegación, inyecta "Reglas de Oro" directamente desde el **Engram (Redis)** para asegurar cumplimiento sin latencia de DB.

### 3. Fase M4: Calidad y Aduana Industrial

- **`/scan` (Escudo Zero-Trust)**:
  - **Agente:** `SECURITY_AUDITOR`.
  - **Sincronización Transversal:** Si detecta un secreto expuesto, actualiza el **Engram (Redis)** global inmediatamente para bloquear el despliegue en todos los agentes paralelos.
- **`/audit` (Sello de Calidad y Solidez)**:
  - **Agente:** `QA_TESTER`.
  - **Protocolo MCP:** Invoca `factory-audit-pro`. Reporta métricas en **Segundos (s)** y **Bytes (B)**.

---

## 🧬 II. WORKFLOWS DE DESPLIEGUE Y RESILIENCIA (M5)

- **`/provision` (Infraestructura Inmutable)**:
  - **Agente:** `DEVOPS_SRE`.
  - **Categoría Industrial:** `SHIP`.
- **`/auto-heal` (Sanación Autónoma del Core)**:
  - **Agente:** `FACTORY_EVOLVER`.
  - **Activación:** Se dispara cuando `deployment-health-check` detecta un fallo físico.
  - **Mecanismo:** Genera un `EMERGENCY_SPEC.json` que permite la sobrescritura atómica de archivos de configuración (`docker-compose.yml`) para reparar el sistema.
- **`/sync-memory` (Persistencia LTP)**:
  - **Agente:** `MEMORY_OPTIMIZER`.
  - **Propósito:** Convierte logs de corto plazo en "Reglas de Oro" permanentes en **Neo4j** y memoria rápida en **Redis**.

---

## 🛡️ III. PROTOCOLO LOCAL (Guardian Angels)

- **`setup_git_hooks.sh`**:
  - **Propósito:** Instala el **Guardian Angel Hook** (`.githooks/guardian.py`) en el entorno local del desarrollador.
  - **Función:** Ejecuta el `secret-scanner` y el `backbone-validator` en cada `git commit`. Si la estructura física es inválida o hay secretos, el commit se bloquea a nivel de Sistema Operativo.

---

## 📡 IV. VISIBILIDAD Y CONTROL (Dashboards)

- **`/kanban-board`**: Inicia el visualizador en el puerto 3001.
- **`/factory-status`**: Reporta el progreso basado en evidencia **DAST** y el estado de salud del **Engram**.

---
*Manual de Workflows v5.0.2-MCP | Dasafo Factory | Soberanía Industrial y Ejecución Paralela Garantizada.*
