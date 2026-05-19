# Módulos do Flask para acesso ao contexto da requisição e retorno de JSON
from flask import request, jsonify

# Biblioteca JWT + acesso a variáveis de ambiente
import jwt, os

# Preserve metadados da função original ao usar decorator
from functools import wraps

# Chave secreta usada para validar tokens
# Deve ser a mesma usada pelo serviço de auth
SECRET_KEY = os.getenv("SECRET_KEY", "supersegredo123")


def token_required(f):
    """
    Decorator que garante que a rota só seja acessada com um JWT válido.

    Fluxo:
    1. Extrai token do header Authorization Bearer
    2. Valida assinatura e expiração
    3. Injeta payload no contexto da requisição
    4. Libera execução da rota

    Em caso de falha, retorna 401 Unauthorized.
    """

    @wraps(f)
    def decorated(*args, **kwargs):

        # Pega o header Authorization
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return jsonify({"error": "Token ausente"}), 401

        try:
            # Garante que o header está no formato "Bearer <token>"
            parts = auth_header.split()
            if len(parts) != 2 or parts[0] != "Bearer":
                return jsonify({"error": "Token inválido"}), 401

            token = parts[1]

            # Decodifica o token usando a chave compartilhada
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

            # Injeta payload no contexto da requisição (para uso nas rotas)
            request.user = payload

        except jwt.ExpiredSignatureError:
            # Token expirado
            return jsonify({"error": "Token expirado"}), 401

        except jwt.InvalidTokenError:
            # Token inválido ou adulterado
            return jsonify({"error": "Token inválido"}), 401

        # Token válido → executa a função original
        return f(*args, **kwargs)

    return decorated