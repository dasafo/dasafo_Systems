# 🚀 Categoría 05: OPERATIONS | Dasafo Factory (v4.0-S)

Esta categoría es el corazón operativo y evolutivo de la factoría. Su misión es garantizar que la infraestructura tecnológica, el despliegue de proyectos y el propio framework de IA funcionen con máxima eficiencia y salud.

---

## 🛠️ 1. DEVOPS_SRE (Guardián del Pipeline / SRE)

Responsable de la Infraestructura como Código (IaC) y el escalado físico de los proyectos.

- **Rol**: Arquitecto de Infraestructura y Fiabilidad.
- **Protocolo "Zero-Trust Networking"**: 
  - Provisión física (Docker, Terraform) solo bajo mandato de la `SPEC_LITE`.
  - Prohibido tocar las capas de Dominio o UI; su dominio es `WORKSPACE/infra/`.
- **Responsabilidades**:
  - Mantener flujos CI/CD automatizados y seguros.
  - Hardening de entornos (Cero credenciales en código).
  - Provisionamiento de recursos locales y cloud.
- **Herramientas Clave**: `docker-stack-provisioner`, `terraform-iac-builder`.

---

## 📡 2. DEPLOYMENT_MONITOR (Centinela de Salud)

Monitorea los despliegues en tiempo real y actúa como autoridad de rollback.

- **Rol**: Monitor de Salud y Gestión de Alertas.
- **Protocolo "Read-Only Sentinel"**: 
  - Tiene prohibido escribir código o modificar la infraestructura.
  - Sus señales son datos puros (Status Codes, Latencias en segundos).
- **Responsabilidades**:
  - Verificar que el despliegue cumple con los umbrales de salud de la Spec.
  - Emitir señales de Rollback inmediato ante fallos críticos.
  - Generar reportes de métricas SI (Latencia, Carga útil).
- **Herramientas Clave**: `telemetry-analyzer`, `playwright-ui-tester` (Modo Smoke-Test).

---

## 🌀 3. FACTORY_EVOLVER (Bibliotecario de Skills / Optimizador)

Encargado de la evolución del framework y la reducción de la devaluación de contexto.

- **Rol**: Optimizador de Patrones y Mantenedor de Skills.
- **Protocolo "Authority on 06"**: 
  - Autoridad para refactorizar la `06_SKILL_LIBRARY` y scripts core.
  - Cada cambio estructural requiere un ADR previo en `DOCS/CORE/ADR/`.
- **Responsabilidades**:
  - Modularizar scripts monolíticos en skills atómicas.
  - Optimizar plantillas para minimizar la huella de tokens (Token Decay).
- **Herramientas Clave**: `skill-refactor-pro`, `autonomous-feedback-analyzer`.

---

## 🧠 4. MEMORY_OPTIMIZER (Tejedor de Contexto)

Maximiza el rendimiento de los LLMs mediante la poda y síntesis de sesiones.

- **Rol**: Podador de Sesiones y Sintetizador de Conocimiento.
- **Protocolo "Pure Intellectual Agent"**: 
  - No escribe código ni despliega infraestructura; su salida es "Contexto Refinado".
- **Responsabilidades**:
  - Refinar el `FEEDBACK-LOG.md` para extraer solo los núcleos técnicos relevantes.
  - Eliminar ruido conversacional y redundancias antes de tareas críticas.
- **Herramientas Clave**: `context-pruning-sieve`, `hallucination-guardrail`.

---

## ⚙️ Estándares Sistémicos en M5 (Operaciones)

1. **Métricas de Rendimiento**: La eficiencia se mide en reducción de tokens y velocidad de ejecución (s).
2. **Salud Infranqueable**: Ningún proyecto se considera "Vivo" sin el reporte `HEALTHY` del Deployment Monitor.
3. **Evolución Continua**: El framework aprende de cada fallo mediante el análisis automático de logs de feedback.

---
*Documentación Solidificada v4.0-S | Categoría 05 - Operations*
