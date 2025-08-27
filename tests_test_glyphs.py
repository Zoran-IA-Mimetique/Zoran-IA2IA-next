import json, pathlib
from jsonschema import validate

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "glyphs" / "schemas"
SAMPLES_DIR = ROOT / "glyphs" / "samples"

def load_schema(intent):
    return json.loads((SCHEMA_DIR / f"{intent}.schema.json").read_text())

def test_samples_validate():
    for s in SAMPLES_DIR.glob("sample_*.json"):
        sample = json.loads(s.read_text())
        intent = sample["intent"]
        schema = load_schema(intent)
        validate(instance=sample, schema=schema)