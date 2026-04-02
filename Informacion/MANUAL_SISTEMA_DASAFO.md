# 🏛️ Manual Maestro de Instrucciones: dasafo_Systems v4.0-S

> **"Industrializando la Excelencia Evolutiva a través de la Soberanía del Disco y el Grafo de Conocimiento."**

**dasafo_Systems** es un ecosistema industrial de Inteligencia Artificial de alto rendimiento diseñado para la ingeniería de software autónoma. Opera bajo el estándar **v4.0-S "Industrial Core"**, que prioriza la **Solidez de Capas**, la **Soberanía de Datos (DAST)** y la **Persistencia a Largo Plazo (LTP)**. 

Este manual constituye la **Fuente Única de Verdad (SSoT)**. Cualquier desviación de estos protocolos se considera una *Cultural Violation* técnica.

---

## 🏗️ I. ARQUITECTURA DE NODOS (El Ecosistema)

El sistema se distribuye en tres nodos físicos y lógicos que garantizan el aislamiento hermético y la resiliencia operativa:

### 🧠 A. `dasafo_FACTORY` (El Núcleo Inmutable)
Es el "Cerebro Central" que contiene el ADN de la factoría. Sus componentes son de solo lectura para la mayoría de los agentes (Zero-Trust):

1.  **`00_GLOBAL_KNOWLEDGE`**: Contiene la Constitución Core, el Mandato de Unidades SI y las plantillas maestras (`PRP_MASTER`, `SPEC_LITE`, `FEEDBACK_SCHEMA`).
2.  **`01-05 Hubs Departamentales`**: Jerarquía de 17 agentes organizados en:
    *   **Hub 01 (Strategy):** Orquestación y Producto.
    *   **Hub 02 (Architecture):** Planos y Diseño.
    *   **Hub 03 (Production):** Implementación de Código y Datos.
    *   **Hub 04 (Compliance):** Seguridad y Calidad.
    *   **Hub 05 (Operations):** Despliegue y Evolución.
3.  **`06_SKILL_LIBRARY`**: Repositorio de scripts atómicos (`run.py`) que ejecutan las tareas físicas.
4.  **`factory_cli.py`**: El puente MCP que comunica la interfaz de usuario con el motor interno.

### ⚡ B. `INFRA` (La Red Eléctrica / Power Grid)
Nodo de servicios compartidos gestionado por Docker Compose que provee la infraestructura persistente:

*   **Postgres (`shared-db`)**: Almacenamiento operativo para estados persistentes complejos.
*   **Neo4j (`kg-db`)**: El Grafo de Conocimiento. Mapa semántico que almacena las "Reglas de Oro" y previene alucinaciones reinyectando experiencias pasadas.
*   **Redis (`cache-node`)**: Gestión de colas de tareas y estados volátiles.
*   **Glances**: Telemetría de hardware (CPU, RAM, Red) accesible en tiempo real.

### 📦 C. `PROJECTS` (El Taller / Workshop)
Espacio mutable donde residen los proyectos individuales. Cada proyecto sigue la estructura **SDD (Spec Driven Development)**:
*   `DOCS/`: Blueprints, ADRs y Reportes.
*   `TASKS/`: Línea de montaje física (`01_PENDING`, `02_IN_PROGRESS`, `03_COMPLETED`).
*   `WORKSPACE/`: El código fuente real del producto.
*   `LOGS/`: Evidencias de ejecución, seguridad y despliegue.

---

## ⚙️ II. EL MOTOR INDUSTRIAL (Mecanismos de Ejecución)

La eficiencia de la factoría reside en la automatización de la micro-gestión mediante tres componentes críticos:

### 🛂 1. Session Hook: La Aduana Universal
Intercepta cada llamada a una habilidad. Sus funciones son:
*   **Auto-Start:** Al ejecutar una tarea, busca la `SPEC_LITE.json` en `01_PENDING` y la mueve automáticamente a `02_IN_PROGRESS`. Si no hay Spec física, la ejecución se bloquea.
*   **Validación de Fase:** Impide que se ejecuten tareas de Producción (M3) si la fase de Arquitectura (M2) no tiene el sello de "Solidified".

