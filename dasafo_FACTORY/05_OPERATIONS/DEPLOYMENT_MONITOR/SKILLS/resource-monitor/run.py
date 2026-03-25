#!/usr/bin/env python3
"""
Resource Monitor Pulse (v3.1)
Part of Dasafo Factory Operations Department.

Directly interfaces with the INFRA node (Glances) to monitor 
the health and resource consumption of factory projects.
"""

import json
import urllib.request
import argparse
import sys

def get_glances_metrics(host="localhost", port=61208):
    """Fetches metrics from the Glances REST API."""
    url = f"http://{host}:{port}/api/3/all"
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        return None, f"Failed to connect to Glances at {url}: {str(e)}"

def format_pulse_report(project_name, metrics):
    """Formats raw Glances metrics into the industrial 'Resource Pulse' report."""
    # Note: Glances 'all' response is a large dictionary. 
    # We extract core metrics for the whole system as a baseline.
    cpu = metrics.get("cpu", {}).get("total", "N/A")
    mem = metrics.get("mem", {}).get("used", 0) / (1024 * 1024) # MB
    disk = metrics.get("fs", [{}])[0].get("used", 0) / (1024 * 1024 * 1024) # GB
    
    status = "✅ STABLE"
    if cpu != "N/A" and float(cpu) > 90:
        status = "🚨 CRITICAL"
    elif float(mem) > 8000: # Threshold for the server
        status = "⚠️ WARNING"

    report = f"""
📈 RESOURCE PULSE: {project_name}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CPU: {cpu}%
RAM: {mem:.2f} MB
DISK: {disk:.2f} GB
Status: {status}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    return report

def main():
    parser = argparse.ArgumentParser(description="Dasafo Operations Stethoscope")
    parser.add_argument("--project", default="FACTORY-GLOBAL", help="Project name to report")
    parser.add_argument("--host", default="localhost", help="Glances API host")
    parser.add_argument("--port", type=int, default=61208, help="Glances API port")

    args = parser.parse_args()

    # 1. Fetch Metrics
    metrics, error = get_glances_metrics(args.host, args.port)
    if error:
        print(f"❌ MONITORING FAILURE: {error}")
        sys.exit(1)
    
    # 2. Format & Print Report
    print(format_pulse_report(args.project, metrics))

if __name__ == "__main__":
    main()
