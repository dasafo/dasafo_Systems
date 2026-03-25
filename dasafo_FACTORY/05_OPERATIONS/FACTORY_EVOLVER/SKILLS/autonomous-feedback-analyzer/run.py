#!/usr/bin/env python3
"""
Autonomous Feedback Analyzer (v3.1)
Part of Dasafo Factory Evolver Department.

Analyzes the FEEDBACK-LOG.md to identify recurring failure patterns
and trigger self-healing architectural updates.
"""

import os
import sys
import argparse
from collections import Counter

def analyze_feedback(log_path):
    """Parses the feedback log and identifies hot spots."""
    if not os.path.exists(log_path):
        return False, "Feedback log not found."

    with open(log_path, 'r') as f:
        content = f.read()

    # Simple keyword-based pattern recognition
    keywords = [
        "ImportError", "ConnectionRefused", "Authentication", 
        "Timeout", "MemoryLimit", "DockerError", "PRP_FAILURE"
    ]
    
    findings = Counter()
    for kw in keywords:
        findings[kw] = content.lower().count(kw.lower())

    # Get top 3 issues
    top_issues = findings.most_common(3)
    
    report = "🧠 EVOLUTIONARY ANALYSIS REPORT\n"
    report += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    for issue, count in top_issues:
        severity = "LOW" if count < 3 else "MEDIUM" if count < 10 else "CRITICAL"
        report += f"- {issue}: {count} occurrences ({severity})\n"
    
    if findings["ImportError"] > 5:
        report += "\n🔧 PROPOSED PATCH: Enforce absolute imports in all production code templates.\n"
    elif findings["ConnectionRefused"] > 5:
        report += "\n🔧 PROPOSED PATCH: Audit dasafo_network and INFRA port persistence.\n"
    
    report += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    return True, report

def main():
    parser = argparse.ArgumentParser(description="Dasafo Factory Evolver")
    parser.add_argument("--log", default="/home/david/Documents/AI/AGENTES/dasafo_Systems/dasafo_FACTORY/FEEDBACK-LOG.md", help="Path to FEEDBACK-LOG.md")

    args = parser.parse_args()

    success, report = analyze_feedback(args.log)
    if success:
        print(report)
    else:
        print(f"❌ EVOLUTION FAILURE: {report}")
        sys.exit(1)

if __name__ == "__main__":
    main()
