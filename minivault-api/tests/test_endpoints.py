import json
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_endpoint():
    response = client.post("/generate", json={"prompt": "Hello, who are you?"})
    assert response.status_code == 200
    assert "response" in response.json()
    assert response.json()["response"] == "I'm a local AI model, running offline!"

def test_generate_endpoint_invalid_input():
    response = client.post("/generate", json={"invalid_key": "Hello, who are you?"})
    assert response.status_code == 422  # Unprocessable Entity for invalid input

def test_generate_endpoint_empty_prompt():
    response = client.post("/generate", json={"prompt": ""})
    assert response.status_code == 200
    assert "response" in response.json()
    assert response.json()["response"] == "I'm a local AI model, running offline!"