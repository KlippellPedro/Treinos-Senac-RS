from flask import Blueprint, request, jsonify
from .service import list_users, get_user, create_user, update_user, delete_user
from .auth import token_required

main = Blueprint("main", __name__)

@main.route("/users", methods=["GET"])
@token_required
def route_list_users():
    users = list_users()
    return jsonify(users), 200

@main.route("/users/<int:user_id>", methods=["GET"])
@token_required
def route_get_user(user_id):
    user = get_user(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "Usuário não encontrado"}), 404

@main.route("/users", methods=["POST"])
@token_required
def route_create_user():
    data = request.get_json()
    user_id, msg = create_user(data)
    if not user_id:
        return jsonify({"error": msg}), 400
    return jsonify({"message": "Usuário criado", "id": user_id}), 201

@main.route("/users/<int:user_id>", methods=["PUT"])
@token_required
def route_update_user(user_id):
    data = request.get_json()
    update_user(user_id, data)
    return jsonify({"message": "Usuário atualizado"}), 200

@main.route("/users/<int:user_id>", methods=["DELETE"])
@token_required
def route_delete_user(user_id):
    delete_user(user_id)
    return jsonify({"message": "Usuário removido"}), 200
