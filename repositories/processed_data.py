from datetime import datetime
from config.database import database

def store_processed_data(processed_data):
    try:
        collection = database["temperature_data"]
        result = collection.insert_many(processed_data, ordered=False)
        return result.inserted_ids
    except Exception as e:
        print(e)
        return []

def get_processed_data_by_location(location, year, month, week):
    filter_query = {
        "location": location,
        "time": {
            "$gte": datetime(year, month or 1, 1).timestamp(),
            "$lt": datetime(year + (month == 0), (month + 1) if month else 1, 1).timestamp()
        }
    }
    # Fetch temperature data
    data = list(database["temperature_data"].find(filter_query))
    if not data:
        return None

def get_processed_data_by_ids(ids):
    rows = database["temperature_data"].find(
        {"_id": {"$in": ids}}, {"time": 1, "location": 1}
    )
    resp = {}
    for row in rows:
        time = row["time"]
        loc = row["location"]
        if loc not in resp:
            resp[loc] = []
        resp[loc].append(time)
    return resp
