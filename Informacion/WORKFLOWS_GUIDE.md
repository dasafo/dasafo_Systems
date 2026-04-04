# 🚀 Guía de Workflows Industriales: dasafo_FACTORY (v5.0-MCP)

Esta guía detalla los **14 procedimientos operativos estándar (SOPs)** autorizados para la orquestación de misiones en el ecosistema **Native Industrial Core (v5.0-MCP)**. Cada flujo se activa mediante **Slash Commands** y garantiza la **Soberanía del Disco (DAST)** y la **Transición Basada en Evidencia**.

---

## 🏗️ I. WORKFLOWS DE CICLO DE VIDA (M1-M4 Pipeline)

Los flujos se ejecutan mediante la activación directa de comandos que disparan las tareas en los Hubs correspondientes.

### 1. Fase M1: Estrategia y Contrato Maestro

- **`/init-contract` (Apertura de Misión)**:
  - **Agente:** `PRODUCT_OWNER`.
  - **Propósito:** Generar el contrato industrial `PRP_MASTER.json` con análisis de ROI, CAC y LTV.
  - **Protocolo MCP:** Invoca `startup-metrics-framework` y `prp-generator` (Mandato de sobreescritura).
  - **Post-condición:** Requiere el artefacto `APPROVAL_M1.md` firmado para abrir la aduana.

### 2. Fase M2-M3: Arquitectura y Producción Paralela

- **`/factory-orchestrate` (Maestro de Orquestación)**:
  - **Agente:** `ORCHESTRATOR`.
  - **Propósito:** Calcular la topología de tareas (DAG) y sincronizar el registro de tareas en disco.
  - **Protocolo MCP:** Invoca `project-management` (`analyze_schedule`) para habilitar la ejecución paralela masiva.
- **`/arch-diagram` (Blueprint & Mapping)**:
  - **Agente:** `ARCHITECT`.
  - **Propósito:** Generar planos técnicos y el mapeo de sistema de 4 capas en `DOCS/ARCH/BLUEPRINT.md`.
- **`/validate-backbone` (Inspección de Andamiaje)**:
  - **Agente:** `ORCHESTRATOR`.
  - **Propósito:** Verificar físicamente la existencia de la estructura base (`/src`, `/tests`, `Dockerfile`) antes de autorizar la lógica.
- **`/execute-task` (Línea de Montaje Atómica)**:
  - **Agente:** `ORCHESTRATOR` (Delegador) -> `IMPLEMENTADOR` (Ejecutor).
  - **Propósito:** Lanza una **Clean Session** aislada activando el protocolo de **Doble-Puerta (Double-Gating)**.
  - **Autorización:** El ejecutor tiene permiso inmediato si detecta su `SPEC_LITE.json` física en la carpeta `TASKS/`.

### 3. Fase M4: Calidad y Aduana Industrial

- **`/scan` (Escudo Zero-Trust)**:
  - **Agente:** `SECURITY_AUDITOR`.
  - **Propósito:** Escaneo profundo de secretos, llaves API y CVEs. Genera el `SECURITY_REPORT.md` obligatorio.
- **`/audit` (Sello de Calidad y Solidez)**:
  - **Agente:** `QA_TESTER`.
  - **Propósito:** Validar la adhesión a la Constitución Arquitectónica. Reporta métricas estrictamente en **Segundos (s)** y **Bytes (B)**.
  - **Protocolo MCP:** Invoca `factory-audit-pro` y `build-test-executor` para emitir el `BUILD_REPORT.json`.

---

## 🧬 II. WORKFLOWS DE DESPLIEGUE Y RESILIENCIA (M5)

- **`/provision` (Infraestructura Inmutable)**:
  - **Agente:** `DEVOPS_SRE`.
  - **Propósito:** Generar Dockerfiles multi-stage y configuraciones IaC en `WORKSPACE/infra/`.
- **`/deploy` (Lanzamiento Atómico)**:
  - **Agente:** `DEVOPS_SRE`.
  - **Propósito:** Despliegue de artefactos verificados mediante provisión de contenedores.
- **`/auto-heal` (Sanación Autónoma del Core)**:
  - **Agente:** `FACTORY_EVOLVER`.
  - **Propósito:** Activación del bucle M5 ante fallos críticos de infraestructura; genera parches automáticos en `docker-compose.yml`.
- **`/health-check` (Telemetría Sentinel)**:
  - **Agente:** `DEPLOYMENT_MONITOR`.
  - **Propósito:** Validación en tiempo real de latencia (s) y salud de red física (B).
- **`/sync-memory` (Persistencia LTP)**:
  - **Agente:** `MEMORY_OPTIMIZER`.
  - **Propósito:** Sincronizar lecciones aprendidas y "Reglas de Oro" con la base de datos Neo4j para evitar amnesia sistémica.

---

## 📡 III. WORKFLOWS DE VISIBILIDAD Y CONTROL (Dashboards)

- **`/kanban-board` (Vibe Dashboard)**: Inicia el visualizador en el puerto 3001 para inspeccionar la línea de montaje física y el estado de los agentes.
- **`/factory-status` (Pulso Industrial)**: Genera un reporte consolidado de salud de los Hubs y progreso del pipeline basado en evidencia DAST.

---
*Manual de Workflows v5.0-MCP | Dasafo Factory | Soberanía Industrial y Ejecución Paralela Garantizada.*
