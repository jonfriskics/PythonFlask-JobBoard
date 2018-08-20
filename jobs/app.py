from flask import g

DATABASE = 'db/jobs.sqlite'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite.connect(DATABASE)