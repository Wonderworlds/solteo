from flask import Blueprint, Response, jsonify, make_response, request
from wtforms import Form, StringField, validators
from wtforms.validators import DataRequired
from db import db
from models.user_model import UserModel
import wtforms_json
from sqlalchemy.exc import IntegrityError

wtforms_json.init()

blueprint = Blueprint("users", __name__, url_prefix="/users")


class UserForm(Form):
    name = StringField(
        "name", validators=[validators.Length(min=3, max=20), DataRequired()]
    )


@blueprint.route("", methods=["GET"])
def getUser():
    users = UserModel.query.all()
    todosDict = [user.to_dict() for user in users]
    return make_response(todosDict, 200)


@blueprint.route("/<string:name>", methods=["GET"])
def getUserInfos(name):
    user = UserModel.query.filter_by(name=name).first()
    if user is None:
        return make_response(jsonify(error="Not found!"), 404)
    return make_response(user.to_dict(), 200)


@blueprint.route("/<string:name>", methods=["PUT"])
def updateUser(name):
    user = UserModel.query.filter_by(name=name).first()
    if user is None:
        return make_response(jsonify(error="Not found!"), 404)
    req = request.get_json()
    form = UserForm.from_json(req)
    if form.validate():
        try:
            user.update(req["name"])
        except IntegrityError as e:
            db.session.rollback()
            return make_response({"error": str(e).split("\n")}, 400)
    else:
        return make_response(form.errors, 400)
    return make_response("User updated", 200)


@blueprint.route("", methods=["POST"])
def createUser():
    req = request.get_json()
    form = UserForm.from_json(req)
    if form.validate():
        try:
            user = UserModel(req["name"])
            user.save()
        except IntegrityError as e:
            db.session.rollback()
            return make_response({"error": str(e).split("\n")}, 400)
        return make_response("User created", 200)
    else:
        return make_response(form.errors, 400)


@blueprint.route("/<string:name>", methods=["DELETE"])
def deleteUser(name):
    user = UserModel.query.filter_by(name=name).first()
    if user is None:
        return make_response(jsonify(error="Not found!"), 404)
    user.delete()
    return make_response("User deleted", 200)
