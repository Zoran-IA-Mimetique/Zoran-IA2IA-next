from fastapi import FastAPI, Body
from typing import Dict, Any
import json, time

app = FastAPI(title="EthicChain Guard (PoC)")

BANNED = {"exploit", "malware", "dox", "hate", "violence", "terror"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/check")
def check(payload: Dict[str, Any] = Body(...)):
    text = json.dumps(payload).lower()
    flagged = [w for w in BANNED if w in text]
    decision = "block" if flagged else "allow"
    return {"decision": decision, "flagged": flagged, "ts": time.time()}