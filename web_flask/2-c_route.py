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
    return "c %s" % text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
