from flask import Blueprint, request,jsonify
from .services import list_users,get_user, create_user,update_user,delete_user
from auth import token_required

main=Blueprint("main", __name__)

@main.route("/users", methods=["GET"])
@token_required
def users():
    users=list_users()
    return jsonify(users),200

@main.route("/users/<int:id>", methods=["GET"])
@token_required
def users_by_id(id):
    user=get_user(id)
    if user:
        return jsonify(user),200
    return ({"error": "Usuario não encontrado"}), 401

