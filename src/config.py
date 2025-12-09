import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "minha_chave_secreta_local")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///tasks.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
