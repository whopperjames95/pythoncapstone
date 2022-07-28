from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path #will need to delete after postgres
from flask_login import LoginManager
from flask_migrate import Migrate 
import os

# app = Flask(__name__)
app =  Flask(__name__)
app.config['SECRET_KEY'] = 'This is the secret key'
# app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #change URI to postgres, example found in Chalon's message
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://whopper95:J0o9i8u7@localhost:5432/aspirations'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


database = SQLAlchemy(app)


Migrate(app,database)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from website.view import views
from website.authentication import auth

app.register_blueprint(views, url_prefx='/') 
app.register_blueprint(auth, url_prefx='/') 



#inside terminal type in command = export FLASK_APP=(main.py) .....not sure here

#also in terminal type = flask db init (this will create a migrations folder)
#next in terminal type = flask db migrate -m "created bucket list table"
#next in terminal type = flask db upgrade

# def create_app():
    


    

    

    

#     from .models import User, Note

#     create_database(app)


#     return app

# def create_database(app):
#     if not path.exists('website/' + DB_NAME):
#         db.create_all(app=app)
#         print('Created Database!')
