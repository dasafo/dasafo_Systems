# 🎮 Guía de Experiencia de Usuario: Director de Operaciones (v3.4.0-S)

Con toda esta infraestructura industrial (**v3.4.0-S**) montada, tu experiencia pasa de ser un simple "chat con una IA" a ser el **Director de Operaciones de una Factoría de Software**. 

Tú ya no picas código ni copias y pegas scripts; tú **gestionas agentes, apruebas contratos y exiges resultados físicos**.

Así es exactamente como usarías la `dasafo_FACTORY` en el día a día a través de la interfaz de **Antigravity**:

---

## ⚙️ Fase 0: Ignición (El "Power Grid")
Antes de abrir la interfaz de chat, preparas el terreno:
1. **Enciendes el Núcleo:** Vas a la terminal, entras en `INFRA/` y ejecutas `docker-compose up -d`. Esto levanta la memoria a largo plazo (Neo4j), la base de datos operativa (Postgres) y la caché (Redis).
2. **Creas el Cascarón:** Ejecutas `./init_project.sh NuevoCRM`. Esto genera instantáneamente las carpetas `DOCS/`, `TASKS/`, `WORKSPACE/` y establece la aduana en **Phase M1 (Discovery)**.

---

## 🗣️ Fase 1: El Contrato (Discovery en Antigravity)
Abres **Antigravity** y seleccionas tu proyecto:
1. **Hablas con el PRODUCT_OWNER:** Le explicas tu idea en lenguaje natural: *"Quiero un CRM ligero para clínicas dentales. Necesito gestión de pacientes y un calendario."*
2. **Pulsas el Botón Rojo:** Escribes en el chat el comando `/init-contract`. 
3. **Magia Industrial:** Antigravity envía la orden por MCP al `skill_engine.py`. El Product Owner ejecuta la skill `prp-generator` y, sin que tú hagas nada, aparece en tu disco duro un `PRP_CONTRACT.json` perfecto de 12 secciones en la raíz de tu proyecto.

---

## 🗺️ Fase 2: Arquitectura y Despiece
Con el contrato firmado en el disco duro, llamas a tus jefes técnicos:
1. **Visualización:** Escribes `/arch-diagram`. El **ARCHITECT** lee el contrato y dibuja los diagramas de base de datos en `DOCS/ARCH/`, asegurándose de apuntar a la base de datos híbrida de la factoría (`dasafo-shared-db`).
2. **Orquestación:** Escribes `/factory-orchestrate`. El **ORCHESTRATOR** despierta, lee el `PRP_CONTRACT.json` y lo despedaza en tareas atómicas. Tu archivo `TASKS/registry.json` se llena de misiones en estado `PENDING`.

---

## 🏭 Fase 3: La Línea de Montaje (Producción)
Aquí es donde la factoría brilla por su protocolo **Zero-Trust** y **Clean Sessions**:
1. **Control Visual:** Escribes `/kanban-board` para abrir tu dashboard visual en `localhost:3001` y monitorizar las tareas.
2. **Ejecución Blindada:** Escribes `/execute-task`. El **ORCHESTRATOR** consulta el Kanban, toma la primera tarea (ej. "Crear Login UI") y **aísla a un FRONTEND_DEV en una sala limpia** (`delegate-clean-session`). 
3. **Resultado Atómico:** El peón (Frontend) genera los componentes Shadcn. Al tener acceso solo a esa pequeña tarea, **no se confunde ni alucina**. Cuando termina, guarda el código en `WORKSPACE/frontend/` y la sesión se destruye automáticamente.

---

## 🛂 Fase 4: Auditoría y Aduana Universal
El código está escrito, pero en esta factoría nada avanza sin pruebas:
1. **Escaneo de Seguridad:** Escribes `/scan`. El **SECURITY_AUDITOR** rastrea el código buscando secretos hardcodeados o vulnerabilidades.
2. **Control de Calidad:** Escribes `/audit`. El **QA_TESTER** revisa la calidad visual y el rendimiento, garantizando que cumple con el mandato del **Sistema Internacional** (latencias en *segundos*, tamaños en *bytes*).
3. **Paso de Fase:** Escribes `/factory-orchestrate` de nuevo. El **ORCHESTRATOR** invoca a la `kanban-solidity-gate`. La aduana verifica que todas las tareas de la Fase M3 tienen evidencia física. Si es así, actualiza el `PROJECT_STATE.json` y promociona el proyecto a la **Fase M4**.

---

## 💡 Resumen de la Experiencia: Pensar, Comandar y Aprobar

Como usuario, tu flujo de trabajo ha evolucionado:
* **Sin Micro-gestión:** Ya no corriges código; **corriges las especificaciones** (`SPEC_LITE.json`).
* **Sin Amnesia:** Ya no sufres porque la IA "se olvida" del contexto en mensajes largos; **cada tarea se ejecuta en una Clean Session fresca**.
* **Seguridad Física:** Tienes la tranquilidad de que el sistema no se saltará pasos; el **`session_hook.py` (Aduana) bloquea físicamente** cualquier intento de avanzar sin pruebas verificables en verde.

**Tu rol se ha elevado.** Eres el dueño de la fábrica.

---
*Manual de Operaciones v3.4.0-S | Guía UX Industrial*
