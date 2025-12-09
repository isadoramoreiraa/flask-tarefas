from src.models.user import User
from flask import jsonify
from src.extensions import db
import jwt, datetime
from src.config import Config

def register(data):
    username = data.get("username")
    password = data.get("password")

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Usuário já existe"}), 400

    user = User(username=username)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()
    
    return jsonify({"message": "Usuário registrado"}), 201



def promote_user(data, current_user_id, is_admin):
    if not is_admin:
        return jsonify({"error": "Acesso negado"}), 403

    username = data.get("username")
    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404

    user.role = "admin"
    db.session.commit()
    return jsonify({"message": f"{username} agora é admin!"})


def login(data):
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({"error": "Credenciais inválidas"}), 401

    token = jwt.encode({
        "user_id": user.id,
        "role": user.role,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }, Config.SECRET_KEY, algorithm="HS256")

    return jsonify({"token": token})
