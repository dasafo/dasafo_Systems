# 🏛️ Manual Maestro de Instrucciones | dasafo_Systems v4.0-S

**dasafo_Systems** es un ecosistema industrial de Inteligencia Artificial de alto rendimiento, diseñado para el desarrollo de software bajo el estándar **v4.0-S "Industrial Core"**. Este manual es la **Fuente Única de Verdad (SSoT)** que define la arquitectura, protocolos y soberanía técnica del sistema.

---

## 🏗️ 1. ARCHITECTURE NODES (El Ecosistema)

El sistema se divide en tres nodos lógicos y físicos que garantizan el aislamiento y la escalabilidad industrial:

### 🧠 A. `dasafo_FACTORY` (The Core)

El corazón inmutable. Contiene la identidad de los agentes, las leyes de la factoría y el motor ejecutivo.

- **`00_GLOBAL_KNOWLEDGE`**: Constitución, Mandatos SI y Plantillas Industriales.
- **`01-05 Hubs`**: Jerarquía de 16 agentes especializados divididos en 5 departamentos (Estrategia, Arquitectura, Producción, Cumplimiento y Operaciones).
- **`06_SKILL_LIBRARY`**: El Repositorio Central. Contiene las herramientas atómicas (`run.py`), incluyendo validadores financieros, de andamiaje y motores de auto-sanación.

### ⚡ B. `INFRA` (The Power Grid)

Nodo de servicios compartidos autogestionados mediante **Docker Compose**.

- **Postgres (`shared-db`)**: Almacenamiento relacional operativo (Malla 2GB).
- **Neo4j (`kg-db`)**: Grafo de conocimiento central. Almacena las "Golden Rules" y previene alucinaciones futuras (LTP).
- **Redis (`cache-node`)**: Caché de estado y tareas en tiempo real.
- **Glances**: Monitor de telemetría y salud del grid (Puerto 61208).

### 📦 C. `PROJECTS` (The Workshop)

Espacio mutable donde se ejecutan las misiones. Cada proyecto es un entorno **SDD (Spec Driven Development)** aislado.

---

## ⚙️ 2. THE INDUSTRIAL ENGINE (El Motor de Ejecución)

La factoría opera mediante un sistema de ejecución por contratos y compuertas físicas (DAST):

### 📡 `factory_cli.py` (MCP Bridge)

Servidor MCP que comunica la IA con las herramientas de la factoría. Implementa el **Session Hook** (Aduana Universal) en cada llamada y reporta el estado de los Hubs.

### 🛂 `session_hook.py` (Aduana Universal)

Middleware de seguridad que intercepta ejecuciones.

- **Regla de Cierre:** Bloquea cualquier skill no autorizada si el estado en `PROJECT_STATE.json` es inconsistente.
- **Double-Gating v4.0-S:** Permite a los agentes ejecutar tareas autónomamente si poseen una `SPEC_LITE.json` o una `EMERGENCY_SPEC.json` física asignada en disco.
- **Fase Segura:** Exige que las fases se completen secuencialmente (M1 -> M5) y verifica evidencias físicas (ej. `BUILD_REPORT.json`).

### 🧪 `skill_engine.py` (The Executive)

Cargador dinámico de habilidades con **Solidity Guard** integrado.

- **Pre-Flight:** Inyecta automáticamente credenciales y permisos de fase desde `INFRA/.env`.
- **Post-Flight Verification:** Verifica físicamente que los artefactos declarados por la skill existan en disco antes de devolver éxito.

---

## 🚀 3. CICLO DE VIDA DE PROYECTO (Phase-Gate Logic)

### 👶 A. Inicialización (`init_project.sh`)

El script de arranque provisiona el chasis blindado del proyecto en versión **v4.0-S**:

1. **Squeleto SDD:** Crea `DOCS/`, `TASKS/`, `WORKSPACE/` y `LOGS/`.
2. **Registry:** Genera `registry.json` y `PROJECT_STATE.json` (Fase M1: Discovery).
3. **Contrato Maestro:** Siembra el `PRP_CONTRACT.json` en la raíz.

