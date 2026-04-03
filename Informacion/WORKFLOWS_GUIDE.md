# 🚀 Guía de Workflows Industriales: dasafo_FACTORY (v5.0-MCP)

Esta guía detalla los **14 procedimientos operativos estándar (SOPs)** autorizados para la orquestación de misiones en el ecosistema **Native Industrial Core (v5.0-MCP)**. Cada flujo está diseñado para garantizar la **Soberanía del Disco (DAST)** y la **Transición Basada en Evidencia**.

---

## 🏗️ I. WORKFLOWS DE CICLO DE VIDA (M1-M5 Pipeline)

Los flujos se ejecutan mediante la herramienta MCP las herramientas MCP **directamente por nombre**, que actúa como el único brazo motriz de la factoría.

### 1. Fase M1: Descubrimiento & Estrategia (Discovery)

* **SOP `init-contract`**:
  * **Agente:** `PRODUCT_OWNER`.
  * **Propósito:** Generar el contrato maestro (`PRP_MASTER.json`) con análisis de ROI, CAC y LTV.
  * **Protocolo MCP:** Invoca las skills `startup-metrics-framework` y `prp-generator`.
  * **Post-condición:** Requiere firma física humana en `APPROVAL_M1.md` para abrir la aduana.

### 2. Fase M2-M3: Arquitectura & Producción (Build)

* **SOP `factory-orchestrate` (Sincronización Total)**:
  * **Agente:** `ORCHESTRATOR`.
  * **Propósito:** Deconstruir el contrato en especificaciones atómicas (`SPEC_LITE.json`) y sincronizar el registro físico de tareas.
  * **Protocolo MCP:** Invoca `kanban-solidity-gate` para verificar la solidez del disco antes de avanzar.
* **SOP `validate-backbone` (Inspección Estructural)**:
  * **Agente:** `ORCHESTRATOR`.
  * **Propósito:** Verificar que el andamiaje del framework (Next.js, FastAPI, etc.) existe físicamente antes de permitir la delegación de lógica.
* **SOP `arch-diagram` (Blueprint Visual)**:
  * **Agente:** `ARCHITECT`.
  * **Propósito:** Generar planos técnicos actualizados y consolidar los ADRs en `DOCS/ARCH/BLUEPRINT.md`.
* **SOP `execute-task` (Línea de Montaje)**:
  * **Agente:** `ORCHESTRATOR` (Delegador) -> `PEON` (Ejecutor).
  * **Propósito:** Lanza una **Clean Session** aislada con guardarraíles predictivos de Neo4j.
  * **Automatización Industrial:** Implementa el **Auto-Start** (bloqueo de tarea) y el **Auto-Commit** (cierre atómico tras el éxito).

### 3. Fase M4: Calidad & Cumplimiento (Compliance)

* **SOP `scan` (Escudo Zero-Trust)**:
  * **Agente:** `SECURITY_AUDITOR`.
  * **Propósito:** Escaneo profundo de secretos y vulnerabilidades. Genera el `SECURITY_REPORT.md` obligatorio.
* **SOP `audit` (Sello de Calidad)**:
  * **Agente:** `QA_TESTER`.
  * **Propósito:** Validar la adhesión al contrato M1. Reporta métricas estrictamente en **segundos (s)** y **bytes (B)**.

### 4. Fase M5: Operaciones & Despliegue (Ops)

* **SOP `provision` (Infraestructura IaC)**:
  * **Agente:** `DEVOPS_SRE`.
  * **Propósito:** Generar Dockerfiles y configuraciones de nube en `WORKSPACE/infra/`.
* **SOP `deploy` (Lanzamiento Atómico)**:
  * **Agente:** `DEVOPS_SRE`.
  * **Propósito:** Despliegue de los artefactos verificados al entorno operacional.

---

## 🧬 II. WORKFLOWS DE RESILIENCIA Y EVOLUCIÓN (LTP)

* **SOP `auto-heal` (Sanación Autónoma)**:
  * **Agente:** `FACTORY_EVOLVER`.
  * **Propósito:** Ante un fallo de infraestructura (ej. puerto bloqueado), el sistema genera un parche automático y refactoriza el `docker-compose.yml` sin intervención humana.
* **SOP `health-check` (Monitor Sentinel)**:
  * **Agente:** `DEPLOYMENT_MONITOR`.
  * **Propósito:** Validación en tiempo real de latencia (s) y salud de red (B).
* **SOP `sync-memory` (Consolidación LTP)**:
  * **Agente:** `MEMORY_OPTIMIZER`.
  * **Propósito:** Extraer lecciones aprendidas e inyectarlas como "Reglas de Oro" en el Grafo de Neo4j para prevenir alucinaciones futuras.

---

## 📡 III. WORKFLOWS DE VISIBILIDAD (Radares)

* **SOP `kanban-board`**: Inicia el dashboard visual en el puerto 3001 para inspeccionar la línea de montaje física.
* **SOP `factory-status`**: Reporte consolidado de salud de los Hubs y estado del pipeline basado en DAST.

---
*Manual de Workflows v5.0-MCP | Dasafo Factory | Soberanía Industrial Garantizada.*
