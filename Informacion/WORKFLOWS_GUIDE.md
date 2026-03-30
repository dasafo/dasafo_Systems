# 🚀 Guía de Workflows Industriales | dasafo_FACTORY (v3.4.0-S)

Esta guía detalla los flujos de trabajo (workflows) disponibles en el ecosistema para la gestión, ejecución y auditoría de proyectos bajo el estándar **SDD Optimized Core**.

---

## 🏗️ Ciclo de Vida del Proyecto

Los workflows se dividen según su propósito dentro del ciclo de vida industrial:

### 1. Fase M1: Descubrimiento (Discovery)

- **`/init-contract`**:
  - **Propósito**: Generar el contrato maestro del proyecto (`PRP_MASTER.json`).
  - **Agente**: `PRODUCT_OWNER`.
  - **Cuándo usarlo**: Al inicio de un nuevo proyecto, tras la conversación inicial de requisitos. Es el paso obligatorio para salir de la Fase M1.
  - **Resultado**: Crea un documento de "Verdad Absoluta" con 12 secciones que define el alcance y los criterios de éxito.

### 2. Fase M3: Producción (Production)

- **`/execute-task`**:
  - **Propósito**: Ejecutar una tarea específica en una **Clean Session** (Entorno Aislado).
  - **Agente**: `ORCHESTRATOR` (vía Delegación a Peones).
  - **Cuándo usarlo**: Durante la fase de desarrollo para implementar lógica de backend, frontend o base de datos. Evita la saturación de tokens y asegura la pureza del contexto.
  - **Resultado**: Código implementado y verificado en el subdirectorio `WORKSPACE/` correspondiente.

### 3. Visualización y Control

- **`/kanban-board`**:
  - **Propósito**: Levantar el Dashboard visual de **Vibe Kanban**.
  - **Agente**: `ORCHESTRATOR`.
  - **Cuándo usarlo**: Siempre que necesites una visión clara del estado del tablero, las tareas pendientes y los bloqueos físicos en el disco.
  - **Resultado**: Servidor local en el puerto 3001 con la interfaz visual del proyecto.

---

## 🛡️ Seguridad, Calidad y Auditoría

- **`/scan`**:
  - **Propósito**: Realizar un escaneo de seguridad profundo bajo el estándar **Zero-Trust**.
  - **Agente**: `SECURITY_AUDITOR`.
  - **Cuándo usarlo**: Antes de cualquier commit importante o transición de fase. Busca secretos expuestos, vulnerabilidades y brechas de seguridad.
  - **Resultado**: `SECURITY_REPORT.md` en la carpeta `LOGS/` del proyecto.

- **`/audit`**:
  - **Propósito**: Validar la calidad y el cumplimiento de una tarea contra el contrato PRP.
  - **Agente**: `QA_TESTER`.
  - **Cuándo usarlo**: Al finalizar una tarea y antes de marcarla como `COMPLETED` en el registro.
  - **Resultado**: Feedback estructurado en `FEEDBACK-LOG.md` y validación de criterios de éxito.

- **`/arch-diagram`**:
  - **Propósito**: Generar diagramas Mermaid actualizados de la arquitectura del sistema.
  - **Agente**: `ARCHITECT`.
  - **Cuándo usarlo**: Durante la Fase M2 o cuando se realicen cambios estructurales significativos.
  - **Resultado**: Archivos Markdown con diagramas técnicos en `DOCS/ARCH/`.

---

## 🎮 Orquestación y Estado Global

- **`/factory-orchestrate`**:
  - **Propósito**: El comando maestro de la factoría para avanzar de fase.
  - **Agente**: `ORCHESTRATOR`.
  - **Cuándo usarlo**: Para sincronizar el `registry.json` con los archivos físicos y mover el proyecto a través del pipeline universal (Aduana Universal).
  - **Resultado**: Transición controlada de fases (M1 -> M2 -> M3...) y delegación automática de tareas.

- **`/factory-status`**:
  - **Propósito**: Generar un reporte de salud y progreso consolidado.
  - **Agente**: `DEPLOYMENT_MONITOR` / `DEVOPS_SRE`.
  - **Cuándo usarlo**: Para obtener un pulso rápido del proyecto, el consumo de memoria del infra y el estado del Kanban.
  - **Resultado**: Informe visual de métricas y salud industrial.

---
*Documentación Solidificada v3.4.0-S | dasafo_FACTORY*
