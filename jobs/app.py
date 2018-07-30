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
    return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
@app.route('/jobs')
def jobs():
    jobs = query_db(
        'SELECT job.id, job.title, job.description, job.salary, employer.id as employer_id, employer.name as employer_name'
        ' FROM job JOIN employer ON employer.id = job.employer_id')
    return render_template('index.html', jobs=jobs)

@app.route('/job/<job_id>')
def job(job_id):
    job = query_db(
        'SELECT job.id, job.title, job.description, job.salary, employer.id as employer_id, employer.name as employer_name'
        ' FROM job JOIN employer ON employer.id = job.employer_id'
        ' WHERE job.id=?', [job_id], True)
    return render_template('job.html', job=job)

@app.route('/employer/<employer_id>')
def employer(employer_id):
    employer = query_db('SELECT * FROM employer WHERE id=?', [employer_id], True)
    jobs = query_db(
        'SELECT job.id, job.title, job.description, job.salary'
        ' FROM job JOIN employer ON employer.id = job.employer_id'
        ' WHERE employer.id=?', [employer_id])
    reviews = query_db(
        'SELECT review, rating, title, date, status'
        ' FROM review JOIN employer ON employer.id = review.employer_id'
        ' WHERE employer.id =?', [employer_id])
    return render_template('employer.html', employer=employer, jobs=jobs, reviews=reviews)

@app.route('/user/<user_id>')
def user(user_id):
    user = query_db('SELECT * FROM user WHERE id=?', user_id, True)
    return render_template('user.html', user=user)

@app.route('/admin')
def admin():
    return render_template('admin.html')
