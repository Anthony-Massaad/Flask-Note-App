# __init__ Makes the Website directory a python package
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) # Represents the name of the file 
    app.config['SECRET_KEY'] = 'secret_key' # Secure the cookie or session data
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # STORING THE DATABSE INSIDE THE WEBSITE DIRECOTRY Just tells flask
    db.init_app(app) # takes the databse and applies the app to it

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # telling flask how to load a user
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app 


def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print('database created')