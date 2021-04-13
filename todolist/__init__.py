import os
from flask import Flask

from todolist.blueprints import register_blueprints
from todolist.extentions import register_extentions


def create_app():
    app = Flask(__name__)
    # app.secret_key = os.urandom(16)
    app.secret_key = 'SECRET_KEY'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:210421@localhost/todo2'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['KEY_ACCESS_TOKEN'] = 'access_token'
    # app.config['KEY_REFRESH_TOKEN'] = 'refresh_token'
    app.config['ACCESS_TOKEN_EXPIRES'] = 3600 * 24 * 7
    # app.config['REFRESH_TOKEN_EXPIRES'] = 3600 * 24 * 30
    register_blueprints(app)
    register_extentions(app)

    return app

