# 🎮 Guía de Experiencia de Usuario (UX): Director de Operaciones

<ctrl94> **"Tú no escribes código. Tú orquestas departamentos y validas evidencias físicas."**

Bienvenido, Director de Operaciones. Bajo el estándar **v4.0-S Industrial Core**, tu rol ha evolucionado de la micro-gestión técnica a la **estratégica funcional**. El sistema ahora cuenta con **Auto-Start**, **Auto-Commit** y **Inmunización Predictiva**, eliminando la necesidad de supervisar cada movimiento de tus agentes.

---

## 🗺️ I. TU CONSOLA DE MANDO (Los 14 Workflows)

Has sido dotado con una botonera de comandos slash (`/`) que activan procesos industriales completos. Úsalos siguiendo el flujo cronológico del proyecto:

### ⚡ 1. Estrategia y Visión (Fase M1: Discovery)
*   **`/init-contract`**:
    *   **Propósito:** Es la primera piedra. El `PRODUCT_OWNER` analiza tu idea y la convierte en un contrato formal de 12 secciones (`PRP_MASTER.json`).
    *   **Valor:** Inyecta proyecciones de ROI, CAC y LTV. Si el proyecto no es financieramente viable, el agente te lo dirá aquí.
    *   **Acción:** Revisa el resumen y firma con un "Aprobado".

### 📋 2. Deconstrucción y Refuezo (Fase M2: Arquitectura)
*   **`/factory-orchestrate`**:
    *   **Propósito:** Sincroniza la "Aduana Universal". Deconstruye el contrato en tareas atómicas (`SPEC_LITE.json`).
    *   **Valor:** Si el disco no coincide con el registro, este comando lo arregla físicamente.
*   **`/validate-backbone`**:
    *   **Propósito:** El inspector de andamiaje. Nadie pone una línea de lógica hasta que el esqueleto (Next.js, FastAPI, Docker) esté físicamente en disco.
    *   **Valor:** Previene la construcción en el vacío y asegura la solidez del framework.

### 🏭 3. Línea de Montaje (Fase M3: Producción)
*   **`/execute-task`**:
    *   **Propósito:** El comando más potente. Lanza una sesión aislada para que un peón ejecute una tarea pendiente.
    *   **Automatización Industrial (v4.0-S):**
        1. **Auto-Start:** Mueve la tarea a `IN_PROGRESS`.
        2. **Inmunización:** Inyecta "Reglas de Oro" de Neo4j en la mente del peón para que no repita errores de proyectos pasados.
        3. **Auto-Commit:** Tras el éxito, mueve la tarea a `COMPLETED` y actualiza el registro por ti.

### 🛡️ 4. Aduana de Calidad (Fase M4: Compliance)
*   **`/scan`**:
    *   **Propósito:** Escaneo de seguridad Zero-Trust. El `SECURITY_AUDITOR` caza secretos, claves API y vulnerabilidades en dependencias.
    *   **Riesgo:** Si falla, la tarea se bloquea. **Zero Leaks allowed.**
*   **`/audit`**:
    *   **Propósito:** El sello de calidad. El `QA_TESTER` revisa que el código cumple con el contrato y reporta en **Segundos (s)** y **Bytes (B)**.
    *   **Valor:** Detecta violaciones contra la constitución de la factoría.

### 🚀 5. Lanzamiento y Resiliencia (Fase M5: Operaciones)
*   **`/provision`**: Prepara la infraestructura como código (Docker, Cloud) en la carpeta `WORKSPACE/infra/`.
*   **`/deploy`**: Sube los artefactos al entorno en vivo.
*   **`/health-check`**: El monitor sentinel verifica latencia y salud constante.
*   **`/auto-heal`**: Sistema inmunológico. Si algo falla en producción, el sistema crea una Spec de emergencia y se parchea solo.

---

## 🏗️ II. CICLO DE VIDA: PASO A PASO DEL DIRECTOR

### 🛤️ Paso 1: Ignición del Taller (Fase 0)
Antes de nada, prepara el flujo de energía:
1.  **Enciende el Núcleo:** Desde la terminal en `INFRA/`, lanza `docker-compose up -d`. Esto levanta el cerebro (Neo4j) y el sistema de datos.
2.  **Crea el Chasis:** Ejecuta `./init_project.sh NombreProyecto`. Esto genera las carpetas industriales blindadas.

### 🛤️ Paso 2: La Visión del Producto (Fase M1)
1.  Llama al `PRODUCT_OWNER` y explícale tu visión.
2.  Ejecuta `/init-contract`. El sistema te entregará un resumen financiero pesado. Si te gusta, fírmalo.

### 🛤️ Paso 3: Producción Inmunizada (Fase M2-M3)
1.  Lanza `/factory-orchestrate` para ver las tareas en `01_PENDING`.
2.  Valida la estructura con `/validate-backbone`.
3.  Comanda `/execute-task`. Observa cómo los agentes entran en sus sesiones, se autogestionan, escriben código y cierran la tarea sin que tú muevas un dedo.

### 🛤️ Paso 4: Auditoría y Despliegue (Fase M4-M5)
1.  Audita la seguridad con `/scan`.
2.  Audita la solidez con `/audit`.
3.  Lanza `/provision` y `/deploy`.
4.  Mantén el sistema vivo con `/health-check` y deja que el `/auto-heal` se encargue de las caídas nocturnas.

---

## 💡 III. TU NUEVO ROL ESTRATÉGICO

En **v4.0-S**, ya no eres un depurador de bugs. Eres un **Auditor de la Verdad Física**:

1.  **Corrige el "Qué" (Specs), no el "Cómo":** Si un agente falla, no edites su código. Edita su `SPEC_LITE.json` o la `PRP_MASTER.json` y relanza la tarea. El sistema aprenderá del error.
2.  **Rigor Métrico:** Rechaza cualquier reporte que no use **segundos (s)** y **bytes (B)**. El lenguaje industrial es matemático.
3.  **LTP (Persistencia a Largo Plazo):** Usa `/sync-memory` al final de cada hito. Esto graba las lecciones aprendidas en el Grafo de Neo4j para que la factoría herede inteligencia acumulativa.

---
*Manual de Operaciones v4.0-S | Director de Operaciones Solidificado.*
