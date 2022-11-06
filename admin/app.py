from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

import config
from models import db, User

app = Flask(__name__)
app.secret_key = config.SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bot.db'
db.init_app(app)
db.app = app


if __name__ == '__main__':
    admin = Admin(app)
    admin.add_view(ModelView(User, db.session))
    db.create_all()

    app.run('0.0.0.0', 8000)
