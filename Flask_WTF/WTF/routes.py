# https://www.youtube.com/watch?v=vzaXBm-ZVOQ

from flask import render_template
from Flask_WTF.WTF import app
from Flask_WTF.WTF.form import LoginForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return '<h1>The Username is {} and Password is {}.</h1>'.format(form.username.data, form.password.data)
    return render_template('form2.html', form=form)