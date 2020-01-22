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


@app.route('/states', strict_slashes=False)
def states():
    """ Lists the states """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def cities_by_states(id):
    """ Lists the cities by state ID """
    states = storage.all("State")
    new_obj = None
    for key, state in states.items():
        if state.id == id:
            new_obj = state
            break
    return render_template('9-states.html', states=new_obj)


if __name__ == '__main__':
    app.run()
