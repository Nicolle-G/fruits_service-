from pymongo import MongoClient
import os 

MONGO_URL = os.environ.get("MONGO_URL", "mongodb://localhost:27017")
client = MongoClient(MONGO_URL)
db = client['fruits_bd']
collection = db['fruits']
