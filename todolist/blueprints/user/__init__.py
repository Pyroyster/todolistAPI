from flask import Blueprint
from flask_restful import Api

from .resources import RegisterAPI, LoginAPI, RenameAPI, ResetPwdAPI, LogoutAPI


def create_user_bp(name='user_bp'):
    user_bp = Blueprint(name, __name__)
    register_api(user_bp)
    return user_bp


def register_api(bp):
    api = Api(bp)

    api.add_resource(RegisterAPI, '/register')
    api.add_resource(LoginAPI, '/login')
    api.add_resource(RenameAPI, '/rename')
    api.add_resource(ResetPwdAPI, '/resetPwd')
    api.add_resource(LogoutAPI, '/logout')


