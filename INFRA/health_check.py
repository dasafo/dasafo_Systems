import socket
import os
import time

# --- CONFIGURACIÓN DE NODOS (Power Grid) ---
NODES = {
    "Neo4j (Knowledge Graph - HTTP)": ("localhost", 7474),
    "Neo4j (Knowledge Graph - Bolt)": ("localhost", 7687),
    "Postgres (DB Operacional)": ("localhost", 5432),
    "Redis (Caché Industrial)": ("localhost", 6379),
    "Health Monitor (Glances)": ("localhost", 61208)
}

def check_port(host, port, timeout=2.0):
    """Hace un PING TCP para ver si el puerto está aceptando conexiones."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        result = sock.connect_ex((host, int(port)))
        return result == 0
    except Exception:
        return False
    finally:
        sock.close()

def print_separator():
    print("-" * 60)

def main():
    print("\n🚀 Iniciando Operación Nexus: Dasafo Power Grid Health-Check")
    print_separator()
    print("Iniciando sondeo de la malla de red industrial v5.0-MCP...")
    print_separator()
    
    all_healthy = True
    
    for name, (host, port) in NODES.items():
        # Animación mínima para dar feedback visual
        print(f"📡 Sondeando {name} en {host}:{port}...", end="", flush=True)
        time.sleep(0.3)
        
        is_healthy = check_port(host, port)
        
        if is_healthy:
            print(" [ ✅ ONLINE ]")
        else:
            print(" [ ❌ OFFLINE ]")
            all_healthy = False

    print_separator()
    if all_healthy:
        print("🟢 SISTEMA ESTABLE: Los 4 nodos están latiendo y conectados.")
    else:
        print("🔴 ALERTA DE INFRAESTRUCTURA: Uno o más nodos no responden.")
        print("Recomendación: Ejecutar 'docker-compose up -d' o revisar el socket de Docker.")
    print_separator()

if __name__ == "__main__":
    main()
