import os
from flask import Flask
from app.routes import main
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
# Registra o Blueprint 'main', adicionando suas rotas à aplicação principal
app.register_blueprint(main)


app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
# Configura a chave secreta do Flask usada para JWT e sessões.
# Tenta ler do .env (SECRET_KEY), se não existir, usa 'senac-secret' como padrão.

CORS(app)#Permite requisições de outros domínios como frontend

if __name__ == "__main__":
    app.run(port=int(os.getenv("PORT", 5001)), debug=True)