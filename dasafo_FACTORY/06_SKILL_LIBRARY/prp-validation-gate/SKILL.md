---
version: 3.2.0-S
agent: PRODUCT_OWNER
---

# 📜 Skill | PRP Validation Gate

## Objective

Act as the mandatory industrial checkpoint to guarantee perfect alignment between user vision and factory execution before any production work begins.

## 🛠️ Interface (v3.2.0-S)

### Input Schema (SkillInput.params)

- `contract_path` (string, optional): Absolute path to `PRP_CONTRACT.json`.
- `force_audit` (boolean, optional): Default `false`.

### Output Schema (SkillOutput.result)

- `gate_status`: (string) "OPEN" | "LOCKED".
- `integrity_score`: (float) (0.0-1.0).
- `signing_status`: (string) "VALIDATED" | "DRAFT" | "MISSING".

### ⚖️ Mandato SI (Sistema Internacional)

Los criterios de éxito financieros o técnicos (latencia, throughput, memoria) deben estar definidos estrictamente en unidades del SI dentro del contrato.

## 🛡️ Industrial Constraints (Zero-Trust)

- **Mandatory Checkpoint:** No agent may advance to M2 (Production) without a physically `VALIDATED` contract file.
- **Integrity Lock:** THE Integrity Score is calculated after a physical cross-reference with global Factory standards. Hallucinating a "perfect score" result in automated lock.

## Protocol

1. **Requirement Interview:** Structure the "What", "Why", "Who", and Success Criteria.
2. **Contract production:** Generate/Verify `PRP_CONTRACT.json` in `$TARGET_PROJECT/LOCAL_KNOWLEDGE/`.
3. **Locking:** No agent may advance to M2 (Production) without a "validated" status.

---
*Skill v3.2.0-S | Status: Standardized.*
