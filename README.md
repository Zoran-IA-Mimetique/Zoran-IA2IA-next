# Zoran IA↔IA — ZUP Skeleton (flat)

**Objet** : dépôt *à plat* prêt à l’emploi pour intégrer un **parser universel** (ZUP) dans le Hub IA↔IA, avec API FastAPI, mode *light* (sans blockchain), schéma pivot JSON‑LD, tests et Docker.

---

## 1) Ce que contient ce ZIP (flat)
- `api.py` — API FastAPI (`/inject`, `/audit`), Pydantic, OpenAPI auto.
- `injector.py` — Gestionnaire d’injection avec **ZUP** si dispo, sinon **fallback**.
- `utils_normalize.py` — Normalisation simple (JSON/CSV/XML basique) pour le fallback.
- `zup.schema.json` — Schéma pivot JSON Schema **versionné**.
- `openapi.yaml` — Spéc OpenAPI 3.0 minimale (endpoints & manifest).
- `config.yaml` — Configuration (mode light / chain placeholders, intégrité HMAC).
- `requirements.txt` — Dépendances Python (FastAPI, Uvicorn, Tests).
- `Dockerfile` + `docker-compose.yml` — Lancement conteneurisé.
- `Makefile` — Raccourcis `install`, `run`, `test`, `docker-up`.
- `tests.py` — Tests rapides avec `TestClient` FastAPI.
- `LICENSE` — MIT.
- `sample.json`, `sample.csv` — Exemples d’inputs.
- `README.md` — Ce guide.

> **Remarque** : si le paquet `zoran-universal-parser` (ZUP) n’est pas encore sur PyPI, le code passe automatiquement en **fallback** via `utils_normalize.py`.

---

## 2) Installation locale (Python 3.10+)

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

> Optionnel si ZUP est publié :  
> `pip install zoran-universal-parser`

### Lancer l’API
```bash
uvicorn api:app --host 0.0.0.0 --port 8000 --reload
```
- Swagger UI : `http://localhost:8000/docs`
- OpenAPI JSON : `http://localhost:8000/openapi.json`

### Tester en 10 secondes
```bash
python tests.py
# ou
pytest -q
```

---

## 3) Utilisation — Hello World

```bash
curl -X POST http://localhost:8000/inject -H "Content-Type: application/json" -d @sample.json
```

Réponse attendue :
```json
{"interaction_id":"<uuid>"}
```

---

## 4) Configuration (mode light / chain)

Fichier `config.yaml` :
```yaml
use_chain: false
storage:
  type: s3
  bucket: zoran-audit
  integrity: hmac-sha256
security:
  ratelimit_rpm: 120
  require_hmac: false  # mettre true en prod
zup:
  schema: zup.schema.json
  context: https://zoran.ai/zup/1
```

- **Mode light** : `use_chain: false` → logs sur S3/Blob (intégrité HMAC).
- **Mode chain (à venir)** : remplace `use_chain: true` et configure Quorum/Besu (placeholders).

---

## 5) Points d’extension

- **ΔM11.3** : branche `run_pipeline()` pour ajouter contrôle/rollback.
- **Hyperglottal** : sérialiser `manifest` avec vos balises avant persistance.
- **PII Masking** : ajouter une passe de masquage dans `process()`.
- **Observabilité** : brancher Prometheus + logs structurés JSON.

---

## 6) FAQ

**ZUP n’est pas dispo ?** → Le fallback gère JSON/CSV/XML basique. Vous pouvez brancher vos parseurs spécifiques sans toucher l’API.  
**Pourquoi un schéma versionné ?** → Compat ascendante, migrations contrôlées.  
**Pourquoi un ZIP à plat ?** → Simplicité de diffusion et copier‑coller rapide.

---

## 7) Licence & contact
- Licence : MIT (voir `LICENSE`).
- Contact : tabary01@gmail.com

Bon build. 🦋
