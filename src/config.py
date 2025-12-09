import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "minha_chave_secreta")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data", "tasks.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
