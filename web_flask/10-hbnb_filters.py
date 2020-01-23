#!/usr/bin/python3
from models import storage
from models.state import State
from flask import Flask, render_template
""" This module import data from storage """

app = Flask(__name__)


@app.teardown_appcontext
def close(arg):
    """ Close the session """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ Lists the states """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == '__main__':
    app.run()
