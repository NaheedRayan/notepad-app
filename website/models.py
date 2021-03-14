from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# The User will inherit database model and UserMixin . The UserMixin is for authentication
# purpose
class User(db.Model , UserMixin):
    id = db.Column(db.Integer , primary_key = True)
    email = db.Column(db.String(150) , unique = True)
    password = db.Column(db.String(150))
    firstname = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    notes = db.relationship('Note')

    # def __repr__(self):
    #     print(f"<Post {self.firstname}>")


class Note(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default = func.now())
    user_id = db.Column(db.Integer , db.ForeignKey('user.id'))
    