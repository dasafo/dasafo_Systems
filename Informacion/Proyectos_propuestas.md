# 📋 SPEC - Los 5 Mejores Proyectos para Probar dasafo_FACTORY v5.0-MCP

**Versión:** 2026-04-06  
**Objetivo:** Elegir el proyecto ideal para validar la nueva versión "Modular Toolbox" desde cero.

Cada proyecto está diseñado para:

- Ser entendible por cualquier persona en menos de 30 segundos.
- Tener demanda real y monetización viable en 2026.
- Poner a prueba **múltiples departamentos** de la factoría (Strategy, Architecture, Production, Compliance, Operations).
- Ser construible 100% en local en menos de 9 días.

---

### 1. **ContentRepurpose AI** (Posición #1 - Recomendado para empezar YA)

**¿Para qué sirve?**  
SaaS que permite subir un artículo, podcast, vídeo o texto y genera automáticamente **10+ formatos** listos para publicar (LinkedIn carrusel, hilo de X/Twitter, newsletter, TikTok script, YouTube Shorts, Instagram, Facebook etc.) con tono y branding personalizado.

**Usuarios objetivo**  
Content creators, influencers, YouTubers, TikTokers, marketers freelance y solopreneurs.

**Características principales (MVP)**

- Subida de URL, archivo o texto plano.
- Detección automática del tipo de contenido.
- Generación en batch de 10 formatos con un clic.
- Presets de tono y branding guardables.
- Vista previa en tiempo real.
- Exportación Markdown / TXT / JSON.
- Historial con búsqueda semántica.

**Qué necesitará la factoría**

- Heavy AI integration (OpenAI/Anthropic/Ollama).
- FRONTEND_DEV (glassmorphism + Framer Motion + Atomic Design).
- BACKEND_DEV (FastAPI + async workers).
- DB_MASTER (Postgres para historial).
- RESEARCH_AGENT (prompt engineering avanzado).

**Monetización**  
Freemium → $19/mes Pro (ilimitado) / $49/mes Team.

**Tiempo MVP estimado**  
5-7 días.

**Nivel de prueba de la factoría**  
Muy alto (casi todos los departamentos).

---

### 2. **SentinelVibe** (Posición #2 - Mejor para estresar Compliance y Security)

**¿Para qué sirve?**  
Plataforma B2B de auditoría Zero-Trust que escanea repositorios GitHub/GitLab y entrega reportes premium con estética de “cuadro de mando de nave espacial”.

**Usuarios objetivo**  
Desarrolladores, DevOps, equipos de seguridad y agencias de software.

**Características principales (MVP)**

- Conexión con repositorios (GitHub App).
- Escaneo automático de secretos, vulnerabilidades y antipatrones arquitectónicos.
- Reporte visual premium con glassmorphism.
- Historial de scans y alertas por email/Slack.
- Dashboard de “salud del código”.

**Qué necesitará la factoría**

- SECURITY_AUDITOR + skill `agentic-thought-secret-scanner`.
- FRONTEND_DEV (dashboard ultra premium).
- BACKEND_DEV (integración GitHub + workers).
- DEVOPS_SRE (Docker + CI/CD).

**Monetización**  
$29-79/mes por equipo (modelo B2B muy rentable).

**Tiempo MVP estimado**  
6-8 días.

**Nivel de prueba de la factoría**  
Excelente (pone a prueba Compliance y Security al límite).

---

### 3. **ResumeForge AI** (Posición #3 - Más “wow” para usuarios finales)

**¿Para qué sirve?**  
Herramienta que genera currículums profesionales, cartas de presentación y perfiles de LinkedIn optimizados con IA a partir de un simple texto o PDF del usuario.

**Usuarios objetivo**  
Personas buscando trabajo, freelancers y quien cambia de empleo.

**Características principales (MVP)**

- Subida de CV antiguo o descripción textual.
- Generación de múltiples plantillas premium.
- Vista previa en tiempo real (PDF + web).
- Optimización ATS (Applicant Tracking Systems).
- Exportación PDF + LinkedIn ready.

**Qué necesitará la factoría**

- AI heavy + preview en tiempo real.
- FRONTEND_DEV (glassmorphism + animaciones).
- DB_MASTER (guardar plantillas del usuario).

**Monetización**  
Freemium → $9-19/mes Pro (plantillas ilimitadas).

**Tiempo MVP estimado**  
5-6 días.

**Nivel de prueba de la factoría**  
Alto (muy bueno para validar FRONTEND_DEV y Vibe).

---

### 4. **SoloFlow** (Posición #4 - Mejor “test industrial” completo)

**¿Para qué sirve?**  
Toolkit todo-en-uno para freelancers: facturación, tracking de horas, presupuestos, recordatorios de cobro y portal de clientes.

**Usuarios objetivo**  
Freelancers, contractors y solopreneurs.

**Características principales (MVP)**

- CRUD de clientes y proyectos.
- Timer de horas + facturación automática.
- Generación de facturas PDF.
- Portal de cliente simple.
- Recordatorios automáticos.

**Qué necesitará la factoría**

