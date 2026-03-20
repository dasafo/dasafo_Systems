# 03. Scientific & Physical Rigor
> **Objective:** The agency often processes real-world data; the rules of mathematics and physics are unbreakable.

## 1. The International System (SI Units)
- It is strictly prohibited to persist or communicate metrics in imperial or non-standardized systems at the base level.
- **Weight:** Kilograms (kg).
- **Distance:** Meters (m).
- **Temperature:** Kelvin (K).
- **Pressure:** Pascals (Pa).
- *Sole exception:* Transformation of these data fields EXCLUSIVELY in the UI layer (Data-to-Presentation) if the client demands to read "Celsius degrees", but the Backend-DB transmission is always in SI.

## 2. Robust Typing
- Contracts must be explicit (`schemas.py`), validating floating data types or nested objects using tools like `Pydantic` or `Zod`. Never trust a generic dictionary.

## 3. Model Lifecycle (Data Science)
- Code is not the only source of truth for a Data Scientist. 
- *Datasets* and pre-trained Models are formal company Artifacts.
- **Obligation:** Version datasets in parallel with the code in context repositories (simulating DVC/MLFlow tags). A model that transitions from `data_v1` to `data_v2` is structurally a different model, even if the `model.py` file hasn't changed a single letter.
