""" Models related to Upload of Dummy Data """

# External Libraries
from pydantic import BaseModel
from typing import Dict, Optional

class UploadResponse(BaseModel):
    """
    Response returned when new Data is uploaded to the DB.
    """
    status: str
    message: str
    data: Optional[Dict] = None
