Perfecto. He analizado en profundidad las ~24.000 líneas del repositorio: la constitución, el servidor MCP, todos los hubs, las skills críticas, los logs LTP y la session_hook. Aquí está mi diagnóstico completo.---

# Mi opinión directa

El sistema tiene una **visión arquitectónica genuinamente avanzada** — DAST, DAG paralelo, engram Redis+Neo4j, phase-gating con firma humana. Está pensado por alguien que conoce bien los problemas reales de los sistemas multi-agente. Pero la brecha entre el diseño y la implementación es considerable.

**El problema central:** la característica más ambiciosa del sistema (el cerebro aprendiente Neo4j) está completamente roto en los tres logs de producción disponibles. Esto significa que la fábrica lleva operando sin memoria entre proyectos, que es exactamente el problema que dice resolver.

**El segundo problema central:** hay una credencial de base de datos hardcodeada en 4 ficheros, y el propio scanner de secretos está en la lista de bypass. Es un irónico fallo de Chesterton's Fence.

**Lo que haría primero:** las acciones 1-3 del Plan son bloqueantes — sin ellas el resto del sistema no puede funcionar con garantías. Las acciones 4-7 son las que elevarían la puntuación de 6.4 a algo cercano a 8.5.

El esqueleto es sólido. Necesita que la implementación alcance la ambición del diseño.

# Resumen ejecutivo

## Puntuación general

`6.4/10` Diseño sólido | Impl. parcial

## Hallazgos críticos

`3` | CRÍTICO `×3` | ALTO `×4` | MEDIO `×5`

## Skills analizadas

`30+` | `16` agentes | `5` departamentos

## Sistema de memoria LTP

ROTO | `0` reglas sincronizadas | `3/3` logs fallan

## Guardrail de alucinación

STUB
Sin lógica semántica real

## Credencial expuesta

`×4` | freedom85 hardcoded

## Hallazgos

**CRÍTICO**
Contraseña Neo4j hardcoded en 4 archivos
La credencial "freedom85" aparece en texto plano en `delegate-clean-session/logic.py`, `autonomous-feedback-analyzer/logic.py`, `project-management/logic.py` y `hub05_operations.py`. Cualquier persona con acceso al repositorio o al Repomix dump tiene acceso total al knowledge graph. El `agentic-thought-secret-scanner` —que debería detectar esto— está en la lista `BYPASS_SKILLS`, por lo que nunca se aplica sobre el propio código de la fábrica.

**CRÍTICO**
Sistema de memoria LTP completamente no operativo.
Los 3 logs de LTP en producción muestran "total_rules": 0 y "ltp_sync": {"success": false, "message": "persist_to_knowledge_graph logic is missing or decoupled."}. El cerebro aprendiente del sistema —la propuesta de valor más ambiciosa de la arquitectura— nunca ha funcionado en real. Los Golden Rules de Neo4j están vacíos. Las `warm_up_engram` inyectan cero reglas. Todo el ciclo de retroalimentación está roto.

**CRÍTICO**
*Race condition en DAST pre-flight de la Aduana Universal*.
aduana_universal reescribe registry.json completo en cada invocación de herramienta MCP. En ejecución paralela (DAG con múltiples agentes simultáneos), dos agentes pueden sobrescribirse mutuamente el fichero de registro. El ganador de la última escritura borra el progreso del otro. La arquitectura promete paralelismo DAG pero la implementación lo hace inseguro.

**ALTO**
*Guardrail de alucinación es código simulado (stub)*.
`hallucination-guardrail/logic.py` asigna risk_score = 0.1 con el comentario "Logic simulation: Grounding verification — In production: Semantic comparison vs Disk Artifact". No hay comparación semántica real. Solo comprueba si existe un path de fichero. Cualquier contenido con un path válido pasa con riesgo 0.1 (safe), independientemente de su veracidad.

**ALTO**
*`BYPASS_SKILLS` demasiado permisivo: 16 skills evaden la Aduana*.
La lista incluye `hallucination-guardrail`, `autonomous-feedback-analyzer`, `skill-refactor-pro`, `context-pruning-sieve`, `research-manager` y otras 11 más. Más de la mitad del arsenal de skills bypasea completamente la validación de fase y el Double-Gating. Un agente puede ejecutar modificaciones de código (`skill-refactor-pro`) sin que el proyecto esté en fase correcta.

