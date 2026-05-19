from flask import Blueprint,request,jsonify

from app.services import (
    list_guest,
    get_guest,
    create_guest,
    update_guest,
    delete_guest
)

main=Blueprint("main", __name__)

@main.route("/guests", methods=["GET"])
def get_guests():
    guests=list_guest()
    return jsonify(guests), 200

@main.route("/guests/<int:guest_id>", methods=["GET"])
def get_guest_by_id(guest_id):
    guest=get_guest(guest_id)
    return jsonify(guest),200

@main.route("/guests", methods=["POST"])
def create_guest_route():
    data=request.json 
    guest_id=create_guest(data)
    return jsonify({"message": "convidado criado com sucesso","id": guest_id}),200

@main.route("/guests/<int:guest_id>", methods=["PUT"])
def update_guest_route(guest_id):
    data=request.json
    update_guest(guest_id,data)
    return jsonify({"message": "convidado atualizado com sucesso"}),200

@main.route("/guests/<int:guest_id>", methods=["DELETE"])
def delete_guest_route(guest_id):
    delete_guest(guest_id)
    return jsonify({"message": "usuario deletado com sucesso"}),200