# http://wtforms.simplecodes.com/docs/0.6/fields.html#basic-fields
# https://wordpress.org/support/topic/google-recaptcha-error-for-owner-invalid-key-type/  ===> recaptcha issue(use recaptcha v2)

# https://www.youtube.com/watch?v=vzaXBm-ZVOQ  ===> WTF
# https://www.youtube.com/watch?v=jR2aFKuaOBs ===> Validators
# https://www.youtube.com/watch?v=VrH0eH4nE-c ==> reCaptcha
# https://www.youtube.com/watch?v=J9O0v-iM0TE ===> macros

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, AnyOf


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired('A username is required!'), Length(min=5, max=10, message='Must be between 5 to 10 characters')])
    password = PasswordField('Password', validators=[InputRequired('A password is required!'), AnyOf(values=['password', 'secret'])])
    recaptcha = RecaptchaField()