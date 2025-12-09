from flask import Flask
from src.extensions import db
from src.config import Config

from src.routes.auth_routes import auth_routes
from src.routes.task_routes import task_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    
    with app.app_context():
        from src.models.user import User
        from src.models.task import Task
        db.create_all() 

    app.register_blueprint(auth_routes, url_prefix="/auth")
    app.register_blueprint(task_routes, url_prefix="/tasks")

    @app.route("/")
    def home():
        return "Servidor rodando! SQLite conectado."

    return app
