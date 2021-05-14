from fastapi import FastAPI
from fastapi.testclient import TestClient

from fescam.app.main import app

client = TestClient(app)


def test_read_all_enfermeirochefe():
    response = client.get("/enfermeirochefe")
    assert response.status_code == 200

def test_read_enfermeirochefe():
    enf_chefe_id = 1
    response = client.get(f'/enfermeirochefe/{enf_chefe_id}')
    assert response.status_code == 200