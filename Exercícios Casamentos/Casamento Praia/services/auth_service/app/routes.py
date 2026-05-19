from flask import Blueprint,request
from .auth import login_user

main=Blueprint("main", __name__)

@main.route("/login", methods=["POST"])
def login():
    return login_user(request.json)