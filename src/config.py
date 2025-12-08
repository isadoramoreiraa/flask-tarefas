import os

class Config:
    SECRET_KEY = "minha_chave_secreta"
    SQLALCHEMY_DATABASE_URI = "sqlite:///tasks.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
