from Flask_Login.FlaskLogin import app, render_template, redirect, url_for, login_manager, login_user, logout_user, login_required, current_user, SignatureExpired, BadTimeSignature
from forms import LoginForm, RegisterForm, ResetPasswordForm, ConfirmPasswordForm
from Flask_Login.FlaskLogin.models import register_user, retrieve_user_by_name, retrieve_user_by_id, update_password
from werkzeug.security import generate_password_hash, check_password_hash
from Common.Common_Methods import send_mail, confirm_mail

#this is required if using Login Manager
@login_manager.user_loader
def load_user(user_id):
    return retrieve_user_by_id(user_id)


@app.route('/')
def index():
    return render_template('Index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        status = register_user(username=form.username.data, email=form.email.data, password=hashed_password)
        if status is not None:
            return '<h1> '+ status +' </h1>'
        return '<h1>Registration is successful, Please <a href=/login>Login</a></h1>'
    return render_template('Signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        registered_user = retrieve_user_by_name(username=form.username.data)
        if registered_user and check_password_hash(registered_user.password, form.password.data):
            login_user(registered_user, remember=form.remember.data)  #when using LoginManager it is required
            return redirect(url_for('dashboard'))
        else:
            return '<h1>Invalid username or password</h1>'
    return render_template('Login.html', form=form)


@app.route('/logout')
@login_required  #it is used to make sure no one can directly access /logout
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/dashboard')
@login_required  #it is used to make sure no one can directly access /dashboard
def dashboard():
    return render_template('Dashboard.html', name=current_user.username)


@app.route('/forgotten_password', methods=['GET', 'POST'])
def forgotten_password():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        registered_user = retrieve_user_by_name(username=form.username.data)
        if registered_user != 'unknown user' and registered_user.email == form.email.data:
            send_mail(form.email.data, 'reset_password')
            return '<h1>A link has been sent to your registered email to reset your password</h1>'
        else:
            return '<h1>username or email is not registered</h1>'
    return render_template('Forgotten_Password.html', form=form)


@app.route('/confirm_email/<token>', methods=['GET', 'POST'])
def confirm_email(token):
    form = ConfirmPasswordForm()
    try:
        confirmed_email = confirm_mail(token)
    except SignatureExpired:
        return '<h1>Token is expired !</h1>'
    except BadTimeSignature:
        return '<h1>Incorrect Token !</h1>'
    if confirmed_email and form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        update_password(confirmed_email, hashed_password)
        send_mail(confirmed_email, 'confirm_password')
        return redirect(url_for('index'))
    return render_template('Confirm_Email.html', form=form, token=token)