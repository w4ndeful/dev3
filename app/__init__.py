# app/__init__.py
from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    # Завантаження конфігурації
    app.config.from_object('config')

    from app.users import users_bp
    app.register_blueprint(users_bp, url_prefix='/users')

    return app
