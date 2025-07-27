from app.models.local_model import LocalModel
from app.utils.logger import log_request_response
import json

class GeneratorService:
    def __init__(self):
        self.model = LocalModel()

    def generate_response(self, prompt: str) -> str:
        response = self.model.generate(prompt)
        return response

    def process_request(self, request_data: dict) -> dict:
        prompt = request_data.get("prompt", "")
        response = self.generate_response(prompt)
        
        log_request_response(request_data, response)
        
        return {
            "response": response
        }