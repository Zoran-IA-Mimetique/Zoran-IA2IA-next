import argparse, json, pathlib
from jsonschema import validate, ValidationError

def main():
    p = argparse.ArgumentParser()
    p.add_argument("glyph", help="path to glyph json")
    args = p.parse_args()
    glyph = json.loads(pathlib.Path(args.glyph).read_text())
    intent = glyph.get("intent")
    schema = json.loads((pathlib.Path(__file__).resolve().parents[1] / "glyphs" / "schemas" / f"{intent}.schema.json").read_text())
    try:
        validate(instance=glyph, schema=schema)
        print("VALID")
    except ValidationError as e:
        print("INVALID:", e.message)

if __name__ == "__main__":
    main()