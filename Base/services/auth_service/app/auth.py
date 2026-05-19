from flask import jsonify, request  # jsonify: retorna respostas em JSON | request: acessa dados da requisição
import jwt, datetime, bcrypt        # jwt: gera/valida token | datetime: controle de tempo | bcrypt: hash de senha
from functools import wraps         # wraps: preserva metadados ao usar decorators
from .database import get_connection  # Função para conectar ao banco de dados
from .validators import validate_email, validate_password  # Funções de validação de entrada
import os  # Permite acessar variáveis de ambiente

# Define a chave secreta usada para assinar o JWT
# Tenta pegar do .env, se não existir usa valor padrão
SECRET_KEY = os.getenv("SECRET_KEY", "senac-secret")


# Função responsável por gerar o token JWT
def gerar_token(user):
    payload = {
        "id": user["id_usuario"],  # ID do usuário
        "role": user["id_perfil"],  # Perfil do usuário (admin, cerimonialista, etc.)
        # Define tempo de expiração do token (2 horas)
        "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=2)
    }
    # Codifica o payload usando a SECRET_KEY
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


# Função responsável pelo login do usuário
def login_user(data):
    # Extrai email e senha do JSON recebido
    email = data.get("email")
    senha = data.get("senha")

    # Valida o email
    valid, msg = validate_email(email)
    if not valid:
        return jsonify({"error": msg}), 400

    # Valida a senha
    valid, msg = validate_password(senha)
    if not valid:
        return jsonify({"error": msg}), 400

    # Conecta ao banco de dados
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Busca usuário pelo email
    cursor.execute("SELECT * FROM usuario WHERE email=%s", (email,))
    user = cursor.fetchone()

    # Fecha conexão com banco
    cursor.close()
    conn.close()

    # Se usuário não existir, retorna erro 404
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404

    # Verifica se a senha fornecida corresponde ao hash armazenado
    if bcrypt.checkpw(senha.encode(), user["senha"].encode()):
        # Gera token JWT
        token = gerar_token(user)

        # Remove senha do retorno (segurança)
        del user["senha"]

        # Retorna token e dados do usuário
        return jsonify({
            "token": token,
            "user": user
        }), 200

    # Se senha estiver incorreta
    return jsonify({"error": "Senha inválida"}), 401


# Decorator para proteger rotas com autenticação JWT
def token_required(f):
    @wraps(f)  # Mantém nome e metadata da função original
    def decorated(*args, **kwargs):

        # Obtém o token do header Authorization
        token = request.headers.get("Authorization")

        # Se não houver token, bloqueia acesso
        if not token:
            return jsonify({"error": "Token ausente"}), 401

        try:
            # Espera formato: "Bearer TOKEN"
            token = token.split(" ")[1]

            # Decodifica o token usando a SECRET_KEY
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

            # Armazena dados do usuário na requisição
            request.user = data

        except Exception:
            # Se token for inválido ou mal formatado
            return jsonify({"error": "Token inválido"}), 401

        # Se tudo estiver ok, executa a função protegida
        return f(*args, **kwargs)

    return decorated