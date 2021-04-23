from enum import unique

from sqlalchemy.orm import backref
from covid19 import db
from datetime import datetime


class User(db.Model):
    id = db.Columnn(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    posts = db.relationship('Posts', backref="author", lazy=True)

    def __repr__(self):
        return f"User is '{self.email}'"


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    city = db.Column(db.String, nullable=False)
    descrip = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)