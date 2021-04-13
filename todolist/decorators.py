from functools import wraps
from flask import g
from todolist.errors import api_abort
from todolist.blueprints.helpers import get_token, validate_token


def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token()
        if token is None:
            return api_abort(401, 'token is required')
        g.current_token = token
        # print(g.current_token)
        return f(*args, **kwargs)
    return decorated


def login_required(f):
    @wraps(f)
    @auth_required
    def decorated(*args,**kwargs):
        current_user = validate_token(g.current_token)
        if current_user is None:
            return api_abort(401, 'invalid_token')

        g.current_user = current_user
        return f(*args,**kwargs)
    return decorated
"""
def auth_required():
    def wrapper(f):
        def decorator(*args, **kwargs):
            token = get_token()
            if token is None:
                return api_abort(401, 'token is required')
            g.current_token = token
            # print(g.current_token)
            return f(*args, **kwargs)
        return decorator
    return wrapper


def login_required():
    def wrapper(f):
        @auth_required()
        def decorator(*args, **kwargs):
            # print(g.current_token)
            current_user = validate_token(g.current_token)
            if current_user is None:
                return api_abort(401, 'invalid_token')

            g.current_user = current_user
        return decorator
    return wrapper

"""
