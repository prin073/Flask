from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadTimeSignature


app = Flask(__name__)

app.config.from_pyfile('Config/configuration.cfg') #loading the configurations

Bootstrap(app)

db = SQLAlchemy(app)

mail = Mail(app)
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])


#this is the last step in login application development
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


#import here otherwise it won't be able to find app module
from Flask_Login.FlaskLogin import routes