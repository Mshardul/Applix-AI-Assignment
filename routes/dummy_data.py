from fastapi import APIRouter, HTTPException
import shutil

from services.process import process_temperature_data
from config import database
from utilities import file_handler
from data import dummy_data

router = APIRouter()

@router.get("/")
async def get_dummy_data(start_time: int=-1, end_time: int=-1):
    try:
        dummy_data.generate_temperature_data(start_time, end_time)
        return {
            "status": "success",
            "message": "File created successfully",
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
