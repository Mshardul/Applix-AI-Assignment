from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil

from services.process import process_temperature_data
from config.database import database
from utilities import file_handler

router = APIRouter()

@router.post("/")
async def upload_temperature_data(file: UploadFile = File(...)):
    """
    1. Receive CSV / XLSX files
    2. Parse and Clean the Data
    3. Store Cleaned-up Data in MongoDB.
    """
    # Save file temporarily
    file_extension: str = file.filename.split(".")[-1]
    file_path = file_handler.random_file_name(file_extension)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        # Process the uploaded file
        data = process_temperature_data(str(file_path))
        if not data:  # Ensure data is not empty before inserting
            raise HTTPException(status_code=400, detail="No valid data found in the file.")

        # Insert into MongoDB
        collection = database["temperature_data"]
        collection.insert_many(data)
        print("data saved in the db")

        return {
            "status": "success",
            "message": "File processed successfully",
            "data": {"records_inserted": len(data)}
        }

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))

    finally:
        # Cleanup file after processing
        if file_path.exists():
            file_path.unlink()