from transformers import pipeline

class LocalModel:
    def __init__(self):
        self.model = pipeline("text-generation", model="gpt2")  # Replace with the desired local model

    def generate_response(self, prompt: str) -> str:
        response = self.model(prompt, max_length=50, num_return_sequences=1)
        return response[0]['generated_text'] if response else "No response generated."