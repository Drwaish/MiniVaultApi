import json
import pytest
from app.services.generator import generate_response

def test_generate_response_valid_prompt():
    prompt = "Hello, who are you?"
    expected_response = "I'm a local AI model, running offline!"
    
    response = generate_response(prompt)
    
    assert response == expected_response

def test_generate_response_empty_prompt():
    prompt = ""
    expected_response = "Prompt cannot be empty."
    
    response = generate_response(prompt)
    
    assert response == expected_response

def test_generate_response_invalid_prompt():
    prompt = None
    expected_response = "Prompt cannot be None."
    
    response = generate_response(prompt)
    
    assert response == expected_response

def test_generate_response_logging():
    prompt = "Test logging"
    response = generate_response(prompt)
    
    with open('logs/log.jsonl', 'r') as log_file:
        logs = log_file.readlines()
    
    assert len(logs) > 0
    log_entry = json.loads(logs[-1])
    assert log_entry['prompt'] == prompt
    assert log_entry['response'] == response