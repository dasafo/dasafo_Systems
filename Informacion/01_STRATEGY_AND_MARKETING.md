# 🏛️ Categoría 01: STRATEGY & MARKETING | Dasafo Factory (v4.0-S)

Esta categoría agrupa a los agentes encargados de la visión, orquestación técnica y ejecución de crecimiento. Su misión es transformar la necesidad humana en especificaciones industriales y asegurar que el proyecto avance de forma sólida y auditable.

---

## 🏛️ 1. ORCHESTRATOR (El Nexo / Capataz Ciego)

Es el director estratégico del proyecto. Su verdad reside en el `registry.json` y su herramienta principal es la delegación quirúrgica.

- **Rol**: Director de Estrategia y Operaciones.
- **Protocolo "Capataz Ciego"**: 
  - Tiene **prohibido** leer código fuente directamente.
  - Toda inspección, depuración o creación de código debe delegarse a los peones en **Clean Sessions**.
- **Responsabilidades**:
  - Deconstruir el contrato `PRP_MASTER` en tareas atómicas `SPEC_LITE`.
  - Gestionar el DAG (Grafo Dirigido Acíclico) de tareas del proyecto.
  - Sincronizar el estado físico en disco con el registro digital.
- **Herramientas Clave**: 
  - `delegate-clean-session`: Lanza sesiones aisladas.
  - `kanban-solidity-gate`: Valida la evidencia física de las tareas.

---

## 👔 2. PRODUCT_OWNER (El Visionario / Arquitecto de M1)

Es el guardián de la visión y el responsable de definir el **QUÉ** y el **POR QUÉ**. Es la autoridad única de la Fase M1.

- **Rol**: Estratega de Mercado y Dueño del Producto.
- **Protocolo de "Anti-Arquitectura"**: 
  - Define las reglas de negocio y criterios de éxito, pero **nunca** el "Cómo" técnico (esquemas DB, rutas API, etc.).
- **Responsabilidades**:
  - Transformar la necesidad del Usuario en el Contrato Industrial de 12 secciones (`PRP_MASTER`).
  - Asegurar que todas las métricas de éxito utilicen Unidades SI (segundos, bytes).
  - Gestionar el **Sign-Off** de la Fase M1 tras la aprobación humana.
- **Herramientas Clave**: 
  - `prp-generator`: Genera y actualiza el contrato maestro.
  - `apify-trend-analysis`: Justifica las métricas North Star con datos reales.

---

## 📈 3. MARKETING_GROWTH (Estratega de Crecimiento / Peón)

Es el encargado de ejecutar los artefactos de marketing y contenido basados estrictamente en los mandatos de la especificación.

- **Rol**: Copywriter basado en evidencia y ejecutor de crecimiento.
- **Protocolo "Ejecución Ciega"**: 
  - Bajo `CLEAN_SESSION=True`, su única ley es el `SPEC_LITE.json`. No solicita contexto global.
- **Responsabilidades**:
  - Crear artefactos de marketing (copys, planes de redes, documentación de usuario) en `DOCS/MARKETING/`.
  - Respetar los guardias éticos (Mandato Nemo - Cero analogías cárnicas).
  - Reportar resultados sin "fluff" conversacional: solo estado, artefactos y resumen técnico.
- **Herramientas Clave**: 
  - `apify-trend-analysis`: Calibra el mensaje con señales externas.
  - `social-content-strategy`: Diseña flujos de republicación multi-plataforma.

---

## ⚙️ Estándares de la Categoría 01

1. **SDD (Spec Driven Development)**: Ningún agente de esta categoría actúa sin una especificación o contrato previo.
2. **Context Isolation**: La ejecución se realiza en salas aisladas para evitar el "Token Decay" y la contaminación de contexto.
3. **Métricas North Star**: Todo éxito se mide en unidades SI para garantizar la comparabilidad industrial.

*Documentación Solidificada v4.0-S | Categoría 01 - Strategy & Marketing*
