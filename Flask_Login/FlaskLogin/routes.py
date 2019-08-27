from scrapy.downloadermiddlewares import redirect

from Flask_Login.FlaskLogin import app, render_template, redirect, url_for, login_manager, login_user, logout_user, login_required, current_user
from forms import LoginForm, RegisterForm
from Flask_Login.FlaskLogin.models import register_user, retrieve_user_by_name, retrieve_user_by_id
from werkzeug.security import generate_password_hash, check_password_hash


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
        register_user(username=form.username.data, email=form.email.data, password=hashed_password)
        return '<h1>Registration is successful</h1>'
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



# def forgot_password():

