from flask import Flask
from app.routes import main
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()
app=Flask(__name__)
app.register_blueprint(main)
CORS(app)
if __name__=="__main__":
    app.run(
        host=os.getenv("DB_HOST"),
        port=os.getenv("PORT"),
        debug=True
    )