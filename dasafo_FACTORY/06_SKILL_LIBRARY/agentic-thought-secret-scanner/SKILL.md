---
version: v5.0-MCP (Nativa)
agent_authorization: [BACKEND_DEV, DATA_SCIENTIST, DB_MASTER, QA_TESTER, SECURITY_AUDITOR, DEVOPS_SRE]
source: https://skills.sh/useai-pro/openclaw-skills-security/credential-scanner
protocol: Zero-Trust / DAST
---

# 🔍 Skill | agentic-thought-secret-scanner

## Objetivo

Identificar y mitigar la exposición accidental de credenciales sensibles (claves API, contraseñas, claves privadas) dentro del espacio de trabajo. Basado en el protocolo industrial **Credential Scanner**.

## 🛠️ Interfaz v5.0-MCP Nativa

**Uso Mandatorio:** Argumentos directos. El parámetro `params_json` está **DEPRECADO**.

### Parámetros

- `agent` (string): Tu ID de Agente autorizado.
- `target_project` (string): Ruta física al proyecto.
- `network_preflight` (boolean): Opcional (defecto: `false`). Escala hallazgos a **CRITICAL**.
- `isolate` (boolean): Opcional (defecto: `false`). Ejecución en Clean Session.

## 🛡️ Restricciones Industriales

- **Máscara Zero-Exposure:** Los secretos se ocultan mediante `████████`.
- **Soberanía DAST:** Generación obligatoria de reporte en `LOGS/AUDITS/`.
- **Unidades SI:** Tiempos reportados estrictamente en **segundos (s)**.

---
**ORIGEN:** [credential-scanner by useai-pro](https://skills.sh/useai-pro/openclaw-skills-security/credential-scanner)
