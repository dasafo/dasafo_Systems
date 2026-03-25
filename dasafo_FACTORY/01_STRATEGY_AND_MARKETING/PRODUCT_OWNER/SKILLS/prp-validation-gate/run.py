#!/usr/bin/env python3
"""
PRP Contract Validation Gate (v3.1)
Part of Dasafo Factory Strategy Department.

This tool validates a project's PRP_CONTRACT.json against the industrial template
to ensure mission solidity before proceeding to M2 (Architecture).
"""

import json
import os
import sys
import argparse
from datetime import datetime

def validate_contract(contract_path, template_path):
    """Checks if the project contract matches the required schema and is complete."""
    try:
        with open(template_path, 'r') as f:
            template = json.load(f)
        with open(contract_path, 'r') as f:
            contract = json.load(f)
    except Exception as e:
        return False, f"Error reading files: {str(e)}"

    # Basic Schema Validation
    missing_root_keys = [key for key in template.keys() if key not in contract]
    if missing_root_keys:
        return False, f"Missing root keys: {', '.join(missing_root_keys)}"

    # Vision Validation
    if "vision" in template:
        missing_vision_keys = [key for key in template["vision"].keys() if key not in contract.get("vision", {})]
        if missing_vision_keys:
            return False, f"Missing vision parameters: {', '.join(missing_vision_keys)}"

    # Check if mandatory fields are still placeholders
    for key, value in contract.get("vision", {}).items():
        if value == template["vision"].get(key):
            return False, f"Field '{key}' is still using the placeholder value from the template."

    return True, "Solidity check PASSED."

def sign_contract(contract_path, signer_name):
    """Signs the contract and marks it as validated."""
    try:
        with open(contract_path, 'r') as f:
            contract = json.load(f)
        
        contract["prp_status"] = "validated"
        contract["validated_at"] = datetime.now().isoformat()
        contract["validated_by"] = signer_name
        
        with open(contract_path, 'w') as f:
            json.dump(contract, f, indent=2)
        
        return True, f"Contract signed by {signer_name}."
    except Exception as e:
        return False, f"Failed to sign contract: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="Dasafo Factory PRP Gate")
    parser.add_argument("--contract", required=True, help="Path to the project's PRP_CONTRACT.json")
    parser.add_argument("--template", required=True, help="Path to the universal PRP_CONTRACT_TEMPLATE.json")
    parser.add_argument("--sign", action="store_true", help="Attempt to sign the contract if validation passes")
    parser.add_argument("--signer", default="PRODUCT_OWNER", help="Name of the signer")

    args = parser.parse_args()

    # Absolute path checks
    if not os.path.exists(args.contract):
        print(f"ERROR: Contract file not found at {args.contract}")
        sys.exit(1)
    if not os.path.exists(args.template):
        print(f"ERROR: Template file not found at {args.template}")
        sys.exit(1)

    # 1. Validation
    success, message = validate_contract(args.contract, args.template)
    if not success:
        print(f"❌ SOLIDITY FAILURE: {message}")
        sys.exit(1)
    
    print(f"✅ {message}")

    # 2. Signing
    if args.sign:
        success, message = sign_contract(args.contract, args.signer)
        if not success:
            print(f"❌ SIGNATURE FAILURE: {message}")
            sys.exit(1)
        print(f"✍️ {message}")

if __name__ == "__main__":
    main()
