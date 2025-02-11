""" Models related to Upload of Dummy Data """

# Standard Libraries Import
from typing import Dict, Optional

# External Libraries Import
from pydantic import BaseModel

class UploadResponse(BaseModel):
    """
    Response returned when new Data is uploaded to the DB.
    """
    status: str
    message: str
    data: Optional[Dict] = None
