#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.state import State
from os import getenv

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template(
        "10-hbnb_filters.html", states=states, amenities=amenities
    )


@app.teardown_appcontext
def close(x):
    """ closes the db storage """
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
