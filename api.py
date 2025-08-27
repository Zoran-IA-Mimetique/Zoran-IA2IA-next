from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import uuid4
from typing import Optional, Dict, Any
import json

from injector import InjectorManager

app = FastAPI(title="Zoran IA2IA Hub API", version="1.0.0")
injector = InjectorManager(schema_path="zup.schema.json")

class UniversalManifest(BaseModel):
    id: Optional[str] = None
    type: str = Field("UniversalManifest", const=True)
    payload: Dict[str, Any]
    source: Optional[str] = None
    extra: Optional[Dict[str, Any]] = None

@app.post("/inject")
def inject(manifest: UniversalManifest):
    try:
        mid = manifest.id or str(uuid4())
        data = manifest.model_dump()
        data["id"] = mid
        result = injector.process(data)
        if result.get("status") == "error":
            raise HTTPException(status_code=400, detail=result["message"])
        return {"interaction_id": mid}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/audit/{id}")
def audit(id: str):
    # Placeholder audit trail
    return {"id": id, "events": []}
