from . import db # importing the current package (website) the db variable
from flask_login import UserMixin
from sqlalchemy.sql import func

# Creates a database model and archetecture for consistency 

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(100000))
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # the database will do it for us for date
    user_id =  db.Column(db.Integer, db.ForeignKey('user.id'))


# User Table
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')


