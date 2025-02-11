""" Routers related to Data Retreival """

# Third Party Libaries Import
from datetime import datetime
from fastapi import APIRouter, Query
from pymongo import ASCENDING

# Internal Project Imports
from config.database import database
from models.retrieve import TemperatureDataResponse
from utilities.data_handler import structure_for_frontend

router = APIRouter()

@router.get("/", response_model=TemperatureDataResponse, summary="Retrieve Temperature Data")
async def get_temperature_data(
    start_time: int = Query(None, description="Start time as a UNIX timestamp"),
    end_time: int = Query(None, description="End time as a UNIX timestamp")
):
    """
    - Retrieves temperature data between a given time range.
    - Defaults to the last **30 days** if no time range is provided.

    - Returns formatted data for
       - Values Chart
       - Values Table
       - Statistics Table
    """
    print("params: ", start_time, end_time)
    collection = database["temperature_data"]

    # Set default values if start_time and end_time are not provided
    if end_time is None:
        end_time = int(datetime.utcnow().timestamp())  # Current time
    if start_time is None:
        start_time = end_time - (30*24*60*60)  # 30 days ago

    # Query MongoDB for records within the time range
    records = list(collection.find(
        {"time": {"$gte": start_time, "$lte": end_time}},
        {"_id": 0, "time": 1, "temperature": 1, "location": 1}
    ).sort("time", ASCENDING))
    print(start_time, end_time, records)
    if not records:
        return {"status": "success", "data": {"labels": [], "cityLabels": [], "datasets": []}}

    # Return formatted response
    response = structure_for_frontend(records)
    return {
        "status": "success",
        "data": response
    }
