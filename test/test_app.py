from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from fruits_service.service.app import app
import pytest

MONGO_URL = "mongodb://localhost:27017"

@pytest.mark.asyncio
async def test_dummy():
    test_app = app.test_client()
    
    test_client = AsyncIOMotorClient(MONGO_URL)
    db = test_client['fruits_bd'] 
    await db.fruits.delete_many({})

    res = await test_app.post("/fruits", json={"name": "banana", "color": "yellow"})
    assert res.status_code == 201
    json_res = await res.get_json()
    fruit_id = str(json_res["id"])  


    res = await test_app.put(f"/fruits/{fruit_id}", json={"name": "lemon", "color": "green"})
    assert res.status_code == 200

    fake_id = str(ObjectId())
    res = await test_app.put(f"/fruits/{fake_id}", json={"name": "kiwi", "color": "green"})
    assert res.status_code == 404


    res = await test_app.get(f"/fruits/{fruit_id}")
    assert res.status_code == 200
    json_res = await res.get_json()
    assert json_res["name"] == "lemon"
    assert json_res["color"] == "green"  

    res = await test_app.get(f"/fruits/{fake_id}")
    assert res.status_code == 404

    res = await test_app.get("/fruits")
    assert res.status_code == 200
    json_res = await res.get_json()
    assert len(json_res) == 1
    assert json_res[0]["name"] == "lemon"
    assert json_res[0]["color"] == "green"

    
    res = await test_app.delete(f"/fruits/{fruit_id}")
    assert res.status_code == 200

    res = await test_app.delete(f"/fruits/{fake_id}")
    assert res.status_code == 404

 
    await test_client.drop_database("fruits_bd")
    test_client.close()
