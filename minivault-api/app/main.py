from fastapi import FastAPI
from app.api.endpoints import router as api_router
from app.utils.logger import setup_logging
import logging

app = FastAPI(title="MiniVault API")

# Setup logging
setup_logging()

# Include API routes
app.include_router(api_router)

@app.get("/health")
async def health_check():
    return {"health": "OK"}

if __name__ == "__main__":
    try:
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000)
    except Exception as e:
        logging.error(f"Error starting the application: {e}")