from fruits_service.bd.connection import db
from bson import ObjectId

collection = db['fruits']

def insert_fruit(data):
    fruit = {
    "name": data.get("name"),
    "color": data.get("color"),
    "type": data.get("type"),
    "updates": data.get("updates"),
    "start_tracking_timestamp": data.get("start_tracking_timestamp"),
    "last_tracking_timestamp": data.get("last_tracking_timestamp"),
    "count": data.get("count")
    }
    result = collection.insert_one(data)
    return str(result.inserted_id)

def update_fruit(fruit_id, data):
    fruit = {
    "name": data.get("name"),
    "color": data.get("color"),
    "type": data.get("type"),
    "updates": data.get("updates"),
    "start_tracking_timestamp": data.get("start_tracking_timestamp"),
    "last_tracking_timestamp": data.get("last_tracking_timestamp"),
    "count": data.get("count")
    }
    result = collection.update_one(
        {"_id": ObjectId(fruit_id)},
        {"$set": data}
    )
    return result.modified_count

def delete_fruit(fruit_id):
    result = collection.delete_one({"_id": ObjectId(fruit_id)})
    return result.deleted_count

def get_fruit(fruit_id):
    result = collection.find_one({"_id": ObjectId(fruit_id)})
    if result:
        result["_id"] = str(result["_id"]) 
    return result

def list_fruit():
    fruits = []
    for result in collection.find():
        result["_id"] = str(result["_id"]) 
        fruits.append(result)
    return fruits

