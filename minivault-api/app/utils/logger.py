import logging
import json
from datetime import datetime

def setup_logging():
    # Configure the logger
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("logs/log.jsonl"),
            logging.StreamHandler()
        ]
    )

def log_request_response(prompt: str, response: str):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "response": response
    }
    logging.info(json.dumps(log_entry))