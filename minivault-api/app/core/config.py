from pydantic import BaseSettings

class Settings(BaseSettings):
    model_path: str = "path/to/local/model"
    log_file: str = "logs/log.jsonl"
    api_version: str = "v1"

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()