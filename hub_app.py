from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from typing import Any, Dict
import json, os, pathlib
from jsonschema import validate, ValidationError

app = FastAPI(title="Zoran IA2IA Hub (PoC v2)")

SCHEMA_DIR = pathlib.Path(__file__).resolve().parents[1] / "glyphs" / "schemas"

class Message(BaseModel):
    glyphe: Dict[str, Any]
    payload: Dict[str, Any] = {}

def load_schema(intent: str) -> dict:
    fn = SCHEMA_DIR / f"{intent}.schema.json"
    if not fn.exists():
        raise FileNotFoundError(f"Unknown glyphe schema: {intent}")
    return json.loads(fn.read_text(encoding="utf-8"))

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/glyphs/validate")
def glyphs_validate(glyphe: Dict[str, Any] = Body(...)):
    intent = glyphe.get("intent")
    if not intent:
        raise HTTPException(400, "Missing 'intent' in glyphe")
    try:
        schema = load_schema(intent)
        validate(instance=glyphe, schema=schema)
    except FileNotFoundError as e:
        raise HTTPException(404, str(e))
    except ValidationError as e:
        raise HTTPException(422, f"Invalid glyphe: {e.message}")
    return {"valid": True, "intent": intent}

def ethic_guard_check(msg: Dict[str, Any]) -> Dict[str, Any]:
    # Simple heuristic PoC: block if payload contains banned terms
    banned = {"exploit", "malware", "dox", "hate", "violence"}
    text = json.dumps(msg).lower()
    flagged = [w for w in banned if w in text]
    return {"allowed": not flagged, "flagged": flagged}

@app.post("/messages")
def submit_message(message: Message):
    guard = ethic_guard_check(message.dict())
    if not guard["allowed"]:
        raise HTTPException(403, f"Blocked by EthicChain: {guard['flagged']}")
    # In-memory accept (stub). Real impl would enqueue/persist.
    return {"status": "accepted", "guard": guard}