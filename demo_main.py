import json, random, pathlib

# Demo: simulate two agents exchanging a validated glyph through the hub (offline stub).

ROOT = pathlib.Path(__file__).resolve().parents[1]
SAMPLES_DIR = ROOT / "glyphs" / "samples"
print("Demo start — loading a random glyph sample...")
samples = sorted(SAMPLES_DIR.glob("sample_*.json"))
sample = json.loads(samples[random.randrange(len(samples))].read_text())
print("Chosen:", sample["meta"]["id"], "intent:", sample["intent"])
print("→ This PoC ships files only; run the FastAPI apps via docker-compose to exercise endpoints.")