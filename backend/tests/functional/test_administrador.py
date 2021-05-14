from fastapi import FastAPI
from fastapi.testclient import TestClient

from fescam.app.main import app

client = TestClient(app)

def test_read_all_administrador():
    response = client.get("/administrador")
    assert response.status_code == 200

def test_read_administrador():
    administrador_id = 1
    response = client.get(f'/administrador/{administrador_id}')
    assert response.status_code == 200