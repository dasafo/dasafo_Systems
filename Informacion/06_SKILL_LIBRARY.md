# 🧰 Categoría 06: SKILL LIBRARY | Dasafo Factory (v3.4.0-S)

La **Skill Library** es el repositorio central de capacidades atómicas de la factoría. Cada skill es un módulo de ejecución independiente, diseñado bajo el estándar **v3.4.0-S**, con esquemas de entrada/salida rígidos y mandatos de seguridad integrados.

---

## 🚀 1. Core Orchestration & Management
*Capacidades críticas para la gestión del ciclo de vida del proyecto.*

- **delegate-clean-session**: Lanza sub-agentes en entornos aislados para evitar el "Token Decay" del Orquestador.
- **prp-generator**: Motor dual para generar Contratos Maestros (PRP_MASTER) y Especificaciones Atómicas (SPEC_LITE).
- **project-management**: Sincroniza el estado físico del proyecto con reportes diarios (Standups) y semanales.
- **kanban-solidity-gate**: Puerta de aduana física que bloquea transiciones de fase si existen tareas pendientes en disco.

---

## 📐 2. Architecture & Design
*Herramientas para la creación de planos técnicos y sistemas de diseño.*

- **architecture-decision-records (ADR)**: Registro inmutable de decisiones técnicas y sus compensaciones (trade-offs).
- **api-contract-generator**: Diseño de contratos OpenAPI 3.1 con enfoque "Design-First" y cumplimiento de RFC 7807.
- **database-architect-strategic**: Diseño multimodelo (SQL/NoSQL) con proyecciones de rendimiento en segundos y bytes.
- **atomic-design-tokens**: Sincronización visual mediante jerarquías de tokens (Primitive, Semantic, Component).

---

## ⚙️ 3. Development & Implementation
*Motores de ejecución para la construcción de código de producción.*

- **async-fastapi-logic**: Generación de backends asíncronos bajo patrones de Repositorio y validación Pydantic.
- **supabase-stack-expert**: Especialista en migraciones SQL, políticas RLS y optimización de consultas Postgres.
- **shadcn-component-library**: Construcción atómica de UIs premium basadas en componentes accesibles y consistentes.

---

## 🛡️ 4. Compliance, Quality & Security
*Sistemas de defensa, auditoría y protección contra alucinaciones.*

- **agentic-thought-secret-scanner**: Detector de fugas de credenciales en código, logs y pensamiento del agente.
- **factory-audit-pro**: Diagnóstico de salud en 5 dimensiones (Perf, A11y, Tema, Resiliencia, Anti-Patrones).
- **hallucination-guardrail**: Verificación factual del contenido contra la "Única Fuente de Verdad" (SSoT) física.

---

## 🔬 5. Research & Strategy
*Capacidades de investigación científica y análisis de crecimiento.*

- **arxiv-technical-digest**: Investigación académica real. Prohíbe alucinar papers; solo utiliza la API de ArXiv.
- **apify-trend-analysis**: Captura de tendencias reales de mercado mediante scrapers especializados.
- **autonomous-feedback-analyzer**: Síntesis de patrones de feedback y detección de urgencia emocional.
- **api-docs-generator**: Transformación de contratos YAML en documentación técnica profesional.
- **social-content-strategy**: Repurposing de contenido pilar en ecosistemas de activos para redes sociales.

---

## ⚙️ Mandatos Industriales (General)

1. **Mandato SI**: Todas las métricas en todas las skills deben expresarse en **Segundos (s)** y **Bytes (B)**.
2. **Zero-Trust**: Los resultados "mockeados" están prohibidos. La ejecución debe dejar evidencia física en disco.
3. **Redundancy Lock**: Las skills fallan por defecto si intentan sobrescribir estructuras críticas sin autorización explícita.
4. **Context Isolation**: Las skills operan sin acceso a la historia global de la conversación, centrándose únicamente en su `params`.

---
*Librería de Skills Solidificada v3.4.0-S | Dasafo Factory*
