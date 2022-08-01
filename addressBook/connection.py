import sqlite3
from conatants import DB_PATH


def connect_to_db(db_name):
    ## Database Connection
    return sqlite3.connect(DB_PATH + db_name + '.db')