### 🧪 2. Skill Engine: El Ejecutivo Atómico
El motor que carga las habilidades y garantiza su integridad.
*   **Inyección JIT (Just-In-Time):** Antes de ejecutar, inyecta credenciales del `.env` global y reglas de Neo4j en la memoria del agente.
*   **Auto-Commit:** Tras el éxito de una skill bajo aislamiento, el motor mueve los artefactos a `03_COMPLETED` y cierra la tarea en el registro sin intervención humana.

### 📊 3. DAST (Disk Artifact State Tracking)
En v4.0-S, el **disco duro es la única fuente de verdad**. Si un agente dice que terminó, pero el archivo no existe físicamente en la carpeta correspondiente, la tarea se considera fallida.

---

## 🚀 III. CICLO DE VIDA DEL PROYECTO (M1-M5 Pipeline)

### 🕵️ M1: Discovery & Economics
*   **Acción:** El `PRODUCT_OWNER` crea el `PRP_MASTER.json`.
*   **Mandato:** Debe incluir el análisis de CAC (Costo de Adquisición) y LTV (Valor de Vida del Cliente) mediante el `startup-metrics-framework`.
*   **Cierre:** Firma física (Approval) del usuario.

### 📐 M2: Architecture & Backbone
*   **Acción:** El `ARCHITECT` crea el plano estructural (`blueprint.md`).
*   **Gate:** El `project-backbone-validator` confirma que la estructura de carpetas del framework existe físicamente. No se programa funcionalidad hasta que el "esqueleto" sea sólido.

### ⚙️ M3: Implementation (Atomic Production)
*   **Acción:** Delegación de `SPEC_LITE` a peones de producción.
*   **Predictive Shield:** El Orquestador inyecta "Reglas de Oro" de proyectos pasados para evitar errores de implementación recurrentes.

### 🛡️ M4: Compliance & Quality Gate
*   **Acción:** Escaneo de secretos con `agentic-thought-secret-scanner` y auditoría de calidad de código.
*   **Solidity Score:** El `QA_TESTER` emite una puntuación de solidez basada en la cobertura de tests y adhesión al Mandato SI.

### 🚀 M5: Operations & Sentinel
*   **Acción:** Provisión de infra e ignición del entorno Live.
*   **Auto-Heal:** El sistema monitoriza logs corporales y parchea automáticamente la infraestructura ante fallos de puerto o memoria.

---

## ⚖️ IV. MANDATOS Y ÉTICA DE LA FACTORÍA

### 1. Mandato de Unidades SI (Estándar de Medición)
Toda métrica técnica en reportes debe expresarse exclusivamente en:
*   **Tiempo:** Segundos (s) (ej: Latencia API: 0.12s).
*   **Espacio:** Bytes (B) (ej: Tamaño Bundle: 450,230B).

### 2. Soberanía Vegetariana (Factoría de Software)
Prohibido el uso de analogías de "carnicería", "matadero" o "consumo de recursos" que impliquen sufrimiento animal. Somos una factoría de alta tecnología, no un proveedor de carnes.

### 3. Zero-Trust de Identidad
Cada agente tiene su propia "Aduana de Pensamiento" (Thought Boundary). Ningún agente puede leer la memoria de otro a menos que se use el grafo de conocimiento compartido.

---

## 🕹️ V. MATRIZ DE CONTROL (Comandos de Director)

| Comando | Función Industrial | Responsable |
| :--- | :--- | :--- |
| `/init-contract` | Sella la visión y viabilidad financiera. | Product Owner |
| `/factory-orchestrate` | Sincroniza el disco con el plan de ataque. | Orchestrator |
| `/execute-task` | Lanza la línea de montaje con inmunidad Neo4j. | Orchestrator/Peon |
| `/audit` | Valida la solidez y cumplimiento de SI Units. | QA Tester |
| `/scan` | Ejecuta el escudo Zero-Trust de secretos. | Security Auditor |
| `/auto-heal` | Activa la resiliencia autónoma ante fallos. | DevOps / Evolver |
| `/sync-memory` | Graba el aprendizaje del proyecto en el ADN. | Memory Optimizer |

---
*Ratificado: 2026-04-02 | Dasafo Factory v4.0-S | El Futuro de la Ingeniería de Software Solidificada.*
