# 🎮 Guía de Experiencia de Usuario (UX): Director de Operaciones

> **"Tú no escribes código. Tú orquestas departamentos y validas evidencias físicas mediante el Protocolo MCP v5.0."**

Bienvenido, Director de Operaciones. Bajo el estándar **v5.0-MCP Native Industrial Core**, tu rol ha evolucionado de la supervisión de scripts a la **Orquestación de Flujos Paralelos**. El sistema ahora opera silenciosamente bajo el capó mediante un servidor MCP centralizado, permitiéndote dirigir misiones complejas usando comandos simplificados y validando el éxito mediante evidencia física (DAST).

---

## 🗺️ I. TU CONSOLA DE MANDO (Slash Commands v5.0)

Ya no lanzas comandos de terminal; ahora activas **SOPs (Procedimientos Operativos Estándar)** mediante comandos slash que los agentes ejecutan invocando herramientas MCP directamente por nombre.

### ⚡ 1. Estrategia y Contrato Maestro (Fase M1)

- **`/init-contract`**:
  - **Propósito:** El `PRODUCT_OWNER` traduce tu visión en un contrato `PRP_MASTER.json` blindado.
  - **Valor:** Define el ROI, CAC y la viabilidad del proyecto.
  - **Acción:** Revisa el resumen y firma físicamente el archivo `APPROVAL_M1.md` en `DOCS/USER/` para abrir la aduana.

### 📋 2. Orquestación y Arquitectura (Fase M2)

- **`/factory-orchestrate`**:
  - **Propósito:** **[Motor DAG]** El `ORCHESTRATOR` deconstruye el contrato en tareas atómicas y calcula la topología para ejecución paralela.
- **`/arch-diagram`**:
  - **Propósito:** Genera el Blueprint visual y el mapeo de sistema de 4 capas.
- **`/validate-backbone`**:
  - **Propósito:** Verifica que el andamiaje estructural (Next.js, FastAPI, etc.) exista físicamente en disco antes de permitir la lógica.

### 🏭 3. Ejecución y Producción (Fase M3)

- **`/execute-task`**:
  - **Propósito:** Lanza una **Clean Session** aislada donde un implementador ejecuta una tarea específica.
  - **Protocolo Doble-Puerta (Double-Gating):** El agente tiene permiso de ejecución inmediata si detecta su `SPEC_LITE.json` en `TASKS/`.
  - **Premium UI Mandate:** En desarrollos web, los agentes deben seguir el estándar **"Aesthetics WOW"** (Tailwind, shadcn/ui, animaciones fluidas).

### 🛡️ 4. Aduana y Lanzamiento (Fase M4-M5)

- **`/scan` / `/audit`**: Escaneos de seguridad Zero-Trust y auditorías de solidez con reportes en **Segundos (s)** y **Bytes (B)**.
- **`/provision` / `/deploy`**: Provisión de infraestructura inmutable y lanzamiento atómico del proyecto.
- **`/sync-memory`**: Sincronización de lecciones aprendidas con **Neo4j** para persistencia a largo plazo (LTP).

---

## 🏗️ II. CICLO DE VIDA: PASO A PASO DEL DIRECTOR

### 🛤️ Paso 1: Ignición del Taller (Fase 0)

1. **Enciende el Núcleo:** Desde `INFRA/`, lanza `docker compose up -d` para activar el cerebro (Neo4j/Supabase) (o si docker no esta levantado , levántalo con `systemctl start docker` o `sudo systemctl start docker`).
2. **Activa el Servidor MCP:** Asegúrate de que Antigravity ha iniciado `factory_mcp_server.py`. Este es tu único canal de mando autorizado.
3. **Crea el Chasis:** Ejecuta `./init_project.sh NombreProyecto` para generar las carpetas blindadas.

### 🛤️ Paso 2: La Visión del Producto (Fase M1)

1. Explica tu idea al `PRODUCT_OWNER`.
2. Ordena ejecutar `/init-contract` vía MCP.
3. **Firma Obligatoria:** Si el ROI y la especificación son correctos, edita `DOCS/USER/APPROVAL_M1.md` poniendo `Status: APPROVED`. Sin esta firma física, el sistema se bloqueará por protocolo Zero-Trust.

### 🛤️ Paso 3: Producción en Paralelo (Fase M2-M3)

1. Lanza `/factory-orchestrate` para visualizar el cronograma DAG.
2. Observa cómo los agentes entran en sesiones aisladas (`CLEAN_SESSION=True`), escriben código en sus zonas de cuarentena y cierran tareas automáticamente al detectar éxito físico (DAST).

### 🛤️ Paso 4: Cierre y Evolución (LTP)

1. Al finalizar el hito, ordena ejecutar el SOP **`/sync-memory`**.
2. Esto graba las "Reglas de Oro" en el Grafo de Neo4j para que la factoría no cometa los mismos errores en misiones futuras.

---

## 💡 III. TUS ESTÁNDARES IRRENUNCIABLES

Bajo el estándar **v5.0-MCP**, actúas como el **Auditor de la Verdad Industrial**:

1. **Soberanía del Disco (DAST):** No aceptes "promesas" textuales. Si un agente afirma haber terminado, verifica que el artefacto exista físicamente en `DOCS/` o `WORKSPACE/`.
2. **Rigor de Unidades SI:** Todos los reportes de rendimiento deben usar **Segundos (s)** y **Bytes (B)**.
3. **Diseño Premium (WOW Factor):** Rechaza cualquier interfaz que parezca básica. Exige gradientes, bordes redondeados, modo oscuro y micro-animaciones (shadcn/ui + Tailwind).
4. **Nemo Safety:** Absoluta prohibición de analogías de consumo animal en cualquier documento o pieza de marketing.

---
*Guía de Experiencia de Usuario v5.0-MCP | Director de Operaciones Solidificado.*
