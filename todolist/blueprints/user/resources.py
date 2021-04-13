from flask import g
from flask_restful import Resource,reqparse
from werkzeug.security import generate_password_hash

from todolist.models import User
from todolist.extentions import db
from todolist.decorators import login_required

from todolist.blueprints.helpers import get_token_info
register_reqparser = reqparse.RequestParser()
register_reqparser.add_argument('username', type=str, location='json')
register_reqparser.add_argument('password', type=str, location='json')

login_reqparser = reqparse.RequestParser()
login_reqparser.add_argument('username', type=str, location='json')
login_reqparser.add_argument('password', type=str, location='json')

reset_pwd_reqparser = reqparse.RequestParser()
reset_pwd_reqparser.add_argument('new_pwd', type=str, required=True, location='json')

rename_reqparser = reqparse.RequestParser()
rename_reqparser.add_argument('new_name',type=str, required=True, location='json')

class RegisterAPI(Resource):
    def post(self):
        info = register_reqparser.parse_args()
        status = 0
        data = {}
        user = User.query.filter_by(username=info['username']).first()
        if user is not None:
            status = 1
            message = "username already exits"
        else:
            new_user = User(info['username'])
            new_user.set_password(info['password'])
            db.session.add(new_user)
            db.session.commit()
            message = 'register succeed'
            data = {'user_id': new_user.id, 'username': new_user.username}
        return {'status':status, 'message':message, 'data':data}

class LoginAPI(Resource):
    def post(self):
        info = login_reqparser.parse_args()
        status = 0
        data = {}
        user = User.query.filter_by(username=info['username']).first()
        if user is None:
            status = 1
            message = 'no account'
        elif user is not None and not user.validate_password(info['password']):
            status = 1
            message = 'Invalid username or password'
        else:
            g.current_user = user
            token_info = get_token_info(user)
            message = 'login succeed'
            data = {'username': user.username,'token':token_info}
        return {'status':status, 'message':message, 'data':data}


class RenameAPI(Resource):
    decorators = [login_required]
    # @login_required
    def post(self):
        info = rename_reqparser.parse_args()
        print(type(g.current_user))
        g.current_user.username = info['new_name']
        db.session.commit()
        return {'status': 0, 'message': 'succeed',
                'data': {'uid': g.current_user.id, 'username': g.current_user.username}}


class ResetPwdAPI(Resource):
    decorators = [login_required]

    def post(self):
        info = reset_pwd_reqparser.parse_args()
        g.current_user.hash_password = generate_password_hash(info['new_pwd'])
        db.session.commit()
        return {'status': 0, 'message': 'succeed',
                'data': {'uid': g.current_user.id, 'username': g.current_user.username}}


class LogoutAPI(Resource):
    decorators = [login_required]

    def delete(self):
        db.session.delete(g.current_user)
        db.session.commit()
        return {'status': 0, 'message': 'logout success', 'data': {}}



