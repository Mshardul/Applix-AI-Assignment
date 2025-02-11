""" Models related to Retreival of Dummy Data """

# External Libraries Import
from pydantic import BaseModel
from typing import Dict

class TemperatureDataResponse(BaseModel):
    """
    Response returned when existing Data is retreived for visualization
    """
    status: str
    data: Dict
