#!/usr/bin/python3
"""Write a script that starts a Flask web application on port 5000 and
displays Hello HBNB!
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    return hello ...
    """
    return "Hello HBNB!"


# run on debug mode
if __name__ == "__main__":
    app.run(port=5000, debug=True)