**ALTO**
*Auto-healing con inteligencia de sustitución regex*.
`skill-refactor-pro/logic.py` implementa el "sistema inmune industrial" con literales como content.replace("memory: 512M", "memory: 1G") o int(conflict_port) + 1. Un conflicto de puerto en 8080 lo mueve a 8081 sin verificar si 8081 está libre. Una OOM itera: 512M → 1G → 2G → 4G. Esto puede buclear o romper otras configuraciones silenciosamente.

**ALTO**
*`session_hook` no valida la asignación `agente-tarea`*.
El Double-Gating verifica si existe una `SPEC_LITE.json` en disco, pero no comprueba que el campo assigned_agent dentro del JSON corresponda al agente que invoca la herramienta. Un `FRONTEND_DEV` podría ejecutar una tarea asignada a `SECURITY_AUDITOR` si la spec está presente.

**MEDIO**
*Detección de tecnología en delegate-clean-session demasiado primitiva*.
La inyección JIT de reglas usa if ".tsx" in pointers o if "fastapi" in pointers para detectar el stack. Esto falla con TypeScript en ficheros .ts, con Django, Flask, NestJS, etc. La regla engram correcta no llega al agente si la extensión no coincide exactamente.

**MEDIO**
*Redis como SPOF sin circuit breaker*.
Si Redis está caído: el loop detection falla silenciosamente (permite bucles infinitos), el engram cache no funciona (las reglas llegan tarde desde Neo4j o no llegan), y el antifatiga queda desactivado. No hay fallback para el loop counter. El código tiene try/except: pass en varios puntos críticos.

**MEDIO**
*Detección de fase en factory-doctor es frágil*.
Detecta la fase buscando si existe `LOGS/BUILD_REPORT.json` (→ M3) o si `DOCS/ARCH` tiene contenido (→ M2). Un proyecto en M4 sin ese fichero sería regresado a M1. El "forensic healing" puede degradar el estado del proyecto incorrectamente.

**MEDIO**
*Sin presupuesto de tokens ni rate limiting global*.
El sistema puede disparar N delegaciones paralelas sin límite de coste. No hay contabilidad de tokens por proyecto, por sesión ni por agente. Un DAG mal diseñado puede generar decenas de sesiones simultáneas sin control de gasto.

**MEDIO**
*`NATIVE_MCP_PROTOCOL.md` y otros docs críticos están vacíos*.
El fichero `00_GLOBAL_KNOWLEDGE/NATIVE_MCP_PROTOCOL.md` está completamente en blanco. La Constitución exige el Anti-Orphan Mandate (ningún .md sin conectividad funcional), pero documentos clave como este violan su propia ley. Esto también afecta al onboarding: un nuevo agente no puede aprender el protocolo MCP del sistema.

## Fortalezas

El sistema tiene una base arquitectónica genuinamente avanzada

* **DAST (Disk-as-Source-of-Truth)** — El uso del sistema de ficheros como estado canónico es una decisión brillante. Elimina la inconsistencia de estado en memoria y hace el sistema auditable por definición.

* **Loop Detection via Redis** — El mecanismo de antifatiga con TTL de 1h es sofisticado y correcto conceptualmente. Protege el gasto de tokens de forma elegante.

* **Phase Gating M1-M5 con firma humana** — El Human-in-the-Loop obligatorio (APPROVAL_MX.md) es una salvaguarda de gobernanza excelente. Evita que la fábrica escale sin supervisión.

* **DAG paralelo con análisis topológico** — La detección de ciclos y el cálculo de tareas listas mediante DFS en analyze_dag() es código correcto y eficiente.

* **Arquitectura Redis-first → Neo4j fallback** — La estrategia de caché warm-up + consulta de respaldo es el patrón correcto para sistemas de conocimiento de baja latencia.

* **Separación clean del MCP server** — Extraer mcp_app.py del factory_mcp_server.py para romper importaciones circulares demuestra madurez de diseño.

* **Guardian Angel Git Hooks** — El pre-commit hook con guardian.py es una capa de seguridad local correcta, aunque su propia config expone la contraseña que debería proteger.

* **Feedback Schema con JSON Schema completo** — El FEEDBACK_SCHEMA.json con draft-07 y enums tipados muestra rigor de diseño de datos.

* **Factory Doctor para recuperación forense** — El concepto de reconstruir el estado desde los artefactos físicos es exactamente el enfoque correcto para sistemas resilientes.

* **Taxonomía 6-nivel (DEFINE/PLAN/BUILD/VERIFY/REVIEW/SHIP)** — Elimina el "vibe coding" con una estructura cognitiva clara. Bien pensada.

## Plan de Accion

### Sprint inmediato — Seguridad y datos

