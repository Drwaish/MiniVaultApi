from transformers import AutoModelForCausalLM, AutoTokenizer
import logging

class LocalModel:
    def __init__(self):
        try:
            self.checkpoint = "HuggingFaceTB/SmolLM-135M-Instruct"
            self.tokenizer = AutoTokenizer.from_pretrained(self.checkpoint)
            self.device = "cuda"
            self.model = AutoModelForCausalLM.from_pretrained(self.checkpoint).to(self.device)
        except Exception as e:
            logging.error(f"Error initializing LocalModel: {e}")
            raise

    def generate_response(self, query: str) -> str:
        try:
            messages = [{"role": "user", "content": query}]
            input_text = self.tokenizer.apply_chat_template(messages, tokenize=False)
            inputs = self.tokenizer.encode(input_text, return_tensors="pt").to(self.device)
            outputs = self.model.generate(inputs, max_new_tokens=50, temperature=0.2, top_p=0.9, do_sample=True)
            response_data = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            data = response_data.split("assistant")
            if len(data) > 0:
                return data[-1]
            else:
                return "No response generated"
        except Exception as e:
            logging.error(f"Error generating response: {e}")
            return "Error generating response"