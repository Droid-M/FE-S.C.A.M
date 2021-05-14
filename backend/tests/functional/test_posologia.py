from fastapi import FastAPI
from fastapi.testclient import TestClient

from fescam.app.main import app

client = TestClient(app)

def test_read_all_posologia():
    response = client.get("/posologia")
    assert response.status_code == 200

def test_read_posologia():
    posologia_id = 1
    response = client.get(f'/posologia/{posologia_id}')
    assert response.status_code == 200