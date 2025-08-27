from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_inject_basic():
    payload = {"type":"UniversalManifest","payload":{"hello":"world"}}
    r = client.post("/inject", json=payload)
    assert r.status_code == 200
    assert "interaction_id" in r.json()

def test_inject_error():
    # Missing payload
    payload = {"type":"UniversalManifest"}
    r = client.post("/inject", json=payload)
    assert r.status_code == 422  # validation error
