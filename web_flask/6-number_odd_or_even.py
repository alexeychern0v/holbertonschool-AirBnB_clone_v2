#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Display “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display “HBNB”"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def ctext(text):
    """Display “C ” followed by given text"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", defaults={"text": "is cool"})
def pytext(text):
    """Display “Python ” followed by given text"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def n_int(n):
    """Displays “n is a number” only if n is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_temp(n):
    """Display a HTML page if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def oddeven(n):
    """Displays a HTML and check if n is odd or even"""
    if n % 2 == 0:
        n = "{} is even".format(n)
    else:
        n = "{} is odd".format(n)
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    """ Main function """
    app.run(host="0.0.0.0", port=5000)