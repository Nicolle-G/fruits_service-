from bson import ObjectId
from bd.connection import db

collection = db['fruits']

async def insert_fruit(data: dict) -> str:
    fruit = {
    "name": data.get("name"),
    "color": data.get("color"),
    "type": data.get("type"),
    "updates": data.get("updates"),
    "start_tracking_timestamp": data.get("start_tracking_timestamp"),
    "last_tracking_timestamp": data.get("last_tracking_timestamp"),
    "count": data.get("count")
    }
    result = await collection.insert_one(fruit)
    return str(result.inserted_id)

async def update_fruit(fruit_id: str, data:dict):
    result = await collection.update_one(
        {"_id": ObjectId(fruit_id)},
        {"$set": data}
    )
    return result.modified_count

async def delete_fruit(fruit_id: str) -> int:
    result = await collection.delete_one({"_id": ObjectId(fruit_id)})
    return result.deleted_count

async def get_fruit_id(fruit_id: str) -> str:
    result = await collection.find_one({"_id": ObjectId(fruit_id)})
    if result:
        result["_id"] = str(result["_id"]) 
    return result

async def list_fruit() -> list[dict]:
    fruits = []
    async for result in collection.find():
        result["_id"] = str(result["_id"]) 
        fruits.append(result)
    return fruits