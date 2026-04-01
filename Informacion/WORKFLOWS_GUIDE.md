# 🚀 Guía de Workflows Industriales | dasafo_FACTORY (v3.4.0-S)

Esta guía detalla los 11 flujos de trabajo (workflows) disponibles en el ecosistema para la gestión, ejecución y auditoría de proyectos bajo el estándar **Industrial Core (v3.4.0-S)**.

---

## 🏗️ Ciclo de Vida del Proyecto (M1-M5)

Los workflows se dividen según su propósito dentro del pipeline universal:

### 1. Fase M1: Descubrimiento (Discovery)
- **`/init-contract`**:
  - **Propósito**: Generar el contrato maestro del proyecto (`PRP_MASTER.json`).
  - **Agente**: `PRODUCT_OWNER`.
  - **Cuándo**: Al inicio de un nuevo proyecto, tras definir los requisitos iniciales. Es el paso obligatorio para salir de la Fase M1.
  - **Resultado**: Crea un documento de 12 secciones con alcances, criterios de éxito e infraestructura (M5).

### 2. Fase M2-M3: Arquitectura y Producción (Build)
- **`/factory-orchestrate`**:
  - **Propósito**: Comando de transición que deconstruye contratos en tareas (`SPEC_LITE.json`) o promociona fases.
  - **Agente**: `ORCHESTRATOR`.
  - **Cuándo**: Para sincronizar el `registry.json` con los archivos físicos y mover el proyecto a través del pipeline.
  - **Resultado**: Transición controlada (M1 -> M2 -> M3...) y delegación automática de tareas a `01_PENDING/`.
- **`/arch-diagram`**:
  - **Propósito**: Genera diagramas Mermaid actualizados de la arquitectura del sistema.
  - **Agente**: `ARCHITECT`.
  - **Cuándo**: Durante la Fase M2 o cambios estructurales significativos.
  - **Resultado**: Archivos técnicos en `DOCS/ARCH/`.
- **`/execute-task`**:
  - **Propósito**: Lanza una **Clean Session** aislada para ejecutar una tarea específica.
  - **Agente**: `ORCHESTRATOR` (vía Delegación a Peones).
  - **Cuándo**: Durante la producción (M3) para implementar Backend, Frontend, Data o DB.
  - **Resultado**: Código funcional y verificado en `WORKSPACE/`.

### 3. Fase M4: Cumplimiento y Calidad (Compliance)
- **`/scan`**:
  - **Propósito**: Realizar un escaneo de seguridad profundo (SAST + Secrets) bajo el estándar **Zero-Trust**.
  - **Agente**: `SECURITY_AUDITOR`.
  - **Cuándo**: Antes de realizar cualquier commit importante o transición de fase.
  - **Resultado**: Reportes en la carpeta `LOGS/` y/o `SECURITY_REPORT.md`.
- **`/audit`**:
  - **Propósito**: Validar la calidad y el cumplimiento de una tarea contra el contrato PRP original.
  - **Agente**: `QA_TESTER`.
  - **Cuándo**: Al finalizar una tarea, reportando latencias y tamaños estrictos en **Segundos (s)** y **Bytes (B)**.
  - **Resultado**: Feedback estructurado en `FEEDBACK-LOG.md`.

### 4. Fase M5: Operaciones y Despliegue (Ops)
- **`/provision`**:
  - **Propósito**: Preparar la infraestructura física (Docker, Terraform, Scripts).
  - **Agente**: `DEVOPS_SRE`.
  - **Cuándo**: Fase M4 aprobada con evidencias físicas sólidas.
  - **Resultado**: Scripts de infraestructura en `WORKSPACE/infra/`.
- **`/deploy`**:
  - **Propósito**: Ejecución del despliegue atómico al entorno de producción.
  - **Agente**: `ORCHESTRATOR` / `DEVOPS_SRE`.
  - **Cuándo**: Infraestructura aprovisionada correctamente.
  - **Resultado**: Sistema operando "Live" en el entorno destino.
- **`/health-check`**:
  - **Propósito**: Monitoreo Sentinel de salud y latencia en tiempo real del sistema desplegado.
  - **Agente**: `DEPLOYMENT_MONITOR`.
  - **Cuándo**: Proyecto en estado "Live" o después de cada `/deploy`.
  - **Resultado**: Reportes de latencia (s) y tamaño (B) en `LOGS/deployment/`.

---

## 📡 Monitoreo y Radares (Visibilidad)

- **`/kanban-board`**:
  - **Propósito**: Levantar el Dashboard visual de **Vibe Kanban** en tiempo real.
  - **Cuándo**: Para monitorizar el flujo de tarjetas y bloqueos físicos sin usar la terminal.
  - **Resultado**: Interfaz web en el puerto 3001.
- **`/factory-status`**:
  - **Propósito**: Generar un reporte de salud y progreso consolidado en formato texto.
  - **Cuándo**: Para obtener un pulso rápido del consumo de memoria, estado de los Hubs y progreso de fases.
  - **Resultado**: Resumen textual directo en el chat.

---
*Documentación Solidificada v3.4.0-S | dasafo_FACTORY*
