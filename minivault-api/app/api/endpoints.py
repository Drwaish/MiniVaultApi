from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import json
from app.utils.logger import log_request_response
from app.services.generator import GeneratorService
import psutil
import time
import platform
import logging

router = APIRouter()

class GenerateRequest(BaseModel):
    prompt: str

class GenerateResponse(BaseModel):
    response: str

genresp = GeneratorService()
@router.post("/generate", response_model=GenerateResponse)
async def generate(request: GenerateRequest):
    try:
        response_text = genresp.generate_response(request.prompt)
        log_request_response(request.prompt, response_text)
        return GenerateResponse(response=response_text)
    except Exception as e:
        logging.error(f"Error in /generate endpoint: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/status")
async def get_status():
    try:
        # Get system uptime
        uptime_seconds = time.time() - psutil.boot_time()
        uptime = {
            "days": int(uptime_seconds // (24 * 3600)),
            "hours": int((uptime_seconds % (24 * 3600)) // 3600),
            "minutes": int((uptime_seconds % 3600) // 60),
            "seconds": int(uptime_seconds % 60),
        }

        # Get memory usage
        memory = psutil.virtual_memory()
        memory_info = {
            "total": memory.total,
            "available": memory.available,
            "used": memory.used,
            "percent": memory.percent,
        }

        # Check GPU info (if available)
        try:
            import torch
            gpu_available = torch.cuda.is_available()
            gpu_info = {
                "gpu_available": gpu_available,
                "gpu_name": torch.cuda.get_device_name(0) if gpu_available else None,
                "gpu_memory": torch.cuda.get_device_properties(0).total_memory if gpu_available else None,
            }
        except ImportError:
            gpu_info = {"gpu_available": False, "gpu_name": None, "gpu_memory": None}

        # System info
        system_info = {
            "os": platform.system(),
            "os_version": platform.version(),
            "architecture": platform.architecture()[0],
        }

        return {
            "uptime": uptime,
            "memory": memory_info,
            "gpu": gpu_info,
            "system": system_info,
        }
    except Exception as e:
        logging.error(f"Error in /status endpoint: {e}")
        raise HTTPException(status_code=500, detail=str(e))