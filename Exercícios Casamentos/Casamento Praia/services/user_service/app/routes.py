from flask import Blueprint,jsonify,request
from .auth import token_required

from app.service import(
    list_user,
    get_user,
    create_user,
    update_user,
    delete_user
)
main=Blueprint("main", __name__)

@main.route("/users", methods=["GET"])
@token_required
def get_user():
    users=list_user()
    return jsonify(users),200

@main.route("/users/</int:user_id>", methods=["GET"])
@token_required
def get_user_by_id(user_id):
    users=get_user(user_id)
    return jsonify(users),200

@main.route("/users", methods=["POST"])
@token_required
def create_user_route():
    data=request.json
    user_id=create_user(data)
    return jsonify({"message": "usuario criado com sucesso", "id":user_id}),200

@main.route("/users", methods=["PUT"])
@token_required
def update_user_route():
    data