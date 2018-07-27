import sqlite3
from flask import g, Flask, render_template

app = Flask(__name__)

DATABASE = 'jobs/db.sqlite3'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    if rv:
        return rv[0] if one else rv
    else:
        return None

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Job
# Title
# Description
# Salary
# Tag

@app.route('/')
@app.route('/jobs')
def jobs():
    jobs = query_db('select * from jobs')
    for job in jobs:
        print(job)
    return render_template('index.html')


@app.route('/job/<job_id>')
def job(job_id):
    return render_template('job.html')

# Employer
# name
# description
# address

# Review
# rating
# title
# date
# status (current/former)

@app.route('/employer/<employer_id>')
def employer(employer_id):
    return render_template('employer.html')

# User
# username
# password
# name
# email
# phone
# role_id

# Role
# type


@app.route('/user/<user_id>')
def user(user_id):
    return render_template('user.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')