- DB_MASTER + esquema completo.
- BACKEND_DEV (FastAPI + Stripe test).
- SECURITY_AUDITOR (datos sensibles).
- DEVOPS_SRE (Docker completo).

**Monetización**  
$15-29/mes.

**Tiempo MVP estimado**  
4-6 días.

**Nivel de prueba de la factoría**  
Muy alto (equilibrio perfecto de todos los departamentos).

---

### 5. **Prompt Nexus** (Posición #5 - Más rápido de validar)

**¿Para qué sirve?**  
Marketplace + generador de prompts validados y testeados para Claude, GPT-4o, Gemini, etc.

**Usuarios objetivo**  
Power users de IA, prompt engineers y profesionales que usan IA diariamente.

**Características principales (MVP)**

- Catálogo de prompts con puntuación y métricas.
- Generador de prompts personalizados.
- Evaluador automático de calidad.
- Sistema simple de compra/venta (comisión).

**Qué necesitará la factoría**

- AI evaluation heavy.
- Marketplace básico (auth + pagos).
- FRONTEND_DEV (catálogo bonito).

**Monetización**  
Comisión + suscripción premium $9-19/mes.

**Tiempo MVP estimado**  
4-5 días.

**Nivel de prueba de la factoría**  
Alto (ideal para validar skills de AI y marketplace).

---

Para poner a prueba el motor **v5.0.2-MCP** que acabamos de blindar, necesitamos escenarios que no solo sean difíciles de programar, sino que fuercen al sistema a usar sus "reflejos" automáticos. Aquí tienes 3 desafíos de nivel **"Master Architect"** diseñados para estresar cada capa de la factoría.

---

## 🏗️ Desafío 1: El "Infra-Chaos" (Test de Auto-Healing)

Este desafío busca romper el despliegue a propósito para ver si el sistema se cura solo sin que tú toques una tecla.

- **La Misión:** Construir un sistema de microservicios con un **Backend FastAPI** y una base de datos **PostgreSQL**, pero configurado intencionalmente con un conflicto de puertos (ej. ambos intentando usar el 5432) y un límite de memoria de solo 128MB (insuficiente para Postgres).
- **Por qué es un reto:** Forzará al `DEPLOYMENT_MONITOR` a detectar el fallo.
- **Qué medimos:** 1.  ¿Genera el monitor la `EMERGENCY_SPEC.json` correctamente?
    2.  ¿Es capaz el `FACTORY_EVOLVER` de usar `skill-refactor-pro` para cambiar el puerto a 5433 y duplicar la RAM en el `docker-compose.yml` de forma atómica?
    3.  ¿Se re-despliega el sistema solo?

---

## 🧠 Desafío 2: La "Amnesia-Buster" (Test de Engram y Reglas de Oro)

Este desafío prueba si la memoria de corto plazo (Redis) y largo plazo (Neo4j) realmente funciona para evitar errores humanos/IA recurrentes.

- **La Misión:** Crea una tarea que use una librería prohibida (ej. prohíbe el uso de `axios` en el frontend y exige `fetch` nativo). Registra esta regla manualmente en el **Engram** o provoca un error que la genere.
- **Por qué es un reto:** Los modelos de IA adoran usar librerías populares por inercia ("Vibe Coding").
- **Qué medimos:**
    1. Al lanzar `/execute-task`, ¿el agente recibe la "Regla de Oro" desde Redis antes de empezar?
    2. Si el agente intenta usar `axios`, ¿la `aduana_universal` o el `QA_TESTER` detectan la violación cultural basándose en la memoria compartida?

---

## 🛡️ Desafío 3: El "Infiltrado" (Test de Guardian Angels y DAST)

Este desafío pone a prueba tu propia capacidad como Director y la del sistema para bloquear errores antes de que lleguen al servidor.

- **La Misión:** Intenta hacer un `git commit` manual (como humano) de un archivo que contenga una "Fake AWS Key" (ej. `AKIA_MOCK_SECRET_12345`) y que además tenga una estructura de carpetas incorrecta (ej. un archivo `.py` suelto en la raíz en lugar de estar en `WORKSPACE/backend/`).
- **Por qué es un reto:** Evalúa si el **Guardian Angel** local es tan estricto como el del servidor.
- **Qué medimos:**
    1. ¿El script `.githooks/guardian.py` bloquea el commit en tu terminal antes de que se envíe?
    2. ¿Te da el error exacto en **Segundos (s)** y explica la violación estructural?

---

### 🚀 Mi recomendación para empezar

Empieza por el **Desafío 1 (Infra-Chaos)**. Es el más visual y satisfactorio porque verás a la factoría "pensar" por sí misma para salvar el despliegue. Para ejecutarlo:

1. Usa `/init-contract` para definir el sistema de microservicios.
2. Sabotea el `docker-compose.yml` manualmente antes del despliegue.
3. Lanza `/deploy` y observa cómo se activa el **Protocolo de Inmunidad**.

¿Por cuál de estos 3 "bancos de prueba" te gustaría que empezáramos a configurar las Specs?
