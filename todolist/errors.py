from flask import jsonify,current_app
from werkzeug.http import HTTP_STATUS_CODES


def api_abort(code, message=None,**kwargs):
    if message is None:
        message = HTTP_STATUS_CODES.get(code, '')
    response = jsonify(code=code, message=message, **kwargs)
    response.status_code = code
    return response