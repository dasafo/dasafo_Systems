import http.server
import socketserver
import json
import sys
import os
from pathlib import Path

# Argumentos pasados por el run.py
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 3001
PROJECT_ROOT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(".")

class KanbanHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Endpoint de lectura DAST (Lee directo del disco)
        if self.path == "/api/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            registry_path = PROJECT_ROOT / "TASKS" / "registry.json"
            state_path = PROJECT_ROOT / "PROJECT_STATE.json"

            registry_data = []
            state_data = {}

            if registry_path.exists():
                with open(registry_path, "r", encoding="utf-8") as f:
                    registry_data = json.load(f)
            if state_path.exists():
                with open(state_path, "r", encoding="utf-8") as f:
                    state_data = json.load(f)

            response = {"registry": registry_data, "state": state_data}
            self.wfile.write(json.dumps(response).encode("utf-8"))
        
        # Servir la interfaz gráfica principal
        elif self.path == "/":
            self.path = "ui/index.html"
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        else:
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Asegurar que el servidor corre desde el directorio de la skill
os.chdir(Path(__file__).parent)

print(f"[*] Vibe Kanban Industrial Server running on port {PORT}")
print(f"[*] Target Project: {PROJECT_ROOT}")

# Iniciar servidor
with socketserver.TCPServer(("", PORT), KanbanHandler) as httpd:
    httpd.serve_forever()