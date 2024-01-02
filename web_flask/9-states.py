#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from os import getenv

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states_list():
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Route for the cities_by_states route"""
    states = storage.all(State)
    for x in states.values():
        if x.id == id:
            return render_template("9-states.html", state=x)
    return render_template("9-states.html", state=None)


@app.teardown_appcontext
def close(x):
    """ closes the db storage """
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
