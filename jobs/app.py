import sqlite3
import datetime
from flask import g, Flask, flash, render_template, request, redirect, url_for

app = Flask(__name__)

DATABASE = 'db/jobs.sqlite'

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
        ' WHERE job.id = ?', [job_id], True)
    return render_template('job.html', job=job)

@app.route('/employer/<employer_id>')
def employer(employer_id):
    employer = query_db('SELECT * FROM employer WHERE id=?', [employer_id], True)
    jobs = query_db(
        'SELECT job.id, job.title, job.description, job.salary'
        ' FROM job JOIN employer ON employer.id = job.employer_id'
        ' WHERE employer.id = ?', [employer_id])
    reviews = query_db(
        'SELECT review, rating, title, date, status'
        ' FROM review JOIN employer ON employer.id = review.employer_id'
        ' WHERE employer.id = ?', [employer_id])
    return render_template('employer.html', employer=employer, jobs=jobs, reviews=reviews)

@app.route('/employer/<employer_id>/review', methods=('GET', 'POST'))
def review(employer_id):
    if request.method == 'POST':
        review = request.form['review']
        rating = request.form['rating']
        title = request.form['title']
        date = datetime.datetime.now().strftime("%m/%d/%Y")
        status = request.form['status']
        error = None

        if not review:
            error = 'Review is required.'
        elif not rating: 
            error = 'Rating is required.'
        elif not title: 
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO review (review, rating, title, date, status, employer_id)'
                ' VALUES (?, ?, ?, ?, ?, ?)',
                (review, rating, title, date, status, employer_id)
            )
            db.commit()
            return redirect(url_for('employer', employer_id=employer_id))

    return render_template('review.html', employer_id=employer_id)

@app.route('/admin')
def admin():
    jobs = query_db(
        'SELECT job.id, job.title, job.description, job.salary, employer.id as employer_id, employer.name as employer_name'
        ' FROM job JOIN employer ON employer.id = job.employer_id')
    return render_template('admin/index.html', jobs=jobs)

@app.route('/admin/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        salary = request.form['salary']
        employer_id = request.form['employer_id']
        error = None

        if not title:
            error = 'Title is required.'
        elif not employer_id: 
            error = 'Employer is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO job (title, description, salary, employer_id)'
                ' VALUES (?, ?, ?, ?)',
                (title, description, salary, employer_id)
            )
            db.commit()
            return redirect(url_for('admin'))

    employers = query_db('SELECT id, name FROM employer')
    return render_template('admin/create.html', employers=employers)
