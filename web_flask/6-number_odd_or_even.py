#!/usr/bin/python3
"""script that runs flask and assigns variables for url creation"""
from flask import Flask, render_template

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
def python(text="is cool"):
    """function that returns python and text"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """function that returns number and n"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """function that returns number and n"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def evenOdd_template(n):
    txt = "even" if n % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html", n=n, txt=txt)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
