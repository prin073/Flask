from Flask_Login.FlaskLogin import app, Message, url_for, serializer, mail


def send_mail(to_email, activity):
    token = serializer.dumps(to_email, salt='email-confirm')

    msg = Message(subject='Confirm email', sender=app.config['MAIL_USERNAME'], recipients=[to_email])

    link = url_for('confirm_email', token=token, _external=True)

    if activity == 'reset_password':
        msg.body = 'Your link is {}'.format(link)
    elif activity == 'confirm_password':
        msg.body = 'Your password has been reset'

    mail.send(msg)


def confirm_mail(token):
    email = serializer.loads(token, salt='email-confirm', max_age=3600)
    return email

