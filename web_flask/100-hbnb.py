#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.user import User

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    users = storage.all(User)
    for _, place in places.items():
        for _, user in users.items():
            if place.user_id == user.id:
                place.user = user
                break
    return render_template(
        "100-hbnb.html", states=states, amenities=amenities, places=places
    )


@app.teardown_appcontext
def close(x):
    """ closes the db storage """
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
