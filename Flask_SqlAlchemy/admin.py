#Can be created from command line,

#I have handled it in routes.py

from Flask_SqlAlchemy.Flask_Sql_Alchemy import db

if __name__ == '__main__':
    db.create_all()
