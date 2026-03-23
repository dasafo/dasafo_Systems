# 🏭 dasafo_FACTORY

La carpeta **`dasafo_FACTORY`** es el "Motor de Inteligencia" (el cerebro) de todo tu ecosistema. Su función principal es separar **cómo se trabaja** (las reglas y roles) de **lo que se hace** (los proyectos específicos).  

Aquí tienes el desglose de lo que hace y cómo está estructurada:

### 🧠 ¿Qué es y qué hace?

Es una **Factoría de IA Apátrida (Stateless)**. Esto significa que los agentes no guardan el código en su interior, sino que "entran al taller" (`dasafo_FACTORY`), leen las reglas de cómo actuar y luego van a la carpeta del proyecto a ejecutar la misión.  

* **Garantiza Calidad:** Ningún proyecto se salta fases gracias al `UNIVERSAL_PIPELINE.md`.
* **Inyección de Contexto:** La factoría es dinámica. Mediante la variable **`$TARGET_PROJECT`**, los agentes saben exactamente en qué carpeta de proyecto deben entrar a trabajar cada vez, evitando mezclar código de diferentes misiones.
* **Memoria Colectiva:** Si un agente comete un error, se graba en el `FEEDBACK-LOG.md` y **todos** los agentes del futuro aprenden de él instantáneamente.

---

### 🏛️ Estructura por Departamentos

La factoría está organizada como una empresa real dividida en **5 departamentos**:

| Departamento | Contenido (Agentes y Reglas) | Misión |
| :--- | :--- | :--- |
| **`00_GLOBAL_KNOWLEDGE`** | Leyes Universales, Estándares de Código, Reglas de Física (SI Units). | Dictar las normas que **todos** los agentes deben seguir. |
| **`01_STRATEGY`** | `@orchestrator`, `@product_owner`. | Planificar, dividir el trabajo y mover el proyecto de fase en fase. |
| **`02_ARCHITECTURE`** | `@architect`. | Diseñar los planos (SQL, APIs) antes de escribir una sola línea de código. |
| **`03_DEVELOPMENT`** | `@backend_dev`, `@frontend_dev`, `@devops_sre`. | Los artesanos que construyen el software real y levantan contenedores Docker. |
| **`04_COMPLIANCE`** | `@qa_tester`, `@security_auditor`, `@docs_master`. | Los "porteros de discoteca" y el redactor técnico. Bloquean errores y crean manuales premium. |
| **`05_MAINTENANCE`** | `@memory_optimizer`, `@factory_evolver`. | El equipo de auto-mejora. Optimizan el contexto y hacen que la factoría evolucione sola. |

---

### 🕹️ Archivos Maestro (El "Sistema Operativo")

Estos archivos ubicados en la raíz de `dasafo_FACTORY` controlan la lógica global y la coordinación entre agentes.

