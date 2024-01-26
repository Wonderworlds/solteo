from flask import Blueprint, Response, jsonify, make_response, request
from wtforms import Form, StringField, validators
from wtforms.validators import DataRequired, Optional
from models.todo_model import TodoModel
from app import db
import wtforms_json

from models.user_model import UserModel

wtforms_json.init()

blueprint = Blueprint("todo", __name__, url_prefix="/todos")


class TodoForm(Form):
    title = StringField("title", validators=[validators.Length(min=0, max=30)])
    body = StringField("body", validators=[DataRequired()])
    user_name = StringField(
        "user_name", validators=[validators.Length(min=3, max=20), Optional()]
    )


@blueprint.route("", methods=["GET"])
def getTodos():
    todos = TodoModel.query.all()
    todosDict = [todo.to_dict() for todo in todos]
    return make_response(todosDict, 200)


@blueprint.route("/from/<string:name>", methods=["GET"])
def getTodosFrom(name):
    user = UserModel.query.filter_by(name=name).first()
    if user is None:
        return make_response(jsonify(error="Not found!"), 404)
    todos = TodoModel.query.filter_by(user_id=user.id).all()
    todosDict = [todo.to_dict() for todo in todos]
    return make_response(todosDict, 200)


@blueprint.route("/<string:id>", methods=["GET"])
def getTodoInfos(id):
    todo = TodoModel.query.get(id)
    if todo is None:
        return make_response(jsonify(error="Not found!"), 404)
    return make_response(todo.to_dict(), 200)


@blueprint.route("/<string:id>", methods=["PUT"])
def updateTodo(id):
    todo = TodoModel.query.get(id)
    if todo is None:
        return make_response(jsonify(error="Not found!"), 404)
    req = request.get_json()
    form = TodoForm.from_json(req)
    if form.validate():
        if "title" not in req:
            req["title"] = ""
        if "user_name" in req:
            user = UserModel.query.filter_by(name=req["user_name"]).first()
            if user is None:
                return make_response(jsonify(error="User not found!"), 404)
            todo.update(req["title"], req["body"], user.id)
        else:
            todo.update(req["title"], req["body"], None)
    else:
        return make_response(form.errors, 400)
    return make_response("Todo updated", 200)


@blueprint.route("", methods=["POST"])
def createTodo():
    req = request.get_json()
    form = TodoForm.from_json(req)
    if form.validate():
        if "title" not in req:
            req["title"] = ""
        if "user_name" in req:
            user = UserModel.query.filter_by(name=req["user_name"]).first()
            if user is None:
                return make_response(jsonify(error="User not found!"), 404)
            todo = TodoModel(req["title"], req["body"], user.id)
            todo.save()
        else:
            todo = TodoModel(req["title"], req["body"], None)
            todo.save()
        return make_response("Todo created", 200)
    else:
        return make_response(form.errors, 400)


@blueprint.route("/<string:id>", methods=["DELETE"])
def deleteTodo(id):
    todo = TodoModel.query.get(id)
    if todo is None:
        return make_response(jsonify(error="Not found!"), 404)
    todo.delete()
    return make_response("Todo deleted", 200)
