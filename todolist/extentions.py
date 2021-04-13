from flask_sqlalchemy import SQLAlchemy
from flask_whooshee import Whooshee
import redis
from flask_cors import CORS

db = SQLAlchemy()
whooshee = Whooshee()
cors = CORS()
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)


def register_extentions(app):
    db.init_app(app)
    whooshee.init_app(app)
    cors.init_app(app)

