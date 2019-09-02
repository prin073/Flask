from Flask_Login.FlaskLogin import db, UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))


def create_a_table():
    db.create_all()


def register_user(**kwargs):
    try:
        user = User(**kwargs)
        db.session.add(user)
        db.session.commit()
    except:
        return "User already exists"


def retrieve_user_by_name(username):
    try:
        user = User.query.filter_by(username=username).first_or_404()
    except:
        user = 'unknown user'
    finally:
        return user


def retrieve_user_by_id(user_id):
    return User.query.get(int(user_id))


def update_password(email, password):
    user = User.query.filter_by(email=email).first_or_404()
    user.password = password
    db.session.commit()


