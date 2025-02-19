#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """view for /"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """view for /hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text: str):
    """view for /c/<text> where text is any value"""
    return "C {}".format(escape(text).replace('_', ' '))


@app.route("/python/", strict_slashes=False)
def python1():
    """view for /python/"""
    return "Python is cool"


@app.route("/python/<text>", strict_slashes=False)
def python2(text: str):
    """view for /python/<text> where text is any value"""
    return "Python {}".format(escape(text).replace('_', ' '))


if __name__ == '__main__':
    # Start the Flask application on 0.0.0.0 at port 5000
    app.run(host='0.0.0.0', port=5000)
