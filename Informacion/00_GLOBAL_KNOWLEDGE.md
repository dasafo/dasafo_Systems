# 🌍 Dasafo Factory | GLOBAL KNOWLEDGE (v5.0-MCP Solidificada)

> **Versión Actual:** v5.0-MCP "Native Industrial Core"
> **Estado Operativo:** Producción / Industrialización Completa
> **Gobernanza:** Zero-Trust / Spec-Driven Development (SDD) / Human-Gate (HITL)

---

## 📜 I. LA CONSTITUCIÓN CORE (v5.0-MCP)

### 1. La Ley de la Spec (SDD)

- **Spec Sobre Todo:** No se inicia ninguna misión sin un `PRP_MASTER.json` (Fase M1) o `SPEC_LITE.json` (Ejecución).
- **Aislamiento de Fase:** Las transiciones (M1-M5) están bloqueadas físicamente por la presencia de artefactos en disco. Sin evidencia física, no hay avance.
- **Soberanía del Director (HITL):** Ninguna transición de fase es válida sin un artefacto de aprobación firmado por un humano en `DOCS/USER/APPROVAL_MX.md`. El estatus debe ser explícitamente `Status: APPROVED`.

### 2. Context Isolation (Clean Sessions)

- **Soberanía de Memoria:** Los agentes operan bajo `CLEAN_SESSION=True`. Solo leen los `context_pointers` autorizados por el Orquestador.
- **Artifact-First:** La comunicación entre agentes se realiza mediante cambios en el sistema de archivos, eliminando hilos conversacionales infinitos.
- **Política No-Noise:** El `FEEDBACK-LOG` es un sustrato técnico para el `MEMORY_OPTIMIZER`, no un historial de chat.

### 3. El Mandato MCP (Zero-Trust)

- **Prohibición de Terminal:** El uso de comandos de terminal (`bash`, `sh`) o ejecución directa de scripts está estrictamente prohibido para operaciones de la fábrica.
- **Invocación Directa:** Los agentes DEBEN invocar sus herramientas MCP directamente por nombre (ej. `prp-generator`, `kanban-solidity-gate`) a través del servidor `dasafo_FACTORY_Core_v5.0`.
- **Mandato Backbone:** Ningún agente de implementación puede ser despachado sin la validación previa física del andamiaje mediante `project-backbone-validator`.
- **Valla de Chesterton:** Prohibido borrar código legado sin un ADR (Architecture Decision Record) que justifique la acción.

### 4. Métricas Industriales (Estándares SI)

- **Precisión Temporal:** Siempre expresada en **Segundos (s)**.
- **Precisión de Recursos:** Siempre expresada en **Bytes (B)**.

### 5. Persistencia a Largo Plazo (LTP)

- **Conocimiento Permanente:** Todo aprendizaje, fallo crítico o decisión arquitectónica DEBE registrarse en el Grafo de Conocimiento compartido (Neo4j - `kg-db`).
- **Descubrimiento de Servicios:** Las habilidades priorizan los hostnames industriales `dasafo-shared-db` (relacional) y `dasafo-shared-kg` (semántico).

---

## 🛠️ II. ARQUITECTURA Y CICLO DE VIDA (M1-M5)

1. **M1: Discovery & Finance:** Market fit, ROI financiero y firma del Contrato Maestro.
2. **M2: Architecture & Foundation:** Provisión de infra (IaC), definiciones DTO y validación de Backbone.
3. **M3: Implementation (Atomic):** Desarrollo basado en Specs con guardarraíles predictivos inyectados vía Neo4j.
4. **M4: Validation & Quality (QA):** Auditoría industrial y escaneo Zero-Trust de secretos.
5. **M5: Ops & Auto-Heal:** Despliegue, monitoreo de salud y persistencia de memoria final.

---

## 🚀 III. ESTRATEGIA DE CRECIMIENTO (Go-To-Market)

Basada en el template `growth_strategy.md`:

- **Propuesta de Valor Empírica:** Enfoque en soluciones industrializadas, no herramientas genéricas.
- **ROI Técnico:** Análisis basado en métricas SI (ROI en s, B).
- **Estética Industrial:** Voz quirúrgica y directa. Diseño visual basado en dark mode y glassmorphism.
- **Mandato Ético:** Factoría Vegetariana (prohibidas analogías de explotación animal).

---

## 📊 IV. TELEMETRÍA DE MISIÓN (Sistema Pulse)

Basada en el template `telemetry.md`. Todo reporte DEBE incluir:

- **Consumo de Recursos (B):** Delta de almacenamiento, overhead de red, consumo de tokens.
- **Rendimiento (s):** Tiempo de ejecución, tasa de éxito, profundidad del grafo DAG.
- **Salud Sistémica:** Puntuación de Solidez (1-10), Tasa de alucinación (Meta: 0%), Evidencia DAST (Disk IO Truth).

---

## ✅ V. PROTOCOLO DE APROBACIÓN (Sign-off)

La transición requiere la **Plantilla de Aprobación** (`approval.md`):

1. **Evidencia Física:** Artefactos probatorios en `DOCS/`.
2. **Solidity Gate:** Log de ejecución de `kanban-solidity-gate` confirmado.
3. **Seguridad:** Clearance de `agentic-thought-secret-scanner` (PASSED).
4. **Firma Humana:** Obligatoria en `DOCS/USER/APPROVAL_MX.md`.

---

## 📝 VI. ESQUEMA DE FEEDBACK (LTP)

```json
{
  "id": "FB-XXXX",
  "version": "v5.0-MCP",
  "timestamp": "ISO_8601",
  "context": { "agent": "ID", "project": "NAME", "phase": "M[1-5]" },
  "severity": "critical | high | medium | low",
  "error_description": "Definición técnica precisa",
  "golden_rule": "Regla derivada para Neo4j",
  "categories": ["security", "infrastructure", "performance", "solidity-guard"]
}
```

---
*Ratificado: 2026-04-04 | Dasafo Factory v5.0-MCP Industrialized Spanish Edition.*
