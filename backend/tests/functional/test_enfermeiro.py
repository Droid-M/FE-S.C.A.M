from fastapi import FastAPI
from fastapi.testclient import TestClient

from fescam.app.main import app

client = TestClient(app)

def test_read_all_enfermeiro():
    response = client.get("/enfermeiro")
    assert response.status_code == 200

def test_read_enfermeiro():
    atendente_id = 1
    response = client.get(f'/enfermeiro/{atendente_id}')
    assert response.status_code == 200