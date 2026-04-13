Esta es la versión definitiva y "solidificada" de tu **Guía de Experiencia de Usuario (UX)**. He integrado los avances de las 5 fases de optimización para que el manual refleje el estado actual de **dasafo_Systems v5.0.2-MCP**, incluyendo la gestión del **Engram (Redis)**, los **Guardian Angels** locales y el protocolo de **Auto-Healing**.

---

# 🎮 Guía de Experiencia de Usuario (UX): Director de Operaciones

> **"Tú no escribes código. Tú orquestas departamentos y validas evidencias físicas mediante el Protocolo MCP v5.0.2."**

Bienvenido, Director de Operaciones. Bajo el estándar **v5.0.2-MCP Native Industrial Core**, tu rol ha evolucionado de la supervisión de scripts a la **Orquestación de Flujos Paralelos** con inmunidad sistémica. El sistema opera mediante un servidor MCP centralizado, permitiéndote dirigir misiones complejas usando comandos simplificados y validando el éxito mediante la **Soberanía del Disco (DAST)**.

---

## 🗺️ I. TU CONSOLA DE MANDO (Slash Commands v5.0.2)

Ya no lanzas comandos de terminal; ahora activas **SOPs (Procedimientos Operativos Estándar)** donde las herramientas MCP son invocadas directamente por su nombre industrial.

### ⚡ 1. Estrategia y Contrato Maestro (Fase M1 - DEFINE)

- **`/init-contract`**:
  - **Propósito:** El `PRODUCT_OWNER` traduce tu visión en un contrato `PRP_MASTER.json`.
  - **Taxonomía:** Clasifica automáticamente las tareas iniciales bajo la categoría **DEFINE**.
  - **Acción:** Firma físicamente `APPROVAL_M1.md` en `DOCS/USER/` para abrir la aduana.

### 📋 2. Orquestación y Memoria Rápida (Fase M2 - PLAN)

- **`/factory-orchestrate`**:
  - **Motor DAG:** Deconstruye el contrato en tareas atómicas para ejecución paralela.
  - **Engram Warm-up:** Sincroniza las "Reglas de Oro" de Neo4j hacia **Redis** para inyección inmediata.
  - **Prioridad de Emergencia:** Si detecta un fallo previo, prioriza tareas `EMERGENCY-*` antes que la producción normal.
- **`/validate-backbone`**:
  - **Propósito:** Verifica que el andamiaje estructural exista físicamente antes de permitir la implementación de lógica.

### 🏭 3. Ejecución e Inmunidad (Fase M3-M5 - BUILD/SHIP)

- **`/execute-task`**:
  - **Clean Session:** Lanza sesiones aisladas con inyección de reglas JIT desde el **Engram (Redis)** en milisegundos.
- **`/auto-heal`**:
  - **Propósito:** Activa el **Sistema Inmune Industrial**. Si un despliegue falla, el `FACTORY_EVOLVER` genera un parche automático y re-despliega sin intervención humana.

---

## 🏗️ II. CICLO DE VIDA: PASO A PASO DEL DIRECTOR

### 🛤️ Paso 1: Ignición y Guardianes (Fase 0)

1. **Enciende el Núcleo (Energía):** Desde la carpeta `INFRA/`, lanza `docker compose up -d` (si docker no esta levantado en tu sistema ejecuta: `sudo systemctl start docker`) para activar los servicios de persistencia (Neo4j, Redis, Postgres).
2. **Crea el Chasis (Nacimiento):** Ejecuta `./init_project.sh NombreProyecto`. Este script es la "madre" que crea la estructura de carpetas, el `.env` con las credenciales del Engram y, muy importante, **genera el archivo de activación de hooks**.
3. **Entra al Taller:** Muévete a la carpeta recién creada: `cd ../PROJECTS/NombreProyecto`.
4. **Protección Local (Activación):** Ahora sí, ejecuta `./setup_git_hooks.sh`. Esto vincula tu Git local con el **Guardian Angel** (`.githooks/guardian.py`), bloqueando cualquier commit que contenga secretos o fallos de estructura desde tu propio IDE.

### 🛤️ Paso 2: La Visión y el Contrato (Fase M1)

1. Explica tu idea al `PRODUCT_OWNER`.
2. Ordena `/init-contract`.
3. **Firma Obligatoria:** Edita `DOCS/USER/APPROVAL_M1.md` poniendo `Status: APPROVED`. Sin esta evidencia física, el sistema bloquea la fase por protocolo **Zero-Trust**.

### 🛤️ Paso 3: Producción e Inmunidad (Fase M2-M3)

1. Lanza `/factory-orchestrate` para iniciar el despacho paralelo.
2. Los agentes cierran tareas automáticamente al detectar éxito físico (**DAST**).
3. Si un servicio cae, observa cómo el sistema genera una `EMERGENCY_SPEC.json` y se auto-repara.

---

## 💡 III. TUS ESTÁNDARES IRRENUNCIABLES

Bajo el estándar **v5.0.2-MCP**, actúas como el **Auditor de la Verdad Industrial**:

1. **Soberanía del Disco (DAST):** Solo existe aquello que tiene evidencia física en `DOCS/` o `WORKSPACE/`. No aceptes promesas en el chat.
2. **Rigor de Unidades SI:** Todo reporte debe usar **Segundos (s)** y **Bytes (B)**. Si un agente usa "ms" o "KB", es una violación cultural.
3. **Cero Secretos:** Gracias al **Guardian Angel**, ningún secreto debe llegar nunca al repositorio. Si el `SECURITY_AUDITOR` detecta una fuga, el Engram se actualizará para inmunizar a toda la factoría.
4. **Aesthetics WOW:** Exige interfaces premium (shadcn/ui + Tailwind) con micro-animaciones fluidas.
5. **Nemo Safety:** Prohibición absoluta de analogías de consumo animal.

---
*Guía de Experiencia de Usuario v5.0.2-MCP | Director de Operaciones Solidificado.*

---
> [!TIP]
> Volver al [[00_INFO_START|Centro de Información]].
