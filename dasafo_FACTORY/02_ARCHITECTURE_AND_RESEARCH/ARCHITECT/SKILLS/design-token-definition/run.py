#!/usr/bin/env python3
"""
Design Token Validator (v3.1)
Part of Dasafo Factory Architecture Department.

Enforces visual consistency by validating UI styles against 
the factory's premium 'Vibe-DNA' tokens.
"""

import json
import argparse
import sys
import os

DEFAULT_TOKENS = {
    "colors": {
        "brand": "#00E5FF",  # Electric Blue
        "danger": "#FF3D00", # Neon Red
        "background": "rgba(10, 10, 10, 0.8)", # Glass Dark
        "surface": "rgba(255, 255, 255, 0.05)" # Glass Surface
    },
    "spacing": {
        "unit": 8,
        "xs": 4, "sm": 8, "md": 16, "lg": 24, "xl": 32
    },
    "typography": {
        "primary": "Outfit, sans-serif",
        "secondary": "Inter, sans-serif"
    },
    "effects": {
        "glass_blur": "12px",
        "transition": "300ms cubic-bezier(0.4, 0, 0.2, 1)"
    }
}

def validate_tokens(project_tokens_path):
    """Compares project tokens against factory standards."""
    try:
        with open(project_tokens_path, 'r') as f:
            project_tokens = json.load(f)
    except Exception as e:
        return False, f"Error reading project tokens: {str(e)}"

    missing_classes = [cls for cls in DEFAULT_TOKENS.keys() if cls not in project_tokens]
    if missing_classes:
        return False, f"Missing token classes: {', '.join(missing_classes)}"
    
    # Check for "plain" colors (anti-vibe check)
    if "colors" in project_tokens:
        for name, value in project_tokens["colors"].items():
            if value.lower() in ["red", "blue", "green", "black", "white"]:
                return False, f"Color '{name}' uses a generic value '{value}'. Premium vibe required."

    return True, "Design tokens are VALID and PREMIUM."

def main():
    parser = argparse.ArgumentParser(description="Dasafo Design Architect Tool")
    parser.add_argument("--action", choices=["export", "validate"], required=True)
    parser.add_argument("--output", help="Path to export default tokens")
    parser.add_argument("--input", help="Path to project tokens for validation")

    args = parser.parse_args()

    if args.action == "export":
        output_path = args.output or "design_tokens.json"
        with open(output_path, 'w') as f:
            json.dump(DEFAULT_TOKENS, f, indent=2)
        print(f"✅ Default Dasafo Vibe tokens exported to {output_path}")

    elif args.action == "validate":
        if not args.input:
            print("ERROR: --input is required for validation.")
            sys.exit(1)
        
        success, message = validate_tokens(args.input)
        if success:
            print(f"✅ {message}")
        else:
            print(f"❌ DESIGN CONSISTENCY FAILURE: {message}")
            sys.exit(1)

if __name__ == "__main__":
    main()
