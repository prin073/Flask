# https://www.youtube.com/watch?v=_sgVt16Q4O4&t=181s  ===> handling checkboxes
# https://stackoverflow.com/questions/19794695/flask-python-buttons ==> different action on different submit button selection

from flask import render_template, request, redirect, url_for

from flask_sqlalchemy import sqlalchemy
from Flask_SqlAlchemy.Flask_Sql_Alchemy import app

from Flask_SqlAlchemy.Flask_Sql_Alchemy.models import *


@app.route('/')
def index():
    try:
        complete_todos = retrieve_complete_todos()
        incomplete_todos = retrieve_incomplete_todos()
    except sqlalchemy.exc.OperationalError:
        create_a_table()
        complete_todos = retrieve_complete_todos()
        incomplete_todos = retrieve_incomplete_todos()

    return render_template('index.html', incomplete=incomplete_todos, complete=complete_todos)


@app.route('/add', methods=['POST'])
def add():
    create_todo(text=request.form.get('todoitem'), complete=False)
    return redirect(url_for('index'))


@app.route('/update', methods=['POST'])
def update():
    list_items = request.form.getlist('todo_chkbox')  # to handle multi checks
    print list_items
    if request.form.get('update_button') == 'Complete Item':
        update_todo_by_id(list_items)
    elif request.form.get('update_button') == 'Delete Item':
        delete_todo_by_id(list_items)
    return redirect(url_for('index'))

