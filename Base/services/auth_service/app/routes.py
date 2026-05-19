from flask import Blueprint, request  # Importa Blueprint para modularizar rotas e request para acessar dados das requisições
from .auth import login_user           # Importa a função de autenticação que processa login e gera token

# Cria o Blueprint 'main', que vai agrupar as rotas relacionadas
main = Blueprint("main", __name__)

# Define a rota /login que responde apenas ao método POST
@main.route("/login", methods=["POST"])
def login():
    # Pega os dados enviados pelo cliente em formato JSON
    data = request.get_json()

    # Se não houver JSON no corpo da requisição, retorna erro 400 (bad request)
    if not data:
        return {"error": "JSON inválido ou ausente"}, 400

    # Chama a função login_user passando os dados do JSON e retorna o resultado
    return login_user(data)