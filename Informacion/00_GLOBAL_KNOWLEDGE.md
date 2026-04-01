# 🌍 Dasafo Factory | GLOBAL KNOWLEDGE

> **Versión Actual:** v4.0-S "SDD Optimized Core"  
> **Estado:** Operativo (Rigor Industrial)  
> **Gobernanza:** Zero-Trust / Specs / Clean Sessions

---

## 📜 I. LA CONSTITUCIÓN CORE (v4.0-S)

### 1. Spec Driven Development (SDD)

- **Nada existe sin Spec:** No se inicia trabajo sin un `PRP_MASTER.json` (Fase M1) o `SPEC_LITE.json` (Ejecución).
- **Aislamiento de Fase:** El paso entre fases (M1-M5) está bloqueado físicamente por artefactos en disco. Sin artefacto, no hay transición.
- **Mandato de Resultado:** Toda tarea finaliza con un reporte "Zero Fluff": `status`, `artifacts`, `summary`.

### 2. Context Isolation (Clean Sessions)

- **Memory Sovereignty:** Los agentes operan bajo `CLEAN_SESSION=True`. Solo leen los `context_pointers` autorizados por el Orquestador.
- **No-Noise Policy:** El `FEEDBACK-LOG` es un sustrato técnico, no una conversación. Se poda mediante el `MEMORY_OPTIMIZER`.
- **Artifact-First:** La comunicación entre agentes es vía cambios en el sistema de archivos, eliminando hilos conversacionales infinitos.

### 3. Zero-Trust & Solidity

- **Acceso Quirúrgico:** Sin permisos fuera del dominio técnico asignado.
- **Solidity Gate:** Ninguna fase cierra sin validación de `kanban-solidity-gate` y clearance de `SECURITY_AUDITOR`.
- **Chesterton's Fence:** Prohibido borrar código sin un ADR (Architecture Decision Record) que explique el "Por qué".

### 4. Métricas Industriales y Financieras

- **Precisión Temporal:** Siempre en Segundos (s).
- **Precisión de Recursos:** Siempre en Bytes (B).
- **Viabilidad (ROI):** Todo proyecto requiere un Target CAC y LTV definido en M1.

### 5. Infraestructura Híbrida (LTP)

- **Persistencia LTP:** Todo aprendizaje agentico o fallo crítico debe registrarse en el Grafo de Conocimiento compartido (`kg-db` / Neo4j) como "Golden Rules".
- **Service Discovery:** Las Skills deben priorizar el uso de los hostnames industriales (`dasafo-shared-db`, `dasafo-shared-kg`).
- **Aislamiento Local:** Los archivos fuente residen en el `target_project`, garantizando que la ejecución sea efímera pero el conocimiento permanente.

---

## 🛠️ II. ARQUITECTURA DE PROYECTOS

### 1. Ciclo de Vida (M1-M5)

1. **M1: Discovery & Finance:** Definición técnica, KPIs financieros y firma de `PRP_MASTER.json`.
2. **M2: Architecture & Foundation:** Setup de infraestructura, validación de Backbone y DTOs básicos.
3. **M3: Implementation (Atomic):** Desarrollo en sprints atómicos con guardarraíles predictivos inyectados desde Neo4j.
4. **M4: Validation & QA:** Pruebas de integración, detección de *Cultural Violations* y `kanban-solidity-gate`.
5. **M5: Ops & Auto-Heal:** Despliegue, monitoreo Sentinel, Auto-Sanación de Infraestructura y consolidación de memoria.

### 2. Estructura de Directorios (Top Down)

- `/domain`: Lógica pura, sin dependencias externas.
- `/application`: Orquestación de casos de uso.
- `/infrastructure`: Adaptadores, bases de datos, APIs externas.
- `/ui`: Interfaz "muda" (renders data only).

---

## 🚀 III. ESTRATEGIA DE CRECIMIENTO (G1-G3)

Para sistemas en producción que requieren escalabilidad industrial.

- **G1 (Tuning):** Benchmarking con unidades SI (s, B). Capacidad hasta 10k conc.
- **G2 (Scale-Out):** Extracción de microservicios y modularización estricta.
- **G3 (Redundancy):** Despliegue cross-region y test de failover.

---

## 📡 IV. TELEMETRÍA Y SISTEMA PULSE

Toda auditoría de sistema debe reportar:

- **ResponseTime (s):** Latencia media.
- **MemoryUsage (B):** Tamaño del heap.
- **NodeStatus:** (OK/Degraded/Critical).
- **ResourceDrift (%):** Desviación respecto a la especificación original.

---

## ✅ V. PROTOCOLO DE APROBACIÓN (SIGN-OFF)

Antes de finalizar cualquier proyecto (`PRP_FINAL_SIGN_OFF`):

1. **Infra:** Secrets y Variantes fijadas (Pinned).
2. **Gov:** `PRP_CONTRACT.json` sincronizado.
3. **Code:** 0 Errores de Lint (`solidity-gate`).
4. **Docs:** `WALKTHROUGH.md` actualizado al código real.

---

## 📝 VI. FEEDBACK SCHEMA (INDUSTRIAL)

Cada iteración o fallo debe generar un objeto de feedback estructurado según `FEEDBACK_SCHEMA.json` para su análisis automático por el `FACTORY_EVOLVER`:

```json
{
  "id": "ERR-XXXX",
  "version": "v4.0-S",
  "timestamp": "2026-03-30T17:52:00Z",
  "context": {
    "agent": "ORCHESTRATOR",
    "project": "CurrentProject",
    "phase": "M1_DISCOVERY"
  },
  "severity": "critical | high | medium | low",
  "error_description": "Descriptivo y técnico",
  "correction": "Acción inmediata tomada",
  "golden_rule": "Regla para prevenir recurrencia",
  "categories": ["security", "infrastructure", "solidity-guard"]
}
