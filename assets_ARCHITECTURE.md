# Architecture (PoC v2)

- Hub FastAPI expose `/health`, `/glyphs/validate`, `/messages`.
- EthicChain reçoit des charges utiles et renvoie `allow|block` (heuristiques PoC).
- Glyphes JSON sont validés via JSON Schema (draft-07).
- 100 scénarios YAML pilotent des tests IA→IA.