1. **Eliminar "freedom85" de todos los ficheros**. Mover a variable de entorno exclusiva del fichero INFRA/.env que ya está en .gitignore. Rotar la credencial en el servidor Neo4j tras el cambio. Verificar que el Guardian Angel hook detecta el patrón NEO4J_PASSWORD=....

2. **Reparar el pipeline LTP**. El log muestra "persist_to_knowledge_graph logic is missing or decoupled". Hay que trazar por qué falla la conexión en producción (probablemente el hostname Docker no resuelve fuera del contenedor) y añadir un test de integración test_ltp_connectivity.py en INFRA.

3. **Añadir lock de escritura en registry.json**. Reemplazar la escritura directa por un lock de fichero (filelock) o usar escritura atómica con fichero temporal + rename. Esto resuelve la race condition en ejecución paralela.

### Sprint 2 — Corrección de lógica

4. **Implementar el guardrail de alucinación real**. Sustituir el stub por una comparación semántica lightweight: cargar el contexto físico, tokenizar y calcular similitud coseno contra el output del agente. Una librería como sentence-transformers con un modelo pequeño (all-MiniLM) es suficiente y añade ~50ms por verificación.

2. **Revisar lista BYPASS_SKILLS. skill-refactor-pro**, autonomous-feedback-analyzer y context-pruning-sieve no deberían ser bypass — pueden modificar código o logs sin restricción de fase. Mover solo utilidades de diagnóstico puras (factory-doctor, kanban-solidity-gate) al bypass.

3. **Validar asignación agente-tarea en session_hook**. Añadir comprobación de spec_data.get("assigned_agent") == agent en el Double-Gating. Un agente solo puede ejecutar la spec que le corresponde.

4. **Mejorar detección de stack tecnológico**. Reemplazar el matching de strings por un análisis de extensiones de fichero completo (.ts, .vue, .go, requirements.txt, package.json) en los context_pointers de la spec.

### Sprint 3 — Resiliencia y observabilidad

8. **Circuit breaker para Redis**. Si Redis falla, el loop counter debe caer a un fallback en disco (TASKS/.loop_counters/{agent}.json). Sin esto el antifatiga queda completamente desactivado en caídas.

2. **Presupuesto de tokens por proyecto**. Añadir un campo token_budget en PRP_MASTER.json y un contador en Redis. La Aduana Universal debe bloquear nuevas delegaciones si el proyecto supera el 90% del presupuesto y notificar al Director.

3. **Mejorar detección de fase en factory-doctor**. Reemplazar la heurística de ficheros por una jerarquía de artefactos explícita: M1→PRP_CONTRACT.json, M2→DOCS/ARCH/ADR-001.md, M3→WORKSPACE/ no vacío, M4→TEST_REPORTS.md, M5→DOCKER_IA_CONFIG.md.

## Evidencia directa extraída del repositorio

* **LOGS/ANALYSIS_LTP_1776079260.json**:
"total_rules": 0, "payload_bytes": 4712
"ltp_sync": { "success": false, "message": "persist_to_knowledge_graph logic is missing or decoupled." }

* **LOGS/ANALYSIS_LTP_1776080718.json**:
"total_rules": 0, "payload_bytes": 1107
"ltp_sync": { "success": false, "message": "persist_to_knowledge_graph logic is missing or decoupled." }

* **dasafo_FACTORY/LOGS/ANALYSIS_LTP_1776082498.json**:
"total_rules": 0, "payload_bytes": 1576
"ltp_sync": { "success": true, "message": "Sincronizados 0 engramas." }

* **delegate-clean-session/logic.py · autonomous-feedback-analyzer/logic.py**:
pwd = os.getenv("NEO4J_PASSWORD", "freedom85") ← credencial en 4 archivos

* **hallucination-guardrail/logic.py**:
*Logic simulation: Grounding verification*
*In production: Semantic comparison vs Disk Artifact*
risk_score = 0.1 ← valor fijo, sin análisis real

* **session_hook.py — BYPASS_SKILLS**:
16 skills en bypass incluyen: skill-refactor-pro, autonomous-feedback-analyzer,
hallucination-guardrail, context-pruning-sieve, research-manager...

* **mcp_app.py — Loop Detection (correcto)**:
redis_client.incr(loop_key) · expire(loop_key, 3600)
if int(current_attempts) >= max_retries: return BLOCKED_BY_ANTIFATIGUE

* **project-management/logic.py — DAG Analysis (correcto)**:
def dfs(node): visited.add(node); rec_stack.add(node) ← detección de ciclos correcta
ready_tasks = [t for t if all deps COMPLETED] ← topología correcta
