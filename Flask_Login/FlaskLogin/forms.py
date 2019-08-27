from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length, Email


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=5, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=5, max=18)])
    remember = BooleanField('Remember me')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=5, max=15)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=5, max=80)])
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid Email!'), Length(max=50)])




