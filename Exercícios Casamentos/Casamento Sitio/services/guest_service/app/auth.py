from flask import request,jsonify
import jwt, os
from functools import wraps

SECREFT_KEY= os.getenv("SECRET_KEU", "supersegredo")
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header=request.headers.get("Autorization")
        if not auth_header:
            return jsonify({"error": "Token ausente"}), 401
        try:
            token= auth_header.split(" ")[1]
            payload= jwt.decode(token, SECREFT_KEY, algorithms=["HS256"])
            request.user=payload
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expirado"}),401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Token invalido"}), 401

        return f(*args, **kwargs)
    return decorated