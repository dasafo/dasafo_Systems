# 🚀 Guía de Workflows Industriales | dasafo_FACTORY (v4.0-S)

Esta guía detalla los 14 flujos de trabajo (workflows) disponibles en el ecosistema para la gestión, ejecución, auditoría y auto-sanación de proyectos bajo el estándar **Industrial Core (v4.0-S)**.

---

## 🏗️ Ciclo de Vida del Proyecto (M1-M5)

Los workflows se dividen según su propósito dentro del pipeline universal:

### 1. Fase M1: Descubrimiento (Discovery)

- **`/init-contract`**:
  - **Propósito**: Generar el contrato maestro del proyecto (`PRP_MASTER.json`) inyectando proyecciones financieras.
  - **Agente**: `PRODUCT_OWNER`.
  - **Cuándo**: Al inicio de un nuevo proyecto, tras definir los requisitos iniciales.
  - **Resultado**: Crea un documento de 12 secciones con métricas SI y KPIs Financieros (Target CAC, Target LTV) mediante la skill `startup-metrics-framework`.

### 2. Fase M2-M3: Arquitectura y Producción (Build)

- **`/factory-orchestrate`**:
  - **Propósito**: Comando de transición que deconstruye contratos en tareas (`SPEC_LITE.json`) o promociona fases.
  - **Agente**: `ORCHESTRATOR`.
  - **Cuándo**: Para sincronizar el `registry.json` con los archivos físicos y mover el proyecto a través del pipeline de la Aduana Universal.
- **`/arch-diagram`**:
  - **Propósito**: Genera diagramas Mermaid actualizados de la arquitectura del sistema.
  - **Agente**: `ARCHITECT`.
  - **Cuándo**: Durante la Fase M2 o cambios estructurales significativos.
  - **Resultado**: Archivos técnicos en `DOCS/ARCH/`.
- **`/validate-backbone`** *(Nuevo v3.4.5)*:
  - **Propósito**: Verifica físicamente que el andamiaje del framework (Scaffolding) existe en el disco duro.
  - **Agente**: `ORCHESTRATOR`.
  - **Cuándo**: Antes de despachar a los peones (`FRONTEND_DEV`, `BACKEND_DEV`) para evitar construcciones en el vacío.
- **`/execute-task`**:
  - **Propósito**: Lanza una **Clean Session** aislada con guardarraíles predictivos de Neo4j.
  - **Agente**: `ORCHESTRATOR` (vía Delegación a Peones).
  - **Cuándo**: Durante la producción (M3). El Orquestador inyecta las *Golden Rules* históricas de Neo4j en la `SPEC_LITE` antes de delegar.
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
  - **Cuándo**: Al finalizar una tarea, reportando *Cultural Violations* o errores arquitectónicos.
  - **Resultado**: Feedback estructurado en `FEEDBACK-LOG.md` listo para ser procesado.

### 4. Fase M5: Operaciones y Despliegue (Ops)

- **`/provision`**:
  - **Propósito**: Preparar la infraestructura física (Docker, Terraform, Scripts).
  - **Agente**: `DEVOPS_SRE`.
  - **Cuándo**: Fase M4 aprobada con evidencias físicas sólidas.
  - **Resultado**: Scripts de infraestructura en `WORKSPACE/infra/`.
- **`/deploy`**:
  - **Propósito**: Ejecución del despliegue atómico al entorno de producción.
  - **Agente**: `DEVOPS_SRE`.
  - **Cuándo**: Infraestructura aprovisionada y `SECURITY_REPORT.md` en estado `PASSED`.
  - **Resultado**: Sistema operando "Live" en el entorno destino.
- **`/auto-heal`** *(Nuevo v4.0-S)*:
  - **Propósito**: Sistema Inmunológico Industrial. Parchea automáticamente bloqueos de infraestructura.
  - **Agente**: `DEVOPS_SRE` (Trigger) -> `FACTORY_EVOLVER` (Ejecución).
  - **Cuándo**: Cuando un despliegue falla por conflictos de puertos o memoria (OOM).
  - **Resultado**: Archivo `docker-compose.yml` refactorizado físicamente en el disco.
- **`/sync-memory`** *(Nuevo v4.0-S)*:
  - **Propósito**: Extrae los *Engramas Agenticos* y las reglas de oro para consolidar la Persistencia de Largo Plazo (LTP).
  - **Agente**: `MEMORY_OPTIMIZER`.
  - **Cuándo**: Ciclo de sueño de la factoría. Se ejecuta para convertir el `FEEDBACK-LOG.md` a nodos en la base de datos Neo4j.
  - **Resultado**: Grafo de conocimiento actualizado (prevención de futuras alucinaciones).

---

## 📡 Monitoreo y Radares (Visibilidad)

- **`/kanban-board`**:
  - **Propósito**: Levantar el Dashboard visual de **Vibe Kanban** en tiempo real.
  - **Agente**: `ORCHESTRATOR`.
  - **Cuándo**: Para monitorizar el flujo de tarjetas y bloqueos físicos sin usar la terminal.
  - **Resultado**: Interfaz web en el puerto 3001.
- **`/factory-status`**:
  - **Propósito**: Generar un reporte de salud y progreso consolidado en formato texto.
  - **Agente**: `DEPLOYMENT_MONITOR`.
  - **Cuándo**: Para obtener un pulso rápido del consumo de memoria, estado de los Hubs y progreso de fases.
  - **Resultado**: Resumen textual directo en el chat.
- **`/health-check`**:
  - **Propósito**: Monitoreo Sentinel de salud y latencia en tiempo real del sistema desplegado.
  - **Agente**: `DEPLOYMENT_MONITOR`.
  - **Cuándo**: Proyecto en estado "Live" o después de cada `/deploy`.
  - **Resultado**: Reportes de latencia (s) y tamaño (B) en `LOGS/deployment/`.

---
*Documentación Solidificada v4.0-S | dasafo_FACTORY*
