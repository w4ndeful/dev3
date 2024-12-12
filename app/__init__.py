# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.users import users_bp
    app.register_blueprint(users_bp, url_prefix='/users')

    return app
