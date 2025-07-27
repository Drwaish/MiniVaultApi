# MiniVault API

## Project Overview

The MiniVault API is a lightweight local REST API designed to simulate a core ModelVault feature: running a local LLM (Large Language Model) to respond to user prompts completely offline. This project utilizes FastAPI for the API framework and integrates with Hugging Face Transformers for local model capabilities.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd minivault-api
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Access the API**
   The API will be available at `http://127.0.0.1:8000`. You can test the `/generate` endpoint using tools like Postman or curl.

## API Endpoints

### POST /generate

- **Input:**
  ```json
  {
    "prompt": "Hello, who are you?"
  }
  ```

- **Output:**
  ```json
  {
    "response": "I'm a local AI model, running offline!"
  }
  ```

## Logging

All requests and responses are logged to `logs/log.jsonl` for tracking and debugging purposes.

## Tradeoffs and Improvements

- **Local Model Usage:** The API currently uses a stubbed response. Future improvements could include integrating a real local model via Ollama or Hugging Face Transformers for more dynamic responses.
- **Error Handling:** Implementing more robust error handling and validation for incoming requests can enhance the API's reliability.
- **CLI Interface:** A command-line interface could be added to facilitate testing and interaction with the API directly from the terminal.
- **Docker Support:** A Dockerfile is included for easy setup and reproducibility of the development environment.

## Bonus Features

- A `/status` endpoint could be implemented to provide insights into memory usage, GPU status, or uptime information.
- Packaging the application as a self-contained local tool could improve the developer experience.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.