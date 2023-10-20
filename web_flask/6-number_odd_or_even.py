#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    "displays Hello HBNB!"
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    "displays HBNB"
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    "displays C followed by the value of the text variable"
    return f"C {escape(text.replace('_', ' '))}"


@app.route('/python')
@app.route('/python/<text>')
def py(text="is cool"):
    "displays Python followed by the value of the text variable"
    return f"Python {escape(text.replace('_', ' '))}"


@app.route("/number/<int:n>")
def is_number(n):
    "displays n is a number only if n is an integer"
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def show_number(n):
    "displays a HTML page only if n is an integer"
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_or_even(n):
    "displays a HTML page only if n is an integer"
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
