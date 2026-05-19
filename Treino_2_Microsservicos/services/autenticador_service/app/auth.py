from flask import jsonify
import jwt,datetime,bcrypt
from functools import wraps
from .database import get_connection
from .validator import validate_email,validate_password
import os

SECRET_KEY= os.getenv("SECRET_KEY")

def gerar_token(user):
    payload = {
        "id": user["id_usuario"],
        "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=2)
    }

def login_user(data):
    email=data.get("email")
    senha=data.get("senha")

    valid,msg = validate_email(email)
    if not valid:
        return jsonify({"error": msg}), 400

    valid,msg = validate_password(senha)
    if not valid:
        return jsonify({"error": msg}), 400

    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuario WHERE email=%s", (email,))
    user=cursor.fetchone()
    cursor.close()
    conn.close()
    
    if not user:
        return jsonify({"error": "Usuario não encontrado"})
    
    if bcrypt.checkpw(senha.encode(), user["senha"].encode()):
        token=gerar_token(user)
        del user["senha"]
        return jsonify({"token": token, "user": user})
    
    return jsonify({"error": "Senha inválida"}), 401

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        from flask import request
        token=request.headers.get("Authorization")

        if not token:
            return jsonify({"error": "Token ausente"}), 401
        
        try:
            token=token.split(" ")[1]
            jwt.decode(token, SECRET_KEY, algorithms= ["HS256"])

        except Exception as e:
            return jsonify({"error": "Token inválido", "details": str(e)}), 401
        
        return f (*args, **kwargs)
    return decorated