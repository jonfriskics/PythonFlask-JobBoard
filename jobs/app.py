import sqlite3
from flask import g

DATABASE = 'db/jobs.sqlite'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = sqlite3.connect(DATABASE)
        g._database = db