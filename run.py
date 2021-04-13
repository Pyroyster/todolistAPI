from todolist import create_app
from todolist.extentions import db
from todolist.models import User,Task

app = create_app()
ctx = app.app_context()
ctx.push()
db.create_all()

if __name__ == '__main__':
    app.run(port=5009, debug=True)