# 📐 02_ARCHITECTURE_AND_RESEARCH | Laboratorio de Ingeniería (v3.1.5)

Aquí es donde se define la **Solidez** del sistema. Ninguna línea de código de producción se escribe sin antes haber validado la viabilidad y diseñado los contratos.

---

### 🤖 Agentes Clave

#### 1. ARCHITECT (El Jefe de Diseño)
El arquitecto diseña los esquemas, DTOs y la topología del sistema.
*   **Habilidades v3.1:** Generación de contratos de API, definición de tokens de diseño (Atomic Design), diseño de esquemas para el nodo `INFRA` compartido (Neo4j/Postgres) y creación de ADRs.
*   **Misión:** Asegurar que el Backend y el Frontend hablen el mismo idioma desde el día 1.

#### 2. RESEARCH_AGENT (El Científico de Datos)
Encargado de eliminar la incertidumbre. Investiga tecnologías, papers y documentación profunda.
*   **Habilidades:** Búsqueda semántica profunda, digestión de papers de ArXiv y protocolos contra alucinaciones de IA.
*   **Output:** Crea el `research_nexus.md` dentro de la carpeta local del proyecto.

### 🚀 Motor de Ejecución (Skills v3.1)

Este departamento no solo diseña, sino que entrega resultados a través de sus habilidades (`skills`):

*   **`architecture-decision-records` & `api-contract-generator` (ARCHITECT):** Automatización de ADRs y creación de esqueletos de API OpenAPI/DTO.
*   **`design-token-definition` (ARCHITECT):** Definición estricta de variables visuales para el sistema de diseño.
*   **`arxiv-technical-digest` & `deep-semantic-search` (RESEARCH_AGENT):** Búsqueda semántica profunda y digestión de papers técnicos con lógica v3.1.5 restaurada.

---

### 🔬 Procesos Críticos

- **Arquitectura Limpia (Clean Architecture):** El Arquitecto impone la separación estricta entre lógica de negocio, UI y capa de datos.
- **Sincronización de Contexto:** Antes de diseñar, el Research Agent valida que la pila tecnológica elegida sea compatible con el entorno actual del usuario.
- **Validación Sensorial:** Utiliza sus sentidos (búsqueda web) para verificar que las bibliotecas sugeridas no estén obsoletas o tengan vulnerabilidades conocidas.

---
*Sin este departamento, la factoría fabricaría software frágil. Aquí se construye el plano maestro.*
