from Flask_Login.FlaskLogin import db, UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))


def create_a_table():
    db.create_all()


def register_user(**kwargs):
    user = User(**kwargs)
    db.session.add(user)
    db.session.commit()


def retrieve_user_by_name(username):
    return User.query.filter_by(username=username).first()


def retrieve_user_by_id(user_id):
    return User.query.get(int(user_id))


