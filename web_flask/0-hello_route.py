"""A script that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """view for /"""
    return "Hello HBNB!"


if __name__ == '__main__':
    # Start the Flask application on 0.0.0.0 at port 5000
    app.run(host='0.0.0.0', port=5000)
