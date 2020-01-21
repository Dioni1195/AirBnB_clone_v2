#!/usr/bin/python3
from flask import Flask
""" This is a Hello world code """


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Prints Hello HBNB """
    return 'Hello HBNB!'
app.run()
