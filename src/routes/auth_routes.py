from flask import Blueprint, request
from src.controllers.auth_controller import register, login, promote_user
from src.config import Config
import jwt

auth_routes = Blueprint("auth_routes", __name__)

@auth_routes.post("/register")
def register_user():
    return register(request.json)

@auth_routes.post("/login")
def login_user():
    return login(request.json)


def get_user_from_token():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    try:
        data = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
        return data["user_id"], data["role"] == "admin"
    except:
        return None, None

@auth_routes.put("/promote")
def promote():
    user_id, is_admin = get_user_from_token()
    return promote_user(request.json, user_id, is_admin)
