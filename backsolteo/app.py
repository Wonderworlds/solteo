import os
from dotenv import load_dotenv

load_dotenv()
from flask import Flask, jsonify, make_response, request
from db import db, Database
from config import Config
from flask_migrate import Migrate
from flask_cors import CORS
from modules import todo_bp, user_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.getenv("APP_SETTINGS", "config.DevelopmentConfig"))
    app.config.from_object(Config)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    CORS(app)
    db.init_app(app)
    Database(app.config["SQLALCHEMY_DATABASE_URI"])
    Migrate(app, db)
    from models import todo_model, user_model

    app.register_blueprint(todo_bp.blueprint)
    app.register_blueprint(user_bp.blueprint)
    return app


app = create_app()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error="Route not found!"), 404)


if __name__ == "__main__":
    app.run("127.0.0.1", "5000", debug=True)
