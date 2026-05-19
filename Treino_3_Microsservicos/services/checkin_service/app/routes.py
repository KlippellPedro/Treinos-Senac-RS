from flask import Blueprint, request, jsonify
from functools import wraps
import jwt, os
from .service import realizar_checkin

main = Blueprint("main", __name__)
SECRET_KEY = os.getenv("SECRET_KEY", "senac-secret")


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"error": "Token ausente"}), 401

        try:
            token = token.split(" ")[1]
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            request.user = data
        except Exception:
            return jsonify({"error": "Token inválido"}), 401

        return f(*args, **kwargs)

    return decorated


@main.route("/checkin/<int:id_convidado>", methods=["POST"])
@token_required
def checkin(id_convidado):
    id_usuario = request.user["id"]

    response, status = realizar_checkin(id_convidado, id_usuario)
    return jsonify(response), status