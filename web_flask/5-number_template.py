#!/usr/bin/python3
"""
The airbnb flask app package instantiation
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    return "C " + text.replace("_", " ")


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
