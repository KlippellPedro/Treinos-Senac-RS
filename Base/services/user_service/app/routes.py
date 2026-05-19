# Blueprint do Flask para organizar rotas do módulo de usuários
from flask import Blueprint, request, jsonify

# Importa funções de negócio service layer
from .service import list_users, get_user, create_user, update_user, delete_user

# Importa decorator de autenticação JWT
from .auth import token_required

# Cria o Blueprint chamado "main" para agrupar as rotas
main = Blueprint("main", __name__)


# GET /users -> Lista todos os usuários
@main.route("/users", methods=["GET"])
@token_required  # Protege a rota, só acessível com token válido
def route_list_users():
    users = list_users()        # Chama camada de serviço para buscar usuários
    return jsonify(users), 200  # Retorna lista em JSON + status 200 OK


# GET /users/<user_id> -> Retorna usuário específico
@main.route("/users/<int:user_id>", methods=["GET"])
@token_required
def route_get_user(user_id):
    user = get_user(user_id)            # Busca usuário pelo ID
    if user:
        return jsonify(user), 200       # Retorna dados se encontrado
    return jsonify({"error": "Usuário não encontrado"}), 404  # 404 se não existir


# POST /users -> Cria um novo usuário
@main.route("/users", methods=["POST"])
@token_required
def route_create_user():
    data = request.get_json()                  # Pega dados JSON do body
    user_id, msg = create_user(data)          # Cria usuário via service
    if not user_id:                            # Se falhou, retorna erro
        return jsonify({"error": msg}), 400
    return jsonify({"message": "Usuário criado", "id": user_id}), 201  # 201 Created


# PUT /users/<user_id> -> Atualiza usuário existente
@main.route("/users/<int:user_id>", methods=["PUT"])
@token_required
def route_update_user(user_id):
    data = request.get_json()       # Pega dados JSON do body
    update_user(user_id, data)     # Atualiza via service
    return jsonify({"message": "Usuário atualizado"}), 200  # 200 OK


# DELETE /users/<user_id> -> Remove usuário
@main.route("/users/<int:user_id>", methods=["DELETE"])
@token_required
def route_delete_user(user_id):
    delete_user(user_id)           # Chama service para deletar usuário
    return jsonify({"message": "Usuário removido"}), 200  # 200 OK