#!/usr/bin/python3
""" a script that starts a Flask web application"""
from models.state import State
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close(x):
    """ closes the db storage """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
