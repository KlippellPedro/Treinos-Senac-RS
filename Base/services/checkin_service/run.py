from flask import Flask
from flask_cors import CORS
from app.routes import main
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.register_blueprint(main)

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "senac-secret")

CORS(app)

if __name__ == "__main__":
    app.run(port=int(os.getenv("PORT", 5004)), debug=True)