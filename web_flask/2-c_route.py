#!/usr/bin/python3
"""
starts a web application using Flask
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
        the messsage needed to display
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb1():
    """
        the messsage needed to display
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hbnb2(text):
    """
        the messsage needed to display
    """
    return 'C ' + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
