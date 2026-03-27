# 🧰 06_SKILL_LIBRARY | El Almacén de Habilidades (v3.2.0-S)

La carpeta **`06_SKILL_LIBRARY`** es el corazón pulsante de la factoría. No contiene solo instrucciones, sino **Habilidades Ejecutables (Skills)** reales: módulos de lógica en Python (`run.py`) que permiten a los agentes interactuar con el mundo físico, analizar datos, generar código y auditar seguridad con precisión industrial.

En la versión **v3.2.0-S "Modular Toolbox"**, todas las habilidades han sido estandarizadas bajo el protocolo de interfaz **SkillInput / SkillOutput**, asegurando que cualquier agente pueda invocar cualquier habilidad de forma segura y predecible.

---

### 🧬 Anatomía de una Habilidad (Standard v3.2.0-S)

Cada habilidad es un micromódulo diseñado para ser invocado mediante el `skill_engine.py`:

*   **`SKILL.md`**: El contrato de la habilidad. Define el objetivo, el agente responsable (aunque pueden ser compartidas) y el esquema exacto de entrada y salida (vía `skill_schema.py`).
*   **`run.py`**: El motor lógico. Contiene la implementación real. En v3.2.0-S, todas incluyen resolución de rutas dinámica para ser ejecutables desde cualquier punto de la factoría.
*   **Agnosticismo de Máquina**: Gracias al uso de `sys.executable`, las habilidades se ejecutan siempre dentro del entorno Python correcto del usuario, evitando errores de dependencias.

---

### 📖 Catálogo por Categorías (Modular Toolbox)

Con más de 80 habilidades industriales disponibles, la factoría se divide en 5 dominios de poder:

#### 1. Estrategia y Orquestación (01_STRATEGY)
*   `ra-agile-orchestration`: Distribución multi-agente y enrutamiento DAG.
*   `prp-generator`: Creación industrial de contratos de visión.
*   `dag-routing`: Descomposición de intenciones en grafos de tareas con dependencias.

#### 2. Arquitectura e Investigación (02_ARCHITECTURE)
*   `adr-generator-pro`: Generación de registros de decisiones arquitectónicas.
*   `deep-semantic-search`: Búsqueda de alta precisión en datos científicos y del proyecto.
*   `api-contract-generator`: Diseño de APIs compatibles con Swagger/OpenAPI.

#### 3. Producción y Ejecución (03_PRODUCTION)
*   `async-fastapi-logic`: Generación de lógica asíncrona robusta.
*   `atomic-design-tokens`: Consistencia en Colores, Espaciado y Tipografía premium.
*   `resilient-error-handling`: Implementación de Circuit Breakers y reintentos.

#### 4. Cumplimiento y Calidad (04_COMPLIANCE)
*   `kanban-solidity-gate`: La "Aduana Universal" que bloquea cambios sin validación física.
*   `agentic-thought-secret-scanner`: Escaneo rudo de secretos y claves API.
*   `browser-visual-validation`: Pruebas de regresión visual con Playwright.

#### 5. Operaciones y Evolución (05_OPERATIONS)
*   `autoshield-preflight-check`: El sistema inmune que inyecta memoria de errores pasados.
*   `autonomous-feedback-analyzer`: Destilación de lecciones aprendidas del `FEEDBACK-LOG.md`.
*   `context-compression`: Optimización de tokens para máxima eficiencia de costes.

---

### 🛡️ Protocolo de Ejecución: Solidity Guard
- **Preflight Check**: Antes de invocar cualquier habilidad crítica, los agentes ejecutan `autoshield-preflight-check` para verificar la integridad del entorno.
- **Validación de Artefactos**: Todas las habilidades deben dejar una "prueba física" en las carpetas `LOGS/` o `WORKSPACE/` para que el Auditor pueda validar el éxito de la tarea.
- **Uso de Unidades SI**: Bajo el mandato v3.2.0-S, cualquier habilidad que procese datos físicos debe operar exclusivamente en el Sistema Internacional.

---
*Skill Library v3.2.0-S | El Motor de la Factoría dasafo_Systems.*
