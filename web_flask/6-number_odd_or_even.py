#!/usr/bin/python3
"""
start a web application using flask
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    the messsage needed to display
    """
    return "Hello HBNB!"


@app.route('/<hbnb>', strict_slashes=False)
def hbnb(hbnb):
    """
    the messsage needed to display
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def texts(text):
    """
    the messsage needed to display
    """
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def default(text="is cool"):
    """
    the messsage needed to display
    """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def check_for_int(n):
    """
    the message + number needed to display
    """
    return str(n) + " is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_templatee(n):
    """
    the message + number needed to display
    """
    return render_template("5-number.html", content=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numbersandevenness(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        evenness = 'even'
    else:
        evenness = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           result=evenness)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)