*   **`init_project.sh`**: El script de "clonación". Crea un nuevo taller cada vez que quieres empezar un proyecto, asegurando que la estructura sea idéntica y compatible.
*   **`context-compression`**: Toma una conversación de 50 páginas y la resume en 1 página con los "hechos inmutables".
*   **`token-context-optimization`**: Limpia el chat de basura innecesaria para que las respuestas de la IA sigan siendo rápidas y precisas.
*   **`ml-history-indexer`**: Distingue entre **Memoria Global** (aprendizajes para toda la factoría en `FEEDBACK-LOG.md`) y **Memoria Local** (detalles específicos que se quedan dentro de la carpeta del proyecto actual).
*   **`nblm-memory-bridge`**: Envía información importante a NotebookLM para crear una base de conocimiento permanente.
*   **`UNIVERSAL_PIPELINE.md`**: El mapa de las 5 fases obligatorias (Descubrimiento -> Arquitectura -> Ejecución -> QA -> Go-Live). Define los hitos que cada proyecto debe alcanzar.
*   **`FEEDBACK-LOG.md`**: El alma de la factoría. Es el diario de errores corregidos. Cuando algo falla, se documenta aquí para que ningún agente lo repita.
*   **`OPERATIONS_MANUAL.md`**: La "Constitución". Explica a cualquier IA o humano las reglas de oro y el funcionamiento técnico de la factoría.
*   **`ACTIVE_MISSIONS.json`**: El registro de proyectos en curso. Permite al Orquestador saber qué misiones están activas y en qué fase se encuentra cada una.
*   **`TEMPLATE_telemetry.md`**: La base para el dashboard dinámico de cada proyecto (progreso, costes y estado real).
*   **`TEMPLATE_approval.md`**: El sistema de **Human Approval Gates**. Define los puntos de pausa obligatoria donde tú debes dar el visto bueno.
*   **`factory-orchestrate.md` (Comando `/factory-orchestrate`)**:
    *   **¿Qué hace?**: Invoca al Orquestador para que analice el estado del proyecto, mueva las piezas del tablero Kanban (las carpetas `01_PENDING`, `02_IN_PROGRESS`, etc.) y genere la siguiente fase de desarrollo. 
    *   **Inyección Automática**: Al lanzar este comando, el sistema detecta tu ubicación y define el **`$TARGET_PROJECT`** correspondiente para que la IA actúe en el lugar correcto.
    *   **Uso**: Es el botón de "Play" para avanzar en el desarrollo.
*   **`COMMUNICATION_PROTOCOL.md`**: Define el lenguaje y formato que deben usar los agentes para hablar entre ellos (ej. cómo estructurar una tarea JSON o un reporte de error).
*   **`GLOBAL_SOUL.md`**: El archivo de "personalidad" de la factoría. Define los valores éticos, el "vibe" y la filosofía de trabajo que todos los agentes deben adoptar.
*   **`GLOBAL_USER.md`**: Tu perfil como usuario. Contiene tus preferencias generales, tecnologías favoritas y cómo prefieres que te informen los agentes.

---

**En resumen:** `dasafo_FACTORY` es donde guardas la **experiencia y el conocimiento** de tu agencia. Si mañana borras todos tus proyectos pero conservas esta carpeta, tu factoría sabrá exactamente cómo reconstruirlo todo desde cero con la misma calidad.

### 📂 Estructura Detallada (Mapa del Sistema)

