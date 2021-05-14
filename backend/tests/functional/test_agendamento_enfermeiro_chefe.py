from fastapi import FastAPI
from fastapi.testclient import TestClient

from fescam.app.main import app

client = TestClient(app)

def test_read_all_agendamento_enfermeiro_chefe():
    response = client.get("/agendamento_enfermeiro_chefe")
    assert response.status_code == 200

def test_read_agendamento_enfermeiro_chefe():
    agend_enfchefe_id = 1
    response = client.get(f'/agendamento_enfermeiro_chefe/{agend_enfchefe_id}')
    assert response.status_code == 200