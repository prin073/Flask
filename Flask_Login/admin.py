from Flask_Login.FlaskLogin import db

db.create_all()

# select sql from sqlite_master where tbl_name='user' and type='table';
# PRAGMA table_info(table_name)  ==> both are same