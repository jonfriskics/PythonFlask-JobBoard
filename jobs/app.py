from flask import Flask, render_template

app = Flask(__name__)

def jobs():
  return render_template('index.html')