# MiniVault API

## Project Overview

The MiniVault API is a lightweight local REST API designed to simulate a core ModelVault feature: running a local LLM (Large Language Model) to respond to user prompts completely offline. This project utilizes FastAPI for the API framework and integrates with Hugging Face Transformers for local model capabilities. It is ideal for developers looking to prototype or test local AI model interactions without relying on external services.

### Key Features
- **Offline Capability**: Operates entirely offline, ensuring data privacy.
- **FastAPI Framework**: Leverages FastAPI for high performance and ease of use.
- **Extensibility**: Designed to be easily extended with additional endpoints or model integrations.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- (Optional) Docker for containerized deployment

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Drwaish/MiniVaultApi.git
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

- **Description**: Generates a response based on the provided prompt.
- **Headers**:
  ```json
  {
    "Content-Type": "application/json"
  }
  ```
- **Input**:
  ```json
  {
    "prompt": "Hello, who are you?"
  }
  ```
- **Output**:
  ```json
  {
    "response": "I'm a local AI model, running offline!" // Response may vary based on the model
  }
  ```
- **Error Response**:
  ```json
  {
    "error": "Invalid input. 'prompt' field is required."
  }
  ```

## Logging

All requests and responses are logged to `logs/log.jsonl` for tracking and debugging purposes. Each log entry is in JSON Lines format, making it easy to parse and analyze. Example log entry:
```json
{
  "timestamp": "2025-07-27T12:34:56",
  "endpoint": "/generate",
  "request": {
    "prompt": "Hello, who are you?"
  },
  "response": {
    "response": "I'm a local AI model, running offline!"
  }
}
```
## CLI Tool

The MiniVault API includes a CLI tool for interacting with the application directly from the terminal. This tool simplifies testing and provides an alternative to using API clients like Postman or curl.

### Usage

1. **Run the CLI Tool**
   Navigate to the `minivault-api` directory and execute the CLI tool:
   ```bash
   python cli_tool.py --help
   ```
   This will display the available commands and their usage.

2. **Generate a Response**
   To generate a response using the CLI tool, use the following command:
   ```bash
   python cli_tool.py generate --prompt "Hello, who are you?"
   ```
   Example output:
   ```
   Response: I'm a local AI model, running offline!
   ```

3. **Additional Commands**
   The CLI tool can be extended with additional commands for more functionality. Use the `--help` flag to explore all available options.
   
## Tradeoffs and Improvements

- **Local Model Usage**: The API currently integrating a real local model via  Hugging Face Transformers for more dynamic responses.
- **Error Handling**: Implementing more robust error handling and validation for incoming requests can enhance the API's reliability.
- **CLI Interface**: A command-line interface could be added to facilitate testing and interaction with the API directly from the terminal.
- **Docker Support**: A Dockerfile is included for easy setup and reproducibility of the development environment.
- **Monitoring**: Adding a `/status` endpoint to provide insights into memory usage, GPU status, or uptime information.
- **Packaging**: Packaging the application as a self-contained local tool could improve the developer experience.






