from flask import Flask, request, jsonify
from fruits_service.bd.crud import insert_fruit, update_fruit, delete_fruit, get_fruit, list_fruit
from bson import ObjectId

app = Flask(__name__)

@app.route("/fruits", methods=["POST"])
def create():
    data = request.get_json()
    fruit_id = insert_fruit(data)
    return jsonify({"id": fruit_id}), 201

@app.route("/fruits/<id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    updated_count = update_fruit(id,data)
    if updated_count:
        return jsonify({"mensaje": "updated fruit"}),200
    return jsonify({"bug": "fruit not found"}), 404

@app.route("/fruits/<id>", methods=["DELETE"])
def delete(id):
    deleted_count = delete_fruit(id)
    if deleted_count:
        return jsonify({"message": "fruit deleted"}), 200
    return jsonify({"bug": "fruit not found"}), 404

@app.route("/fruits/<id>", methods=["GET"])
def get(id):
    result = get_fruit(id)
    if result:
        return jsonify(result), 200
    return jsonify({"bug": "fruit not found"}), 404

@app.route("/fruits", methods=["GET"])
def get_list():
   fruits = list_fruit()
   return jsonify(fruits), 200  


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

