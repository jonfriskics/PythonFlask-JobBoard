from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
  return render_template('index.html')