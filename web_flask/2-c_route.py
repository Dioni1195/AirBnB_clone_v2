#!/usr/bin/python3
from flask import Flask
""" This is a Hello world code with different routes """


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Prints Hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Prints HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text=None):
    """ Prints with a parameter"""
    txt = text.replace('_', ' ')
    return 'C {}'.format(txt)
app.run()
