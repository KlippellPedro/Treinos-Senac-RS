from flask import Blueprint,request,jsonify
from .services import list_guests, get_guest, create_guest, update_guest, delete_guest

main=Blueprint("main", __name__)
@main.route("/guests", methods=["GET"])
def guests():
    event_id =request.args.get("event_id")
    search=request.args.get("search")
    data=list_guests(event_id)
    return jsonify(data)

@main.route("/guests/<int:id>", methods=["GET"])
def guests_by_id(id):
    return jsonify(get_guest(id))

@main.route("/guests/<int:id>", methods=["POST"])
def create():
    data=request.json
    result=create_guest(data)
    if result is None:
        return jsonify({"error": "CPF já cadastrado"}), 400
    return jsonify({"id": result})

@main.route("/guests/<int:id>", methods=["PUT"])
def update(id):
    data=request.json
    ok=update_guest(id,data)
    return jsonify({"sucess": ok})

@main.route("/guests/<int:id>", methods=["DELETE"])
def delete():
    delete_guest(id)
    return jsonify({"sucess": True})