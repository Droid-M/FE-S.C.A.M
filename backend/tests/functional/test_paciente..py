from fastapi import FastAPI
from fastapi.testclient import TestClient

from fescam.app.main import app

client = TestClient(app)

def test_read_all_paciente():
    response = client.get("/paciente")
    assert response.status_code == 200

def test_read_paciente():
    paciente_id = 1
    response = client.get(f'/paciente/{paciente_id}')
    assert response.status_code == 200