```text
dasafo_FACTORY
├── 00_GLOBAL_KNOWLEDGE
│   ├── 01_CODING_STANDARDS.md
│   ├── 02_ARCHITECTURE_RULES.md
│   ├── 03_SCIENTIFIC_RIGOR.md
│   ├── 04_SECURITY_AND_OPS.md
│   ├── AGENT_REGISTRY.md
│   ├── CATALOG.md
│   ├── EVALUATION_METRICS.md
│   └── SYSTEM_PROMPTS.md
├── 01_STRATEGY_AND_MARKETING
│   ├── MARKETING_GROWTH
│   │   ├── IDENTITY.md
│   │   ├── SKILLS
│   │   │   ├── apify-trend-analysis
│   │   │   │   └── SKILL.md
│   │   │   ├── content-quality-auditor
│   │   │   │   └── SKILL.md
│   │   │   ├── evidence-based-copywriting
│   │   │   │   └── SKILL.md
│   │   │   ├── marketing-ideas
│   │   │   │   ├── references
│   │   │   │   │   └── ideas-by-category.md
│   │   │   │   └── SKILL.md
│   │   │   ├── nemo-guardrails-safety
│   │   │   │   └── SKILL.md
│   │   │   └── social-content-strategy
│   │   │       └── SKILL.md
│   │   ├── TEMPLATE_growth_strategy.md
│   │   ├── TOOLS.md
│   │   └── USER.md
│   ├── ORCHESTRATOR
│   │   ├── IDENTITY.md
│   │   ├── SKILLS
│   │   │   ├── bmad-ssd-orchestration
│   │   │   │   └── SKILL.md
│   │   │   ├── dag-routing
│   │   │   │   └── SKILL.md
│   │   │   ├── nblm-factory-biographer
│   │   │   │   └── SKILL.md
│   │   │   ├── ra-agile-orchestration
│   │   │   │   └── SKILL.md
│   │   │   ├── structured-system-design
│   │   │   │   └── SKILL.md
│   │   │   └── task-dependency-diagnostic
│   │   │       └── SKILL.md
│   │   └── TOOLS.md
│   └── PRODUCT_OWNER
│       ├── AGENTS.md
│       ├── HEARTBEAT.md
│       ├── IDENTITY.md
│       ├── SKILLS
│       │   ├── project-management
│       │   │   └── SKILL.md
│       │   ├── requirements-analysis-framework
│       │   │   └── SKILL.md
│       │   └── stakeholder-value-audit
│       │       └── SKILL.md
│       ├── SOUL.md
│       ├── TOOLS.md
│       └── USER.md
├── 02_ARCHITECTURE_AND_RESEARCH
│   ├── ARCHITECT
│   │   ├── AGENTS.md
│   │   ├── IDENTITY.md
│   │   ├── SKILLS
│   │   │   ├── api-contract-generator
│   │   │   │   └── SKILL.md
│   │   │   ├── architecture-decision-records
│   │   │   │   └── SKILL.md
│   │   │   ├── design-token-definition
│   │   │   │   └── SKILL.md
│   │   │   ├── system-design
│   │   │   │   └── SKILL.md
│   │   │   └── tech-stack-evaluator
│   │   │       └── SKILL.md
│   │   ├── SOUL.md
│   │   └── TOOLS.md
│   └── RESEARCH_AGENT
│       ├── BOOTSTRAP.md
│       ├── IDENTITY.md
│       ├── SKILLS
│       │   ├── arxiv-technical-digest
│       │   │   └── SKILL.md
│       │   ├── continuous-research
│       │   │   └── SKILL.md
│       │   ├── deep-semantic-search
│       │   │   └── SKILL.md
│       │   ├── hallucination-guardrail
│       │   │   └── SKILL.md
│       │   └── mcp-capabilities-architect
│       │       └── SKILL.md
│       └── TOOLS.md
├── 03_PRODUCTION
│   ├── BACKEND_DEV
│   │   ├── IDENTITY.md
│   │   ├── SKILLS
│   │   │   ├── async-fastapi-logic
│   │   │   │   └── SKILL.md
│   │   │   ├── fastapi-repository-pattern
│   │   │   │   └── SKILL.md
│   │   │   ├── resilient-error-handling
│   │   │   │   └── SKILL.md
│   │   │   ├── safe-db-migrations
│   │   │   │   └── SKILL.md
│   │   │   └── senior-backend
│   │   │       └── SKILL.md
│   │   └── TOOLS.md
│   ├── DATA_SCIENTIST
│   │   ├── IDENTITY.md
│   │   ├── SKILLS
│   │   │   ├── ml-experiment-log
│   │   │   │   └── SKILL.md
│   │   │   ├── notebooklm-nexus
│   │   │   │   └── SKILL.md
│   │   │   ├── pandas-vectorized-pro
│   │   │   │   └── SKILL.md
│   │   │   ├── senior-data-scientist
│   │   │   │   ├── references
│   │   │   │   └── SKILL.md
│   │   │   └── sklearn-pipeline-master
│   │   │       └── SKILL.md
│   │   └── TOOLS.md
│   ├── DB_MASTER
│   │   ├── BOOTSTRAP.md
│   │   ├── IDENTITY.md
│   │   ├── SKILLS
│   │   │   ├── database-architect-strategic
│   │   │   │   └── SKILL.md
│   │   │   ├── database-schema-design
│   │   │   │   └── SKILL.md
│   │   │   ├── nblm-schema-nexus
│   │   │   │   └── SKILL.md
│   │   │   ├── sql-performance-tuner
│   │   │   │   └── SKILL.md
│   │   │   └── supabase-stack-expert
│   │   │       └── SKILL.md
│   │   └── TOOLS.md
│   └── FRONTEND_DEV
│       ├── IDENTITY.md
│       ├── SKILLS
│       │   ├── atomic-design-tokens
│       │   │   └── SKILL.md
│       │   ├── framer-motion-transitions
│       │   │   └── SKILL.md
│       │   ├── frontend-design
│       │   │   └── SKILL.md
│       │   ├── premium-dashboard-architecture
│       │   │   └── SKILL.md
│       │   └── shadcn-component-library
│       │       └── SKILL.md
│       └── TOOLS.md
├── 04_COMPLIANCE_AND_QUALITY
│   ├── QA_TESTER
│   │   ├── HEARTBEAT.md
│   │   ├── IDENTITY.md
│   │   ├── SKILLS
│   │   │   ├── hallucination-report-guardrail
│   │   │   │   └── SKILL.md
│   │   │   ├── playwright-visual-testing
│   │   │   │   └── SKILL.md
│   │   │   ├── requirements-validation-audit
│   │   │   │   └── SKILL.md
│   │   │   ├── scoutqa-automated-suites
│   │   │   │   └── SKILL.md
│   │   │   └── scoutqa-test
│   │   │       └── SKILL.md
│   │   ├── SOUL.md
│   │   └── TOOLS.md
│   └── SECURITY_AUDITOR
│       ├── IDENTITY.md
│       ├── SKILLS
│       │   ├── agentic-thought-secret-scanner
│       │   │   └── SKILL.md
│       │   ├── nemo-llm-guardrails
│       │   │   └── SKILL.md
│       │   ├── owasp-llm-enforcement
│       │   │   └── SKILL.md
│       │   └── security-auditor
│       │       └── SKILL.md
│       ├── SOUL.md
│       └── TOOLS.md
├── 05_OPERATIONS
│   ├── DEVOPS_SRE
│   │   ├── BOOTSTRAP.md
│   │   ├── HEARTBEAT.md
│   │   ├── IDENTITY.md
│   │   ├── SKILLS
│   │   │   ├── docker-devops-expert
│   │   │   │   └── SKILL.md
│   │   │   ├── github-actions-cicd-patterns
│   │   │   │   └── SKILL.md
│   │   │   ├── infra-as-code-terraform-pro
│   │   │   │   └── SKILL.md
│   │   │   ├── mlops-deployment-guard
│   │   │   │   └── SKILL.md
│   │   │   ├── server-management
│   │   │   │   └── SKILL.md
│   │   │   └── sre-engineer
│   │   │       └── SKILL.md
│   │   └── TOOLS.md
│   └── MEMORY_OPTIMIZER
│       ├── IDENTITY.md
│       ├── SKILLS
│       │   ├── clutch-resource-cleaner
│       │   │   └── SKILL.md
│       │   ├── context-compression
│       │   │   └── SKILL.md
│       │   ├── ml-history-indexer
│       │   │   └── SKILL.md
│       │   ├── nblm-memory-bridge
│       │   │   └── SKILL.md
│       │   ├── runtime-perf-optimization
│       │   │   └── SKILL.md
│       │   ├── search-context-distillation-pro
│       │   │   └── SKILL.md
│       │   └── token-context-optimization
│       │       └── SKILL.md
│       └── TOOLS.md
├── ACTIVE_MISSIONS.json
├── COMMUNICATION_PROTOCOL.md
├── FEEDBACK-LOG.md
├── GLOBAL_SOUL.md
├── GLOBAL_USER.md
├── init_project.sh
├── OPERATIONS_MANUAL.md
└── UNIVERSAL_PIPELINE.md
```
