import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

db = sqlite3.connect(
    'jobs/db.sqlite3', detect_types=sqlite3.PARSE_DECLTYPES
)

# Job
# Title
# Description
# Salary
# Tag

@app.route('/')
@app.route('/jobs')
def jobs():
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