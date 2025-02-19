#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from os import getenv

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Route for the cities_by_states route"""
    states = None
    states = storage.all(State)
    return render_template(
        "8-cities_by_states.html", states=states, cities=states
    )


@app.teardown_appcontext
def close(x):
    """ closes the db storage """
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
