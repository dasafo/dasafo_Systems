# 🎮 Guía de Experiencia de Usuario (UX): Director de Operaciones

> **"Tú no escribes código. Tú orquestas departamentos y validas evidencias físicas mediante el Protocolo MCP."**

Bienvenido, Director de Operaciones. Bajo el estándar **v4.0-MCP Native Industrial Core**, tu rol ha evolucionado de la supervisión de scripts a la **validación de flujos industriales**. El sistema ahora opera mediante un servidor MCP centralizado que garantiza que ningún agente actúe sin una especificación física y tu aprobación previa.

---

## 🗺️ I. TU CONSOLA DE MANDO (Los 14 SOPs Industriales)

Ya no usas "comandos slash" manuales en una terminal; ahora activas **Workflows** que los agentes ejecutan invocando la herramienta MCP `execute_industrial_skill`.

### ⚡ 1. Estrategia y Visión (Fase M1: Discovery)

* **SOP `init-contract`**:
  * **Propósito:** El `PRODUCT_OWNER` traduce tu visión en un contrato `PRP_MASTER.json` de 12 secciones.
  * **Valor:** Inyecta proyecciones de ROI, CAC y LTV.
  * **Acción:** Revisa el resumen y firma físicamente el archivo `APPROVAL_M1.md` en `DOCS/USER/` para abrir la aduana.

### 📋 2. Deconstrucción y Refuerzo (Fase M2: Arquitectura)

* **SOP `factory-orchestrate`**:
  * **Propósito:** Sincroniza la "Aduana Universal". El `ORCHESTRATOR` deconstruye el contrato en tareas atómicas (`SPEC_LITE.json`).
* **SOP `validate-backbone`**:
  * **Propósito:** El inspector de infraestructura. Verifica que el framework (Next.js, FastAPI, etc.) esté físicamente en el disco antes de delegar lógica.

### 🏭 3. Línea de Montaje (Fase M3: Producción)

* **SOP `execute-task`**:
  * **Propósito:** Lanza una **Clean Session** aislada donde un agente de producción ejecuta una tarea específica.
  * **Automatización MCP:**
        1. **Inmunización:** Inyecta "Reglas de Oro" de Neo4j para evitar errores pasados.
        2. **Auto-Commit:** Tras el éxito, el motor MCP mueve la tarea a `03_COMPLETED` y destruye la especificación para evitar duplicidad.

### 🛡️ 4. Aduana de Calidad (Fase M4: Compliance)

* **SOP `scan`**:
  * **Propósito:** Escaneo Zero-Trust de secretos y vulnerabilidades por el `SECURITY_AUDITOR`.
* **SOP `audit`**:
  * **Propósito:** El `QA_TESTER` valida que el código cumple con la arquitectura y reporta en **Segundos (s)** y **Bytes (B)**.

### 🚀 5. Lanzamiento y Resiliencia (Fase M5: Operaciones)

* **SOP `provision` / `deploy`**: Prepara y sube la infraestructura como código.
* **SOP `health-check`**: Monitoreo constante de latencia y salud operativa.
* **SOP `auto-heal`**: Si el sistema detecta un fallo (ej. puerto bloqueado), se parchea a sí mismo creando una Spec de emergencia.

---

## 🏗️ II. CICLO DE VIDA: PASO A PASO DEL DIRECTOR

### 🛤️ Paso 1: Ignición del Taller (Fase 0)

1. **Enciende el Núcleo:** Desde `INFRA/`, lanza `docker compose up -d` para levantar el cerebro (Neo4j) y los datos (si el motor de docker esta down, levántalo con `systemctl start docker` o `sudo systemctl start docker`).
2. **Activa el Servidor MCP:** Asegúrate de que Antigravity ha iniciado `factory_mcp_server.py`. Este es el único canal autorizado.
3. **Crea el Chasis:** Ejecuta `./init_project.sh NombreProyecto` para generar las carpetas blindadas.

### 🛤️ Paso 2: La Visión del Producto (Fase M1)

1. Explica tu idea al `PRODUCT_OWNER`.
2. Instruye al agente para que ejecute el SOP `init-contract` vía MCP.
3. **Firma Obligatoria:** Si el ROI es correcto, edita `DOCS/USER/APPROVAL_M1.md` poniendo `Status: APPROVED`. Sin esto, el sistema se bloqueará por protocolo.

### 🛤️ Paso 3: Producción Inmunizada (Fase M2-M3)

1. Lanza el flujo de orquestación para ver las tareas pendientes.
2. Observa cómo los agentes entran en sesiones aisladas (`CLEAN_SESSION=True`), escriben código en `WORKSPACE/` y cierran tareas automáticamente.

### 🛤️ Paso 4: Cierre de Memoria (LTP)

1. Al finalizar el hito, ordena ejecutar el SOP **`sync-memory`**.
2. Esto graba las lecciones aprendidas en el Grafo de Neo4j para que la factoría no cometa los mismos errores en el próximo proyecto.

---

## 💡 III. TU NUEVO ROL ESTRATÉGICO

Bajo el estándar **v4.0-MCP**, ya no eres un depurador. Eres un **Auditor de la Verdad Física**:

1. **Soberanía del Disco:** Si un agente dice que terminó, verifica que el archivo exista en `03_COMPLETED/`. No aceptes promesas textuales.
2. **Rigor de Unidades SI:** Todo reporte debe usar **segundos (s)** y **bytes (B)**. El lenguaje de la factoría es matemático.
3. **Nemo Safety:** Mantén la ética industrial. Absoluta prohibición de analogías de consumo animal en cualquier documento.

---
*Guía de Experiencia de Usuario v4.0-MCP | Director de Operaciones Solidificado.*
