""" Database Communication for Processed Data """

# Internal Project Imports
from config.database import database

def store_processed_data(processed_data):
    """ Store Processed Data to the DB """
    try:
        collection = database["temperature_data"]
        result = collection.insert_many(processed_data, ordered=False)
        return result.inserted_ids
    except Exception as e:
        print(e)
        return []
