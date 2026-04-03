"""
Servidor MCP Industrial (v5.0 Nativo) para dasafo_FACTORY.
Punto de entrada: importa los Hubs para registrar herramientas y ejecuta mcp.run().

ADR: La lógica de mcp + aduana_universal vive en mcp_tools/mcp_app.py
para evitar importaciones circulares. Este archivo solo actúa como entrypoint.
"""

# 1. Re-exportar mcp y aduana_universal para compatibilidad hacia atrás
from mcp_tools.mcp_app import mcp, aduana_universal  # noqa: F401

# 2. Importar los hubs para que sus @mcp.tool() se registren al cargar
from mcp_tools import (  # noqa: F401
    core_dast,
    hub01_strategy,
    hub02_arch,
    hub03_prod,
    hub04_compliance,
    hub05_operations,
)

# =====================================================================
# 🧰 HERRAMIENTAS NATIVAS MCP — REGISTRADAS EN LOS HUBS
# =====================================================================
# Las herramientas están registradas modularmente en:
#   - mcp_tools/core_dast.py       → delegate-clean-session, kanban-solidity-gate, etc.
#   - mcp_tools/hub01_strategy.py  → prp-generator, startup-metrics-framework, etc.
#   - mcp_tools/hub02_arch.py      → architecture-decision-records, api-contract-generator, etc.
#   - mcp_tools/hub03_prod.py      → async-fastapi-logic, shadcn-component-library, etc.
#   - mcp_tools/hub04_compliance.py→ factory-audit-pro, agentic-thought-secret-scanner, etc.
#   - mcp_tools/hub05_operations.py→ docker-stack-provisioner, deployment-health-check, etc.

if __name__ == "__main__":
    mcp.run()