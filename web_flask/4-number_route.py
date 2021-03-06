#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_HBNB():
    return "Hello HBNB!"


@app.route('/hbnb')
def HBNB():
    return "HBNB"


@app.route('/c/<text>')
def C(text):
    text = text.replace('_', ' ')
    return "C %s" % text


@app.route('/python/')
@app.route('/python/<text>')
def python(text="is cool"):
    text = text.replace('_', ' ')
    return "Python %s" % text


@app.route('/number/<int:n>')
def number(n):
    return "%d is a number" % n

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
