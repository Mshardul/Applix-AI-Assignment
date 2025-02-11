""" Database Communication for Processed Data """

# Standard Libraries Import
from datetime import datetime

# Internal Project Imports
from config.database import database

def store_raw_data(file_name: str, raw_data, created_at: int) -> bool:
    """ Store Raw Data to the DB """
    try:
        raw_collection = database["temperature_data_raw"]
        raw_collection.insert_one({
            "filename": file_name,
            "created_at": created_at,
            "uploaded_at": int(datetime.utcnow().timestamp()),
            "raw_data": raw_data
        })
        return True
    except Exception as e:
        print(e)
        return False
