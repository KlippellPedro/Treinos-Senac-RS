from flask import Blueprint, request, jsonify
from mysql.connector import IntegrityError

from app.service import (
    list_guests,
    get_guest,
    create_guest,
    update_guest,
    delete_guest
)

main = Blueprint("main", __name__)

@main.route("/guests", methods=["GET"])
def get_guests():
    guests = list_guests()
    return jsonify(guests), 200


@main.route("/guests/<int:guest_id>", methods=["GET"])
def get_guest_by_id(guest_id):
    guest = get_guest(guest_id)

    if not guest:
        return jsonify({"error": "Convidado não encontrado"}), 404

    return jsonify(guest), 200



@main.route("/guests", methods=["POST"])
def create_guest_route():
    data = request.json


    if not data or "nome" not in data or "email" not in data:
        return jsonify({"error": "Dados inválidos"}), 400

    try:
        guest_id = create_guest(data)

        return jsonify({
            "message": "Convidado criado com sucesso",
            "id": guest_id
        }), 201

    except IntegrityError as e:
        # CPF duplicado (unique constraint)
        if "cpf" in str(e):
            return jsonify({"error": "CPF já cadastrado"}), 400

        return jsonify({"error": "Erro de integridade no banco"}), 400



@main.route("/guests/<int:guest_id>", methods=["PUT"])
def update_guest_route(guest_id):
    data = request.json

    if not data:
        return jsonify({"error": "Dados inválidos"}), 400

    try:
        update_guest(guest_id, data)

        return jsonify({
            "message": "Convidado atualizado com sucesso"
        }), 200

    except IntegrityError as e:
        if "cpf" in str(e):
            return jsonify({"error": "CPF já cadastrado"}), 400

        return jsonify({"error": "Erro ao atualizar"}), 400



@main.route("/guests/<int:guest_id>", methods=["DELETE"])
def delete_guest_route(guest_id):
    guest = get_guest(guest_id)

    if not guest:
        return jsonify({"error": "Convidado não encontrado"}), 404

    delete_guest(guest_id)

    return jsonify({
        "message": "Convidado removido com sucesso"
    }), 200