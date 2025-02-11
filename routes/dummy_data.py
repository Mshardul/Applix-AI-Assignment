""" Routers related to Dummy Data """

# Third Party Libaries Import
from fastapi import APIRouter, Query, HTTPException

# Internal Project Imports
from data import dummy_data
from models.dummy_data import DummyDataResponse

router = APIRouter()

@router.get("/", response_model=DummyDataResponse, summary="Generate Dummy Data")
async def get_dummy_data(
    start_time: int = Query(-1, description="Start time as a UNIX timestamp"),
    end_time: int = Query(-1, description="End time as a UNIX timestamp")
):
    """
    Generates dummy temperature data within the given time range.
    """
    try:
        dummy_data.generate_temperature_data(start_time, end_time)
        return {
            "status": "success",
            "message": "File created successfully",
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
