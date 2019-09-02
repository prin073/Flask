from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length, Email


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=5, max=15)], render_kw={"placeholder": "Username"})
    password = PasswordField('Password', validators=[InputRequired(), Length(min=5, max=18)], render_kw={"placeholder": "Password"})
    remember = BooleanField('Remember me')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=5, max=15)], render_kw={"placeholder": "Username"})
    password = PasswordField('Password', validators=[InputRequired(), Length(min=5, max=80)], render_kw={"placeholder": "Password"})
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid Email!'), Length(max=50)], render_kw={"placeholder": "xyz@email.com"})


class ResetPasswordForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=5, max=15)], render_kw={"placeholder": "Username"})
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid Email!'), Length(max=50)], render_kw={"placeholder": "xyz@email.com"})


class ConfirmPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[InputRequired(), Length(min=5, max=80)], render_kw={"placeholder": "Password"})




