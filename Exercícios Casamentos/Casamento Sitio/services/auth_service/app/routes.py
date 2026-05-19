from flask import Blueprint, request
from .auth import login_user

main=Blueprint("main", __name__)

@main.route("/login", methods=["POST"])
def login():
     data= request.get_json()

     if not data:
          return {"error": "JSON invalido ou ausente"}, 400
     
     return login_user(data)