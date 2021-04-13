from .todo import create_todo_bp
from .user import create_user_bp

todo_bp = create_todo_bp()
user_bp = create_user_bp()


def register_blueprints(app):
    app.register_blueprint(todo_bp, url_prefix='/api')
    app.register_blueprint(user_bp, url_prefix='/api/user')
