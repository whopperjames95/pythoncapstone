from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_migrate import Migrate 
import os


app =  Flask(__name__)




database = SQLAlchemy(app)


Migrate(app,database)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from website.view import views
from website.authentication import auth

app.register_blueprint(views, url_prefx='/') 
app.register_blueprint(auth, url_prefx='/') 

