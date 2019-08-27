from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # To silent the warning message

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.db'

app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = 'ITISASECRET'


Bootstrap(app)
db = SQLAlchemy(app)


#this is the last step in login application development
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


#import here otherwise it won't be able to find app module
from Flask_Login.FlaskLogin import routes