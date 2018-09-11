from flask import Flask, render_template
from sqlite import sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
  return render_template('index.html')