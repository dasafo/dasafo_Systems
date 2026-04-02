# 🌍 Dasafo Factory | GLOBAL KNOWLEDGE (v4.0-S Solidificada)

> **Versión Actual:** v4.0-S "Industrial Core - Double-Gate Enabled"
> **Estado Operativo:** Producción / Industrialización Completa
> **Gobernanza:** Zero-Trust / Spec-Driven Development (SDD) / Mandato SI

---

## 📜 I. LA CONSTITUCIÓN CORE (v4.0-S)

### 1. Spec-Driven Development (SDD)
- **Spec Sobre Todo:** No se inicia ninguna misión sin un `PRP_MASTER.json` (Fase M1) o `SPEC_LITE.json` (Ejecución).
- **Aislamiento de Fase:** Las transiciones entre M1 y M5 están bloqueadas físicamente por la presencia de artefactos en disco. Sin artefacto, no hay transición.
- **Mandato de Resultado:** Toda tarea debe terminar con un reporte "Zero Fluff": `status`, `artifacts` y `summary`.

### 2. Context Isolation (Clean Sessions)
- **Soberanía de Memoria:** Los agentes operan bajo `CLEAN_SESSION=True`. El acceso está restringido estrictamente a los `context_pointers` autorizados.
- **Política No-Noise:** El `FEEDBACK-LOG` es un sustrato técnico, no un chat compartido. Es procesado y comprimido por el `MEMORY_OPTIMIZER`.
- **Artifact-First:** La comunicación entre agentes se realiza mediante cambios en archivos, eliminando hilos conversacionales infinitos.

### 3. Zero-Trust & Solidity
- **Acceso Quirúrgico:** Los agentes no tienen permisos de escritura fuera de su dominio técnico o las capas de lógica del proyecto.
- **Solidity Gate:** El cierre de hitos requiere validación de `kanban-solidity-gate` y clearance del `SECURITY_AUDITOR`.
- **Valla de Chesterton:** Prohibido borrar código legado sin un ADR (Architecture Decision Record) que justifique el "Por qué".
- **Mandato Backbone:** No se realiza implementación atómica sin validación previa física del andamiaje (scaffolding) mediante el `project-backbone-validator`.

### 4. Métricas Industriales (Estándares SI)
- **Precisión Temporal:** Siempre expresada en **Segundos (s)**.
- **Precisión de Recursos:** Siempre expresada en **Bytes (B)**.

### 5. Soberanía de Infraestructura (LTP)
- **Persistencia a Largo Plazo (LTP):** Todo aprendizaje agentico, fallo crítico o insight arquitectónico debe sincronizarse al Grafo de Conocimiento compartido (`kg-db` / Neo4j) como "Golden Rules".
- **Descubrimiento de Servicios:** Los agentes priorizan el uso de hostnames industriales (`dasafo-shared-db`, `dasafo-shared-kg`).
- **Ejecución Local, Conocimiento Global:** Los archivos residen localmente, pero el conocimiento se persiste globalmente para la evolución de la factoría.

---

## 🛠️ II. ARQUITECTURA Y CICLO DE VIDA (M1-M5)

1. **M1: Discovery & Finance:** Market fit, proyección ROI (CAC/LTV) y firma del `PRP_MASTER.json`.
2. **M2: Architecture & Foundation:** Provisión de infra, definiciones DTO y validación de Backbone.
3. **M3: Implementation (Atomic):** Desarrollo basado en SDD con guardarraíles predictivos inyectados desde Neo4j LTP.
4. **M4: Validation & Quality (QA):** Auditoría industrial, validación de contratos y escaneo de secretos.
5. **M5: Ops & Auto-Heal:** Despliegue, monitoreo Sentinel en tiempo real y parches de auto-sanación.

### 🏛️ Separación de Capas (SoC)
- `/domain`: Lógica de negocio pura, sin dependencias.
- `/application`: Orquestación de casos de uso y flujo de lógica.
- `/infrastructure`: Adaptadores, bases de datos y gateways externos.
- `/ui`: Capa de renderizado mudo / componentes de diseño atómico.

---

## 🚀 III. ESTRATEGIA DE CRECIMIENTO Y MARKETING

Gestionado por `MARKETING_GROWTH` mediante `social-content-strategy` y `apify-trend-analysis`.

- **Hooks Basados en Valor:** Mensajería directa basada en métricas SI (ROI en s, B).
- **Estética Industrial:** Modos oscuros premium, glassmorphism y tokens de diseño responsivo.
- **Mandato Ético:** Cero menciones a analogías de carne/matadero (Factoría Vegetariana).

---

## 📊 IV. TELEMETRÍA DE MISIÓN (Sistema Pulse)

Todo reporte de auditoría o ciclo de vida DEBE incluir:
- **Resource Delta:** Consumo de tokens, Delta de almacenamiento (B), Sobrecarga de red (B).
- **Performance:** Tiempo de ejecución (s), Tasa de éxito (%), Profundidad DAG.
- **Systemic Health:** Puntuación de Solidez (1-10), Tasa de alucinación (Target: 0%), Evidencia Disk IO.

---

## ✅ V. PROTOCOLO DE APROBACIÓN (SIGN-OFF)

La transición entre fases requiere la **Plantilla de Aprobación de Hitos**:
1. **Artefactos Físicos:** Evidencia documentada en `DOCS/` (Blueprints, ADRs).
2. **Chequeo de Solidez:** Log de `kanban-solidity-gate` confirmado como SOLIDIFIED.
3. **Clearance de Seguridad:** Resultado de `agentic-thought-secret-scanner`: PASSED.
4. **Rigor Técnico:** Métricas validadas en Unidades SI (s, B).
5. **Human Sign-off (HITL):** Firma del usuario obligatoria para M1 y M5 (Release final).

---

## 📝 VI. ESQUEMA DE FEEDBACK Y APRENDIZAJE

Las anomalías se registran como objetos JSON procesables para permitir la mejora autónoma vía `FACTORY_EVOLVER`:

```json
{
  "id": "FB-XXXX",
  "version": "v4.0-S",
  "timestamp": "ISO_8601_TIMESTAMP",
  "context": {
    "agent": "ID_AGENTE_AUTORIZADO",
    "project": "NOMBRE_PROYECTO",
    "phase": "M[1-5]_FASE"
  },
  "severity": "critical | high | medium | low",
  "error_description": "Definición técnica precisa de la desviación",
  "correction": "Acción inmediata de corrección / mitigación",
  "golden_rule": "Regla universal derivada para prevención futura",
  "categories": ["security", "infrastructure", "performance", "solidity-guard"]
}
```

---
*Ratificado: 2026-04-02 | Dasafo Factory v4.0-S Industrialized Spanish Edition.*
