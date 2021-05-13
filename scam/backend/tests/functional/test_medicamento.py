from fastapi import FastAPI
from fastapi.testclient import TestClient

from backend.app.app.main import app

client = TestClient(app)

def test_read_all_medicamento():
    response = client.get("/medicamento")
    assert response.status_code == 200

def test_read_medicamento():
    medicamento_id = 1
    response = client.get(f'/medicamento/{medicamento_id}')
    assert response.status_code == 200