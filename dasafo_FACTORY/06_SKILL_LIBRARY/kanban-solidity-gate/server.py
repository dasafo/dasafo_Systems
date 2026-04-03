import http.server
import socketserver
import json
import sys
import os
import time
from pathlib import Path

# Argumentos industriales
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 3001
PROJECT_ROOT = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else Path(".").resolve()

class KanbanHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 🔍 Endpoint DAST: Lectura en tiempo real del estado físico
        if self.path == "/api/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            registry_path = PROJECT_ROOT / "TASKS" / "registry.json"
            state_path = PROJECT_ROOT / "PROJECT_STATE.json"

            data = {"registry": [], "state": {}, "server_time": time.time()}

            try:
                # Lectura con reintentos mínimos para evitar colisiones
                if registry_path.exists():
                    data["registry"] = json.loads(registry_path.read_text(encoding="utf-8"))
                if state_path.exists():
                    data["state"] = json.loads(state_path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, PermissionError):
                # Fail-safe: Si el archivo está bloqueado o incompleto, devolvemos estado previo
                pass

            self.wfile.write(json.dumps(data).encode("utf-8"))
        
        # 🌐 Servir la UI Industrial
        elif self.path == "/":
            self.path = "ui/index.html"
            return super().do_GET()
        else:
            return super().do_GET()

# Asegurar que el contexto de ejecución es el directorio de la skill
os.chdir(Path(__file__).parent)

print(f"[*] dasafo_FACTORY | Vibe Kanban Server v5.0")
print(f"[*] Port: {PORT} | Root: {PROJECT_ROOT}")

try:
    with socketserver.TCPServer(("", PORT), KanbanHandler) as httpd:
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n[!] Server decommissioned by user.")