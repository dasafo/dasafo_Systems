# 🏛️ Manual Maestro de Instrucciones | dasafo_Systems v3.4.0-S

**dasafo_Systems** es un ecosistema industrial de Inteligencia Artificial de alto rendimiento, diseñado para el desarrollo de software bajo el estándar **v3.4.0-S "Industrial Core"**. Este manual es la **Fuente Única de Verdad (SSoT)** que define la arquitectura, protocolos y soberanía técnica del sistema.

---

## 🏗️ 1. ARCHITECTURE NODES (El Ecosistema)

El sistema se divide en tres nodos lógicos y físicos que garantizan el aislamiento y la escalabilidad industrial:

### 🧠 A. `dasafo_FACTORY` (The Core)
El corazón inmutable. Contiene la identidad de los agentes, las leyes de la factoría y el motor ejecutivo.
- **`00_GLOBAL_KNOWLEDGE`**: Constitución, Mandatos SI y Plantillas Industriales.
- **`01-05 Depts`**: Jerarquía de 15 agentes especializados.
- **`06_SKILL_LIBRARY`**: El **Top 18 Hub**. Repositorio central de habilidades atómicas (`run.py`).

### ⚡ B. `INFRA` (The Power Grid)
Nodo de servicios compartidos autogestionados mediante **Docker Compose**.
- **Postgres (`shared-db`)**: Almacenamiento relacional operativo (Malla 2GB).
- **Neo4j (`kg-db`)**: Grafo de conocimiento central (Malla 4GB).
- **Redis (`cache-node`)**: Caché de estado y tareas en tiempo real.
- **Glances**: Monitor de telemetría y salud del grid (Puerto 61208).

### 📦 C. `PROJECTS` (The Workshop)
Espacio mutable donde se ejecutan las misiones. Cada proyecto es un entorno **SDD (Spec Driven Development)** aislado.

---

## ⚙️ 2. THE INDUSTRIAL ENGINE (El Motor de Ejecución)

La factoría opera mediante un sistema de ejecución por contratos y compuertas físicas:

### 📡 `factory_cli.py` (MCP Bridge)
Servidor MCP que comunica la IA con las herramientas de la factoría. Implementa el **Session Hook** (Aduana Universal) en cada llamada.

### 🛂 `session_hook.py` (Aduana Universal)
Middleware de seguridad que intercepta ejecuciones.
- **Regla de Cierre:** Bloquea cualquier skill no autorizada si el estado en `PROJECT_STATE.json` es inconsistente.
- **Fase Segura:** Exige que las fases se completen secuencialmente (M1 -> M2 -> M3...).
- **Proof of Build:** En fases técnicas (M3/M4), exige la existencia física de `BUILD_REPORT.json`.

### 🧪 `skill_engine.py` (The Executive)
Cargador dinámico de habilidades con **Solidity Guard** integrado.
- **Pre-Flight:** Inyecta automáticamente credenciales desde `INFRA/.env`.
- **Post-Flight Verification:** Verifica físicamente que los artefactos declarados por la skill existan en disco antes de devolver éxito.
- **Phase-Gate Enforcement:** Evita "saltos de fase" accidentales en el estado del proyecto.

---

## 🚀 3. CICLO DE VIDA DE PROYECTO (Phase-Gate Logic)

### 👶 A. Inicialización (`init_project.sh`)
El script de arranque provisiona el chasis blindado del proyecto:
1. **Squeleto SDD:** Crea `DOCS/`, `TASKS/`, `WORKSPACE/` y `LOGS/`.
2. **Registry:** Genera `registry.json` y `PROJECT_STATE.json` (Fase M1: Discovery).
3. **Contrato Maestro:** Siembra el `PRP_CONTRACT.json` en la raíz para ser definido por el **PRODUCT_OWNER**.

### 📜 B. El Mandato de 12 Secciones (PRP)
Ningún proyecto avanza a M3 (Producción) sin un **PRP_MASTER** firmado. Debe incluir:
- Objetivos, Historias de Usuario, Riesgos, Contratos de Datos y **Métricas SI** numéricas.

---

## 🛡️ 4. SEGURIDAD Y SOLIDEZ (Solidify Guard)

- **Mandato SI:** Todas las métricas de rendimiento, tiempo o recursos deben expresarse en **Segundos (s)** y **Bytes (B)**.
- **Zero-Trust Secret Scanner:** Escaneo mandatorio de secretos antes de cualquier commit o cierre de tarea.
- **Clean Session Protocol:** Los agentes de producción operan en "Sesiones Limpias", con acceso limitado únicamente a lo definido en la especificación (`SPEC_LITE.json`).
- **Antifragilidad:** Todo error técnico se registra en el `FEEDBACK-LOG.md` del proyecto para ser analizado por el **FACTORY_EVOLVER**.

---

## 🕹️ 5. COMANDOS DE CONTROL (Slash Commands)

| Comando | Acción | Impacto Industrial |
| :--- | :--- | :--- |
| **`/init-contract`** | Activa al PRODUCT_OWNER | Genera el PRP_MASTER de 12 secciones. |
| **`/factory-orchestrate`** | Avanza la Aduana | Convierte PRP en tareas atómicas y abre la siguiente compuerta. |
| **`/scan`** | Auditoría de Seguridad | Ejecuta el Secret Scanner y QA Tester sobre el código. |
| **`/factory-status`** | Reporte de Estado | Muestra la verdad física del disco vs el progreso reportado. |

---

## 🍱 6. GESTIÓN DE INFRAESTRUCTURA (Ops)

1. **Setup:** `cd dasafo_Systems/INFRA`.
2. **Config:** `cp .env.shared .env` y configurar secretos reales.
3. **Boot:** `docker-compose up -d`.
4. **Resilience:** Los servicios corren sobre `dasafo_network` y son accesibles por las skills mediante inyección dinámica de entorno.

---
*Manual Maestro v3.4.0-S | dasafo_Systems — Industrializando la Excelencia.*
