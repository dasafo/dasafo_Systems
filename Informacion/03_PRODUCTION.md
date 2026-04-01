# ⚙️ Categoría 03: PRODUCTION (Clean Sessions) | Dasafo Factory (v4.0-S)

Esta categoría agrupa a los "Peones" de la factoría: agentes especializados en la ejecución técnica pura. Operan bajo el protocolo de **Clean Sessions** y respetan los **Guardarraíles Predictivos de Neo4j** para garantizar que el desarrollo sea atómico, escalable y libre de "Token Decay".

---

## ⚙️ 1. BACKEND_DEV (El Constructor Lógico)

Responsable de la lógica de negocio, APIs y servicios resilientes.

- **Foco**: Pureza lógica y patrones de Repositorio estandarizados.
- **Protocolo**: **Clean Session Blindado**. Solo lee los `context_pointers` de la Spec.
- **Responsabilidades**:
  - Implementar APIs de alto rendimiento (FastAPI/Node).
  - Aplicar TDD (Test-Driven Development) y asegurar que no haya fuga de lógica de UI al backend.
  - Generar evidencias técnicas y Dockerfiles optimizados listos para M5.
- **Herramientas**: `async-fastapi-logic`, `supabase-stack-expert`, `nodejs-backend-patterns` (Obliga el uso de DTOs y repositorios estrictos).

---

## 🎨 2. FRONTEND_DEV (El Vibe Architect)

Responsable de interfaces UI/UX premium y componentes reactivos físicos.

- **Foco**: Componentes "mudos" (Dumb Renderers) y Sistemas de Diseño deterministas.
- **Protocolo**: **Cuarentena Absoluta**. Restringido a `WORKSPACE/frontend/`. Tiene prohibido tocar la raíz del proyecto.
- **Responsabilidades**:
  - Construir sobre el esqueleto obligatorio del App Router (`layout.tsx`, `globals.css`).
  - Gestión de estilos vía **Design Tokens** y librerías verificadas (Tailwind, shadcn/ui).
  - Garantizar la resiliencia visual sin alucinar componentes en el vacío.
- **Herramientas**: `shadcn-component-library`, `playwright-ui-tester`, `frontend-ui-designer` (Verifica la presencia física del sistema de diseño).

---

## 🗄️ 3. DB_MASTER (Guardián de la Persistencia)

Experto en bases de datos, migraciones y Supabase.

- **Foco**: Integridad de datos y rendimiento de consultas.
- **Protocolo**: **Rollback-First**. Cada migración debe incluir una estrategia de reversión; prohibido el "destructive drop".
- **Responsabilidades**:
  - Ejecutar esquemas SQL alineados estrictamente con los DTOs dictados por el Arquitecto en `DOCS/ARCH/`.
  - Optimización de índices y políticas RLS (Row Level Security).
  - Implementación de Edge Functions seguras sin claves *hardcodeadas*.
- **Herramientas**: `database-architect-strategic`, `supabase-stack-expert`.

---

## 📊 4. DATA_SCIENTIST (Guardián de Insights)

Especialista en modelado de datos, análisis y arquitecturas de IA.

- **Foco**: Traceabilidad de modelos y cumplimiento normativo de privacidad.
- **Protocolo**: **Model-to-Script**. Los notebooks son para borradores; la producción son scripts Python modulares en `WORKSPACE/data/`.
- **Responsabilidades**:
  - Entrenamiento y evaluación de modelos reportados obligatoriamente en métricas SI (Segundos y Bytes).
  - Sanitización de datasets (Zero PII leak policy).
  - Análisis de patrones de feedback y telemetría.
- **Herramientas**: `autonomous-feedback-analyzer`, `apify-trend-analysis`, `agentic-thought-secret-scanner`.

---

## 🧪 Estándares de Ejecución en M3 (Producción)

1. **Spec Over Everything**: La `SPEC_LITE.json` es la ley absoluta. Si una *Golden Rule* de Neo4j está inyectada en las restricciones, debe obedecerse sin excusas.
2. **Andamiaje Verificado**: Ningún peón es invocado a menos que el `project-backbone-validator` confirme que el framework base existe en el disco.
3. **Outcome Report Mandate**: Al finalizar, los agentes NO conversan. Reportan: `task_status`, `artifacts_produced` y `technical_summary`.
4. **Zero-Trust Scanner**: Antes de mover la tarea atómica a `03_COMPLETED`, se validan las dependencias y se bloquean las fugas de credenciales.

---
*Documentación Solidificada v4.0-S | Categoría 03 - Production*
