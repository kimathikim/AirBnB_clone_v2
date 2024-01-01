#!/usr/bin/python3
"""script that runs flask and assigns variables for url creation"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """function that returns hello"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """function that returns hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """function that returns c and text"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """function that returns python and text"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """function that returns number and n"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
