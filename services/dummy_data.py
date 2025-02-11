""" Processing Dummy Data """

# Standard Libraries Import
import random
import time

# Third Party Libraries Import
import pandas as pd

# Internal Project Imports
from utilities import file_handler

CITIES: list[str] = ["Delhi", "Mumbai", "Kolkata", "Chennai"]

def generate_temperature_data(start_time: int = -1, end_time: int = -1):
    """
    Generates a CSV file with 5000 random temperature records.
    - time: Random UNIX timestamp between start_time and end_time.
    - temperature: Random float between 10°C and 45°C.
    - location: Random city from ['Delhi', 'Mumbai', 'Kolkata', 'Chennai'].
    - created_at: Current UNIX timestamp
    """

    data = []

    if end_time < 0:
        end_time = int(time.time())
    if start_time < 0 or start_time >= end_time:
        start_time = end_time - 30*24*60*60

    for _ in range(50):
        timestamp: int = random.randint(start_time, end_time)
        temperature: float = round(random.uniform(10, 45), 2)
        location: str = random.choice(CITIES)
        created_at: int = int(time.time())
        data.append({"time": timestamp, "temperature": temperature, "location": location, "created_at": created_at})

    # Sort data by time
    data.sort(key=lambda x: x["time"])

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Save to CSV
    output_file: str = str(file_handler.random_file_name("csv"))
    df.to_csv(output_file, index=False)
    print(f"CSV file '{output_file}' created successfully with 5000 records.")
