from flask import Blueprint, request, jsonify
from .service import (
    list_guests,
    get_guest,
    create_guest,
    update_guest,
    delete_guest
)

main = Blueprint("main", __name__)

# =========================
# LISTAR CONVIDADOS
# =========================
@main.route("/guests", methods=["GET"])
def guests():
    event_id = request.args.get("event_id")
    search = request.args.get("search")

    data = list_guests(event_id)

    return jsonify(data)


# =========================
# BUSCAR POR ID
# =========================
@main.route("/guests/<int:id>", methods=["GET"])
def guest_by_id(id):
    return jsonify(get_guest(id))


# =========================
# CRIAR CONVIDADO
# =========================
@main.route("/guests", methods=["POST"])
def create():
    data = request.json
    result = create_guest(data)

    if result is None:
        return jsonify({"error": "CPF já cadastrado"}), 400

    return jsonify({"id": result})


# =========================
# ATUALIZAR
# =========================
@main.route("/guests/<int:id>", methods=["PUT"])
def update(id):
    data = request.json
    ok = update_guest(id, data)

    return jsonify({"success": ok})


# =========================
# DELETE
# =========================
@main.route("/guests/<int:id>", methods=["DELETE"])
def delete(id):
    delete_guest(id)
    return jsonify({"success": True})