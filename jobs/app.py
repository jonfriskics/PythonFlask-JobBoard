import sqlite3

from flask import g, Flask, render_template

app = Flask(__name__)

DATABASE = 'db/jobs.sqlite'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def query_db(query, args=(), one=False):
    db = get_db()
    cursor = db.execute(query, args)
    results = cursor.fetchall()
    cursor.close()
    return (results[0] if results else None) if one else results

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')