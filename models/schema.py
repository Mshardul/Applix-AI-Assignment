import time
from pydantic import BaseModel
from typing import Optional


class TemperatureData(BaseModel):
    """ the data that will be stored in the DB """
    time: int                                               # UNIX timestamp
    temperature: float                                      # Degree Celsius
    location: str                                           # Location name (City, eg)
    created_at: int = int(time.time())
