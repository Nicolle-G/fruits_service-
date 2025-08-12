from bson import ObjectId
from quart import Quart, request, jsonify, Response
from bd.crud import insert_fruit, update_fruit, delete_fruit, get_fruit_id, list_fruit

app = Quart(__name__)

@app.route("/fruits", methods=["POST"])
async def create() -> Response:
    data = await request.get_json()
    fruit_id = await insert_fruit(data)
    return jsonify({"id": fruit_id}), 201

@app.route("/fruits/<id>", methods=["PUT"])
async def update(id: str) -> Response:
    data = await request.get_json()
    updated_count = await update_fruit(id,data)
    if updated_count:
        return jsonify({"message": "updated fruit"}),200
    return jsonify({"bug": "fruit not found"}), 404

@app.route("/fruits/<id>", methods=["DELETE"])
async def delete(id: str) -> Response:
    deleted_count = await delete_fruit(id)
    if deleted_count:
        return jsonify({"message": "fruit deleted"}), 200
    return jsonify({"bug": "fruit not found"}), 404

@app.route("/fruits/<id>", methods=["GET"])
async def get(id: str) -> Response:
    result = await get_fruit_id(id)
    if result:
        return jsonify(result), 200
    return jsonify({"bug": "fruit not found"}), 404

@app.route("/fruits", methods=["GET"])
async def get_list() -> Response:
   fruits = await list_fruit()
   return jsonify(fruits), 200  

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)