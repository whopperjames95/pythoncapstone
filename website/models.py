# database models 
from website import database 
from flask_login import UserMixin
from sqlalchemy.sql import func


# from flask_wtf import FlaskForm
# from flask_wtf.file import FileField



class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(200), unique=True)
    password = database.Column(database.String(200))
    first_name= database.Column(database.String(150))
    notes = database.relationship('Note')
    notess = database.relationship('Bucket')
    notesss = database.relationship('Travel')




class Note(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    data = database.Column(database.String(10000))
    date = database.Column(database.DateTime(timezone=True), default=func.now())
    user_id = database.Column(database.Integer, database.ForeignKey("user.id"))

class Bucket(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    data = database.Column(database.String(10000))
    date = database.Column(database.DateTime(timezone=True), default=func.now())
    user_id = database.Column(database.Integer, database.ForeignKey("user.id"))


class Travel(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    data = database.Column(database.String(10000))
    date = database.Column(database.DateTime(timezone=True), default=func.now())
    user_id = database.Column(database.Integer, database.ForeignKey("user.id"))

