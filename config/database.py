from pymongo import MongoClient
import os

# MongoDB credentials
MONGODB_USERNAME: str = "shardullingwal94"
MONGODB_PASSWORD: str = "CnjwIBhgbdDtNFMy"

# MongoDB Atlas connection string
MONGODB_URI: str = "mongodb+srv://shardullingwal94:CnjwIBhgbdDtNFMy@temperaturemonitoring.b5nd1.mongodb.net/?retryWrites=true&w=majority&appName=TemperatureMonitoring"

# Connect to MongoDB
client = MongoClient(MONGODB_URI)
database = client["TemperatureMonitoring"]
