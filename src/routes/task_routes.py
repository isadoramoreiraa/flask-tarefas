from flask import Blueprint, request
from src.controllers.task_controller import *
import jwt
from src.config import Config

task_routes = Blueprint("task_routes", __name__)

def get_user_from_token():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    try:
        data = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
        return data["user_id"], data["role"] == "admin"
    except:
        return None, None


@task_routes.post("/")
def create():
    user, is_admin = get_user_from_token()
    return create_task(request.json, user)


@task_routes.get("/")
def read():
    user, is_admin = get_user_from_token()
    return get_tasks(user, is_admin)


@task_routes.put("/<int:task_id>")
def update(task_id):
    user, is_admin = get_user_from_token()
    return update_task(task_id, request.json, user, is_admin)


@task_routes.delete("/<int:task_id>")
def delete(task_id):
    user, is_admin = get_user_from_token()
    return delete_task(task_id, user, is_admin)
