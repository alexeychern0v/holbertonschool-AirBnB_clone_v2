#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """ Returns "Hello HBNB!" """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def HB():
    """ Returns "HBNB!" """
    return "HBNB!"


if __name__ == "__main__":
    """ Main Function """
    app.run(host="0.0.0.0", port=5000)