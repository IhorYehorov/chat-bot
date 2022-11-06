from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    mention = db.Column(db.String(64), unique=True)
    in_search = db.Column(db.Boolean, default=False)
    in_chat_with = db.Column(db.Integer, unique=True)

    def __repr__(self):
        return f'{self.mention}'
