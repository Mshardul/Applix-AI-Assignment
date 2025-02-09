# External Libraries
from datetime import datetime
from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
from typing import Optional

# Internal Project Imports
from repositories.processed_data import store_processed_data
from repositories.raw_data import store_raw_data
from services.process import process_temperature_data
from utilities import file_handler

router = APIRouter()

@router.post("/")
async def upload_temperature_data(file: UploadFile = File(...)):
    """
    1. Receive CSV / XLSX files
    2. Parse and Clean the Data
    3. Store Cleaned-up Data in MongoDB.
    """
    entry_time: int = int(datetime.utcnow().timestamp())

    # data_store_response
    raw_data_stored: bool = False
    processed_data_stored: bool = False

    # Save file temporarily
    file_name: Optional[str] = file.filename
    if not file_name:
        return HTTPException(status_code=400, detail="Unrecognizable File Name")

    file_extension: str = file_name.split(".")[-1]
    file_path = file_handler.random_file_name(file_extension)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        # Process the uploaded file
        raw_data, data = process_temperature_data(str(file_path))
        if not (raw_data and data):  # Ensure data is not empty
            raise HTTPException(status_code=400, detail="No valid data found in the file.")

        # store data
        raw_data_stored = store_raw_data(
            file_name=file_name+str(entry_time),
            created_at=entry_time,
            raw_data=raw_data
        )
        if raw_data_stored:
            processed_data_stored = bool(store_processed_data(processed_data=data))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        # Cleanup file after processing
        if file_path.exists():
            file_path.unlink()

    # return response
    exit_time: int = int(datetime.utcnow().timestamp())
    data_resp = {
        "raw_data_stored": raw_data_stored,
        "processed_data_stored": processed_data_stored,
        "response_time": (exit_time-entry_time),
    }
    if raw_data_stored and processed_data_stored:
        return {
            "status": "Success",
            "message": "Records proceseed Successfully!"
        }
    return {
        "status": "Error",
        "message": "Could not process request. Pleas try again later!",
        "data": data_resp
    }
