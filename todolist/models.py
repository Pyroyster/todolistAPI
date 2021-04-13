from .extentions import db, whooshee
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), unique=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, username):
        self.username = username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        return True

    def get_id(self):
        return self.id

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True


@whooshee.register_model('task', 'description')
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, db.ForeignKey(User.id))
    task = db.Column(db.String(50))
    description = db.Column(db.String(500))
    done = db.Column(db.Boolean, default=False)
    timeStart = db.Column(db.DateTime, index=True)
    timeOver = db.Column(db.DateTime)

    def __init__(self, task, timeOver, uid):
        self.task = task
        self.timeStart = str(datetime.now())[0:19]
        self.timeOver = timeOver
        self.uid = uid