### 📜 B. El Mandato de 12 Secciones y Lógica Financiera (PRP)

Ningún proyecto avanza a M2 sin un **PRP_MASTER** firmado. Este debe incluir:

- Objetivos, Riesgos, Contratos de Datos, **Métricas SI** (s, B) y **KPIs Financieros** obligatorios (Target CAC, Target LTV) calculados vía `startup-metrics-framework`.

### 🏗️ C. Backbone y Prevención (M2-M3)

Antes de escribir código de producción:

- El `project-backbone-validator` audita que el andamiaje del framework exista físicamente.
- El Orquestador consulta Neo4j para inyectar reglas anti-alucinación en la Spec basadas en el historial de la factoría.

---

## 🛡️ 4. SEGURIDAD, SOLIDEZ Y AUTO-SANACIÓN

- **Mandato SI:** Todas las métricas de rendimiento deben expresarse en **Segundos (s)** y **Bytes (B)**.
- **Zero-Trust Secret Scanner:** Escaneo mandatorio de secretos antes de cualquier commit o cierre de tarea.
- **Clean Session Protocol:** Los agentes operan en "Sesiones Limpias", con acceso limitado a lo definido en su especificación.
- **Sistema Inmunológico (Auto-Heal):** Si un despliegue falla por conflictos de infraestructura, el SRE genera una alerta atómica y el `FACTORY_EVOLVER` parchea automáticamente el código.
- **Persistencia a Largo Plazo (LTP):** Las *Cultural Violations* detectadas en auditorías se inyectan en Neo4j como nodos de aprendizaje, creando una memoria muscular a prueba de fallos.

---

## 🕹️ 5. COMANDOS DE CONTROL (Slash Commands Universales)

| Comando | Hub | Impacto Industrial |
| :--- | :--- | :--- |
| **`/init-contract`** | L01 | Genera el PRP_MASTER con proyecciones financieras (CAC/LTV). |
| **`/factory-orchestrate`** | L01 | Convierte PRP en tareas atómicas (`SPEC_LITE`) y sincroniza el Kanban. |
| **`/validate-backbone`** | L01 | Verifica físicamente el esqueleto del proyecto antes de producir. |
| **`/arch-diagram`** | L02 | Dibuja la arquitectura en formato Mermaid. |
| **`/execute-task`** | L03 | Lanza una sesión limpia de producción con guardarraíles de Neo4j. |
| **`/scan`** | L04 | Ejecuta el Secret Scanner bajo estándar Zero-Trust. |
| **`/audit`** | L04 | Valida calidad y cumplimiento de SI Units. Detecta violaciones culturales. |
| **`/provision`** | L05 | Aprovisiona infraestructura como código (Docker/Terraform). |
| **`/deploy`** | L05 | Despliega los artefactos verificados al entorno Live. |
| **`/health-check`** | L05 | Verifica latencia y salud en tiempo real (M5). |
| **`/auto-heal`** | L05 | Dispara el parcheo autónomo de infraestructura caída. |
| **`/sync-memory`** | L05 | Convierte logs temporales en Engramas permanentes dentro de Neo4j. |
| **`/factory-status`** | All | Reporte de progreso de fases y salud de Hubs. |
| **`/kanban-board`** | All | Lanza el dashboard visual en el puerto 3001. |

---

## 🍱 6. GESTIÓN DE INFRAESTRUCTURA (Ops)

1. **Setup:** `cd INFRA`.
2. **Config:** `cp .env.shared .env` y configurar secretos reales.
3. **Boot:** `docker-compose up -d`.
4. **Resilience:** Los servicios corren sobre `dasafo_network`. El Grafo Neo4j (`kg-db`) es el cerebro persistente de la factoría y no debe ser borrado entre proyectos.

---
*Manual Maestro v4.0-S | dasafo_Systems — Industrializando la Excelencia Evolutiva.*
