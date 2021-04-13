from flask import Blueprint
from flask_restful import Api

from .resources import TodoAPI, TodoListAPI


def create_todo_bp(name='todo_bp'):
    todo_bp = Blueprint(name, __name__)
    register_api(todo_bp)
    return todo_bp


def register_api(bp):
    api = Api(bp)
    api.add_resource(TodoAPI, '/todolist/<int:id>', endpoint='todo')
    api.add_resource(TodoListAPI, '/todolist', endpoint='todolist')
    return api