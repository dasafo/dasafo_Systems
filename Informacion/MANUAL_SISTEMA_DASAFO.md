# 🏛️ Manual Maestro de Instrucciones | dasafo_Systems v3.2.0-S

**dasafo_Systems** es un ecosistema industrial de Inteligencia Artificial diseñado para escalar el desarrollo de software con precisión militar y estética premium. Este manual es la **Fuente Única de Verdad (SSoT)** que captura toda la dimensión técnica, operativa y estratégica del proyecto.

---

## 🧠 1. EL CEREBRO: `dasafo_FACTORY`

Representa la inteligencia central y las leyes inmutables. Es el lugar donde residen los **Prompts de Sistema**, las **Leyes Globales** y el **Motor Ejecutivo**.

### 🏛️ La Constitución: The Core (`00_THE_CORE.md`)
Define los principios de diseño que rigen a todos los agentes:
*   **Solidity Guard:** Blindaje total contra alucinaciones. Inyecta memoria de errores pasados vía **AutoShield**.
*   **3 Pilares Maestros:** **Solidez** (Código industrial), **Vibe** (Velocidad estética) e **Industrialización** (Procesos repetibles).
*   **Chesterton's Fence:** Prohibición de refactorizar sin entender el propósito original documentado.

### ⚙️ El Motor: The Engine (`01_THE_ENGINE.md`)
Orquestación basada en **DAG (Grafos Acíclicos Dirigidos)**.
*   **Aduana Universal:** Prohibición estricta de avance de fase si existen tareas pendientes. No hay "Go-Live" sin validación física de artefactos en `TASKS/03_COMPLETED/`.

### 🗄️ El Registro: The Registry (`02_THE_REGISTRY.md`)
*   **`registry.json`:** SSoT digital del estado de cada proyecto.
*   **Sincronización `task.md`:** Espejo visual del Kanban físico para auditoría humana inmediata.

---

## 🧰 2. EL MOTOR EJECUTIVO: TECH STACK

La infraestructura de habilidades que permite a la IA interactuar con el mundo físico.

*   **`factory_cli.py` (MCP Bridge):** Interfaz JSON-RPC 2.0 que conecta el asistente con las herramientas de la factoría.
*   **`skill_engine.py` (Modular Toolbox):** Cargador dinámico de habilidades desde `06_SKILL_LIBRARY/`. Permite ejecutar lógica de alto rendimiento con aislamiento total entre el agente y la herramienta.
*   **`skill_schema.py` (Contratos de Datos):** Estandarización de `SkillInput` (Parámetros/Contexto) y `SkillOutput` (Resultados/Artefactos/Trazabilidad).

---

## 🧱 3. EL VIVERO DE SERVICIOS: `INFRA/`

Suministra servicios compartidos mediante Docker Compose para todos los proyectos activos.

*   **Red Unificada (`dasafo_network`):** Red de bridge aislada para comunicación segura entre servicios.
*   **Recursos Blindados:**
    *   **Neo4j (`kg-db`):** Grafo de conocimiento central (4GB RAM limit).
    *   **Postgres (`shared-db`):** Base de datos operativa compartida (2GB RAM limit).
    *   **Glances:** Monitor de salud global del sistema.

---

## 🛠️ 4. EL TALLER DE PROYECTOS: `PROJECTS/`

Aquí ocurre la acción mutable. Cada proyecto hereda el ADN de la factoría mediante el script `init_project.sh`.

*   **WORKSPACE:** Código de producción (Backend, Frontend, Shared).
*   **TASKS (Industrial Kanban):** Estructura física numerada (`01_PENDING` a `05_REJECTED`) para la trazabilidad de tareas atómicas.
*   **LOCAL_KNOWLEDGE:** Repositorio de ADRs (Decisiones Arquitectónicas), investigaciones y el contrato crucial `PRP_CONTRACT.json`.
*   **LOGS (Telemetría):** Historial granular de sesiones, errores e incidentes de seguridad.

---

## 🔍 5. AGENTES Y ROLES DE GOBERNANZA

Interactúas con una jerarquía de 16 agentes especializados, coordinados por los "Agentes de Puerta":

1.  **ORCHESTRATOR** 👑: El director universal. Descompone intenciones en tareas ejecutables.
2.  **PRODUCT_OWNER** 📋: El guardián de la visión. Valida el **PRP** antes de cualquier fase de producción.
3.  **ARCHITECT** 📐: El ingeniero jefe. Diseña planos, DTOs y garantiza el SoC (Separación de Intereses).
4.  **QA / SECURITY** 🛡️: El sistema inmune. Auditan secretos, calidad y cumplimiento normativo.

---

## 📊 6. EVOLUCIÓN Y APRENDIZAJE: `FEEDBACK-LOG.md`

El sistema es **Antifrágil**: crece y mejora con el desorden y los errores.
*   **Bucle de Feedback:** Cada alucinación o error de infraestructura se registra en el log global.
*   **Meta-Evolución:** El agente `FACTORY_EVOLVER` analiza patrones para mutar los protocolos globales y las habilidades hacia la perfección industrial.

---

## 🕹️ 7. COMANDOS DE PODER (Slash Commands)

| Comando | Acción Industrial |
| :--- | :--- |
| **`/factory-orchestrate`** | Avanza el pipeline industrial y genera la siguiente ola de tareas. |
| **`/scan`** | Activa el escáner de seguridad y calidad técnica (Solidity Guard). |
| **`/factory-status`** | Reporte visual ejecutivo del progreso y salud de la infraestructura. |
| **`/audit`** | Revisión profunda y destructiva antes del cierre oficial de una tarea. |
| **`/arch-diagram`** | Genera diagramas de arquitectura en Mermaid en tiempo real. |

---

## 🚀 8. GUÍA DE INICIO RÁPIDO: PUESTA EN MARCHA

1.  **Infraestructura:** Inicia el nodo central: `cd INFRA && docker-compose up -d`.
2.  **Inicialización:** Crea el esqueleto del proyecto: `./init_project.sh NombreProyecto`.
3.  **Definición:** Llama al **PRODUCT_OWNER** para redactar el `PRP_CONTRACT.json`.
4.  **Firma:** Revisa el contrato en `LOCAL_KNOWLEDGE/` y cambia `"prp_status": "draft"` → `"signed"`.
5.  **Ejecución:** Ordena: *"PRP firmado. Proceder con el Orchestrator"*.

---

> [!IMPORTANT]
> **"Industrializing Excellence"**
> dasafo_Systems opera bajo un modelo de confianza cero donde cada línea de código debe ser justificada, probada y documentada.

---
*Manual Maestro v3.2.0-S | dS — SSoT Oficial.*
