# 🚀 Guía de Workflows Industriales: dasafo_FACTORY (v4.0-S)

Esta guía detalla los **14 flujos de trabajo (workflows)** autorizados para la orquestación de misiones en el ecosistema **Industrial Core (v4.0-S)**. Cada flujo está diseñado para garantizar la **Soberanía del Disco (DAST)** y la **Transición Basada en Evidencia (Phase-Gate Logic)**.

---

## 🏗️ I. WORKFLOWS DE CICLO DE VIDA (M1-M5 Pipeline)

Los flujos se agrupan por etapa dentro del "Universal Pipeline" de la factoría.

### 1. Fase M1: Descubrimiento & Estrategia (Discovery)
*   **`/init-contract`**:
    *   **Agente:** `PRODUCT_OWNER`.
    *   **Propósito:** Generar el contrato maestro del proyecto (`PRP_MASTER.json`) inyectando análisis de ROI, CAC y LTV.
    *   **Pre-condición:** Briefing inicial por parte del Director de Operaciones.
    *   **Post-condición:** Generación física de `PRP_MASTER.json` en la raíz del proyecto. El sistema bloquea el paso a M2 si no existe este artefacto.
    *   **Skill:** `prp-generator` + `startup-metrics-framework`.

### 2. Fase M2-M3: Arquitectura & Producción (Build)
*   **`/factory-orchestrate` (Sincronización Total)**:
    *   **Agente:** `ORCHESTRATOR`.
    *   **Propósito:** Deconstruir el contrato maestro en especificaciones atómicas (`SPEC_LITE.json`) y sincronizar el registro de tareas en el disco.
    *   **Pre-condición:** Contrato M1 aprobado.
    *   **Post-condición:** Población de la carpeta `TASKS/01_PENDING/` con specs autorizadas.
    *   **Skill:** `kanban-solidity-gate` + `registry-manager`.
*   **`/validate-backbone` (Inspección Structural)**:
    *   **Agente:** `ORCHESTRATOR`.
    *   **Propósito:** Verificar físicamente que el andamiaje del framework (Next.js, FastAPI, etc.) existe en disco antes de delegar lógica de negocio.
    *   **Pre-condición:** Tareas de arquitectura (M2) completadas.
    *   **Post-condición:** Reporte de validación oficial; habilitación del Hub 03 (Producción).
    *   **Skill:** `project-backbone-validator`.
*   **`/arch-diagram` (Blueprint Visual)**:
    *   **Agente:** `ARCHITECT`.
    *   **Propósito:** Generar planos técnicos actualizados en formato Mermaid basándose en la estructura física del proyecto.
    *   **Resultado:** Archivos `.md` en `DOCS/ARCH/`.
*   **`/execute-task` (La Línea de Montaje)**:
    *   **Agente:** `ORCHESTRATOR` (Delegador) -> `PEON` (Ejecutor).
    *   **Propósito:** Lanza una **Clean Session** aislada con guardarraíles predictivos de Neo4j para ejecutar una spec técnica.
    *   **Automatización Industrial (v4.0-S):** Implementa el **Auto-Start** (mueve la tarea a `02_IN_PROGRESS`) y el **Auto-Commit** (mueve a `03_COMPLETED` tras el éxito).
    *   **Skill:** `delegate-clean-session` + `skill-engine` (Inject Golden Rules).

### 3. Fase M4: Calidad & Cumplimiento (Compliance)
*   **`/scan` (Escudo Zero-Trust)**:
    *   **Agente:** `SECURITY_AUDITOR`.
    *   **Propósito:** Escaneo profundo de secretos, claves API y vulnerabilidades en dependencias.
    *   **Post-condición:** Generación de `SECURITY_REPORT.md`. Si hay filtraciones, el proyecto se bloquea automáticamente.
    *   **Skill:** `agentic-thought-secret-scanner` + `dependency-vulnerability-scanner`.
*   **`/audit` (Sello de Calidad)**:
    *   **Agente:** `QA_TESTER`.
    *   **Propósito:** Validar que el código escrito cumple con el contrato M1. Reporta métricas en **segundos (s)** y **bytes (B)**.
    *   **Valor:** Detecta antipatrones y "Cultural Violations" para inyectar en la memoria analítica.
    *   **Skill:** `factory-audit-pro` + `pytest-logic-verifier`.

### 4. Fase M5: Operaciones & Despliegue (Ops)
*   **`/provision` (IaC Infrastructure)**:
    *   **Agente:** `DEVOPS_SRE`.
    *   **Propósito:** Preparar Dockerfiles, Terraform o scripts de nube en `WORKSPACE/infra/`.
    *   **Pre-condición:** Auditoría M4 aprobada.
    *   **Skill:** `infra-provisioner` + `docker-stack-provisioner`.
*   **`/deploy` (Lanzamiento Industrial)**:
    *   **Agente:** `DEVOPS_SRE`.
    *   **Propósito:** Despliegue atómico de artefactos al entorno en vivo.
    *   **Skill:** `registry-manager` + `docker-stack-provisioner`.

---

## 🧬 II. WORKFLOWS DE RESILIENCIA Y EVOLUCIÓN (LTP)

Flujos transversales que mantienen la salud y la inteligencia de la factoría.

*   **`/auto-heal` (Sanación Autónoma)**:
    *   **Agente:** `DEVOPS_SRE` (Aviso) -> `FACTORY_EVOLVER` (Parcheo).
    *   **Propósito:** Si un despliegue o la salud del sistema falla por conflictos de infraestructura (OOM, Puertos bloqueados), el sistema se parchea solo.
    *   **Skill:** `infra-provisioner` (Emergency Refactor) + `factory-doctor`.
*   **`/health-check` (Ojo Sentinel)**:
    *   **Agente:** `DEPLOYMENT_MONITOR`.
    *   **Propósito:** Monitoreo en tiempo real de latencia (s), salud y tamaño de respuesta (B).
    *   **Skill:** `deployment-health-check` + `latency-pulse-reporter`.
*   **`/sync-memory` (Consolidación LTP)**:
    *   **Agente:** `MEMORY_OPTIMIZER`.
    *   **Propósito:** Extraer lecciones aprendidas de los logs e inyectarlas como "Reglas de Oro" permanentes en el Grafo de Neo4j.
    *   **Resultado:** Prevención de alucinaciones futuras.
    *   **Skill:** `context-pruning-sieve` + `kg-db-sync`.

---

## 📡 III. WORKFLOWS DE VISIBILIDAD (Radares)

*   **`/kanban-board`**: Levanta el dashboard visual de **Vibe Kanban** en el puerto 3001.
*   **`/factory-status`**: Genera un reporte rápido de salud de los Hubs, estado del pipeline y bloqueos físicos en disco.

---
*Manual de Workflows v4.0-S | Dasafo Factory | Industrializando la Precisión.*
