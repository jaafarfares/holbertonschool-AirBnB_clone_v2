#!/usr/bin/python3
"""
starts a web applicatin using flask
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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
