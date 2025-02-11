""" Models related to Generation of Dummy Data """
# External Libraries
from pydantic import BaseModel

class DummyDataResponse(BaseModel):
    """
    Response returned when Dummy Data is generated
    """
    status: str
    message: str
