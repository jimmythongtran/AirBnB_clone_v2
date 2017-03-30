#!/usr/bin/python3
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    storage.close()


@app.route('/states')
def states():
    data = storage.all("State")
    return render_template("9-states.html", data=data)


@app.route('/states/<id>')
def statesID(id):
    dataid = storage.all("State")
    identity = ""
    for i in dataid:
        if id == i:
            identity = dataid[i]
    return render_template("9-states.html", identity=identity)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
