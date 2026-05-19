from flask import Flask
from app.routes import main
from flask_cors import CORS
from dotenv import load_dotenv
import os

# carrega variáveis do .env
load_dotenv()

app = Flask(__name__)

# registra rotas
app.register_blueprint(main)

# libera acesso do front (SPA)
CORS(app)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 5002)),
        debug=True
    )