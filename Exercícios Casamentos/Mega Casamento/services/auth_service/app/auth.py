from flask import jsonify, request
from functools import wraps
from database import get_connection
from .validators import validate_email,validate_password
import jwt,datetime,bcrypt
import os

SECRET_KEY= os.getenv("SECRET_KEY")

def gerar_token(user):
    payload= {
        "id": user["id_usuario"],
        "role": user["id_perfil"],
        "exp": datetime.datetime.now(datetime.timezone.utc)+ datetime.timedelta(hours=2)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def login_user(data):
    email= data.get("email")
    senha= data.get("senha")
    valid,msg=validate_email(email)
    if not valid:
        return jsonify({"error": msg}),400
    valid,msg=validate_password(senha)
    if not valid:
        return jsonify({"error": msg}),400
    
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuario WHERE email=%s", (email,))
    user=cursor.fetchone()
    cursor.close()
    conn.close()
    
    if bcrypt.checkpw(senha.encode(), user["senha"].encode()):
        token=gerar_token(user)
        del user["senha"]
        return jsonify({"token": token, "user": user}),200
    return jsonify({"error": "Senha inválida"}),401

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token= request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "Token ausente"}),401
        try:
            token=token.split(" ")[1]
            data=jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            request.user=data
        except Exception:
            return jsonify({"error": "Token inválido"}), 401
        return f(*args, **kwargs)
    
    return decorated