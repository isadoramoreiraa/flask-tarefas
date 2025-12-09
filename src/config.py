import os

basedir = os.path.abspath(os.path.dirname(__file__))


db_path = os.path.join(basedir, "data")
os.makedirs(db_path, exist_ok=True)

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "minha_chave_secreta")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(db_path, "tasks.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
