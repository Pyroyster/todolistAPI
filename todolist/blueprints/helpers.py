from flask import g,current_app,request
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from functools import wraps

from todolist.models import User
#import redis
# from app.extentions import pool
# r = redis.Redis(connection_pool=pool)


def get_token():
    token = request.headers.get('Authorization', None)
    if token is None:
        return None

    if 'Authorization' in request.headers:
        try:
            token = request.headers['Authorization'].split(';')[0]
        except ValueError:
            token = None
    else:
        token = None

    token = token
    return token


def generate_token(user, expires=3600 * 24 * 7):
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expires)
    token = s.dumps({'id': user.id}).decode('ascii')
    return token


def validate_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except (BadSignature, SignatureExpired):
        return None
    # print(data['id'])
    user = User.query.get(int(data['id']))
    # print(user)
    if user is None:
        return None
    # g.current_user = user
    return user


def get_token_info(user):
    token = generate_token(user, 3600 * 24 * 7)
    token_info = {
        'token': token,
        'expires': 3600 * 24 * 7
    }
    return token_info



