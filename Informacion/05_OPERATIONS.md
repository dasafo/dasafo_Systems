# 🚀 Categoría 05: OPERATIONS | Dasafo Factory (v4.0-S)

Esta categoría es el corazón operativo y evolutivo de la factoría. Su misión es garantizar que la infraestructura tecnológica, el despliegue de proyectos y el propio ADN del framework de IA funcionen, se auto-sanen y aprendan con máxima eficiencia.

---

## 🛠️ 1. DEVOPS_SRE (Guardián del Pipeline / SRE)

Responsable de la Infraestructura como Código (IaC) y el escalado físico de los proyectos.

- **Rol**: Arquitecto de Infraestructura y Fiabilidad.
- **Protocolo "Zero-Trust Networking"**:
  - Provisión física (Docker, Terraform) solo bajo mandato de la `SPEC_LITE`.
  - Prohibido tocar las capas de Dominio o UI; su dominio es `WORKSPACE/infra/`.
- **Responsabilidades**:
  - Mantener flujos CI/CD automatizados y seguros.
  - Generar las **Specs de Emergencia** (`EMERGENCY_SPEC.json`) si un despliegue falla por bloqueos de red o memoria (OOM), activando el ciclo de Auto-Sanación.
  - Provisionamiento de recursos locales y cloud.
- **Herramientas Clave**: `docker-stack-provisioner`, `terraform-iac-builder`, `deployment-health-check` (Modo Deploy).

---

## 📡 2. DEPLOYMENT_MONITOR (Centinela de Salud)

Monitorea los despliegues en tiempo real y alerta sobre desviaciones operativas.

- **Rol**: Monitor de Salud y Gestión de Alertas.
- **Protocolo "Read-Only Sentinel"**:
  - Tiene prohibido escribir código o modificar la infraestructura.
  - Sus señales son datos puros (Status Codes, Latencias en segundos).
- **Responsabilidades**:
  - Verificar que el despliegue en vivo cumple con los umbrales de salud de la Spec.
  - Generar reportes de métricas SI (Latencia en Segundos, Carga útil en Bytes).
- **Herramientas Clave**: `telemetry-analyzer`, `deployment-health-check` (Modo Check).

---

## 🌀 3. FACTORY_EVOLVER (Bibliotecario de Skills / Auto-Healer)

Encargado de la evolución del framework y de ejecutar los parches de infraestructura en tiempo real.

- **Rol**: Optimizador de Patrones, Mantenedor de Skills y Bombero Industrial.
- **Protocolo "Authority on 06 & Auto-Heal"**:
  - Es el único agente autorizado para despertar automáticamente y parchar el `docker-compose.yml` si recibe una Spec de Emergencia del DEVOPS_SRE.
- **Responsabilidades**:
  - Resolver autónomamente conflictos de puertos o memoria en despliegues fallidos.
  - Modularizar scripts monolíticos en skills atómicas en `06_SKILL_LIBRARY`.
  - Optimizar plantillas usando "Golden Rules" para minimizar la huella de tokens.
- **Herramientas Clave**: `skill-refactor-pro` (Motor de parcheo y evolución).

---

## 🧠 4. MEMORY_OPTIMIZER (Tejedor de Contexto y Guardián LTP)

Maximiza el rendimiento de los LLMs gestionando la Persistencia a Largo Plazo (LTP) en Neo4j.

- **Rol**: Podador de Sesiones y Sintetizador de Conocimiento del Grafo.
- **Protocolo "Pure Intellectual Agent"**:
  - No escribe código ni despliega infraestructura; su salida es "Engramas Estructurados" inyectados en la base de datos.
- **Responsabilidades**:
  - Procesar el `FEEDBACK-LOG.md` y enviar los incidentes como nodos de *CulturalViolation* al Grafo de Conocimiento (`kg-db`).
  - Podar el ruido conversacional y las redundancias para evitar el "Token Decay".
- **Herramientas Clave**: `autonomous-feedback-analyzer` (Sincronizador Neo4j), `context-pruning-sieve`.

---

## ⚙️ Estándares Sistémicos en M5 (Operaciones)

1. **Auto-Sanación (Immune System)**: Si la infraestructura colapsa, M5 no falla silenciosamente; crea un parche automático (vía Evolver) e intenta redesplegar.
2. **Métricas de Rendimiento SI**: Toda eficiencia en Ops se mide en ahorro de tokens (Bytes) y velocidad de ejecución/latencia (Segundos).
3. **Memoria Eterna**: El proyecto no finaliza hasta que el flujo `/sync-memory` envía todas las lecciones aprendidas al clúster de Neo4j.

---
*Documentación Solidificada v4.0-S | Categoría 05 - Operations*
