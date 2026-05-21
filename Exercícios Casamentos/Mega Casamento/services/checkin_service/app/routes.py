from flask import Blueprint, request, jsonify
from functools import wraps
import jwt
import os
from .services import realizar_checkin

main = Blueprint("main", __name__)
SECRET_KEY= os.getenv("SECRET_KEY")

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header= request.headers.get("Authorization")
        if not auth_header:
            return jsonify({"error": "Token ausente"}), 401
        try:
            token=auth_header.split(" ")[1]
            data=jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            request.user= data
        except IndexError:
            return jsonify({"error": "Formato inválido do token"}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Token inválido"}), 401
        return f(*args, **kwargs)
    return decorated

@main.route("/checkin/<int:id_convidado>", methods=["POST"])
@token_required
def checkin(id_convidado):
    id_usuario=request.user.get("id")
    if not id_usuario:
        return jsonify({"error": "Usuario inválido no token"}), 401
    response,status=realizar_checkin(id_convidado,id_usuario)
    return jsonify(response), status
