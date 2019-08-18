# Downloading sqlite for windows for commandline
# https://www.google.com/search?q=installing+sqlite+on+windows&rlz=1C1GCEA_enIN771IN771&oq=installing+sqlite+&aqs=chrome.1.69i57j0l5.10618j0j4&sourceid=chrome&ie=UTF-8#kpvalbx=_kINWXaieE4SwkwXj0beoDA26

# other links
# ============
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#connection-uri-format
# https://stackoverflow.com/questions/21243291/flask-sqlalchemy-when-are-the-tables-databases-created-and-destroyed


from Flask_SqlAlchemy.Flask_Sql_Alchemy import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)
    # creation_date = db.Column(db.DateTime, default=datetime.now)


def create_a_table():
    db.create_all()


def create_todo(**kwargs):
    """create a task"""
    task = Todo(**kwargs)
    db.session.add(task)
    db.session.commit()


def retrieve_all_todos():
    return Todo.query.all()


def retrieve_complete_todos():
    return Todo.query.filter_by(complete=True).all()


def retrieve_incomplete_todos():
    return Todo.query.filter_by(complete=False).all()


def update_todo_by_id(list_id):
    """update a task by id"""
    for id in list_id:
        todo = Todo.query.filter_by(id=int(id)).first()
        todo.complete = True
    db.session.commit()


def delete_todo_by_id(list_id):
    """delete a task by id"""
    for id in list_id:
        todo = Todo.query.filter_by(id=int(id)).first()
        db.session.delete(todo)
        db.session.commit()