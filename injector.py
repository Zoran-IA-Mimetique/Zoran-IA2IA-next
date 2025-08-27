from typing import Any, Dict
import json

# Try ZUP import (optional)
try:
    from zup import ZUP  # type: ignore
    ZUP_AVAILABLE = True
except Exception:
    ZUP_AVAILABLE = False

from utils_normalize import fast_normalize

class InjectorManager:
    def __init__(self, schema_path: str = "zup.schema.json"):
        self.zup = ZUP(schema_path) if ZUP_AVAILABLE else None

    def process(self, raw_input: Any) -> Dict:
        try:
            if self.zup:
                graph = self.zup.parse(raw_input)          # type: ignore[attr-defined]
                manifest = graph.to_jsonld()               # type: ignore[attr-defined]
            else:
                normalized = fast_normalize(raw_input)
                manifest = {
                    "@context": "https://zoran.ai/zup/1",
                    "type": "UniversalManifest",
                    "payload": normalized,
                    "extra": {"parser": "fallback"}
                }
            return self.run_pipeline(manifest)
        except Exception as e:
            return {"status": "error", "stage": "parse", "message": str(e)}

    def run_pipeline(self, manifest: Dict) -> Dict:
        # Hook: ΔM11.3, Hyperglottal, audit/logs, persistence…
        # For now, just acknowledge
        return {"status": "ok", "manifest_id": manifest.get("id", None)}
